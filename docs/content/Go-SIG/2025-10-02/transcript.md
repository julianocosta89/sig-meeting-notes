SIG: Go SIG
Date: 2025-10-02
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Bryan Boreham 00:01:56 Hello there.
Damien Mathieu 00:02:01 Hey!
Bryan Boreham 00:02:04 How you doing?
Damien Mathieu 00:02:05 Good, how are you?
Bryan Boreham 00:02:07 Pretty good.
that point in the day when I feel I really should have done something.
Damien Mathieu 00:02:16 Which time zone are you in?
Bryan Boreham 00:02:18 London.
Damien Mathieu 00:02:19 Okay, so 5… 5PM, yes, I agree.
If you told me I'm in the US, it's 9 AM, then no, you have time.
Bryan Boreham 00:02:42 In the document.
Tyler Yahn 00:03:11 Hey, y'all.
Damien Mathieu 00:03:14 Hey!
Tyler Yahn 00:03:15 How's it going?
Damien Mathieu 00:03:16 Good, how are you?
Tyler Yahn 00:03:18 Doing well.
Bryan Boreham 00:03:21 Aye.
David Ashpole (dashpole) 00:03:37 Hey, everyone.
Tyler Yahn 00:03:40 Hey, how's it going?
Damien Mathieu 00:03:41 It's going well. Hey, Davey.
Robert Pająk 00:03:43 Whoa.
Damien Mathieu 00:03:44 And, and Robert, congratulations, David.
David Ashpole (dashpole) 00:03:49 Yes, thank you.
I suppose it doesn't come as a surprise that I'm now the DC liaison for Pick up big.
Tyler Yahn 00:04:02 You're the liaison for the Ghost Signal?
David Ashpole (dashpole) 00:04:05 Yeah, yeah, so, I suppose, I'm on the TC now, which is exciting.
Tyler Yahn 00:04:11 Oh…
Damien Mathieu 00:04:15 Yeah, that's why I'm… saturating him.
Tyler Yahn 00:04:19 Cool, yeah, congratulations.
Thanks. I thought… wait, we have a TC liaison?
David Ashpole (dashpole) 00:04:27 like, it used to be Josh McDonald a long time ago, and then… it was… it's been Tigrin.
Damien Mathieu 00:04:37 We had a…
David Ashpole (dashpole) 00:04:38 for a while.
Damien Mathieu 00:04:39 We had a liaison meeting with someone,
A few months ago, but was neither Josh nor Tegan.
Tyler Yahn 00:04:49 Yeah, that was a juicy.
David Ashpole (dashpole) 00:04:50 Yeah, that was a GC retro.
Damien Mathieu 00:04:51 Okay, so we have both a GC and a TC liaison?
I guess we're doing good work, so we don't hear about them, and we don't know about them.
David Ashpole (dashpole) 00:05:13 Definitely.
Tyler Yahn 00:05:20 Yeah, well, cool, yeah, I guess now we have our GC liaison, or TC liaison joining every week.
Yeah, even better. So, if you haven't yet, please go ahead and add your name to the attendees list. We can jump in here. So, first up, Damien, you wanted to talk about…
go…
Damien Mathieu 00:05:40 Yes.
Tyler Yahn 00:05:40 I.O. incident?
Damien Mathieu 00:05:42 Yes, so I know it's been discussed last week, but it was rather in the heat of things last week. There was an incident on Thursday last week, on Go.opentelemetry.io.
basically, it runs on App Engine, and the… there was an ask to add a CAA DNS entry, which prevents some certificates to be generated if they are not defined in the DNS entry.
And so, only that same script was defined, and so Google couldn't, do that.
This has been resolved, but go.hotel.io is still rather a snowflake.
because we are the only ones running on App Engine and using… issuing certificate that way and everything. So, I linked a PR
In the document.
that kind of moves the GoVanity URLs project from, running as a Go app on App Engine to Hugo, which is a static thing, for Netlify.
So, for my plan, I know this is not Go SDK specific, but we are kind of de facto owners of this with the collectors folks.
My goal here is, make it working on Netly 5, and do the switch, and then remove the Go code, so that we can roll back more easily if we need to.
So, basically, it's rather simple, because everything is static. The only kind of catchy thing is setting up proper redirects in Netlify, so that everything in the sub-package folders properly goes back to the top of the package.
So yeah, that's the PR,
I think it would make sense to go that way, because we are less of a snowflake. Not a snowflake anymore, since that's how OpenTymmetry as I.O. works already, and, kind of how we operate the… all the assets we have, the only asset we have, which is alternative.io.
Tyler Yahn 00:08:00 Yeah, I don't… I don't have access to any of this stuff, and I'm the one responsible for it.
Damien Mathieu 00:08:06 You mean, oh, VDNS entries and everything?
Tyler Yahn 00:08:09 No, Netlify and Hugo? Like, I don't, like…
Damien Mathieu 00:08:13 So, I mean, Hugo, you do have access to it. It's an open source static site generator. It's the one used by OpenGeometry.io.
Netlify, I don't have access either.
I have a test app that shows that it does work.
If this code is considered, good by folks, I will be working with the people who have access, which is mostly Severin.
To get things moved forward.
Basically, it's a cheesy thing to get DNS entries changed.
Tyler Yahn 00:08:56 Yeah, isn't that what caused the incident in the first place?
Damien Mathieu 00:08:59 No, it was a, SSL certificate.
Tyler Yahn 00:09:05 Right, that couldn't get updated because of what?
Damien Mathieu 00:09:08 Because CAA DNS entry is being changed, and so…
Tyler Yahn 00:09:12 DNS entry is what I'm saying.
Damien Mathieu 00:09:13 Yes, but the reason why the DNS entry was wrong was because we are the only ones running on Google, and we are the only ones having a Google certificate.
So when they set up the CIA entry, they considered OpenTeometer.io was the only asset, and so they did not think of Google.
Tyler Yahn 00:09:35 Yeah, I mean, I think… I think that's, like, one way to look at it. Another way to look at it is that, like, the people who had the responsibility to maintain this, who were…
on this call right now didn't have the correct permissions, and they didn't have the controls in, like, maintaining it. So, I see your PR here moving us further away from that, instead of moving us into a place where
People who are actually responsible for this are, like, in control of this.
Damien Mathieu 00:10:00 But,
At the same time, we are on App Engine, I don't think… I don't know about you, but I don't have any experience using App Engine, and I was awake. I was talking with Pablo at the same time, but I just didn't know.
How that could have been solved.
Tyler Yahn 00:10:18 Yeah, I am experienced. I know David's pretty experienced there, and I… yeah.
Damien Mathieu 00:10:24 I mean, this did not happen during, David's, waking hours.
Tyler Yahn 00:10:29 Yeah, but, like, to say that, like, the incident is the cause of, like, when it happened is not really an effective way to actually, like.
talk about the incident, right? Like, we think we need to talk more about, like, roles and responsibility.
And, like, we can look at, like, the actual problems that occurred, and we can try to resolve those. Like, this, this, first off, like.
I think this is good, like, don't get me wrong, like, this is, like, a fine step, I'm happy moving to Netlify, but, like.
This isn't the actual problem.
Damien Mathieu 00:10:57 I… The platform that they're actually running on? Yeah, I… I mean, I…
Tyler Yahn 00:11:01 I feel like some, like, concern, but, like, that's not actually where the problem that, like, caused the incident. It's not the thing that caused, like, the prolongation of the incident.
It also isn't a part of the…
resolution that happened for the incident. So, like.
This is… this is, like, to say this is going to resolve future incidents is not…
I think, good enough.
Damien Mathieu 00:11:25 I think it's not just about us owning that code, it's also about, streamlining with how other, similar things are being run, and the fact that it's, even though we are responsible for this code, we are technically not responsible for DNS entries.
And so the fact that, because it's only us being in a different platform.
People forget about us, which makes sense, and going back to the same platform as where everyone else is means that we are not forgotten about anymore, and that kind of prevents this kind of incident.
Tyler Yahn 00:12:04 Yeah, I don't think so. I think that's… that's a, a pipe dream. Like, I think… I think to think that, like.
you had a person with authority making changes on our behalf without consulting any of us? Like, that, I think, is where the problem came from. I don't think the problem came from the platform.
Like, I think the problem came from, like, there's an ownership issue, and then you had a lack of checks and balances.
Damien Mathieu 00:12:29 So we should check every DNS… Entry change?
Tyler Yahn 00:12:34 That is going to affect us, absolutely, yeah.
I, like, I don'.
Damien Mathieu 00:12:38 How are we doing?
Tyler Yahn 00:12:38 So, like.
Damien Mathieu 00:12:39 how do we detect that a specific TNS entry is going to affect us? And I'm not even sure those are managed by infrastructure.
Tyler Yahn 00:12:47 Yeah, you're kind of making my point for me.
like, this is exactly the problem, is somebody in the project, on their own, unilaterally, made a change.
That affected us, and we had no oversight into this.
Like, that's actually the problem.
The problem is not, like, the platform it's running on.
Damien Mathieu 00:13:08 But, I mean, should we care about every DNS entry change in OpenTelemetry.io? It feels like that's.
Tyler Yahn 00:13:15 If it can affect our ability to serve our project 100%, it should. Like, yeah, I absolutely think we should.
Damien Mathieu 00:13:22 Sure, but, like, this change is kind of reducing how it affects us.
Tyler Yahn 00:13:29 Yeah, like, this is, I think, this is my problem, is, like, like I said, like, I like… I like moving somewhere. I don't like moving somewhere I don't have control over it. I think that that's, like, the actual problem that I'm trying to point out, is, like, the incident was caused by this lack of oversight.
And what this is going to do is it's going to take our ability to serve this, and it's going to pass this off into somebody else's hands even more. So now we don't control the DNS, now we don't control the platform, now we don't control the rollout. Like, none of this is actually controlled by us anymore.
We have no oversight into this. We have no, like, ability to actually have a check and balance anymore. So, like.
Having this rolled out, like, do we have…
more ability to have a decision in the fate of the project being served, or do we have less? Like…
that's the answer, and, like, I think, like, this is great, I like this idea, but, like, until we have, like, checks and balances put in place to actually resolve, like.
core issues that were addressed in the incident. Like, that's actually gonna be the problem that we need to solve.
Damien Mathieu 00:14:28 I mean, then we should ensure that, maintainers of these products have access to the platform that hosts
go.otel.io. Because we currently don't. Only the GC has, which is admin at opento.io.
Tyler Yahn 00:14:42 Right.
I agree.
David Ashpole (dashpole) 00:14:44 Do you think it's…
Damien Mathieu 00:14:45 It's technically the same thing for Netlify, so that doesn't change.
Sorry, David.
David Ashpole (dashpole) 00:14:52 Are you taking it as a given that we, the GoSig, should ultimately be responsible for go.opentelemetry.io?
Damien Mathieu 00:14:59 It's also…
Tyler Yahn 00:15:01 I'm asking for the URL that gets resolved by us for our package.
Ultimately, we need to have the ability to, like, affect change there, wherever that is.
David Ashpole (dashpole) 00:15:14 Okay, so you'd.
Tyler Yahn 00:15:14 I think it's.
David Ashpole (dashpole) 00:15:15 like, to delegate that to some other SIG that does all, like, the website stuff or something.
Damien Mathieu 00:15:21 I think I agree with David. Our responsibility is to ensure that it's available, it doesn't break, but the fact that it's, like, we don't care about who is operating it.
In my opinion.
David Ashpole (dashpole) 00:15:32 Well, if it's our responsibility to ensure it doesn't break, then… then the buck stops with us, right? So either it's someone else's responsibility, and someone else can do a post-mortem, and…
You know, you can… or we can go to them with the changes you're talking about, or…
Like, we need to be given more ownership. Like, clearly there was some expectation that we were at least gonna help when this outage happened, and none of us had access. I asked for it, and did get it, and was able to help a little bit, but…
Does that make sense?
Tyler Yahn 00:16:02 Yeah, that's… that's actually… that's what I'm saying as well. Yeah, 100%.
Damien Mathieu 00:16:07 So, actually, to, to your point, Tyler, the original PR from Severin, a year ago, because this was already discussed a year ago when we moved from the original Google-owned Google Apps accounts to the OpenTimetry one.
Which I think is a very good thing we did.
Because otherwise, it would have been way more painful to resolve this issue.
Yes, the original PR was actually moving this configuration to the OpenTelemetry.io website, and so, like, OpenTelemetry.io would have been responsible for both the root website and the go.openteometry.io website.
The reason I did not move KeepFats as my proposal here is because I think we should be responsible for whatever is set up there. We should be responsible for all the packages, like,
that are set up and where they lead to, and we should not have to wait for… it's a question of waiting for, like, comms maintainers,
For this.
Tyler Yahn 00:17:18 Yeah, so, just for background, like, I was involved in that migration. I was a part of it. I was definitely aware of Severn's original PR. That PR didn't go forward for the exact reasons that I'm raising here as well.
And the exact reasons that David's just raised. Like, it's an ownership issue.
Damien Mathieu 00:17:32 But…
What I mean is, yes, there is an ownership issue. We should have access to the platform that hosts this, but if it's…
Google App Engine, then we need access to App Engine, which seems to be its own problem. If it's Netlify, we should probably ask for access to it, but at the same time, it means we are not a snowflake anymore, and we have less risk of unseen
problems. I'm not talking about, things that we see and can say, hey, don't forget about us. I'm talking about things we can… we don't see, we miss for any reason. If… even if
DNS entries get, like, infrastructure changes, and we are pinged on most of them because we are detected. It's not unlikely
But we are missed on some, because, like, it's just, way too broad for DNS.
And I think not being a snowflake anymore.
resolves fats by… because we are just, like,
We're running the same way as the main website.
Which is why I think having access to Netlify or App Engine makes sense, but it's a different issue.
Tyler Yahn 00:18:54 Yeah, I think this is, like I said, like, I'm interested in exploring this, but, like.
This is kind of like… Step 10 out of 10.
Like, there's a lot of steps before this that we need to actually have in place.
like, we can go back to this retrospective, and I don't think it's as comprehensive as it needs to be, like…
there's playbooks, there's, I think, notifications, and there's ownership issues that are not addressed here. And, like, to think that, like.
We're just gonna move everything over to Netlify and not have any more issues?
Damien Mathieu 00:19:27 I don't think that's… I'm not saying that.
Tyler Yahn 00:19:30 and yet we're still asked to have ownership over this domain? Like, that is…
it's kind of a non-starter for me. Like, I have access to Google App Engine, I have the ability to, like, maintain the code there. I don't have access to DNS, I don't have access to…
any sort of list or subscription to DNS changes. That, I think, is a great first step in fixing this, in having some sort of, like, automated way to actually determine what's changed and have a subscription base so that I can be notified of these sort of changes. Understanding these sort of changes, how they're going to affect me is, like, something that then we can work on.
I think running playbooks is a great idea, but I mean, just thinking that we're just gonna switch over here without…
without, like, an operation strategy and an operation plan, I think is a…
premature. And I don't think it's comprehensive, and I think it's going to lead to less reliability.
In the long haul.
So, yeah, like, I like this idea, but, like, there's a lot missing before we attempt this.
Damien Mathieu 00:20:34 Okay.
Tyler Yahn 00:20:36 I'm happy to meet with the docs team, I'm happy to meet with any sort of GC, representatives.
to address this, but, like, yeah, like, this, I think, is a fine step, it's just there's many steps that need to happen before we actually do this.
David, is this in line with what your thoughts are as well?
David Ashpole (dashpole) 00:21:03 I…
I'm actually okay.
pursuing something like this in parallel. It's more just that…
I don't think this SIG is currently really the owner, so this probably just…
Like, this probably just needs to find whoever the current owner is,
Like, I'm on board with migrating away from App Engine, certainly, so…
I think it's still okay to make improvements, as long as, like, the people who do own it
Which I think is basically the GC, right?
Or… No, it was the OpenTelemetry.io folks. If they're on board, then…
Tyler Yahn 00:21:45 Yeah.
It was me.
David Ashpole (dashpole) 00:21:47 And that's how it's…
Tyler Yahn 00:21:48 That's who owned it before. Like, that's the one who was maintaining it. Me and Mike Dame.
And before that, it was,
Another Googler, can't remember his name right now.
But that's, like, in 2019.
Damien Mathieu 00:22:06 Do we want to keep owning it?
That's a good question.
Tyler Yahn 00:22:11 like.
Damien Mathieu 00:22:12 I mean, operations. I think there are two things to be owned here. It's…
Operations, ensuring that the website is available, and what it serves.
David Ashpole (dashpole) 00:22:24 I mean, we should certainly own the package.dev.
Damien Mathieu 00:22:27 Yes, what it's… Stop, what it serves. This is completely separate from that.
I think what it's something we should own.
David Ashpole (dashpole) 00:22:36 sorry, God. Like, we own the actual GoDocs being there, right?
Tyler Yahn 00:22:42 No, that's… I mean, so those are all on… that's the Go team itself at Google that owns this, like, package.dev?
David Ashpole (dashpole) 00:22:48 Yeah, yeah, that's, like, we're responsible for having that URL exists, which…
We're not, like, serving anything, we're just… Published.
Tyler Yahn 00:22:57 We're getting scraped.
Robert Pająk 00:22:58 booster.
Tyler Yahn 00:22:59 To get this, yeah.
Robert Pająk 00:22:59 Isn't it also, it's shared also with the collector? Isn't go open.io slash collector? Also…
Damien Mathieu 00:23:06 And eBPF Profiler, and the latest eBPF, thing as well, so there, it's…
Tyler Yahn 00:23:13 And the audio.
Damien Mathieu 00:23:14 Sharing things.
Yes, there's a lot of things that this is actually serving.
Tyler Yahn 00:23:18 And the…
Robert Pająk 00:23:20 Go Beautiful.
Tyler Yahn 00:23:21 Yeah, build tools, EPIF instrumentation, the proto, yeah, there's a lot.
David Ashpole (dashpole) 00:23:27 essentially all Go packages within the OpenTelemetry namespace.
Tyler Yahn 00:23:32 Is what's being served here.
Yeah, I mean, I, like, that's fine. I'm happy to, like, pass off the ownership, but, like, this is also, again, like, that's not how you pass off ownership, is just, like, by saying this is gonna go to somebody else. Like, we need to actually have, like, clear understandings of, like.
who is gonna run this? Who is going to be the point person? Like, this again goes back to, like, this retrospective, like, there's a lot of, like, other, like, things that need to be done here to actually, like.
Ensure… like, one of the biggest problems of this incident was the fact of ownership, right?
And I think that's… that's more what needs to get resolved here. I think the other thing is, like, once that ownership is established, like, they need to be kept in the loop.
Whether that's us, whether that's another team, like, yeah.
David Ashpole (dashpole) 00:24:14 Sorry, I assume, Tyler, that… that whoever…
like, Pablo seemed to be the point person on the incident, and seemed to have access to everything, so I assumed that this was actually.
Damien Mathieu 00:24:23 I mean…
David Ashpole (dashpole) 00:24:24 But if we're.
Damien Mathieu 00:24:25 Pablo is both collector, maintainer and GC, so, yeah.
David Ashpole (dashpole) 00:24:29 Whoa.
I assume the collector didn't own it. If the collector owns it, then I'm also fine with that. But we do need to have ownership for whatever this thing is. So I agree that that needs to be resolved before this. I thought that…
I thought, Tyler, that you were talking about us taking ownership, not that we already had partial ownership.
Tyler Yahn 00:24:51 Yeah, we did. We… yeah, exactly. So, like, I think that's… that's, I think, kind of, like, the big issue. And think, like.
it's… Yeah.
100%. Like, once you have ownership defined, and whoever is going to own it, I think then this becomes a question you can answer, right? Because if you go and you give this to.
David Ashpole (dashpole) 00:25:10 Yeah.
Tyler Yahn 00:25:11 I don't know, somebody in there, like, there's no way I want to run it in Netlify, like, then that's kind of a misstep at that point.
So, yeah, I think that that's good.
Damien Mathieu 00:25:23 So, would you be, as a next step, because I think we need a next step, if we're not just, like, trolling around.
sorry, I didn't paint that in a condescending way.
How about a discussion meeting, whatever, with, the hotel comms, maybe, collector, maintainers, and us?
Robert Pająk 00:25:45 Maybe also community issue, for transparency?
Damien Mathieu 00:25:49 Sure.
David Ashpole (dashpole) 00:25:50 And I would…
Tyler Yahn 00:25:51 Yeah.
David Ashpole (dashpole) 00:25:52 Come up with a proposal.
I… Even if it's just a straw man, to get people to react to it.
So, either, like, what are the implications of the Hotel Go Sig completely owning it? Like, what do we need to be handed the keys to? Or…
what would the implications be of, like, the communications, say, going in? Whatever, right?
Damien Mathieu 00:26:15 Okay, I can set that up, unless, David, you wanted to do it.
David Ashpole (dashpole) 00:26:20 No, I don't know what the answer to those questions are, so if you do, then please.
Damien Mathieu 00:26:25 Yeah, I'll create a community issue and ping both connector maintainers and comms maintainers and GC, I think.
Because we technically own everything.
about it.
Tyler Yahn 00:26:42 So, yeah, I go the GC, the comms, the collector, the Go Instrumentation, the EVPF instrumentation, EVPF profiler, and then this SIG as well.
Damien Mathieu 00:26:53 Yeah, I don't know about Go instrumentation, but I'm pretty sure a BPF provider has zero interest in this.
Tyler Yahn 00:27:01 The Go instrumentation does, and the eBPF instrumentation does, and I'm speaking as a representative of both of those, and I think that, like, yeah, I appreciate being pinged there. I do think that, like, if the eBPF profiler doesn't actually have a care, that's fine, but they think they need to be, again, like, this is, again, part of the DNS problem that we were.
Damien Mathieu 00:27:18 Yeah.
Tyler Yahn 00:27:18 need to be notified whether they ignore it or not is up to them, I think, is the important thing.
So yeah, thanks for taking on the next steps, I think that's a great idea. How that turns into maybe a meeting, but, like, I think a community issue is a great place to start as well, so yeah.
Damien Mathieu 00:27:34 Okay. Alright, I didn't do that.
Tyler Yahn 00:27:36 Thanks.
Okay, cool. Next up, I want to talk about PR really quick, add the internal observability package to the OpenTelemetry TraceGRPC package. So, this is set up here, it's been up for a little while, it's had a few reviews.
Honestly, this needs to get re, asked, because that was given a long time ago. So I was looking for review. I did want to talk about that comment from David, but otherwise, I think this is ready for review. So, David, you pointed out that, like, right now, what we're using for scope names are things that are internal packages, and your suggestion was to not use that?
I'm a little opposed to not having the scope name be the package that the import is coming from.
There's open telemetry standards here, but I think it's also a little bit easier for people to find the code that's doing the instrumentation if you have the full package name here. The internal package isn't, like, obfuscated, you can still find docs on it, you can still find the package, it's all in the open source space. So, I was wondering, like.
thoughts on this one. I haven't got a response from you, I didn't know if, like, you were abstaining? Okay.
David Ashpole (dashpole) 00:28:53 No, no, I just missed it.
My concern is mostly around stability. Like, it becomes part of the API.
Right? If this is a thing.
Robert Pająk 00:29:02 Robert, sorry, David, just.
David Ashpole (dashpole) 00:29:04 Go for it.
Robert Pająk 00:29:05 I see the same concerns.
So, but the thing is that there's no version.
So it'll still be not kind of stable, because the instrumentation scope will be new each… when you bump each time of the, you know, each time you bump the version… the version of the SDK, you'll have basically a new instrumentation scope because of the version.
Because I cut the stables for him.
David Ashpole (dashpole) 00:29:26 I mean, yes, the version changes, but that's expected. Like, I imagine that people will do, like, collector processors and…
maybe even dashboards and stuff that use Scopename in some way. And so, like, we're gonna keep the OTLP trace gRPC
package.
Name, the same, but…
This would put us, in my opinion… it would give us an obligation to not change where the instrumentation lives.
in our internal packages, and wouldn't allow us to reorganize in the future, right? So, that's… that's the thing that we would be, like, dedicating ourselves to, basically. And I'm…
I'm just not sure if that's what… We want to do.
Does that make sense?
Tyler Yahn 00:30:15 I think so. So, like, if I understand you correctly, like, right now, what you're saying is, like, as we evolve this, we may want to move the location of it in that, when we move the location, it may break a dashboard. That's using this as a filter, is kind of what your issue is, right?
David Ashpole (dashpole) 00:30:28 Yeah, like, I would want us…
If we're gonna go this route, then this just means that, like, I don't… I don't know.
I don't think internal directories get declared stable, because they're not their own module, but, like, basically…
Tyler Yahn 00:30:40 We kind of do, but… yeah.
But anyways, no, I… you're right, but yes, I gotcha. But so, so just, if that's… if that's your point, like.
I do think…
that this is… I don't have any plans of ever changing this. Like, if this becomes, like, a stable feature, like, that is on by default, I would still want this instrumentation to live in a separate package, and if it's gonna live in a separate package, I'd still want it to live in the internal package, because I wouldn't want to export the instrumentation itself.
And… I don't see anything wrong with this name existing. The only thing that I see is that in the creation method of this, that we would change it
so that the environment variable is, like, off by default, or on by default, or pulling in a different thing. So that's kind of, like.
how I see the long-term stability is, like, this would continue to live here in the long term. I also see that, like, if it does change its location.
I would see that as a positive…
to also change the scope name. So, if, like, the observability is exactly the same, like, I get that that's a little bit of a frustration, but I also see it as, like, a package change name from, like, a V1 to a V2 in some sort of, like, evolution, where the API actually may be different, meaning that, like, if we do change this location.
and the scope name changes, that also indicates that the telemetry being sent from it is going to be different. And so, I think.
It also provides us a way to provide that stability. So, in fact, it may be useful to even if, like, we do change the telemetry coming out of this in the future, to even do, like, an observed V2 or something like that. So, like, having the scope name change may be actually a feature, rather than, like, a detriment, but…
Yeah, I don't know what your thoughts on that are.
David Ashpole (dashpole) 00:32:22 Yeah, I mean… Is it… it isn't always possible to go from an internal directory and figure out
what the package is that's using it, right? So, I guess it's… It… so…
Tyler Yahn 00:32:37 Sorry, say that one more time, you can't go from an internal directory.
David Ashpole (dashpole) 00:32:40 Like, I know that we don't allow shared internal directories, but, like, in general, that's a thing that people can do.
Tyler Yahn 00:32:47 Yeah. And, like…
David Ashpole (dashpole) 00:32:51 It is an interesting question, like, if there are multiple modules using instrumentation in a shared directory.
Like, do we want the shared directory, or the shared internal directory to be the thing that people…
We probably do, because it is the same instrumentation code, right? I guess that's your point.
Tyler Yahn 00:33:09 Yeah, like, the goal here is to find, like, when you have the scope, I want it to point at the instrumentation code itself, like, because that's, I mean, yeah, like, I definitely think that, like, having the instrumented package named in some way would be helpful here, because then you could actually do a filter on that, but, like.
That actually is a problem that's more universal. I think that all of our instrumentation could benefit from something like that.
But, like, that being said, like, I think that, like, when you have an issue with this code, you know that the scope name is going to point to the codebase that you can actually go take a look at, and so, like.
Yeah. I mean, I can… I can go directly to this. Instead of, like, going here and then finding out, like, okay, well, where is this telemetry coming from? Like, oh, it's actually coming from an internal package? Like, that's… it's a little bit more of a confusion there, yeah.
David Ashpole (dashpole) 00:33:53 And…
Tyler Yahn 00:33:55 I get that. It's also, like…
David Ashpole (dashpole) 00:34:00 It's hard for me to tell whether users are more commonly going to want to go
Hey, I saw this metric.
It says something's weird.
I wanna go see the package.
And…
It's unclear to me whether they're more often going to be interested in figuring out why the package is doing something weird.
Like, oh my goodness, my requests are being dropped, let me go look at the thing that's dropping my requests, versus, oh my goodness.
the request dropped counter is a little bit funky. I want to go look at the counter. And…
Like, I have this…
Tyler Yahn 00:34:36 I agree. I agree. Like, I honestly, that's kind of, like, what I was kind of trying to say is, like… but I think we have the same problem for the HTTP interpretation for the, you know, any of the interpretation in Contrib right now as well, because, like, you don't actually have, like, codes.
Robert Pająk 00:34:49 Once you drop in?
I remember there were similar discussions.
Around logging bridges.
So, I remember I was talking about the specification and semantic conventions, and most people preferred to have the scope name, not as the…
breach of the log bridge name, but as the thing that is being breached. So, for instance, the name of the logger from ROG4J, or things like that.
This was the preference. So, in the same way people… if we follow the same pattern, then here people probably prefer the name of the thing which is being instrumented.
But on the other hand, this is not what the specification, if I remember, says about the instrumentation scope. I think it's taking the instrumentation library name, or something like that, if you check it for… not for loss, but for metrics. I think it's…
I think it tells exactly what you did, Tyler, if I remember correctly.
Tyler Yahn 00:35:47 Yeah, it does. And this was a whole discussion when it happened, as well.
Robert Pająk 00:35:53 Yep. Yeah.
Tyler Yahn 00:35:54 I remember… There's pretty strong opinions on, like, it being the actual instrumentation, not the instrumented package.
Robert Pająk 00:36:02 I think if you… I think if you find instrumentation scope here, I think this is how…
Yeah, well, it's…
Tyler Yahn 00:36:09 It's actually Instrumentation Library, but yeah.
Robert Pająk 00:36:11 Yep.
Tyler Yahn 00:36:11 This was linked, yeah.
David Ashpole (dashpole) 00:36:14 My… I mean, if that's what the spec says, then I… I'll.
Robert Pająk 00:36:18 party.
My… But I think spec as well.
David Ashpole (dashpole) 00:36:21 My.
Tyler Yahn 00:36:22 Yeah, this is, yeah.
David Ashpole (dashpole) 00:36:24 My preference…
if I could… I don't know if this is legal, or, you know, if it's kosher or not.
My… my feeling is that identifying the module that the telemetry is coming from, because that's a more stable thing, or, like, because that's the thing that people are consuming, is more useful than the package, but if…
And maybe that's a subtle distinction, but, like, if someone's using an instrumentation library that's, like, a different module in a different repo.
Like, that's one thing to point out as a separate entity.
But, like, an internal directory… Which, to me, feels like an implementation detail of…
our SDK feels, like, less useful, but… .
Tyler Yahn 00:37:06 Yeah, I think I've…
David Ashpole (dashpole) 00:37:08 I've shared my opinions, and…
Robert Pająk 00:37:10 I think, David, there will be nothing wrong if we just add an instrumentation scope attribute, which will say what it is instrumenting. But we do not have some…
David Ashpole (dashpole) 00:37:20 Compassion for you.
Tyler Yahn 00:37:22 Yeah, like, that's kind of where I'm on it as well, like, I'm happy to do that. I don't know how easy it is to filter off of an instrumentation scope attribute, but, like, I agree, like, I think that that's… like, honestly, I think we should be doing that for all of our instrumentation packages, because, like.
exactly like what you just said, is like, if I use… Automation.
Yeah, I would tell HGP, like, because, like, if I'm using, like,
you know, one of those other, like, framework HTTP libraries, it's like, I'm pretty sure I know what framework that's gonna instrument, but, like, yeah, like, OSHL HTTP, the Mongo one, like, all of these, like, the host one, like, there's a lot of other places it can get, like, inserted, right? And so I think that there's, like…
value in adding, like, what is instrumented, not necessarily what is instrumentation library is, so…
I'm happy to add that here. I… I suspect, actually.
maybe I'm not happy to add that here. I'm happy to add that in another PR, for all of the places that we do this, and if… if you're down for that, like, I would be interested in adding that, but yeah.
I also think that we may run a little bit of a foul, because it's before the specification defines anything like this, but.
David Ashpole (dashpole) 00:38:30 I'm happy to wait for the spec.
To define things.
Tyler Yahn 00:38:34 This is…
David Ashpole (dashpole) 00:38:35 somewhere.
Tyler Yahn 00:38:35 You're working on, right?
Robert Pająk 00:38:37 I was doing similar stuff for…
I think it's assigned for.
Tyler Yahn 00:38:42 The longer boots, right?
Robert Pająk 00:38:43 memory nine, but I will say that it is a related issue.
Tyler Yahn 00:38:48 I agree, yeah.
Robert Pająk 00:38:51 give me an action item in the agenda, so I do create an issue in the semantic contentions, I can help, at least in this way.
Tyler Yahn 00:38:58 Okay.
Oh, boy.
Okay.
Alright, well, if that's the case, we'll keep moving. This just needs more reviews. David, is it okay if I resolve this and we can, pick this up in Robert's issue and others?
David Ashpole (dashpole) 00:39:28 Yeah, if you can… Did you already link to the spec?
Tyler Yahn 00:39:34 Yeah, I mean, that's what all these links are, yeah. And all of our other naming locations, yeah.
David Ashpole (dashpole) 00:39:39 Okay, that's fine.
Tyler Yahn 00:39:40 So…
David Ashpole (dashpole) 00:39:40 Feel free to resolve. You can just say something like, discussed in the SICK meeting. Thanks.
And you still need approvals on this, right?
Tyler Yahn 00:39:51 Yeah, yeah. So, I tried to, like, break this apart, but it's still… it's getting a little bit big, but…
Yeah, I don't know how to break this apart anymore. If you have suggestions, I'm happy to, to work on it, though.
Okay, also up is related to this. This is something that kind of was inspired by something you said earlier, David, about another institution.
Library is, like, right now, our errors are a little bit,
They're not a little, but they're really unuseful, like, they're very much always, like, the error type just says, like, error string, essentially. It doesn't really give you understanding of what it is. If you look at the semantic conventions, the error type attribute, the semantic convention for it should
be related to whatever, like, the domain-specific error is. So, for things like HTTP or gRPC, like, a status code is expected to be that value.
Which is not gonna be the case, like, we're gonna have, like, our internal concrete types being listed here. So, to be able to provide that, I've actually updated the, parser function that we use here. Like, obviously, you could just do that, like, you could… you don't have to use the parser function, internal to, these semantic convention types, right?
But I did provide the ability to say, like, if you wanted to just pass an error that also returns this error type string, we could then parse that and then use that in whatever we want, or when we're setting this error type key value in the response here. So, it's a little bit nicer instead of, like.
having to take the key and then put a string in, essentially, you get to still use this with normal error passing, if you define the errors well. And you define those errors in a way that, like, they communicate what's actually going on here, so…
I was looking at doing this for that PR we just looked at for the OTEL trace gRPC package, where
you would return, if it's an RPC error, just the standardized message of what that RPC error is. If it's a partial error, you give a little bit more of a description of what that partial error is. If it's… you know, essentially, you go down this chain of, like, what the error is, if it's domain-specific. If it's not, then try to give a little bit more specific, and then…
You fall back to what we've always done, which is just the… the package name and, like, the type structure on this, which is kind of, useless, but, like, it's… it's not…
I guess it's better than other, which is kind of the default. So, yeah, so that's what this is including.
I'm interested to hear what people think about this, because, like, obviously, like I said, like, you don't have to actually use this, you could just use this air type key and then, you know, skip everything and just put whatever you want here,
So, I, you know, it's up to, I think, us to decide, like, how useful or how unuseful we want the semantics. But yeah, go ahead, Robert.
Robert Pająk 00:42:40 I have not only approved it, yeah, I know. I can't problem to click unmute. Basically, I have not approved it for only one reason. I haven't got a chance to check the package type, if this type error interface is rendered correctly, basically. That's the only thing which I haven't checked.
Tyler Yahn 00:42:57 the tight… sorry, the… you haven't.
Robert Pająk 00:42:59 The line… the lines from… if you go to error type go, and lines number from, I think, then,
This is, 18 to 20-something.
Tyler Yahn 00:43:12 19?
Robert Pająk 00:43:14 Yeah, if it is… yeah, if it is rendered correctly in Godok, so, you know, just running package site, and if this stuff is rendered correctly, that's the only thing.
Tyler Yahn 00:43:22 Oh, these docks, if these docks are running correctly? Yeah, yeah.
Robert Pająk 00:43:25 This is the only way I haven't checked.
Because I have not checked it out.
I remember that usually I was doing two spaces, I see there's one space, maybe it's enough.
Tyler Yahn 00:43:36 Yeah, it's a tab, though.
Robert Pająk 00:43:39 If it's a tap, then it works.
Are you sure as a tab?
Tyler Yahn 00:43:43 Yeah, I, I… No, the leader… the leader makes a change at this point. Yeah, that's fair.
Robert Pająk 00:43:54 You can just.
Tyler Yahn 00:43:54 I don't know, check.
Robert Pająk 00:43:56 I could…
Tyler Yahn 00:43:56 Alright, I can check, I can double check, but okay. Yeah. Alright, thanks for the feedback, appreciate it.
But yeah, otherwise, yeah, this is just looking at… Reviews.
Okay, enough of that. Next up, David, do you want to talk about the counter performance improvements?
David Ashpole (dashpole) 00:44:14 I do,
Goodness, where to start? So I've been working on this for… feels like a week or two?
I've tried a couple different approaches. I originally started with the read-write lock, which actually gave
pretty significant performance improvements. And I looked into using a sync map.
As this… and it's a map of attributes, To the sum values.
And that works reasonably well.
It was very tricky to get
It works really well if all you're doing is incrementing, which is basically what you do for cumulative values. Like, you're just throwing increments at atomic counters, and it's super-duper fast.
Deltas was a lot more complicated, because
You need to be able to reset things, and
resetting while you're doing increments means you can lose them. So, I have a solution, it…
it was… it's pretty fun. It borrows a trick from the Prometheus histogram implementation, so if you scroll down and look at… the most important thing here to look at is… it's in Atomic.go, so the first.
Tyler Yahn 00:45:39 Oh, it is? Okay, yeah.
David Ashpole (dashpole) 00:45:40 This, hot-cold weight group.
And… Basically, it allows you to flip a hot bit.
And then wait for all the things that were going to the cold thing to finish.
So it's sort of like a weight group, but that you can flip back and forth.
And that basically means that you can… Swap out the storage?
And then wait for all the rights.
To the now cold one to complete.
So this is, like, at the crux of this optimization and all… and a lot of the future ones I plan to make as well.
So this is fun because then,
We can… for all of our inst… for all of our synchronous measurements, we can actually
Make them all lockless. So, measurements aren't ever blocked by collection.
And for Delta, it actually works super well. It doesn't introduce…
any real issues. The one issue that it introduces for everything is that it is possible.
for two attribute set creations to race, and for us to exceed the attribute limit. So that's one…
Potential downside of this is that now our attribute limit goes from being a hard one, where it's impossible to ever go over it.
To being, like, more of a soft limit.
Tyler Yahn 00:47:12 But can't you, adjust for that on Collect? Like, the final export, right?
David Ashpole (dashpole) 00:47:18 you could. For Delta, that will work, because… Yeah.
Because you should have all of them, yeah.
You can fix it for deltas. For cumulatives.
You have to have some way of, like, predictably doing that, basically.
Tyler Yahn 00:47:34 But you don't have to do the hot-cold swap for Delta, or for cumulative, though, right?
David Ashpole (dashpole) 00:47:38 You don't, but it means that once you've exceeded… for cumulative, once you've exceeded the attribute limit.
You basically, like…
have always exceeded… for every subsequent collection, you've always exceeded it, right? Because cumulative basically just continues to accumulate state and never gets rid of anything, right?
Right.
And so if you're randomly deleting attribute sets.
To get back under your attribute limit for export.
That means that you,
Yeah, you might not pick the same one every time, unless you have some, like, very predictable.
Tyler Yahn 00:48:15 Yeah, but you should never…
For cumulatives, you shouldn't ever exceed, though, right? You should be able to deterministically, like, always stay below.
David Ashpole (dashpole) 00:48:22 Cool, that's That's the thing.
Tyler Yahn 00:48:24 Yeah.
David Ashpole (dashpole) 00:48:25 Say that again.
Tyler Yahn 00:48:26 Well, because, like, you're not… you're not swapping the collection.
David Ashpole (dashpole) 00:48:30 Right, you never swap the issue.
Tyler Yahn 00:48:31 But you should…
David Ashpole (dashpole) 00:48:32 the…
Tyler Yahn 00:48:32 Yeah.
David Ashpole (dashpole) 00:48:33 If you look at sum.go.
And then look at the measure function.
We… we… so the sync map doesn't keep track of the length.
For you.
So we're doing that as a separate counter.
And that means that those two can be inconsistent.
Is the issue.
Tyler Yahn 00:49:00 The data and the length.
David Ashpole (dashpole) 00:49:03 So, right, so the map and the map size that we're keeping track of separately aren't kept in sync.
Tyler Yahn 00:49:10 So,
So first off, it's funny, like, we always kind of knew we'd come back to this. This is one of the original prototypes, was… included this at a different level, but yeah. Can you… instead of using atomic, integers, can you use an atomic value here, then?
Which also encapsulates the length.
As well as the, value that you're trying to… Hold.
David Ashpole (dashpole) 00:49:35 This is… we're talking about the map.
Not the value. So there's two pieces, right? One is taking the sum value and making that into an atomic thing.
And the other is taking our map.
and turning that into… and using a sync map instead of that, right? So, enforcing the aggregation limit
Has to do with the map portion.
Of this change, right?
Tyler Yahn 00:50:02 I guess what I'm saying, though, is, like, instead of… Having two fields here.
David Ashpole (dashpole) 00:50:08 Yep.
Tyler Yahn 00:50:08 have just one, say, values, right? And, like, this is, A two-length, array.
David Ashpole (dashpole) 00:50:15 It doesn't even have to do with resets, though, is what I'm saying.
Like, even if you could set the map to zero and set the length to zero.
We can't atomic… when we add an element, so if you look back at measure.
Right? When we increment the length.
We increment the length after the value is added.
Tyler Yahn 00:50:37 Right, that's what I'm trying to say, though. So, like, if instead of using a sync map, you used a value that points to a sync map?
Right? And that value here, when you try to store it, like, you do a swap compare.
And, like, so when you're trying to do that swap compare, if somebody else has already incremented the length, right, like, that will be an invalid swap at that point.
So you could… Atomically set the length and the map update in one operation here.
David Ashpole (dashpole) 00:51:09 Maybe you can leave it as a comment. I'm not quite… following, are sync maps comparable?
Robert Pająk 00:51:18 I don't think they are…
Tyler Yahn 00:51:20 Hmm… No, I don't think so.
But the pointer address, I think you should be able to do that. Like, so when you're doing that swap compare, you can look at the length of the value that you're trying to actually, set here, right? And you can say, oh, like, this value has actually changed from what I expected it to be.
And if it's changed, then you know that, like, your update needs to get reapplied to the value, right?
David Ashpole (dashpole) 00:51:49 Not 100% following.
Robert Pająk 00:51:51 I'm not sure, Tyler, because the map is only doing the pointer, so it'll always be the same pointer.
You'll notice…
David Ashpole (dashpole) 00:51:58 We're never…
Robert Pająk 00:51:58 winter.
David Ashpole (dashpole) 00:51:59 We're never changing either of these maps. We do clear it.
Once we make it cold.
Tyler Yahn 00:52:12 Yeah, I'm just like…
The thing is, is, like, right now, I see your problem, though, and the problem is the fact that these are the two different fields, right? And, like, these are two different types.
If you can tie these two together into…
Robert Pająk 00:52:23 I think the… I think… I understand, I learned.
David Ashpole (dashpole) 00:52:26 I think the only option will be probably creating our own implementation.
Robert Pająk 00:52:30 Of a sync map, which also has.
Tyler Yahn 00:52:32 Yeah, I'm not too… too concerned about the, the sync… like, honestly, it could just be a map. Like, it doesn't actually have to be a sync map here, right? Because, like, the atomic…
David Ashpole (dashpole) 00:52:40 A lot of the performance on the… because this is actually on the read path.
For the sync map, measurements are, and it has really great Performance, for frequent reads.
So that's a big part of why this is, like, so much faster than the read-write lock approach.
Tyler Yahn 00:53:04 Yeah, okay, I'll have to think about it, but I think that there's a way that you can tie these two together.
David Ashpole (dashpole) 00:53:09 Okay. So…
Tyler Yahn 00:53:11 Yeah, we'll have to think about it.
David Ashpole (dashpole) 00:53:15 And the other thing I want to call out about this PR is that
For cumulatives, not for delta… so Delta doesn't have this problem, but for cumulatives, it also…
Has the issue that…
Basically the exemplar.
Can be recorded So, you can get an ad, That's,
Like, if you add to a counter, right, that the ad can be observed.
In a batch of metric points.
And the exemplar could not be observed in that batch of metric points.
Even if it would have otherwise been observed if it was properly offered, if that makes sense.
Tyler Yahn 00:54:04 Yeah, yeah.
David Ashpole (dashpole) 00:54:05 So basically because… It's not a tom… and the reason why this doesn't work
Or we can't make this work is because we don't have control over the storage of the exemplar reservoir.
At the sum… data point level.
Right? Like, that's an interface that's opaque to us.
So we can't, like, do a hot-cold swap or anything. I talked with… I talked with Josh.
Surrett. And… He seemed to think that this was, like, intended.
And allowed, but…
Tyler Yahn 00:54:43 That's actually what I was gonna say as well.
David Ashpole (dashpole) 00:54:45 Yeah, I think that this is okay.
And I haven't… the way that… and for what it's worth, this is what the Prometheus Go client does as well. They're actually just completely separate API functions, incrementing and recording an exemplar. So, this seems like an acceptable… that, to me, seems like an acceptable…
Thing, but, if people are concerned about that, then…
Now's a good time to voice that.
Tyler Yahn 00:55:13 Yeah, I think you're right. I think exemplars are intentionally, like, a little bit vague, on, like… they're trying to be, you know, as best they can, but it's also, like, a statistical sample across a particular time period, so, like, you're already dealing with variability here.
It is something that I do wonder, though, David, like, if we did have, an issue raised where this is actually going to affect a user, could we add a new method to the exemplar with something, like, that is an atomic operation?
David Ashpole (dashpole) 00:55:46 Hmm… my… So, I noodled on this a little bit.
And I think the best way to solve it is actually If.
If the exemplar Reservoir added a merge function, where you could take a complete set of previously offered points.
And ask for them to be merged in.
Hmm.
And that way, what we could do is… we would have
we would have two some… some points, right? We would have a hot… we would basically introduce a hot and a cold some point, and that way we could wait for
we could wait for measurements to complete to both things, but then we would need to take the cold reservoir and merge it into the new hot one. Yeah. In a way that's, like, as if there was a single one. So, we could. This is…
Tyler Yahn 00:56:44 What you just described was… remember I was saying, like, this has been introduced before at just a different level? That's the level it was introduced at, so, yeah.
David Ashpole (dashpole) 00:56:51 That's… we're gonna have to do that pattern for histograms anyways, when it comes to that, but I wanted to do sums first, because they're a little bit simpler.
Tyler Yahn 00:56:59 Yeah, I definitely think that this is the better approach for
just to get us started. Like, if we need to change that, we could still do that at a higher level, but it'll be something… I think it'll be a lot more complicated, as it was originally. I agree.
One of the things that I did… I've taken a look at this.
David Ashpole (dashpole) 00:57:17 Perfect.
Tyler Yahn 00:57:18 This kind of stands out as something that needs to be two different types. Is that something you've thought about?
I think it was originally made one type just because, like, there was… there was overlap between every method here.
But, like, when you see something like this as clear values on collect, like, it kind of just says to me, like, these two different…
David Ashpole (dashpole) 00:57:41 versus a… yeah, I'm okay with that. Right, yeah.
Tyler Yahn 00:57:44 Yeah.
David Ashpole (dashpole) 00:57:45 I was trying to think of, like.
Almost all of the code is shared.
there's… the only little piece that isn't shared is the, the measure one, right? So I'm happy to split it up, it just means that, like, a lot of it gets duplicated.
Tyler Yahn 00:58:02 I see.
David Ashpole (dashpole) 00:58:03 So this is… yeah, that's the only line where it matters.
Tyler Yahn 00:58:07 Okay. I thought there was more than this, so I missed that. If that's the case, maybe that's…
Not a great suggestion.
David Ashpole (dashpole) 00:58:15 Actually, this line here is just an optimization. It just… we do that so that the cumulative one doesn't have to pay the cost of incrementing an atomic counter.
Or two atomic counters each time to track.
Tyler Yahn 00:58:28 How many have started and finished?
Pretty small, but yeah, I gotcha, yeah. Yeah.
David Ashpole (dashpole) 00:58:32 Right, a couple, you know, 20 nanoseconds, but…
Tyler Yahn 00:58:35 Yeah, yeah. I… but still, okay, yeah, that's a good point.
Okay, yeah, I haven't put it.
David Ashpole (dashpole) 00:58:42 It was…
Tyler Yahn 00:58:42 I'll think more about it, but thanks for the feedback. Yeah, I'll keep looking.
This looks… this looks great, by the way. I really appreciate you diving in here. This is a little bit hairy, but…
This is just the nature of trying to support these generics, so I was… I looked at your Prometheus,
Example, and they only do floats, which is, like, yeah, way nicer, but yeah.
David Ashpole (dashpole) 00:59:06 It's good. Actually… Actually, it's even better for… that we do integers and floats, because…
Prometheus has an optimization that you can see on line, like, 36?
Tyler Yahn 00:59:18 Yeah.
David Ashpole (dashpole) 00:59:18 Where, if it's a whole-valued float, they record it as an integer, so we…
We basically just, like… so they have exactly the same code for just supporting floats, and integer slots very nicely into it. So,
There is a… I saw someone else had a further improvement to this by…
Because the cool thing about sums is that you could split it into, you know, number of CPU cores.
values.
Tyler Yahn 00:59:49 Oh, right.
David Ashpole (dashpole) 00:59:50 Can we assign people to them to super reduce contention?
Tyler Yahn 00:59:54 Yeah, yeah.
David Ashpole (dashpole) 00:59:54 But I think that… I think that'll make it more expensive to store these. I'm just… there's some sweet spot, potentially, where we could…
Fragment this further and get more, concurrent performance.
But I don't know, I'm happy with this, and this is what Prometheus does, so it seems like a good starting point before we go.
Try and do other, more fancy things.
Tyler Yahn 01:00:20 Yeah, that was the other side of the original prototype as well that did this. It had this, like, re-aggregation function, essentially. So, like, it did, like, it allowed sharding. But it also allowed sharding across, like, yeah, different dimensions, so…
I like this, though. So, cool. Alright, yeah, still looking through this, though, so…
Other people need to also give this review.
Cool. We are a minute away from the end. Is that something that this can wait till next time, David, or is it just a quick one minute you can give a overview of these?
David Ashpole (dashpole) 01:00:56 Just… all I want to say is,
these are sequential, so if you can take a look at the benchmark PR, that's pretty simple, and it also fixes a bug that I accidentally introduced.
So, that one would be nice to have in. The other ones are… hopefully just…
To make people feel good about the work is that the histogram one, because there's no
Contention over anything improves performance by about 10x, and the fixed size one, because there's contention on.
Tyler Yahn 01:01:31 Yeah, okay.
David Ashpole (dashpole) 01:01:32 That, like… Some of the shared things improves performance by about 3X, so… That…
There is a lot of room for improvement here.
And… Yeah.
No, this is great.
Tyler Yahn 01:01:45 This is what I was asking for, so it's mostly on me. So, yeah.
David Ashpole (dashpole) 01:01:49 Yeah, cool. But no need to review these yet until… the other stuff, the counter performance improvement and the benchmark PR is probably more important, so…
Tyler Yahn 01:01:58 Absolutely.
Well, cool. Alright, well, we're at the end of time. Thanks, everyone, for joining. Appreciate seeing you here. I'll see you all in a week's time, and otherwise, stay curiously. Bye.
Robert Pająk 01:02:09 Bye.
