SIG: .NET SIG
Date: 2025-08-19
Duration: 38 minutes
Zoom Recording URL: https://zoom.us/rec/share/qoQDNoOr7haTQUoAl1G5I59nXGKXhkAMWH93u9yJzkMzyOlpeaMo7zZQfT631uC1.-NY6aB26S5oz88Td
============================================================

## Zoom Recording Transcript

**Matthew Hensley** 01:19 Me.
**Martin Costello** 01:22 Hey, Matt.
**Alan West** 02:43 Hang on.
**Martin Costello** 02:45 And….
**Matthew Hensley** 02:47 Hello.
**Alan West** 02:54 Let's see here… Hey Simar, is, Raj back?
**Harsimar Kaur (Simar)** 03:00 He is back.
**Alan West** 03:03 You might be joining this one, let me see. Yep, he's here.
Welcome back, Raj.
**Rajkumar Rangaraj** 03:12 Thanks, Anand. Hello, everyone.
**Alan West** 03:35 You wanna take back over the reins, Raj?
Or would you like me to share.
**Rajkumar Rangaraj** 03:41 Sure, Lynn. I'm not prepared for it, it just came back yesterday, so let me try and drive it.
**Alan West** 03:50 Up to you.
**Rajkumar Rangaraj** 03:55 I think.
**Julius Koval** 03:57 Alright.
**Rajkumar Rangaraj** 04:00 Let me share my screen.
Everyone able to see my screen? I'm just….
**Martin Costello** 04:21 Yep.
**Rajkumar Rangaraj** 04:23 God.
Yeah, there is a topic that's been added for discussion by Martin. I think we can start with that today.
**Martin Costello** 04:36 Yeah, so I've… there's a link to the issue I opened this morning there. It's… at least for, like, Docker has highlighted this, it's like, every week we get a Docker we get, like, multiple Docker PRs to update all the shares. Dependabot can't update all of them in one go, so we end up just having to manually patch The PRs?
But I've recently been using Renovate rather than depend a bot for things.
And it seemed… Weirdly, because it's less smart, because it doesn't inherently use the .NET tooling to update .NET dependencies.
It actually does a better job, because it just finds more files and changes more things at the same time.
So, I'm proposing we use that instead of Dependabot, so there's less manual work to do to keep things up to date.
**Rajkumar Rangaraj** 05:39 Martin, I did take a look At this issue yesterday, and did slightly more research on this.
Dependable Board is a native tool to the GitHub, but this is an… The… another external tool that we plan to bring in.
So did you evaluate the licensing part, whether it can be used with any packages and all….
**Martin Costello** 06:06 Well, it's already used by at least two other OpenTelemetry repositories, and we use it at Grafana.
**Rajkumar Rangaraj** 06:13 Okay, prob… maybe even before we merge, we need to understand from them what else is needed. Like, I under… I saw a PR also from you, like, a draft PR, at least. So just want to understand what's the licensing part. Do we need to update any of our licensing stuff before utilizing this? And also….
**Martin Costello** 06:39 Not to my knowledge, it's just a GitHub app you install.
**Alan West** 06:43 Just to comment on that, if you just want to ping Trask on that, he's using this extensively in OpenTelemetry Java.
He'd… he'd know, right, whether there's any particular concerns there.
Though, I suspect there isn't.
**Rajkumar Rangaraj** 06:58 Oh, I can work with Trask offline. That would be easier then. I'll get details regarding the licensing part on this here.
**Alan West** 07:07 Cool.
**Rajkumar Rangaraj** 07:10 So, overall, I saw, even your… from your draft PR, it makes things simpler, but the other question I have it, at least this tool is new to me. The moment when you created an issue, that's when I knew about this one. So, just want to understand, I know it's working for the other repos for other languages.
What's the confidence level that we have at, like, this Renovate works without any issues?
the other repos? Do you have any… I know you… Quoted some example, but is it used in any big repos and really reducing the administrative work there?
**Martin Costello** 07:52 Well, the data points I have is we use it extensively at Grafana, and I've changed almost all of my own personal repositories to use Renovate, because I think it's better than Dependabot to do .NET dependency management.
**Rajkumar Rangaraj** 08:04 Okay.
**Alan West** 08:06 Yeah, and I think Trask is another good data point for that, because he… of… anecdotally from me, because I don't know the details of the Java repos, but he seems to have, drastically reduced his maintenance burden, using Renovate over Dependabot.
And for very similar things as, you know, what we're struggling with here.
**Rajkumar Rangaraj** 08:29 Yeah, the only thing what I want to know is, like, the… when I started reviewing about this tool and everything, still there are issues arises with it, so that's why especially I wanted to know from the .NET, is it, like, used somewhere and proven to be good? So….
**Martin Costello** 08:48 So, one thing….
**Rajkumar Rangaraj** 08:49 that used within Grafana, and you have the… built the confidence with it.
**Martin Costello** 08:54 Another thing I'll say is that the maintainers of it are extremely responsive, and I've done pull requests to renovate, to change things that I've found since adopting it.
And they've pretty much all been merged within a day or two, and then they're available within a few days, whereas Dependabot seems to take a lot longer to take community changes and ship them.
So if we do have problems, there's very good chance we could just fix them.
**Rajkumar Rangaraj** 09:25 Sure. So, from a maintenance perspective, I see this as a lifesaver, instead of us, like, me or Ellen, every… or even the approver. Every time we go and do a small change, if it can be grouped, something like this.
it's good. I don't see… whatever this tool does, I see, as a maintainer, it's a very less work for us. It's reducing us the time, lot of time. So, I'm in favor of it. So, that's why, just to get the other confidence and the licensing part, I just thought I'll… even if you don't add it, I thought I'll bring that question to you if you join.
So, nice. I'll take a look at… I'll have a discussion with Frask, Anyways, the other part you answered about the confidence, how it's been used outside of it.
**Martin Costello** 10:15 Yeah, I think other than the pull request I've opened, which is just an example of how to configure it to get it to do things what I think is the right way.
all that would need to be done is install the app into the repo, into the two .NET repos, and then… merge the config change from Dependabot to the other one, and then it should start picking changes up.
**Rajkumar Rangaraj** 10:40 Sure. Probably even if we plan to do it, I would say we should start with the contribo, and then, move on to the main repo.
**Martin Costello** 10:48 Are you… It might be easier to do it this way round, because it's… Less than 10 projects versus dozens.
**Rajkumar Rangaraj** 11:02 Got it.
Does anyone have any questions here?
**Alan West** 11:15 Nope, I think this is a good thing to look at.
Heard about it for a long time, so it'll be cool to see how it works out.
**Martin Costello** 11:22 I think another thing I'll add is that I was a mass… I've been a massive Dependabot fan for years.
And then I thought this did a better job and moved away from it. So I feel like I've betrayed Dependapot.
**Rajkumar Rangaraj** 11:47 Okay, let's move on to the next topic, as there are no other questions related to it. I see Julius added a topic on Logs Bridge API.
**Julius Koval** 11:58 Yeah, hi. So, … Basically, while you were away, we, I guess talked briefly about the LogsBrush API and some context.
And so I was wondering if you have any thoughts on when it might get stabilized and, you know, or if it might get stabilized in the foreseeable future.
**Rajkumar Rangaraj** 12:26 So, if I recall correctly, I might be slightly incorrect also, if I recall correctly, We are waiting on the, … net team here, to come up with the events API. The reason is, what we feel at this point is, when I had a discussion with Blanche earlier about, because he did the LogsBridge API part in the SDK here, but it's under the experimental flag.
So, the stabilization is pending on the event, because the APIs from there, which might get introduced from the .NET Events API, might overlap with this, so that's where it's pending. Probably we, by this September or sorry, October or November, we should have some conclusive answer on how, we will head to our… head forward with this LoxBridge API. Alan, do you have anything else to add here? Like, you may know even more about… background about this one.
**Alan West** 13:35 Yeah, we talked about this a little bit, while you were out. Blanche was actually on the call at the time. He's not here today, is he?
But he… I believe the work that you were just referring to about the events API from the .NET team.
I think he conveyed that he didn't have very high confidence that they were gonna take that on.
So I guess, I guess that's an open question. … about… Really, what direction… They're gonna go, and will they… Will they bridge this gap, that we currently have?
If they are, that's cool, and I'd love to get more details about that, and it might be helpful if we started communicating those details as well.
But if they're not going to take it on, then… I really do think that we need to start formulating our own plan, as a SIG for how we're gonna land this.
… at least the… because I think the… I think the API that Blanche prototyped a while back… Is… Pretty solid from the standpoint of, like.
completeness of features, with respect to the OpenTelemetry spec.
… So, yeah, I mean, I guess I'd want to hear more about what's happening internally from the .NET logs team.
To see how these… How these, work together.
**Rajkumar Rangaraj** 15:12 I did… review the, the existing part, which is added by Blanche, and even… Blanche and I had a discussion, and we have a thumbs up that this API in the SDK looks good.
Like, last past two months, I've been out, like, I don't know what's happening in that event API, probably I may need to follow up there and see, or just go into the .NET runtime repos and see, where they are heading towards this one. Based on this, I think we need to formulate a plan in the upcoming 6 to see how we can unblock people to use this one.
**Alan West** 15:53 You know, actually, I think… I just realized, I think we're talking about Two, somewhat related things, but… Two different things.
… Julius is… asking about the bridge API, which would enable things like writing log appenders for Siri Log, and others, you know?
….
**Julius Koval** 16:15 Yeah, that's what I meant. I was just, curious, what did you meant by taking on the event API, or…?
**Rajkumar Rangaraj** 16:24 So, exactly, I'm speaking about the same thing here, the log happenst. The only thing is that, the event API, which may get introduced by .NET, may have an overlap with what we are trying to do, … the new API that is part of… which is an experimental now, so it may have an overlap. So, that's why we have to hold this work instead of, hurrying upon it. So, really, I don't know where that is now the events API part, for us to continue on this one.
**Julius Koval** 17:07 I guess I'm not exactly sure.
what's the difference between events and logs? Because my understanding was that events are….
**Rajkumar Rangaraj** 17:15 Yeah.
**Julius Koval** 17:15 Thank you.
**Rajkumar Rangaraj** 17:16 In .NET, it is… they made it really complicated, I mean, with that way, because even if you look at an event name, which got, like, in the spec, it got stabilized recently, but .NET already has an event name, which is a part of… emitted as a part of every log.
If you create using a logger template. So, in the other languages, if you look at it, they need to add that manually in the .NET it emits as a part of the every, log record. It is one of the field in there.
So, things are slightly complex when it comes to this. We don't want to make the logs part much more complex by introducing one layer from the .NET and one layer from the SDK, so we want to try to avoid those kind of issues.
So, there was a, like, a .NET PM earlier. He's not with .NET anymore.
So, he said… he strongly suggested us to hold on to this. He felt that the APAs from this one and the events are going to overlap.
Blanche is not here. Probably it's an app to have the Blanche to have that discussion. Probably, let's see if we can get him. I don't know the internals of how the even ABAs might… come and interfere with this one. I need to go and revisit that part. But definitely, we were holding on to this because the event APA has some relationship with the, the experimental APS that we have it, because the event names and everything is already a part within the log record at this point.
**Julius Koval** 18:58 Well, yeah, I… I added that, actually, when you were gone, so… I guess that was… wondering… I'm just not exactly sure what we're waiting for.
With regards to the event API.
**Alan West** 19:15 Raj, Raj.
… Blanche shared an issue, and I'm not able to find it right now in our previous discussion. The conversation is broader than the events API, and I do think that we need to pull that issue back up.
Apologies, I can't find it right now, but it'd probably be good to have another conversation with you and Blanche present.
Because there's more than just events, right?
The log specification also requires us to support, like, any value, from the specification, which… is not something that iLogger necessarily has good support for, so that'd be, you know, another topic.
That we would want to know, kind of, where the logs team is at with that. And I think this issue, you know, talked about events, it talked about, like, the any value concerns, and it also talked about Like, how… how the… how or if the .NET team would take on supporting … log appenders, you know, built on top of, like, iLogger, I think was the… was one proposal. I think you actually prototyped a solution a while back, but I don't know that we fully vetted it. So I think… I think that there's… There's a variety of topics, not just events.
And I guess it would be good to pull that up and see how all this is interrelated, and pull together a plan for… For all of those.
**Rajkumar Rangaraj** 20:55 Yeah, and one such thing is, like, it is an API, so I'm… whenever we say open telemetry in .NET, most of our APIs are a part of the .NET itself, and not an SDK, so… I was in, … Blanche created all these experimental APIs as a part of the OpenTelemetry.net SDK, but I'm a big fan of moving, that to the .NET install itself instead of having that in the OpenTelemetry SDK. And these are also kind of discussion happened in that issue, so… but we did not end up in a solution which is the right thing and everything. As Alan called out as a… a temporary resolution. If someone asked, hey, I need to have an appender, what will I do with? So that's when I created a proof of concept in the contrib repo, the pull request, to say that you can have some intermediate solution until this is available.
**Julius Koval** 21:55 Well, I, I actually created an appender for analog using the LogsBridge API, and it works well.
I guess those are my two cents.
And, regarding the any value thing, I… Yeah, personally, I think, … I guess my two cents would be that I like the way it works now, because… I guess, currently you just pass in an object, and then… I think the… this… the Protobos serializer, basically.
Figures out what it is.
You know, cause… I guess otherwise, the… the users of the API would have to do that, which… You know, I guess it would be less convenient.
So I guess that's, those are my thoughts on that.
**Alan West** 22:49 Do you think it would be possible to get, somebody from the .NET logs team on one of our calls? Maybe, maybe them, and maybe Blanche, who's.
**Rajkumar Rangaraj** 22:57 Yeah.
And that team has gone through a big change.
**Alan West** 23:02 Okay.
**Rajkumar Rangaraj** 23:03 recent time, so I… and it has just happened before I left, so I don't even know who's the new point of contact in that area. So I had to follow up with Noah to see what changes has happened, and whom we can rely upon. And earlier, Sam Spencer used to help us a lot. He used to join us here, and… drive the clarity and everything. Sam's venture is no more with Microsoft, so that makes it even more difficult.
**Alan West** 23:29 Yeah, Sam was great. … And I think he was… yeah, the issue that I was trying to find, he… it was actually him who had opened it.
And I was trying to drive this.
Yeah, the thing that… the thing that I'd like to… I think… I think would be good for us to connect the dots on sooner than later would be… you know, identifying whether this is still a thing on the .NET logs team radar.
And if not, right, that we can… we can begin to determine what our plan's going to be, right? But if it is, then maybe… maybe it'd be good to get some closer collaboration with that team.
Because I think that that's one of the things that's really been missing here. I think that a lot of people have been asking about this log spreads API for some time now. I mean, like, I think at least a couple of major versions of .NET have Gone by now, and we have continued to kind of hold on to this story that no, like, iLogger is gonna be the future, but it hasn't turned out that way. I think… at least that's been, I think, people's perception here. So I think some, like, closer collaboration could… Maybe dispel some of that perception, and we could maybe better understand what… Where we're going.
**Rajkumar Rangaraj** 24:57 Makes sense, Al.
**Alan West** 25:09 Cool, yeah, so then I guess, … Give it some time to, maybe… Forge a new connection with that team, and see… See if they have some time for us?
**Rajkumar Rangaraj** 25:24 Yes, that's what my plan. I'll go and connect with Noah and see, like, … Post-up.
Point of contact for us to… figure out. The other thing I needed to reach out is, like, connect with Blanche also to understand what he has done, when I was not here.
And if we look at it in the, like, in our repo, what is the next big thing? And I do see this is the next big thing. We don't have any other big feature that's pending on us.
**Alan West** 26:00 Yeah, I agree.
**Rajkumar Rangaraj** 26:09 Cool, let me move on to the… I think this one… I thought it was pending on me, like, but there was a change requested in it.
-Oh.
I don't know who blocked that.
**Alan West** 26:34 Yeah, I did not find time to closely review this one. I know that in, this individual's previous PR, You had raised I think a security concern of some sort, and I didn't quite connect the dots, but I didn't want to necessarily… … Go forward with this until you had a chance to… To take a look at it.
**Rajkumar Rangaraj** 27:01 This one is… then I'll go ahead and take a look at that, because I promised, once after I come back, I'll be looking into this. That's what I… informed. That's the last update on this one.
I think this is a very small thing that I need to… Just do a smaller commit, too.
get this moving. It has… misspell. I'll just go ahead and update this and get this merged.
… DiscordQL fix, I don't know… Martin… I don't know, what's the plan on this? Do you want… So….
**Martin Costello** 27:47 So, I… I don't think this is worth trying to test in a fork, because most of what's been changed is to do things like publish to NuGet. I can't test that works, and it's pretty much a mechanical replace interpolation with an environment variable. So, if code inspection, it looks fine, then I'd say we'd go ahead with it. I haven't fixed… rebased it yet. Go ahead with it, and then if anything does come out that's broken, it can just do a PR and fix it forwards.
Because I don't think it's realistically worth the effort to try and mirror the entire open telemetry setup.
And run all the possible workflows.
To just validate that this works.
**Rajkumar Rangaraj** 28:38 So this is also blocked on the same … if I understand correctly, it's touching the release.
**Martin Costello** 28:49 It is, yeah, but I can't really… Sure, it could potentially break it, but I can't replicate and test doing a release.
**Rajkumar Rangaraj** 28:59 Yeah. Do you want to, like, get the changes to both contrive and SD main ribo at the same time? Can we get it done in the contrib, learn from there, and move the changes over here?
**Martin Costello** 29:11 Well, that's essentially what these PRs are. I did one, and then I did the other, but they've both been stuck on the same reason, which is just, have you tested it?
**Rajkumar Rangaraj** 29:21 probably I'll help you move this, yeah, the contrary one, and then if something arises, we can fix it in the follow-up, yeah.
**Martin Costello** 29:32 Okay, that's fine. Yeah, I just… for what the workflows do, I don't think I can realistically test them in advance.
**Rajkumar Rangaraj** 29:40 I did look at this PR, and it looks good to me, even when… there is an issue related to this, I believe. When that was created, even I tried creating a doing, creating this change, but before that, I saw your PR, then I stopped working on it, so it looks like what I had it in my mind, so it looks good to me.
And I also agree with you, the testing is very, very difficult on another four, as you need to fire a release request and all that. So, probably whichever the thing next release that comes up, we can get this tested with that and see how it goes. If not, we can try and patch shit around that time.
**Martin Costello** 30:25 Yep, okay.
**Rajkumar Rangaraj** 30:35 I don't think… Is there any other thing that needs… attention, okay.
**Martin Costello** 30:42 Would you mind reviewing the second-to-last one? Because I think this is really trivial, and it's been open for ages.
**Rajkumar Rangaraj** 30:50 Oh.
I… if I recall correctly, I just tagged Blanche on it, ….
**Martin Costello** 30:56 You did, and I have as well, and he hasn't responded, and I think it's so trivial that it's just….
**Rajkumar Rangaraj** 31:02 for you to just ping him over a Slack to get the… the reason he said is he has a very strong opinion that it should be, debug assert, so that's why I wanted to take his opinion there.
**Martin Costello** 31:17 I couldn'.
**Rajkumar Rangaraj** 31:18 Like, premium….
**Martin Costello** 31:18 I don't quite understand what you mean. The assertions fail.
**Rajkumar Rangaraj** 31:24 Yeah, … you might… see his earlier comments about this asserts, that he strongly feels that this asserts needs to be present.
**Martin Costello** 31:37 Sure, but they are not… they are… They did not correct.
I did look at it, because I assumed it was a bug, and I looked through the code, and they just thought, like, they're wrong.
**Rajkumar Rangaraj** 31:51 So, you may see… it's not only you, and the people in the past also had the similar opinion, and they tried creating the PR to fix that.
So, probably having… you having that conversation with Blanche over the Slack would help us, move that faster. Blanche may take… he may not be just… watching out the PRs directly, just pinging him, we can get the attention and move that PR. If it's very simple, we are.
**Martin Costello** 32:22 Okay, I'll ping him again, but yeah, I did ping him on GitHub.
**Rajkumar Rangaraj** 32:27 Okay.
No, I would recommend you to ping on the Slack. He may not be taking a look at the notification email from the repo, so he… I think not a major… thing.
So it's a unit test.
This has to be investigated.
I think… the most of these years are already out under here. Is there anyone Need to discuss anything here, or do you have… anyone has any other topic for discussion?
**Alan West** 33:34 There might be one other PR that, you might want to take a look at if you haven't already.
It's in the middle. We talked about it a little bit last week, the batch export processor.
… It's another large one.
Martin's taken a pretty thorough look at it.
I took a quick look at it, had to comment on a new public API that it's introducing that I wasn't super excited about.
But, … had a suggestion that maybe a focus on the Blazor support in this PR. Martin also had a suggestion that it would be cool to have an integration test.
If it is something that we're looking to do, basically declare support for Blazor WebAssembly, … And whatnot.
Anyways, just wanted to bring it to your attention. You might want to take a look.
**Rajkumar Rangaraj** 34:32 I might take, like, a few days to get to this. This PR is huge, and we know this, … we… this is kind of adding this another… … threading is… it does some changes to the threading and everything, what we have it. Always… the entire SDK is designed for the synchronous one, so I… I do believe this is trying to bring some async one, so I don't know how it's going to impact every other part of the SDK, so I need to take a closer look.
**Alan West** 35:07 Yeah, I agree. And that's one of the reasons why I was thinking that it might be good, if possible.
To scope it.
to just be a Blazer thing, you know, something that wouldn't impact or have any effect on… regular consumers of the SDK.
**Rajkumar Rangaraj** 35:24 Yay.
**Alan West** 35:24 … But yeah, that's a big one. So, like, I'd say take your time with it. I'd say that, … I guess the thing that was just on my mind is that It looks like he's gonna continue putting effort into it, and if we… if we want to basically pull on the reins, it'd probably be good to, like, communicate that to them in some way.
I wasn't sure if….
**Martin Costello** 35:49 I think, to be fair as well, it's less async, it's more you can't use threads in Blazor.
It's just… tasks are a way to… do background work that isn't threads, but then if it's a single-threaded model, it will just happen Directly anyway. Like, it won't be… background work.
**Alan West** 36:17 Right.
Yeah, I think there was a previous PR that was actually introducing, like, async versions of our export.
**Rajkumar Rangaraj** 36:28 Yep.
**Alan West** 36:28 Or our, like… on the interface of the processor, but I… that's not what this PR is doing.
Anyways….
**Rajkumar Rangaraj** 36:53 Cool. Are there any other topics?
**Julius Koval** 36:56 I just wanted to ask, you talked about, … contacting some locks people from the .NET team. And so, would you want to bring them on this call, or do you want to contact them separately?
**Rajkumar Rangaraj** 37:11 No, I don't know whether they'll be willing to join here, so I'll let them decide that, or take a call on that part, but I know of one of the .NET guys, so I'm just going to reach him out to see whom we could speak, or where we can find the issues, so that we can go and interact in the .NET repo as a hotel maintainers, or the hotel contributors in those spaces.
**Julius Koval** 37:39 Sure.
… If you talked about it and some issues, would you mind pinging me, if you remember?
I'm curious about this.
Well, I was asking that, … If you discuss this in some issue, if you could ping me, if you remember, because I'd be curious about this.
**Rajkumar Rangaraj** 38:02 Like, I'm going to make it transparent. Whatever information I get, probably I'll bring it in the next SIG. Even if I get all those issues, probably I'll help document here, so we can go back and everyone can find it.
**Julius Koval** 38:16 Okay, cool, thanks.
**Rajkumar Rangaraj** 38:34 Cool, then. I think then we could end the meeting now. Thanks, everyone. Bye.
**Alan West** 38:38 Cool, see y'all.
**Martin Costello** 38:39 Bye.
**Julius Koval** 38:39 What?
