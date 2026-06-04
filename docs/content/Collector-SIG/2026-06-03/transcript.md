SIG: Collector SIG
Date: 2026-06-03
Duration: 72 minutes
============================================================

## Zoom Recording Transcript

Alex Boten 00:03:37 Should we, should we get started? Pablo, do you want to go through the high priority stability phase one issues?
Pablo Baeyens 00:03:44 Yeah, when I left, I added one thing, which is the DRBC above the bots.
Migration, since that's important for… exporters, whoa.
just… Please take a look.
Then, I think… Another thing worth mentioning is… the… Kubernetes Attributes Processor is… Let's see if I can find… Shoe.
But, It's going to transition the, Semantic conventions used to be the… ones… that are… No… I think, stable are the, specification. So, for example… Let's see… Here, it… Do you have any feedback about this, or want to… Say anything about the… Process on what we should do.
Please leave a comment either on that issue or on the parent issue.
I think those two are the most important.
Things, but… If somebody else has something else.
Happy to be corrected.
And I guess with that, we can… want to… the OBI UPF.
district proposal.
So that would be Nimrod.
Nimrod Avni 00:05:59 Yes. Hello?
I'm here.
Yeah, I don't know if, either one, like, if I should share my screen, or some, someone here will share it, the GitHub issue.
Jade Guiton 00:06:16 Or to change the screen.
Nimrod Avni 00:06:19 Yeah, I can share it, one sec.
Yeah, all open… this one.
Yeah.
So… Hello, everyone.
just wanted to… to bring this up to more discussion, because it's been open for a couple weeks now, I think. I'm not sure how… if everyone's familiar with OBI, which is the OpenTelemetry EVPF Instrumentation.
Already, being able to, to run it as a, collector receiver.
We have some examples inside our refo, but there's no… official, auto distribution that supports Obi being a receiver.
And… I think there was an attempt by, I think by Tyler.
to put it in the, collector in SRIB, and I think there were some pushbacks because Needing to rework a lot of the config there to… Being more generic and play better with the… The, the collector contrib.
But I think, while this happens, I think we can… we can maybe… have, a separate collector distribution, either, just an Obi-Wan.
And similar to the hotel profiler distribution, that, there's already one.
or some sort of a generalized EBPF collector, or, like, a privileged collector that runs privilege workloads that include the EDPS, Profiler, Obi, and maybe even other ones, like, SystemD, and, Journal, like, everything that needs, like, privilege.
I think many customers will want all of their privilege workloads inside a single collector distribution.
So I just wanted to bring it up, I think there was some discussion from… Florian here, which is part of the profiling SIG. The… I think the only pushback is that OB can't be directly built with OCB, because it needs to prefet some, eBPF-generated, like, generate the eBPF binaries and it… you can't just, link it to a Go, just to a Go package, but there is a… Kind of a straightforward, Way of, of doing it.
wait, let me, Yeah, there's kind of a straightforward way of doing it with some prefetch.
script.
Fetching the, fetching all those binaries, and then doing this kind of a replace Inside the manifest in order to build it.
So I just wanted to bring it up.
If anyone has any doubts or any, like, opinions on that, just wanna try to push this.
Pablo Baeyens 00:09:41 I would personally prefer not to have separate distros for the different eBPF things, I would prefer to have a single… Can you find one?
I understand that it needs to be different from other districts because of the privileges.
required.
I don't see the… I'll leave you on having them be in separate distributions, if somebody wants to… Run them separately, they can… Or they should be able to use OCD for that.
Nimrod Avni 00:10:16 Yeah, you could just enable only specific receiver, like, only the OB receiver, only the profiler receiver, and you can… Like, fine-grain control the privileges each one needs.
If you want to do it that way, or you can combine them, especially that… Obi and the profiler already have some sort of, like, com… like, basically the profiler can use OB's, trace… context to enrich its profiles with trace context, so that, like, if you run them together, they can, like, benefit from each other. I think it maybe makes sense to have them both in the same distribution, but if people want to either separate them or only enable one of them, that's pretty easy.
And I mainly wanted to know how can I, push this forward, if I need any more approvals from anyone, anyone has any objections, I can open, like, a mock PR of a new distribution.
Pablo Baeyens 00:11:24 So, provided that other people agree with me, I think the first step would be to get, agreement with… The profiling people about… unifying things and ironing out any… any issues there.
Nimrod Avni 00:11:44 Yeah, I think we have, I talked with, Florian.
And he also came up to the OB FIG, and I think he agreed, but I can get, more… a consensus.
Confirmation from them, and ask, people to… comment here.
Pablo Baeyens 00:12:05 Yeah, I'm also a bit concerned about that last comment on, like, I… Don't know the specifics of what needs to be done to build Obi, but I… Would be surprised if Go generate, wouldn't be able to… handle anything, and then we could just use OCB?
I think… To me, that seems something important, too.
Abdullah here.
Nimrod Avni 00:12:39 I think there's… I can summarize the whole discussion here of, like.
For it to completely work with, Go tooling, we need to commit all the eBPF generate binaries to GitHub, which, after considering it, it will just, be a lot of overhead on, like, stuff… on, like, Git management, because it sums up to, like, a couple things, like, 12 megabytes compressed, something like that, and saving it for the full history.
might cause to slow down some pulls, and I think we ended up deciding on Doing the solution of just uploading those artifacts and allowing, Yeah, basically allowing, some pre-built script to download them, and doing it with the replace to make it to work.
And there's still, like, some examples in the OP repository of How you actually do it.
But this is a good example here of… Doing this replace, and doing this… basically this, this, like, prefetch script.
Like, I don't know if that… unless someone has a PIN, like, if it should be a blocker on… doing, like, having Obi as a receiver, or not?
Pablo Baeyens 00:14:06 That is not a pattern that we, use with any other component right now, so I would be wary of… Opening the door to that without a good justification.
I… I… I mean… I don't think it is out of… The conversation to discuss changes on… OCB2.
Support this if we needed it.
But… I'm not sure we would even need that.
Raven?
Braydon Kains (Google) 00:14:39 Does it have to live?
in releases?
Is it the end of the world to… have a… an eBPF collector, Separate repo with its own… Docker Hub repo, that sort of thing.
Nimrod Avni 00:14:58 For me, I think it's fine, as long as it's some… like, an official distribution that OTEL manages. I think it can even live in a different repo, but, I just don't know if there's any collector distributions managed in different… in a different repository than this one.
But I'm open to having it in a separate place, as long as it's something that, like.
we can say that this is, like, the official hotel distribution of… of, like, eBPF-based components, or something like that.
Braydon Kains (Google) 00:15:32 Yeah, I can't speak for the full collector group, but from my perspective, like, if this was… a separate repo where people were guided to, if they want an eBPF or an OB-enabled collector, they could go to this other repo, which has its own set of maintainers and its own sort of, like.
maybe not full sig, but, like, its own maintainers and its own way of operating that is separate from the releases repo that the collector SIG operates. It doesn't… it doesn't seem that bad to me. I guess the… The challenge is you'll have to… you'll kind of need to go through the whole, like.
Process with the community to, like, say, this is why we want a separate repo.
This is why it doesn't fit in the releases repo.
Like, I don't… I don't think anything… I looked through this a couple weeks ago, just for something unrelated, I just happened to be seeing all the… all this work for, like, prefetching the generated binaries and stuff, and, like, it doesn't seem… that bad, but it's also completely unique to this problem of trying to distribute an eBPF-enabled collector, and maybe it just… deserves to live in its own repo that is separate from the one managed by the collector, SIG.
Douglas Camata 00:16:47 I think, I think, given the reasoning.
I'm not sure if I think it's a good idea to distribute it in a separate repo, because… as someone that works sometimes in the releases repo, I know how tough it is to set all these… all these things there up.
And I'm not sure if it makes sense to, you know, do a whole separate thing for… for an eBPF distro, or an OB distro, whatever we decide to call it, or whatever it goes. I think, to me, the biggest question is.
Do we really want… to have this, distro with OB.
Yes or no? And then, let's see, okay.
what do we need to achieve it, right? Like, do we need, OCB to… to be changed, and do we want to change OCB, or can we do it in a different way, because I think first we have to answer, right? Like, do we agree that we want an OB distro, or… or we don't want. And then we can see maybe how we can make it happen. I think it would be… nice if… agreeing that we want OB in a distro, it is built in the releases repo. Maybe it needs something different than OCB to be built, but I think the release repo could accommodate it.
Like, the fact that releases repo is using OCB is just a detail.
that could be different for different distros. We have different jobs for different distros, we could have something custom if we need.
Braydon Kains (Google) 00:18:48 The problem I see is that, like, we can answer yes or no, do we want an OB distro, or an EBPF distro, but… It's one thing to say, that sounds like a good idea, and another thing to say.
okay, this is what we have to do, we have to totally break every way that every other distro works to make it work. That sort of influences the decision, and… It looks… pretty different to me. I… So, I don't work in the releases repo specifically, but I work on… our, like, Google-built collector, and, you know, I have a tool that, like, basically generates everything that the releases repo does for the most part, other than the GitHub actions.
And I'm not sure what… what is super important about it being part of the releaser's release train versus it just being its own thing for the people who want to enable the eBPF solutions specifically? Like, I think if someone wants an eBPF collector.
it's already sufficiently distinct from everything else in the releases repo. So maybe I'm just missing, like, what… Why it's important that it lives there versus a separate repo.
Douglas Camata 00:19:59 I would… I would just say, for the sake of reusing all the automation and infrared that is already there, nothing much besides this.
And, you know, people are maybe used to, oh, we need to do something with the… distributions that are released, we go there. Oh, we want to see the… all of the artifacts of release, version X, we go there and everything is there, right? So… It… it is concentrating all of the automations, it's where all of the releases are published, so mostly this, from my point of view.
Braydon Kains (Google) 00:20:43 I don't feel strong enough to give a hard no, but I find myself not… agreeing.
Mostly just because this feels sufficiently distinct from all the… all of our other distributions. Like, this is a collector that to my understanding, has to run privileged, and comes with a lot of extra stuff that our other distributions don't. Like, it would be shaped differently for that reason. So, like, the people who want an eBPF collector They already know they need something that is different than everything else.
So it feels fine for it to be a separate repo, but… I'm not… a releases maintainer, so I… I can't say no, that's just my… that's just my opinion, though.
Douglas Camata 00:21:30 Yeah, I also don't hold my opinion strongly we should just consult more people and see what else they have to say, what other very valid points they could bring.
Pablo Baeyens 00:21:51 the… Sorry.
Nimrod Avni 00:21:53 Sorry, go ahead.
Pablo Baeyens 00:21:54 my closing thoughts in 10 seconds. From my side, I think… because we already have the eBPF provider, It feels like… this does fit, in principle, as something that could be on an EBPF distribution. The thing that I feel hesitant about is I don't like that the build process is completely different, brings How a lot of implications work.
Maintenance, basically.
Nimrod Avni 00:22:29 Okay, yeah, I was just about to ask if, one of the reasoning to have it as a different repo, is it, A, the fact that it is, like, a privileged collector that needs to run in a separate manner, because to counter to that is we already have the EPF profiler there, but if the argument is that the build process is different.
I can… I think we already, like… talked… talked a lot in… inside the OB, OBSIG regarding the trade-offs of, like, how we can make it work with OCB, but… It's just a matter of if it's a blocker, like, that we were saying that it's probably, like, it can't be there until it is, like, part of the normal build process.
Then we can take it again with either changing how we do it, or maybe adding some ability to OCB to, for example, take the source from an external place that is not, like, not just Godamat, but maybe, some external source.
And then it… then it could be, like, part of the normal conflict, so I can do some more exploring there, but just want to know which part exactly is the… is the thing that, is blocking us, and I can also look into it regardless.
Braydon Kains (Google) 00:23:52 You can ignore the privileged comment. I think I've already lost that fight, because the eBPF distro exists, so ignore that part. Focus on the build process part.
Nimrod Avni 00:24:05 Okay.
Okay, so I, I, I'll, I'll, I guess I'll go check again and see if there's either something we can do, either in OB, or maybe some donation to OCB, also need to see… What's the process there, if there's some other way to get that?
And yeah, I guess I'll update the issue and the suggestion there, if there's any update, and also get some More confirmation from the profiler people, if that makes sense to have it in the same… distribution.
I think that's the… I think that's a good… Thank you.
Pablo Baeyens 00:25:04 Thanks.
Next would be Thomas with the AWS Secrets Manager extension.
Thomas Baldwin 00:25:12 Thank you, Pablo.
Hi, my name is Thomas Baldwin. I am an engineer with Bloomberg. We work within the public cloud domain. We are also… I'm here with two of my colleagues, Mike and Larry. We're also part of the OpenTelemetry Bloomberg Mentorship Program, for some context.
Let me go ahead and share my screen, if that's okay.
Alright. So, I'm, I'm reaching out to… Find someone, an approver or a maintainer, to go ahead and help us move forward with this and sponsor this extension we are proposing. And what this extension does is it goes ahead and it resolves an issue we raised. And the reason we raised this issue, it's around credential rotation, which is a policy that we have to adhere to within our company.
we rotate secrets on an interval. I don't want to say the interval out loud, but it is a pretty frequent, periodic interval, and so one thing we've done on the back end is we've made sure that these secrets that store in AWS Secrets Manager or Azure or GCP Secrets Manager, there is a process where it's continuously kicked off and rotated on the backend. However, within the VM itself where the collector is running.
it needs to be updated internally, and so the way we solve this for ourselves is, instead of using the existing provider that exists for Secrets Manager, what we notice is it would have to restart the entire agent.
we built an extension to go ahead and do this. And I know that Part of donating a new component means you have to show that it's been battle-tested and used, and so I did go ahead and Well, one, I did go ahead and I wanted to share a quick architecture diagram we've attached to this component as to how it works and how it's able to do the refreshes and do it concurrently using an atomic store. And then lastly, I did take some screenshots. I did have to blur them out because there is… sensitive information on them, some information we wouldn't want to share, but just to kind of go ahead and show usage of how this is being used today. And so, within these Kubernetes clusters that are running.
they are all running our, OpenTelemetry collector using our extension, and we have our own distribution here at Bloomberg of the Agent.
any extension there for as well. And so, we've been running this for a little over a year. Within Kubernetes VMs, I think we have about 450 VMs that have been running this, and then we have actual customers just using VMs directly, where we have another 40 or so, and so… This is something we've been maintaining ourself for about a year or so, and it's something that we thought would be nice to go ahead and contribute back to the community, and we ourselves fully plan to go ahead and maintain this. But it would be nice to go ahead and share this with others and, welcome contributions.
As well.
And I will… I guess leave it at that.
Blake Rouse 00:28:27 But you said this was done, as an auth extension for the ability for refreshing, I see this as AWS-specific would it… Does that kind of pattern apply?
to other clouds, or that's an AWS-only pattern?
Thomas Baldwin 00:28:45 So we actually do this for Azure and GCP as well. However, I know there is a requirement when you donate a component that it has to be battle-tested, and we've only recently rolled this out to Azure and GCP, and therefore.
while we did raise PRs for those, I'm not presenting those to be donated right now, and I will wait till those are battle-tested and have as much usage and, you know, time as we have had with AWS.
But it… the same context does apply to Azure and GCP. We do do the same thing.
Blake Rouse 00:29:17 I mean, my first thought is just, logically, I don't know if that… like you said something about Secrets Manager, I don't know anything about it, so I'm just… just from an outside person listening.
Is the Secrets man… is there a secrets manager per cloud, or there's, like, one secrets manager?
That's multiple clouds. I'm just wondering, from the standpoint of using this, does this make sense to be each one of them Extension, or does it make sense for there to be, like, a cloud auth extension that… you define which cloud you want it to be. That's just kind of my thought right now.
Thomas Baldwin 00:29:55 Yeah, that's a good… that's a good question, and it's something we originally thought about. Originally, we were going to contribute this back to the basic auth extension, but there is a Secrets Manager per cloud. The reason we went separate is because we didn't want to add the SDKs and the dependencies to other extensions that the customer sorry, the engineer may not need, because say a customer's only using GCP, they may not want the dependencies for Azure and AWS as well, which is why we broke them out separately, and how we arrived at this. But we're happy to be wrong, and we're open to alternatives and any suggestions.
I see, I believe.
Blake Rouse 00:30:34 That sounds like a valid reason.
Thomas Baldwin 00:30:36 Yes, and as part of this work, before we were able to do it, there was some internals from the basic auth extension that we worked with another engineer to go ahead and break those out into helper functions so we weren't reusing code, and that's what, this PR was related to.
With respect to, the basic off-shared logic. I see Braden has his hand up, though, Happy to… happy to answer any questions.
Braydon Kains (Google) 00:31:02 Yeah, I just thought I'd mention that in terms of, like, there being a secret manager per cloud, there's some… precedent for… us doing, like, one… one component per cloud, because in Config Provider, we have a Google Secret Manager, Config Provider, and then AWS… it doesn't say AWS, it's just called Secret Manager Provider, and we've already said that maybe we should rename that when we were introducing the Google one, because it's kind of confusing, but anyway. This is kind of becoming, a common pattern in Contrib, in general, is that, like.
like, I always kind of thought that we should do things like a resource detector processor, where a resource detector has all these sub-components.
of the… like, this is the GCP Resource Detector, the AWS, the Azure, and they all live under one component.
But that has… caused a lot of problems for people who want to build slimmer binaries with less dependencies. Basically.
Thomas Baldwin 00:32:01 Yeah.
Braydon Kains (Google) 00:32:02 basically what Thomas pointed out. So, there is precedent for each of the secret managers having their own component, as much as it kind of… Sucks on the maintainer side to have.
3 different components that largely do the same thing, but we've… we've… implemented that pattern in, like, all those new serverless extensions that are coming out. There's, like, 3 different… S3 compatible exporters. It's not… it wouldn't be the first time we've done it, so I wouldn't, like, push back on it, I think.
Thomas Baldwin 00:32:37 Yeah, I think that makes sense as well.
Braydon Kains (Google) 00:32:40 For what it's worth, I would like to find a way for config provider watch to not have to restart the whole graph.
So that would be kind.
Thomas Baldwin 00:32:47 Yeah, that would solve it.
Braydon Kains (Google) 00:32:48 Not a problem.
Thomas Baldwin 00:32:50 Yeah.
Braydon Kains (Google) 00:32:50 Complicated problem, though.
Thomas Baldwin 00:32:52 Yeah, yeah.
Braydon Kains (Google) 00:32:53 That's kind of what Blake's… yeah, Blake's RFC is basically doing that.
Blake Rouse 00:32:58 Yeah, that RFC was, merged, so it's just a matter of getting… getting the work done now, but yeah.
Thomas Baldwin 00:33:05 And so… sorry, go ahead.
Ravishankar Gnanaprakasam 00:33:07 Thomas, sorry to interrupt. So, one quick thing. So, this, extension that you're proposing is more around like a pool-based model, right? You will… you would keep polling the secrets Manager, or how does that work?
Thomas Baldwin 00:33:20 Yes, that's exactly correct, and the user has the ability to go ahead and configure the refresh interval, is what we call it, where it will pull, on a basis. And it does it on a separate thread, so you're not taking up main thread time as it's doing that.
Ravishankar Gnanaprakasam 00:33:37 Nope.
Cool.
Thomas Baldwin 00:33:43 It sounds like, though, Blake, if you are to merge and figure out the work as to how to go ahead and change secrets with the, Providers without restarting the agent.
I guess there would be no need for this then, right?
Ravishankar Gnanaprakasam 00:34:02 I mean, like, the… Sorry, sorry, Blake, yeah, go ahead.
Blake Rouse 00:34:07 Correct. If it was a config provider that would, you know.
call the channel to say, hey, something's changed.
that would initiate a reload, and only reload what has changed.
Once we get to the end state of that.
And the collector.
Thomas Baldwin 00:34:28 Got it. And this… In this case, if the config provider, it's the same config, but it has gone ahead and fetched a different secret value, would that cause it to restart, or is it only if, like, the explicit strings in the config have changed that the user is filling out?
Blake Rouse 00:34:49 No, it would be the computed config, so it would be the config.
After the rendering of… Like, that piece.
Thomas Baldwin 00:35:00 Oh, so it would include the secret value, then?
Blake Rouse 00:35:05 Don't hold me to it, but it should. I'd have to look. Got it. It should, yeah.
Thomas Baldwin 00:35:11 Got it, okay. So then I think we would still need this, because it sounds like the collector would still restart.
If that's the case.
Maybe that's something that I can… well, if… if… maybe I'm misunderstanding you, but if… if… the collector has a secret, it starts up with a secret, and it checks, say, 3 days later. And it gets another secret value, and it pulls that in.
If the computed config has not changed because it's a different value, would that cause a restart of the agent?
Blake Rouse 00:35:42 But… Well, that would consider… that would be considered a different config, right? It's a different value.
Thomas Baldwin 00:35:47 Okay, so then it would restart.
Blake Rouse 00:35:50 We would restart only what changed.
Thomas Baldwin 00:35:55 Got it.
Braydon Kains (Google) 00:35:56 Yeah, so I think it would… it wouldn't replace… it wouldn't replace this, unfortunately. I think what would need to happen would…
Blake Rouse 00:36:02 I'm confused, I think I would.
Braydon Kains (Google) 00:36:05 I think they don't want any components to reload upon changing a value of a secret.
Thomas Baldwin 00:36:11 Yeah.
Blake Rouse 00:36:11 Oh, okay, sorry, misunderstood. I see what you're saying.
Thomas Baldwin 00:36:14 Yeah.
Blake Rouse 00:36:14 Yes.
Thomas Baldwin 00:36:15 Yeah.
Blake Rouse 00:36:15 requirements.
Thomas Baldwin 00:36:15 Amazon.
Braydon Kains (Google) 00:36:18 I would like to see that sort of thing work. I don't know how it would in confap, because we… it would basically just be, like, a dynamic… a dynamic value that can change throughout the life of a confap without changing the contents, and I'm not sure if the current implementation would Make that possible, but we've been encountering other scenarios where we would like.
Pablo Baeyens 00:36:41 I don't think it… Yeah, I don't think it would work in Comp Map. Maybe it could be done, like, specific components that Clara support for… listening for config changes, and they handle the reload in their own way. That could be a thing.
But from Confmap itself, I think that would be basically doing a version 2.
Jade Guiton 00:37:07 Potentially, this could be an extension interface.
Like, a conflict provider could also act as an extension that can, you know, dynamically provide values.
Blake Rouse 00:37:28 Yeah, there's a… there's a… in the RFC for partial reload, there's a notion of a reload interface that a component could Implement, and if they implemented that interface, they would be able to handle a config reload on their own.
So if your component was to want to know about those values changing without being restarted.
At the end of, hopefully, partial reload support in the collector.
it would have the reload called on it instead of it being stopped and started. And so then you could do it.
Internally, without, you know, Restarting the component.
Thomas Baldwin 00:38:11 Got it.
Blake Rouse 00:38:12 Would that remove the need for this, or still wouldn't remove the need for this?
Thomas Baldwin 00:38:17 I think as long as the receivers and the exporters, don't… need to reload or restart as a result of the value changing? That would… that would remove the need for this.
But from… the reason we found it as an extension played nicely is because the nice thing about the extensions is it only needs to reload, you know, where the authentication extension is being used, and so that was… It tied really nicely into there.
But if we're able to get that same functionality, we have no bias towards doing it that way.
Ravishankar Gnanaprakasam 00:38:55 Also, one another thing, Thomas, I'm not sure… I hope you would have checked it, but… I'm just trying to find the reference, so there is something I remember seeing in our collector, there is something called a watcher interface that was exposed on a.
Thomas Baldwin 00:39:07 Yes.
Ravishankar Gnanaprakasam 00:39:08 level, if I'm not wrong, yeah, exactly. So… Because there are other issues that I remember seeing in the same report regarding Postgres password file rotation and other things.
Which has a similar use case of, you know, pulling the file… pulling from a different, source, or from a file watching and things.
I… I mean, like, more than two use cases, like.
Maybe we need a different, like, someone was suggesting to have a watcher kind of a thing, notifier, something like that.
Not sure if Watcher will solve the problem here, but yeah.
Thomas Baldwin 00:39:48 Yeah, what we observed with the watcher specifically, and I believe we did list it out as an alternative we had considered, is that the flow would be that the on ResolverOnChange sends the events to its watcher channel, the config provider watch exposes that channel to the collector, collector run receives it, and calls reload configuration.
And then reload configuration, unfortunately, calls the service shutdown, which would shut down every receiver, processor, exporter, and extension. And then, at that point, the setup configuration component would recreate everything.
Ravishankar Gnanaprakasam 00:40:22 Yeah, I think the… I remember seeing the current implementation is, like, reload the whole, component graph altogether. But yeah, I think Blake's work will probably, simplify that altogether.
Blake Rouse 00:40:37 Correct. My work is exactly to short-circuit that, to only restart what has changed. So in this case, if it was an exporter that has a new password, it would just restart the exporter.
And everything else would stay running.
Thomas Baldwin 00:40:51 Got it. And what would happen to the, stuff that's, like, held in queue at the time when the export is restarting? Would we lose that? Or if we're… assume we're not writing to persistent storage of the queue, would that be lost while that's restarting?
Blake Rouse 00:41:08 So it would be called… so it would be… the exporter would be stopped, so, like, stopped would be called on the exporter, and every event that is there would be, Basically, contacts canceled, back up to the caller.
And so then the caller would have to then retry upon it restart and being reconnected.
Thomas Baldwin 00:41:27 Got it.
So then, in theory, we shouldn't lose any data when that happens.
Blake Rouse 00:41:32 Not lose any data.
Thomas Baldwin 00:41:37 Okay.
Blake Rouse 00:41:39 Unless there's a bug in the receiver or something, where they don't handle the context cancel retraft or something, but yeah.
Thomas Baldwin 00:41:46 Got it.
Awesome. Blake, is there anywhere we could maybe follow along on the work, or even help contribute to it? Do you have any, you know, working branches or anything like that? We'd be happy to help out.
Blake Rouse 00:41:59 Yeah, so there's actually two working branches on the… the RFC's merged, it's in… it's in core, you can look at that, that's where I would start. And then there's two working branches that kind of existed before the RFC, and I'm working to bring those back now, the first… the first phase, as you'll see in the RFC, is just support at the receiver level, so we'll just support restarting receivers, so adding new receivers, removing receivers, we'll just work at the receiver level. And there's a PR for that. I need to clean it up and get it, like, ready for, like.
review, I haven't done that yet. And then there is a second PR that, does, like, as, like, a full POC implementation of the whole thing toward… to the end.
So, that one will be used as, like… that's kind of like a… give people an idea of what it will look like, and then we'll take that and, split that into the phases, basically. There is actually a third PR that I could send you, if you just want to, like, message me on the Hotel Collector's Slack.
Called a gate component, which is a… What you will see in the RFC is an alternative implementation, and I haven't… you don't need that for Phase 1 of the receivers, because the receivers are the first link in the chain. They're not, like, in the middle, like processors, or at the end, like exporters. So… There's a notion of a gate, which allows, basically, the collector to pause the flow of events, as you were describing, through each consumer.
And that will allow us… hopefully will allow us to swap, let's say, a processor bid pipeline without stopping and restarting the receiver in front of it.
And so that applies for that exporter case that I was talking about. There's two ways of doing this implementation. The first way is that if the exporter changes, we stop the exporter, the processor, and all the receivers.
Or we go down the second implementation, where we don't need to restart or stop any of those. We basically kind of Just pause the flow of events, And that's blocking on the callers, so, like, it, you know, it just pauses, stops the exporter, restarts the… starts the new exporter with the new config, reconnects it, and clicks, and then basically says resume, and then the event starts rolling again.
Thomas Baldwin 00:44:29 Got it.
Blake Rouse 00:44:29 So, yeah, that's kind of where we are in this journey.
Thomas Baldwin 00:44:34 Okay, that's awesome. I'll definitely, reach out to you on the, Hotel Collector channel.
We'd be happy to help.
Thank you so much.
jmacdonald 00:44:49 I wanted to ask a question to see if I understood this conversation, which I think I did, and mainly it's about the extension granularity, and I wanted to see if I understood correctly. So, it sounded like we were talking about basic auth extension, and then we were talking about AWS Secrets extension.
And I heard that Braden's point, that basically all the clouds have these secret extensions, but they're not the same exactly. And… what I think I heard is that, I mean, we're still doing basic auth extension, it's still… the auth mechanism is still the basic auth, and it's the fact that we have to get a secret from somewhere that is the change that's happening here. It sounds to me like we could make an extension called, like, Secret Getter, or Secrets, access… extension, and then we could have a secrets Access extension for AWS and GCP and Azure and so on. And then we would only be using the basic auth extension. Now, the pros and cons are that we have more extensions in total, because we have to have the basic auth and the different secrets extensions. I'm not sure whether that would be better or worse, but I wanted to make sure that was the framing At least, that we have here. Have you thought about separating or making a new extension for secrets?
Thomas Baldwin 00:46:03 Yes, so, I mean, that is what we did, is, the flow originally was we were just gonna raise the PR to the basic auth extension to add in the AWS one, and we realized, hey, why are we adding dependencies to this that they don't need? And, we built an AWS Secrets Manager extension. There was a lot of overlap from some of the internals from BasicAuth, so we raised a PR to move those into helpers.
And we… then we incorporated those into the AWS Secrets Manager extension. And then we did the same thing for Azure and GCP as well. The reason I didn't bring up Azure and GCP is those haven't been tested nearly as long in production as AWS has.
But yes, that's… that's where we're at. But we also did notice there is the config map providers for AWS GCP, as well. It was just… the main limitation we ran into is The whole exporter was shutting down and restarting if we changed the values.
Blake Rouse 00:46:58 I think that… I think that came differently, though, right? What you're saying, is that… more like the file storage extension is what you're kind of leaning towards, right? The design?
Josh, you're saying… you're saying.
You would just use the basic auth extension, and then it… you would point it to the AWS Extension.
And so it would use that extension to get its basic off, and so that way, you don't actually… implement a… AWS basic auth extension, it's just, like, an AWS Secrets extension that the basic auth the extension pulls the data from. Is that what you're describing?
jmacdonald 00:47:44 That is where.
Thomas Baldwin 00:47:45 Oh, I get it.
jmacdonald 00:47:46 Yeah, I'm more or less just promoting the idea that the extensions are powerful, and we can create new APIs when we need them. It's just a thought.
Thomas Baldwin 00:47:57 I get it.
Would that be worth exploring, even with the work that Lake is doing?
jmacdonald 00:48:06 I don't have an opinion.
as to the pros and cons, it sounds like these are such small components, like, basic auth is so simple that maybe it's not worth factoring it twice, you know? Like, having a basic auth extension with a sub-extension for secrets may be more trouble than it's worth. I just believe it's possible, and it might be worth considering at some point.
Thomas Baldwin 00:48:27 Got it.
Well, thank you so much.
jmacdonald 00:48:45 I think I have the next item on our agenda.
I couldn't find it.
And… So, hi everybody, I'm Josh McDonald.
I have taken up this task, which I'm excited to talk to you about.
To try and help with the batch processor migration.
So, this is an RFC. I've had quite a bit of review on it, but what happened was so much review came in telling me it was too complicated, that I… almost rewrote it. So it now has been largely rewritten with feedback from the reviewers, and I'm here to talk about it.
let me briefly walk you through it so that we can discuss. I know there's not much time left.
But the, the main idea here is that, what we're trying to do is… I will skip over the defects and, like, what the new stuff is, because this has been coming for quite a while. What we want to do is take the batch processor out of the core, replace it with something new that will be different and breaking from the perspective of a user who's migrating, but most users should not be using batch processors. So, The idea is that by default, users will take away their batch processor, and most of them will begin using exporter helper batching.
So it's a little hard to read in this form, but… but basically saying, I've changed some of my opinions from the last review, the reason I got involved in this long ago was that I want… for my particular vendor and my use case that I've had in the past, I wanted error propagation, meaning I really, really want to know if the backend is giving me errors. I want to see that propagate backwards all the way back to the SDK. Otherwise, it's not clear that… that we're handling overload the way, at least, that I wanted to. So, but I have backed off of that. So, so error propagation will… would remain off by default at the exporter helper, and what that means is that you're allowing data to enter a queue, even if it's just an in-memory queue, and then return success.
We do have flags to change that behavior, but I'm not proposing we change that.
I am proposing that we enable this flag called block on overflow by default. It is debatable, and there has been a position in the other direction, so we'll come to that at the end. Block on overflow means you're going to pause and wait for your context deadline to be exceeded when the queue is full, as opposed to failing fast, and we'll talk about that in a bit.
Lastly, I'm proposing that we enable batching by default, so that if collectors are run with out-of-the-box configuration, most exporters will just get batching.
Since we're no longer supporting a sort of standard batch processor.
For the record, the reason… the proposal is for a new processor called QBatch Processor. It's a simple name change. It contains functionality equivalent to the old batch processor, but it's implemented using the newer code. It's way more maintainable for us. It's also still a sort of niche case. You have to know why you're doing this, and we will not advertise the QBatch processor nearly as much as we used to advertise the batch processor.
So, I've stated the reasons why people ask for a lot of comments on this. Why some exporters might keep what they have, poll-based.
order-sensitive, built-in queuing is another reason that people have. So, Let me skip over. One thing we're trying to avoid is double batching, meaning it will cost users if more than one batch processing is being applied.
So, I… I'm asking for you to review this. This is the sort of quick summary. So, there'll be multiple phases. Phase… phase one is… would be the next few months. I will be doing some work to get this new processor created.
And a few more things. We're gonna get the documentation ready for some sort of go moment, which would be, I guess… I'm proposing August, so that would be the 1.58 release.
6 releases later in October, we would begin to remove the batch processor from the core manifest, meaning it will not be part of the build anymore, the core distribution or the contribution. Does still exist in the source code at that point, so that if you're building a custom distro, you get more time, you can still keep building with it, but we've added warnings. Warnings that when you have two batch processors would stay in effect, so that custom builds, or still using the batch processor, would get warned at that point.
And that's in addition to the 6 releases of warning that the batch processor would be deprecated. So for 6 releases, you'll get those warning that's about to happen. 6 more releases, you'll get this warning where you can't build it from… you can't run it from the core or the contrib build, but you can still build it for a custom build, and then eventually it'll get removed.
So, the work to do up front is mainly documentation, creating this new branch processor. In Phase 2, we deprecate And we do a bit of an audit at that point. There are going to be exporters that want to opt out.
of the changes that are coming, and we'll figure that out at that point. We want to do an exit criteria, so we have to make sure that it's working before we do exit that stage. It would be, like, 6 releases, so… time for us to get some users on board. We already have some testing, by the way, that shows that these two are good, though there have been anecdotal reports that there's some performance differences, so we should make sure that that's been sorted out.
Finally, we removed batch processor, you know, it was just two feature flags for the two separate features. And if I, you know, we can… we can… we can decide not to turn on block on overflow. That's sort of the last thing I want to discuss.
I'm gonna take us back to the feedback, because, let's see… very bottom here, Jad has said the opinion, and I, would be glad to discuss it right now.
I, you know, there's a debate over whether it's best to fail fast or not. In my opinion, systems are a bit more efficient when they don't fail fast.
But there are lots of variables here. So what I'm trying to avoid is a situation where an OTel SDK sends data, the queue says, I'm full, fail fast.
Sends it right back to the SDK, who then tries again with the same endpoint, immediately sending the data back to the same endpoint, which is… which is very easy to see happen. So that you end up sending the data back, failing fast, sending the data, failing fast, sending the data, failing fast.
It leads to churning the CPU in a place where, you know, the request has a deadline. That means I'm willing to wait. The request has a deadline, and I'm willing to wait. I think we should wait. What it does is it slows down the producer. It tells them we're overloaded without wasting the cycles on sending the data again, just simply by slowing down.
So that's my preference, but I… I would… Really rather see us remove the batch processor than, you know.
change the default, so I can definitely be convinced.
That we should, continue to fail fast.
So my proposal stands either way, and I would love to hear a discussion about that.
Jade Guiton 00:56:14 Yeah, I have my opinion, obviously, like, I think the CPU here is honestly not as big a deal as the memory use, because, you know, we're talking about a case where the queue overflows, where that's the most pressing concern.
And I do think that while it would be best to have a reasonable, like, retry after header or something like that.
I think exponential back-off on the exporter side is probably at least, a good… way to at least alleviate the memory pressure. But I would definitely like to hear, like, experiences from other people who have, you know, dealt with deploying large fleets of collectors and have dealt with these kinds of out-of-memory issues and, Export, like, queue overflow issues.
Because, yeah, obviously, it's possible that there are multiple cases, maybe… Maybe in some cases, it's better to have one or the other, and… Maybe my experiences are not universal.
No.
jmacdonald 00:57:24 I would say, also, my experience was several years ago, so some of the… a lot of the stuff has changed since then, and now… nowadays, we have memory limiter extension, which can be set as middleware, which… can block the data when you're running out of memory anyway, which I would strongly recommend in addition to this, but I actually think, Maybe it's fine that we have multiple outcomes here, but it's a little bit chaotic, because we're talking about this retry after header, which is part of the OTLP spec, but I believe the current state is that the OTLP receiver doesn't know how to send it.
And I don't believe that we have consistency on the OTLP, producers from the OTL SDKs and so on. So, whether retry after actually works is a… is a… is an open question.
And you're right that exponential backoff is, is going to help there.
I guess maybe my position is that when you have a memory limiter correctly working, we also have… when I was actually testing all this a couple years back, it was the OTEL Aero receiver, which has an explicit emission controller for memory, so that was before we had the memory limiter extension and so on. So I was always operating under memory limit when I was trying to get the queue to block.
So maybe that's the distinction.
Jade Guiton 00:58:46 Yeah, I think… Obviously, the memory limiter extension will do precisely what you mean, you know, fail fast, so we need to be able to handle that case regardless.
I just think… It's a bit of a blunt tool, the memory limiter extension.
it's hard to tune, whereas… and I mean, admittedly, the exporter helper queue is also hard to tune, but I feel like… If we're gonna rely on the memory limiter extension to avoid blowing up memory because we have all these go routines blocking things.
We may as well not have a queue limit at all.
So… I don't know.
I would like to have more opinions than just… than just us two, I guess.
jmacdonald 00:59:40 Certainly, the conservative thing to do is not to change the default.
And I'm so interested in seeing batch processor removed that I would be glad to just move forward like that. I also agree with you that memory limiter extension is not especially easy to tune, and I don't strongly recommend it. I just know that it's better than the memory limiter processor, which was never working for me when I first looked at it.
And as I mentioned, I prefer explicit admission control, which is… something that we put into one receiver, and I, a year ago, spent some time getting to know this group, and that's where the middleware extensions came from, but we never made it as far as having sort of memory-counting admission controller, which is what I'd like to get to.
So, future work. I think I… I'm starting to feel convinced, just to avoid debate, that we should not, try to change any exporter defaults. That said, your position, Jad, was good. The idea that the processor can keep its differences, meaning we want the processor form, that niche use QBatch processor, to wait for a result.
Basically. And to block on overflow both.
That's… that's how the original batch processor worked, and I think we should preserve that. We can also preserve its original defaults with num consumers equals 1, We can also preserve, you know, its defaults with size, so… so the current… the old batch processor defaults were item-based sizing with 1,000 to 1,500 items, whereas the exporter helper defaults are already different from that. Like, we can preserve defaults.
I don't think anyone's debating on that.
Jade Guiton 01:01:18 Yeah, I think that would make sense for the new one.
jmacdonald 01:01:21 Okay. I'm gonna update my document to make it as conservative as possible. Thank you all.
Ravishankar Gnanaprakasam 01:01:30 Also, Josh, on a minor note, on QBatch processor, are you thinking of implementing the persistent queue as well? Like, right now, the exporter has…
jmacdonald 01:01:39 Yes, so basically the idea, and this is… there was a prototype PR put out, actually last summer, that said that this was the model, is that you're taking the exporter helper implementation, and you're putting it into a processor, where the processor is basically nothing more than two exporter helper features combined, the queue and the batch, which are already sort of inextricable from each other. So every feature of the QBatch processor would become part of this process… Every feature of the QBatch Exporter Helper.
queue sender, we call it, would become part of this processor.
In the future.
I mean, when I created.
In fact, the only thing that was holding us back when I produced that PR last summer was that the metrics coming out of this thing look like an exporter helper, even though it's part of a processor. So the only major obstacle for this work that I'm predicting can be done quickly would be to make it so the exporter helper essentially lets you change the metrics prefix. Like, I don't want the metrics to have the name Exporter on them, I want them to have the name processor on them, basically.
Ravishankar Gnanaprakasam 01:02:43 Yep, makes sense.
jmacdonald 01:02:47 Thank you all. I believe we can move on, and I think, Ravi, you're next.
Ravishankar Gnanaprakasam 01:02:53 Yeah, I just have… need direction for two of the issues that I was planning to pick up this week.
So, one was this, basically for the storage ID thing. So, we have this, storage ID, and there were… two works that would actually help us with that, thing. So, one is, there was an earlier issue where it was proposed to have a separate module, similar to config.http or things, can have a config storage or stuff, and then which can be used across all the components and things.
And I think recently Ivan has, raised a merged a PR for, scalar, attributes in optional.
Which could also be a use case there. So, just wanted to understand if we would still be interested in implementing that, storage implementation as a separate module, or… You know, because that discussion was away long before, I guess, 2022 sometime. A lot of things has changed after that, so just wanted to check on that.
jmacdonald 01:04:12 I apologize, Robbie, I think I consumed all the time in the meeting. Most people have left now, and It means it's hard to give an answer. Apologize for that. I think you, I think… thank you for the links, I… Don't have an answer for myself.
Ravishankar Gnanaprakasam 01:04:35 Yep.
jmacdonald 01:04:37 Would anyone here?
Ravishankar Gnanaprakasam 01:04:37 and…
Blake Rouse 01:04:38 I'm a little confused, honestly. Could you just try… maybe start again, and give more context?
Ravishankar Gnanaprakasam 01:04:45 Yeah, so basically, let me… so there are, two issues. One is basically, you know, we have, storage ID, like, even in Exporter Helper also, we do have this, Let me also share my screen if that can help. Okay.
jmacdonald 01:05:03 I put it up.
Ravishankar Gnanaprakasam 01:05:04 Oh, thanks, yeah.
So, we do have two issues. One is, like, in QBatch, we do have storage ID. This basically helps us to, you know, in persistent queues and things like that, where we wanted to store, the data, we do point to a file storage extension kind of a Component, and that will have all the file path and things, and then it helps us to, you know, point to a file location.
So, Currently, what we are doing is… the file storage extension exists, but a lot of components, right now, what they're doing is they are just, referencing to that storage, ID, or the component similar to the component ID, and then using that, you know, in all the components. So… the proposal that came a few years back is that, you know, to have a separate module, similar to configHTTP, and have a config storage kind of a module.
which can be imported in any of the components that uses this storage extension, and there was a SEEK presentation also, if I'm not wrong, but we never implemented with that.
So, are we still… so the open question is, like, are we, still, you know, interested in that kind of an approach? Because right now, we do have a use case in QBatch for that storage ID.
And, so, yeah, it's just an open question, are we still interested? If it's a no, then what Ivan has implemented recently is the implementation for it.
Yeah, I do see Lake and… Sorry, sweat, yeah.
Oh, sweating is here.
Mikołaj Świątek 01:06:48 Thank you.
Ravishankar Gnanaprakasam 01:06:48 You have raised the issue, if I'm not wrong, yeah.
Mikołaj Świątek 01:06:51 Yeah, yeah, that's why I wanted to comment. So, originally, the reason I raised that issue is really just kind of bureaucratic. Right now.
Every component that wants a storage extension has to do this whole dance of looking through all the extensions, and then checking which one, you know, which one fulfills the interface, and then getting a client, getting the extension, getting a client from the extension, passing in all the things it needs. So, I kind of wanted to encapsulate that.
And…
Ravishankar Gnanaprakasam 01:07:26 True.
Mikołaj Świątek 01:07:26 Also, so they don't all have to repeat it, and also to… normalize the way you set the storage ID, basically. Because this is right now identical in all the components that do it, but it's identical by convention. There is no config struct that they're all embedding to do the same thing. So these are… these were the goals of it, but… I think what you want to do, and I still want to… I still want us to do that, for the record, but I think what your goals are a little bit more ambitious, from what I understood.
Ravishankar Gnanaprakasam 01:08:03 Okay.
Blake Rouse 01:08:04 I mean, does that make a lot, do you think that sounds like what you described, a good RFC? Like, an RFC of how to, like, provide the storage extension across to other components?
And some unified interface, so it sounds like something that would be good to talk about there, and then get that in before that's implemented.
Mikołaj Świątek 01:08:26 Maybe, but I also… I also… I'm lazy and didn't want to write an RFC, which is why it doesn't exist.
I forgot to file this, to be honest, but if someone wants to take up the effort of trying to normalize this, I will happily review and help you out.
I recall…
Blake Rouse 01:08:47 I think all the points you just made are valid, like, because everyone…
Mikołaj Świątek 01:08:50 No.
Blake Rouse 01:08:50 this everywhere, so…
jmacdonald 01:08:52 the config auth package is basically the same idea. It's a config with a single ID in it.
Ravishankar Gnanaprakasam 01:08:59 Yeah.
jmacdonald 01:08:59 I… it makes sense.
Mikołaj Świątek 01:09:00 Exactly.
Exactly. That's what… I think that might have been my inspiration at the time as well. So yeah, I don't know if this needs an RFC exactly. It's, like, codifying something that already exists.
In a way, there isn't really much to discuss other than if you want, like… if you wanted to do this differently, essentially, you would have to do breaking changes and all the components that do it right now, so it's… I would say it's not worth it.
But it's probably worthwhile to write, like, a, like, a more detailed description of how this should work exactly, and what it should do, starting with the issue, and if there's… this is controversial, then we can do an RFC. That's how I would approach it.
Jade Guiton 01:09:52 I think that makes sense. And regarding breaking changes, like, the issue that Ravi linked to about changing to config optional, it would also be an API breaking change, so maybe it would make sense to bundle those together?
Mikołaj Świątek 01:10:09 Maybe, but I don't know if we want to actually change anything in the storage… In the user… in the user-facing, not in the API, in the actual user-facing config, I don't think we want to really want to change anything.
Yeah, I mean, I think…
Jade Guiton 01:10:31 I think both of these issues of using config optional and extracting things into a different package is purely an API change.
Mikołaj Świątek 01:10:39 Yeah.
It should be. I don't think… I don't think we have any desire to break anything user-facing in there, or at least I'm not aware of any, like, big problems with what currently exists.
Jade Guiton 01:10:57 Yeah, which is why, well… Yeah, which is why it's not that big of a breaking change, but it's still best to avoid two API breaking changes in a row, I guess.
Ravishankar Gnanaprakasam 01:11:10 Yeah, sure, I think, I would just… I mean, like, feel… I mean, like, I still get mixed opinions, should I go ahead and implement, and then we'll discuss there in the issues? Or I would much appreciate if folks can comment And we can close this offline also, like, we don't have to, take a hard decision on it. It's a… like, like, I go with subject because it's not a very critical change that requires an RFC kind of a thing, I would say, because it's already an existing pattern, and it's just that which pattern we wanted to adopt, so yeah.
Fine.
Mikołaj Świątek 01:11:50 I will…
Ravishankar Gnanaprakasam 01:11:50 I…
jmacdonald 01:11:52 I think we better call it… I do think you have support for your issue.
Ravishankar Gnanaprakasam 01:11:57 Okay.
jmacdonald 01:12:00 Given that Pablo filed it several years ago, I think he probably still believes it. It is a good cleanup for the code. That may be the one thing I can see clearly.
Ravishankar Gnanaprakasam 01:12:13 Do we want it to go ahead with the other one, or… I think we have very few folks, so…
jmacdonald 01:12:19 Yeah, I think we better wait for the next time.
Ravishankar Gnanaprakasam 01:12:22 Okay, sure.
Mikołaj Świątek 01:12:22 Yeah.
Ravishankar Gnanaprakasam 01:12:23 Thanks. Thank you, everyone. Thank you, Josh.
Jade Guiton 01:12:27 Okay, everyone.
