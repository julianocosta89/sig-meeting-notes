SIG: Collector SIG (EU/ET)
Date: 2026-07-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 03:58 Hello!
**Ilia Petrov** 04:04 Come home.
**Pablo Baeyens** 06:57 I hope there's not a lot of people on the order sampling.
But, yeah, I… I wanted to join and direct people to this one, but I… Don't have the old link, unfortunately.
So I guess we can get started, and if somebody's on the wrong one, we'll… See them?
Okay, so for… Issues on the Stability Phase 1… there's a couple of PRs… Okay, thanks, Jade.
Couple of PRs waiting on reviews, there is… this one that marks configure PCS 1.X, I want to keep this one open for… About a couple weeks, at least, and have, broad support, so it will be open until July 30th, but if you If you think there's something that… Should block, configure PCS1.
Please say so.
And then there is… PR for the Kubernetes attributes being marked as 1.0.
Which… Whoa.
Especially needs reviews from the code owners, but in general, If you have feedback.
Please, maybe there, and since it's our first ever components don't contribute to be marked as one point… something? We shouldn't.
I guess be especially careful.
To not get things wrong.
And… I don't know if there's anything else… on… Stability Phase 1.
Well, actually, yes, I have another PR that is related to Stability Phase 1 that I want reviews on.
Which is… This one, which is related to some work that Mikola is doing, for configHTTP.
**Mikołaj Świątek** 09:37 Which has ballooned out of control in terms of the changing country, at the very least.
But it's… it's good changes. It's, like, we are, we are…
**Pablo Baeyens** 09:48 Yes.
**Mikołaj Świątek** 09:49 To reckon with our… with the sins of the past.
**Pablo Baeyens** 09:53 I hope this is the last contribute change that we need to do for that, but yeah, it's definitely… Got bigger than… what I expected.
Okay, so, then… Guess we can talk about the SD Notify extension. Going to mop that out of Stability Phase 1, since it's… Not one of the components.
I guess this is from Ilia?
**Ilia Petrov** 10:30 Yeah, I just wanted to reach out if… Some of the sponsors is interested, and… I mean, someone from the maintainer, from the approvals.
Is he interested in sponsoring the extension?
I believe it's a case of use cases in different environment setups. For instance, for non-Kubernetes?
Environment, the ability for the auto collector.
to communicate with the system geomach way, is very powerful, and on the other side, for Kubernetes workloads, it's also useful, because, for instance, in our use case, we use collectors to ship, works, but, we… we are, like, a Kubernetes management platform.
And, we run collectors as a system, because we might have some issues with the kubelets, or something like this, and we don't want to be dependent from Yeah, from the Kubernetes setup, so that's why we run it as a separate workload, just to receive Potential works that might help us find the root cause.
Yeah, I think that's… It basically, I don't know, I mean, I mean, I have, for the first time in the SIG meeting, and I also… I'm not sure I know that procedure, so if there's… Something that I missed?
**Mikołaj Świątek** 12:20 I think it is great. There isn't really… we don't really have much procedure other than the document. So… I talked to you on Slack about this originally, and the reason I thought it was good in general to talk about this during this meeting is because I think there's an argument in favor of just putting this in Collector Core.
In the same way that, some, like, Windows Service Manager code is in Collector Car, because SystemD is quite ubiquitous.
It kind of makes sense that… it makes sense for this to be an extension, I don't really have… like, conceptual… I'm not conceptually opposed to that being the case, but it also feels like, maybe the Collector itself should interoperate with SystemD in some kind of… direct way, so things kind of work out of the box correctly without users having to add an extension to their config. Does that make sense?
But does everyone else in this call think about that?
That's what I was curious about.
**Ilia Petrov** 13:35 probably one thing from my side, because I thought about, this, to put in the core Collector.
for, at least for the moment, with the current implementation that I have, this is totally fine, because basically I provide no configuration for the extension, because everything is picked out logically. For example, when some watchdog underscore USEC is provided to the extension, it automatically knows what to do.
Oh… the only problem I have with this is that probably I will be a bit more limited in extending it. For instance, I really like the approach from Health Check V2 extension that I… potentially I'm able to get per component.
Health information, which is really crucial for us. Probably just one note, we had production, production issue from our side, where, we used BetterRoute token, extension.
And for some reason, the out token was not provided, and the collector looked like that it was working fine, but the individual component, the out token, was failing, and we were not able to catch that immediately, and And this is, for example, some very nice… use case. But I believe if we put that in… The core, then this type of features will be much harder to implement.
**Mikołaj Świątek** 15:22 Yeah, to me, for example, the fact that it requires no configuration is an argument in favor of putting it in core, if it's, like, obvious what it should.
**Ilia Petrov** 15:32 Oof.
**Mikołaj Świątek** 15:33 and users don't really have to do anything other than include it, then that's a good argument. And being… if there is a way to wire up health tracks.
the right way.
So that, like… I actually don't know whether… I'll take your word on it, because I don't think I've ever seen SystemD actually support, like, report status in any kind of structured way, so if that could actually be wired correctly, so you can actually see, like, per component status in it, that would be quite nice.
And that doesn't really preclude putting it in core either, although it might eventually force us to, like, start sharing the contrip state desegregation package, because right now.
CAR only knows about individual component statuses.
The notion that a pipeline has a status, and that the whole thing has a status is… is kind of a, invention of the HealthJack V2 extension, so that would have to be, generalized. Oh, but… but I think it's a good idea.
But anyway, if you need a sponsor, then I can't do it, because I don't have the power. But maybe someone else in this call does.
**Pablo Baeyens** 17:10 Is there a lot of downside on starting with this as an extension, and then… Once it's matured, think about putting it in core.
Like, I'm not opposed to putting it in core.
there may also be things that I don't know right now that maybe when users use this, allow us to think about, like, maybe we should have done this differently, and I think there's more flexibility if we start with an extension.
**Ilia Petrov** 17:38 Just a question, because I'm a bit… a new tool… To go hotel, but, is it… does it make sense, for instance, to… when you have different distributions for a hotel.
that there are some security risks when you put, let's say, some extension that you don't want actually to use. Because, for instance, if I have a Collector as a data plane.
and it was a Kubernetes deployment. In that case, I don't want to have SD notify capabilities.
And if it's in core, it will be there by default.
So, is there, like, if, let's say, something bad happens, and some very critical vulnerability is found in this LDNotifier extension, or this LDNotifier logic, let's say, and if it's in core.
Will it be a problem?
**Pablo Baeyens** 18:44 Yeah, that's actually a good argument to put it as an extension. We do use build tags to have certain things depending on the operating system, but
**Ilia Petrov** 18:56 Listen.
**Pablo Baeyens** 18:57 the way we distinguish between Kubernetes and non-Kubernetes is based on the distribution. We have a distribution for Kubernetes, and.
**Ilia Petrov** 19:04 Excellent.
**Pablo Baeyens** 19:05 Like, a generic distribution.
**Ilia Petrov** 19:10 Okay, so by default for the… okay, so let's say that distribution, it will not be included, but in the other ones, it will be included.
But if it's in core, then whatever distribution you make, or custom distribution, the logic will be there, a potential…
**Pablo Baeyens** 19:30 Yes, yep.
**Ilia Petrov** 19:31 vulnerability, okay.
Now with this Windows implementation, can it be turned on, or turned off, or by default, it's on?
**Pablo Baeyens** 19:47 I mean, we have… leeway there to make this configurable if we put it in core, but… Yeah, we would need some sort of bespoke mechanism to do that, instead of just… Use the extension, or don't use it.
Yeah, I think putting… living it as an extension is… a good idea. I… don't think I have the time, unfortunately, to sponsor it right now, I guess… if you haven't pushed it already on Auto Collector Dev, Could be a good idea to… also mentioning Inter Sudan.
People that are not in this meeting that could sponsor it concede?
**Ilia Petrov** 20:50 I've posted in… yeah, I've posted it on Auto Collector desk.
**Pablo Baeyens** 20:57 Okay.
**Ilia Petrov** 20:58 I feel… yeah, I feel… I'm a freaking quicker goal.
I can't find a threatened to send it.
**Pablo Baeyens** 21:14 Okay, So I think… This is… What you had to do, and now it's a matter of finding a sponsor.
Let's see if… If somebody volunteers, I'm… Yeah, I'm happy to help you with the process if you ping me on Slack, if you're not able to find somebody. I think this is, like, a good… component.
John.
**Ilia Petrov** 21:52 Thanks.
**Douglas Camata** 22:04 Cool, I see if there are no further questions, I can go next with my point.
So, I wanted to talk about this, component donation proposal that I wrote.
I think yesterday, I already shared in Collector Dev China as well, but I thought about bringing it here for some additional, visibility.
And a TLDR on what this component is, is… A conf map provider.
Based on the Thanos Object Store package.
Which is… a kind of… higher level abstraction over different object storage providers.
So, for example, they support GCS, S3, Azure, OpenStack Swift, among many others, including even local file system, which is a great part for testing, by the way.
We have been… we started to have some interest in a component like this within Coralogix, because we want to have… we wanted to support, other… we wanted to have support for other object storage providers. Particularly, our interest was in GCS.
And, we thought, why not use, something that will support many other providers in case we also have to. It's… it's a… potentially less work than, you know, creating and maintaining a separate component for each one of these providers, or just relying on a potential S3 compatibility layer that could have its own… its own Gotchas of how it is implemented.
So this is how… We started with this component, we have it hosted in, In our repository we own, we are building it into… A build of the… OPA… of the supervisor, of the OPA and P supervisor.
And, And there is… is… is where we use it so far. One thing that could scare some people out a little bit.
is that the Thunder's object store package depends on, Minio client, and some of you might know that Minio had a lot of, let's say, polemic, discussions around licensing, but the client library is Apache.
So there is no, no licensing issue there.
One… One very important downside of adding this component to any distribution is that the binary size increases considerably. You will see in the description of the issue that I had to increase the binary size limit test that exists on the supervisor from 35MB to 61, so that is… something to take into account that I understand could be a big problem for including this component.
And, another detail is that this package has its own configuration file, so that you can configure, which provider do you want to use, and many, many different things inside each provider's configurations. So… So, I added, I am using an environment variable.
That, indicates where this, this configuration file is.
And it can… it can operate.
Without the file, if defaults are good for you.
So, at least it's… it's easy to use.
So… so yeah, there's… all of these things I am mentioning are written in the issue.
I am looking for other people interested in being co-donors slash sponsors, and also, of course, any feedback or opinion, you know, maybe the binary size is something that We don't want to have go up that much, or if that's okay, and there are other implementation details that would have to be changed, Please feel free to comment.
If nothing comes to mind here, just please leave a comment in the issue. I think that would be the best place to talk about it, even better than in my SIG message.
And if there are no comments right now, that's all from my side.
**Jade Guiton** 27:54 Thank you very much.
Are there any… Other impromptu points today?
**Pablo Baeyens** 28:15 Please tell your… Or mates that we've changed the Zoom link.
Guess that's my only ask.
Yeah, it's been the number one problem with the migration of the Zoom links, people joining the old ones, so… I guess we can wrap it up here.
See, you know, internet?
Mike, thank you.
**Douglas Camata** 28:49 Bye-bye.
**Jade Guiton** 28:50 Carry on.
**Ravishankar Gnanaprakasam** 28:50 Bye, everyone, thank you.
