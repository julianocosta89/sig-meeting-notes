SIG: PHP SIG
Date: 2025-09-10
Duration: 75 minutes
============================================================

## Zoom Recording Transcript

Chris Lightfoot-Wild 00:00:35 Hey, Sega.
Sergey 00:00:36 Hello, Chris, how you doing?
How's the weather?
Chris Lightfoot-Wild 00:00:42 What was that, sir?
Sergey 00:00:43 How is the weather? Are you in,
Are you in England or in Scotland? I forgot what…
Chris Lightfoot-Wild 00:00:49 I mean, yeah, in England, not too far from Manchester.
Sergey 00:00:54 Okay. Manchester, it's, it's northern?
in London?
Chris Lightfoot-Wild 00:00:59 Well, we're kind of about halfway up, I guess. I'm in Yorkshire, which is… I've got a… not a Mank accent.
Sergey 00:01:04 Oh, Yorkshire.
Chris Lightfoot-Wild 00:01:05 Yeah.
Sergey 00:01:06 expensive fencing.
So, how is it, the autumn stopped already?
Chris Lightfoot-Wild 00:01:11 It's starting to, we've got a bit of a temperature drop, and yeah, a bit more showery.
Sergey 00:01:17 Mmm.
Chris Lightfoot-Wild 00:01:18 Definitely on the back end so much.
Sergey 00:01:19 Is it a Tolbishop? Like, you have a different amount of, rain during seasons? There are seasons in.
Chris Lightfoot-Wild 00:01:25 But, I mean, in England, it does rain quite a lot.
Sergey 00:01:29 My childhood memory is, like… I spent my childhood in the Soviet Union, and, like, my impression of
mostly what we saw in London was based on Dickinson, so those Dickinson things, like, it's always, like, muddy and rainy and, yeah, so that's.
Chris Lightfoot-Wild 00:01:44 Exclude me.
Sergey 00:01:45 Guess, yeah.
Yeah, Deakinson, you have.
Chris Lightfoot-Wild 00:01:48 Charles Dickinson. Charles Dickinson, yes.
Sergey 00:01:52 Oliver Twist and all that stuff, yeah.
That definitely paints a particular picture of London.
England in general, I guess, yeah.
Chris Lightfoot-Wild 00:02:04 No, the big smoke.
It's the…
Sergey 00:02:07 Was it even there? Like, was it even then, smoke? Like, well, I guess they use coal, right? Yeah.
Chris Lightfoot-Wild 00:02:13 Wing that.
Yeah.
Sergey 00:02:16 Is it different from Manchester? Is Manchester a big city?
Chris Lightfoot-Wild 00:02:20 Well, I think it's got a claim to be in, like, you know, the second city.
Sergey 00:02:24 Oh, okay.
Chris Lightfoot-Wild 00:02:25 I think Birmingham also has a claim, and like, you know…
Sergey 00:02:28 Is it still industrial? Like, do you have smoke as well?
Chris Lightfoot-Wild 00:02:31 No, we don't… no, not in smoke anymore, but a lot of, like, old textile mills and things that are, you know.
The buildings get reused as, like, modernized flats or something, or other things, but they're still kind of… the architecture's still there.
Yeah, a lot of it didn't necessarily get bombed in the war, because obviously in London.
That they were bombing that bit, and didn't get quite as far up north.
So…
Sergey 00:02:56 Hmm.
Chris Lightfoot-Wild 00:02:58 But we're not quite as modernised then, so we're in the dark ages up here.
Sergey 00:03:02 Hmm, not interesting.
Right.
Chris Lightfoot-Wild 00:03:05 Sorry, we… hey, everyone else, we were just… Killing time went fuel.
We do.
Sergey 00:03:12 Hi, Brad.
Bob, is Bob going to join, or…
But he's on vacation.
Pawel Filipczak 00:03:19 Hang.
Chris Lightfoot-Wild 00:03:20 Bro, I can't hear you, I don't know if… Awesome.
Yeah, I think it was Bob off for 2 weeks now, it was on.
Sergey 00:03:31 Hmm.
Brett McBride 00:03:35 Blue.
Chris Lightfoot-Wild 00:03:37 Hello, can he help?
Brett McBride 00:03:37 Oh, good. Okay, sorry about that.
Yeah, I believe Bob's on vacation.
So I'm happy to,
Share screen and run if everyone's… if no one's gonna beat me to it.
Chris Lightfoot-Wild 00:03:51 Alright, I'm only guessed.
Brett McBride 00:04:03 Excuse me. Alright, let's… let's run through it.
No, I've got it.
Tab in Novailia.
I can move it. Okay.
Alright, let's run through in the backlog. I don't think there's anything…
Anything new in this… in this backlog, since last week.
This one, though, I did start working on today, which is… Trying to update.
Matrix temporality, I'm not even entirely yet. I… I started working on that. This is a…
Vision 2.
Thing, which I'm, yeah, trying to work through. That's all I've got at the moment.
But I think I've got some tests passing for it.
Sergey 00:04:59 Version to you, man.
You're targeted for SDK version, too?
Brett McBride 00:05:03 Correct.
Sergey 00:05:04 Hmm.
Brett McBride 00:05:05 Yep.
Sergey 00:05:06 Is it because it also breaks, or it's just, just easier to…
Brett McBride 00:05:10 It's a… it's not an API-breaking change, but it's a behavior-breaking change, I think, as, suggested by… by, Niveay, the…
Sort of the original author of, other metrics
Part of the… of OpenTelemetry.
Sergey 00:05:31 Oh, interesting. He's the guy that built the infrastructure for service provider, right?
Brett McBride 00:05:37 Yes, that's right.
Sergey 00:05:38 I thought he's kind of like a general PHP guy, huh? He's also involved in OpenTelemetry, like, in particular?
Hoping some discussion.
Brett McBride 00:05:45 a year.
Sergey 00:05:45 as well? Oh, okay.
Brett McBride 00:05:46 Yeah, yeah, yeah, if you were to look at that…
Sergey 00:05:48 Like a gen… general… generous PHP guy. Okay.
Brett McBride 00:05:53 No, no, he's, he's had a lot to do with, he wrote the original auto instrumentation.
The entirety of metrics, a lot of context, so some of the really, really hard.
complicated bits of OpenTelemetry have been his main contributions.
Sorry, excuse me, I'm still a bit unwell after 2 weeks. So… what's new?
Okay, I've… I generated just the latest protobuf, which had no… no significant
changes for us. It was mostly, sort of the profile signal, which we don't have any implementation of, but I just thought I'd do it to keep us up to date.
the response propagator interface, that came in yesterday, I think I've had a bit of a look at that.
So, in… In contrary, we've got a couple of, sort of.
backwards propagators, I think they refer to them as, where we can…
Return information to a client from a server.
And that's… I feel like that's been at least a year, possibly even two years, sort of where we've had a…
An implementation in Contra, and we've sort of been waiting for the spec.
to… to catch up. The specs not catching up, the… the related issues have just been sitting there.
Sort of…
just… just waiting for something to happen. And so, I think based on that, this,
this author. There's a couple of guys, I think they might work together.
Who've been trying to push this.
Instead of using our SIG.
Since we… we have the server timing and trace response propagator already, just to sort of push it along. And I think they've got their own reasons as well. They want to implement,
Some type of response propagator, so…
Yeah, that's what this one's about. I'm keeping an eye on it. I think I'm… I'm generally in favor of it, provided we slap experimental all over it. But it's adding some new interfaces into
sort of into our core repository, so that response propagators can be done properly in Contrib.
Chris Lightfoot-Wild 00:08:36 without going… V2, if it's a big enough change, or is that still… because it looks like it's going.
Brett McBride 00:08:42 to the line.
Chris Lightfoot-Wild 00:08:42 at the moment. Yeah, I think it's.
Brett McBride 00:08:44 fine to go into V1.
Chris Lightfoot-Wild 00:08:46 Okay.
Brett McBride 00:08:49 Yeah, I don't see any breaking.
Chris Lightfoot-Wild 00:08:51 Okay.
Sergey 00:08:54 What do you estimate is the timeline for releasing V2?
Brett McBride 00:09:02 That's why I was working on the… what I believe is the one outstanding issue today, because I would like to get it done and out.
Like, in the next couple of weeks, if I can. I'm about to take some extended leave, and I won't have
a lot of… Sort of free time.
to work on OpenTelemetry.
For probably the next 12 months, or 10 months. So I was hoping to be able to get this out.
V2 out, before I go and leave.
Sergey 00:09:36 And, and, what were you thinking about, all these proposals that are still done on V1?
was the plan to also apply them to continue, kind of, maintaining V1, and then also…
merging them in V2, or…
What is the… what do you think would be the best approach of, and all the new stuff? Should it go only to V2 from when V2 isn't released, or…
backported to V1.
Brett McBride 00:10:05 Look, I think… I think probably once we go to V2, we should.
So for the time being, I am sort of forward patching everything that goes into the main branch, out into V2.
I…
Look, we haven't decided yet, but I think my feelings are we don't… we don't have enough maintainers to sort of be maintaining
Sort of V1 and V2.
I'll probably tag it, or create a branch for 1.X, just in case we do need to…
Sort of, you know, Patch in some urgent bug fix or something.
But… but I think my feeling is probably that,
When we release SDK V2, we really focus on that, and it becomes our only
We're our main supportive branch, anyway.
Sergey 00:11:04 So, for now, the approach is, only maybe some security fixes are really important that those will be backported, but
all the new stuff, especially features, only YouTube.
Brett McBride 00:11:15 Yeah, yeah, once it goes out and becomes live, yes.
Sergey 00:11:19 Okay.
Brett McBride 00:11:20 Yeah, yeah, it's not that different, it just has some braking changes in it.
Sergey 00:11:27 No, I just wonder, what about capability… do you also want to, at least all the contrib stuff, also bring it to be compatible with V2, or…
is… yeah, I assume it… those are breaking chases will not,
Will not affect the country, or…
No, they will affect. They will affect it. So… so…
I assume your plan is also to bring it… to be compatible maybe in the same release, to have country also compatible with V2?
Brett McBride 00:11:56 Probably not in the same release, but following on, because obviously they can work with either.
But yes, contrib would be the…
Sort of the most affected, thing, because one of the main…
So the average user shouldn't… shouldn't notice the change, it's more instrumentation authors, which is basically everything in Contrib. So the way that,
We register.
you know, instrumentation modules or whatever has changed slightly. It uses SPI.
Exclusively now.
Yeah, those are the…
Sergey 00:12:40 already switched to SPY? SPI?
Brett McBride 00:12:43 None.
Sergey 00:12:45 Okay, so they plan to switch it after V2?
Brett McBride 00:12:47 Yep.
Sergey 00:12:48 Oh, okay.
And, okay. So then the plan is, first step is to release with SDK. Probably people that will be able to use it, only those that use the decay directly, but…
If they want to use Contrib, they will have to use V1 for time being, and then when the second step will come, when all the instrumentations in Contrib will also be upgraded, then people can also use V2 with the instrumentations from Contrib.
Brett McBride 00:13:15 Yes.
Sergey 00:13:16 Got it. Okay.
Okay, makes sense.
Brett McBride 00:13:23 Cool, nothing else new in… in the main repo?
Chris Lightfoot-Wild 00:13:29 On the back of that, obviously, not to commit to it as any kind of the roadmap that we've got in our board here, but is that the sort of thing, then, if you manage to get V2 tags, we'll just put in all the contract packages as, like, their road to V2, and we can
Between us, maybe picked them off of a… Yeah, the coastline.
Brett McBride 00:13:48 Yeah, yeah, I think so. So, I don't think the changes will be too onerous, but but…
But just… just talking about it now, it's… it does occur to me that we can't install both V1 and V2, so we kind of want…
probably want to sort of switch everything over to be compatible with V2 at, you know, roughly the same time, or in fairly quick succession.
Oh, no, no, maybe not, because maybe we just V2 the, you know, create a later version of, you know, say, V2 of Laravel, which supports SDK V2, or… and I think we kind of talked about that.
Yeah. Obviously, we… Yeah, okay.
Yep.
Sorry, I thought I'd.
Sergey 00:14:37 So you think…
Brett McBride 00:14:38 I need to…
Sergey 00:14:40 Excuse me? Can you repeat that, please?
Brett McBride 00:14:43 I said, I thought I'd just, found a massive hole in my… my plan, but, no, I think… I think it's okay.
Sergey 00:14:51 You think we don't need to upgrade all the contrib, like, more or less in one go?
Brett McBride 00:14:59 No, that's right. It's just that the ones that have been upgraded won't be…
Able to be used at the same time as the ones that haven't.
Sergey 00:15:07 Right, right, but if we assume that people use, like.
a lot of these instrumentations at the same time. Then, in order to have that.
They will have to… they will only be using.
Brett McBride 00:15:21 soon.
Sergey 00:15:21 So, essentially, like you said, only one SDK can be present, right? So, all the instrumentations either need to support… well, they already, all of them support V1, but then if you want to use any… so you will be able to upgrade to V2 only after all the instrumentations that you rely on also upgraded to V2.
Brett McBride 00:15:37 True.
Yes.
Sergey 00:15:39 So, maybe in general it's less of a problem, although I assume it's, depending on which combinations people use, so…
Yeah, I'm just trying to understand our distro, since it packages a lot of instrumentations, maybe it's a different use case, so although…
Even though each user may be not using all the instrumentations, but since all of them can use different combinations of, let's say, 3 or 4 instrumentations, then eventually you get to the same situation that you need all of them to be either V1 or V2, right?
Brett McBride 00:16:08 Yeah, yeah. And look, I think for the average use case, Composer will…
will protect you. You know, you.
Sergey 00:16:17 You mean you will not be able to… it's not something that you will have to discover at runtime? You'll be able to discover it even at the stall time that the combination is impossible? Yeah, that's probably good.
Brett McBride 00:16:27 Yep. Yep.
Yep.
Okay, what else? I don't see anything newer… Interesting… in… In Contrib.
There's a couple of things…
Chris Lightfoot-Wild 00:16:45 There's that… the feat for Laravel and MongoDB, I was kind of…
Brett McBride 00:16:49 Yeah.
Chris Lightfoot-Wild 00:16:50 available.
long and closed it off, because there was a bit of a discussion between me and the author of that PR.
We.
Brett McBride 00:16:56 Where did it get to?
Chris Lightfoot-Wild 00:16:58 Well, there was a resolution, sort of suggested, and he'd found a way of getting it to work. It's kind of basic because it's a, you know, third-party package where they've decided to break the Laravel convention.
And… He's happy that he's got a workaround in place, and he just…
Brett McBride 00:17:15 Oh, okay.
Chris Lightfoot-Wild 00:17:16 But I didn't want to just be, like, a bad guy and close it off and be like, yeah, go away, because, you know, welcome contributions, but…
I was hoping Starbot might have been the bad guy, but again…
Brett McBride 00:17:25 Yeah.
Chris Lightfoot-Wild 00:17:26 You're a bit of hiatus.
Brett McBride 00:17:27 That's wild.
Chris Lightfoot-Wild 00:17:29 Do you want me to, like, follow it up and ask if we're happy to close it, or just…
Brett McBride 00:17:34 Yeah.
Yeah, yeah, yeah, yeah, please do.
Chris Lightfoot-Wild 00:17:39 Well, go on.
It'd be nice to get that list a little leaner.
some of that stuff.
Brett McBride 00:17:45 Yeah.
Yeah, yeah, yeah, yeah, that looks… yes. Just… just skimming that, it does look like he agrees. The author agrees that it can probably be closed.
Cool.
Alright.
SQL Commenter, I think, is close now,
There's just been a lot of… a lot of toing and fro in here, but… but finally, something's actually been, accepted upstream into spec, so, I feel a lot more comfortable in sort of accepting this now. I was quite hesitant when, I'm a sort of SQL commenter.
thing was… was still very much in flux, but, something… something has been accepted into spec now.
So, that's… that's actually pretty close to being, merged in, I think.
If anyone's following that one along.
I don't expect anything in instrumentation.
Can I just… Dependabot, and…
Sorry, I was just looking at that before.
So, I was just about to try and re-tag something here. Something's gone a bit wrong with my…
I think my script, or our, source control.
Where it's sort of… Just complaining about commits that are in the git split that aren't in.
Upstream, or vice versa, but I'll just manually tag that one.
What else? Laravel… Chris, I think you might have…
Chris Lightfoot-Wild 00:19:41 Thank you.
Brett McBride 00:19:42 Been looking at this one already.
Yes.
Chris Lightfoot-Wild 00:19:44 Now, I briefly touched on this last week, about, just trying to make sure that you don't have, like, these orphan spans and things, and it felt as a bit of crossover with the other issue I linked to, so yeah, I'll try and have a look at that, and maybe, you know, help this.
Brett McBride 00:19:59 Yeah… So the core of the problem is that it's sort of termination Process runs completely outside of.
Chris Lightfoot-Wild 00:20:09 Yeah, it's not just an instrumented method, so it… just as its own, you know, it's… we're not… we're not observing it, so…
You can just put the observation in, but obviously then it doesn't have a common route, so there's a suggestion of adding that, and… so I think, know roughly the direction to head in with that, but…
Brett McBride 00:20:28 Yeah, that's quite interesting.
Chris Lightfoot-Wild 00:20:31 But it would be good to, obviously… we talked about the different deployment models, like Octane and whatever FPM or whatever the user's using should probably be covered as well if we're making this change.
So, I need a bit of research into it.
Brett McBride 00:20:49 Yeah.
Sergey 00:20:50 Related to what you mentioned last time about the pausing and then resuming recording based on the… if you're inside the entry point or not?
Oh, it's a different…
Chris Lightfoot-Wild 00:20:59 In my head, there was some kind of crossover with some parts of that, but I'm not entirely certain without looking further.
Brett McBride 00:21:10 No, that's it.
Yeah, so I've actually been playing around a little bit with, the elastic distribution of hotel, over the last couple of weeks, and one of the things that it does that I like, that also the Rust extension that I've been working on does, which may help this, is…
It's the whole auto route span.
thing. So, instead of the root span being created by… you know, when Laravel Application run, or whatever.
you know, runs is… is that it's actually based on, say, rinit and… and R shutdown, so that you've always got that root span, and then instead of…
you know, that first Laravel hook.
Creating a root span, it actually gets the local root span and updates it.
And I feel like that might be a good way to help.
Like, that would… that would cover the… there's no route span running when the termination thing…
Sergey 00:22:16 I also saw that you implemented some outer root spin, Brett, right?
If we can… that would be interesting, that's something I would be interested in, maybe, before you leave for vacation,
Brett McBride 00:22:28 Excuse me.
Sergey 00:22:29 Unify somehow these two approaches, kind of, like, allow extension.
Brett McBride 00:22:32 Yes.
Sergey 00:22:33 maybe using Arnied, and but fall back on your approach if it's not available. Somehow, kind of, like, have it,
This service injectable.
Brett McBride 00:22:43 Yeah, Lauren, it's definitely the better way to do it.
Sergey 00:22:47 Are you sure it will help in this case? Like, in this case, this additional stuff that they want to record, it happens in the context of the same request, or it even happens in the context of a different request? I was not 100% aware.
It still happens in the context of the same RNETAR shutdown, but it's just outside the entry point method that was
That was, used as a kind of, like, root span entry point to the larval.
Chris Lightfoot-Wild 00:23:15 This one's in the same… the same execution, just the…
not covered currently, so I think… I'm not entirely sure, but yes, I think it's covered in the same request lifecycle, is the answer to that.
Brett McBride 00:23:28 Yeah… Okay, yeah, so I assumed that it was all part of the same Request processing, but after
So maybe as a… What happened? So, after the response is sent, is what it says.
Sergey 00:23:48 It's a little bit of a philosophical question, right? Should it be considered.
Brett McBride 00:23:51 Yeah.
Sergey 00:23:52 From the client point of view.
should any processing after response is sent to be considered part of the request processing? Because client doesn't care about it. It might create a false sense of something taking longer than it took from the client point of view.
So it's interesting how can it be conveyed in a clear manner.
Brett McBride 00:24:11 It's a good point. It's a really… it's a really interesting point, yeah, yeah, I… Because if you do…
Sergey 00:24:17 After you send the response, you don't want to imply that this was the overhead that the client was visible to the client.
Brett McBride 00:24:26 True, true, and it would.
Sergey 00:24:29 wouldn't…
Brett McBride 00:24:30 I mean…
Sergey 00:24:32 Yeah, as far as the span is concerned.
Brett McBride 00:24:36 Yeah, if the root span's still open.
Sergey 00:24:38 So maybe the root span, you can have it, maybe it's better to also have these additional spans and call them, like, this is kind of like the request process, and this one is a post-request process, and…
Response, post-response,
It's interesting to maybe sync up with the other agents to see if they have similar challenges that maybe they have. I know that inside Span, you can also set some kind of, like, events, right? You can mark events.
Brett McBride 00:25:04 You can. And the other thing is,
You can link spans, but also… A span can be a…
child span of something would then.
Sergey 00:25:16 Yeah, you can do children here, but…
Brett McBride 00:25:17 falling inside the time, start and end times of that span, they can kind of be detached, and I think the spec does allow for that.
Sergey 00:25:29 I mean, technically, it sounds like it should be some kind of links thing, because it's not part of the processing that client cares about, right?
It's similar if you called into some service, you got the response, but then that service spawned some background job to do something on the background. Even though here, in the model of, when it's synchronous, like FPM, it will incur in the sense that throughput will be affected.
Like, you're still taking time on the… on the thread of the PHP, so it will not be handled… it will not be able to handle that many requests per second, because you're still blocking it.
So in that sense, in this particular request, maybe you didn't…
this particular client didn't see the latency increasing, but throughput, amount of requests will be affected. So, yeah, the whole thing is a little bit… but again, still, you… it will be interesting to how you… this thing probably is better reflected via metrics than spuns, but how to reflect it correctly in the trace…
So it might be an interesting kind of, like, design question, how to… To show it better.
Brett McBride 00:26:32 Yeah, I mean, as described there, it still does… does feel like it's still part of the request.
life cycle. It's just the cleanup phase.
Yeah, but having it as a detached, separate process doesn't feel quite right.
In my mind, anyway.
Sergey 00:26:50 Would you feel like, for example, if it did spawn, like, if it did put it as a job in some kind of queue.
would it be different from that point of view? Like, if it did this processing completely separately as part of some kind of queue, background queue process?
Brett McBride 00:27:05 Yeah, I feel like that would be different. Then I would expect, say, maybe span linking between the two.
Sergey 00:27:13 But, so you think it's different here because it's just because it's in the context of the same request from PHP lifecycle point of view? Because, like.
Depends what you think is more important, client point of view.
the ones that get the response, or the PHP lifecycle model, right? It's, competing kind of approaches here.
Brett McBride 00:27:32 Hmm.
Sergey 00:27:33 Like, if you're all looking, like, from your point of view, like, if it's a P or a PM approach, then it's all about the client, right? What is the experience of the client? If client doesn't see it, it's like we did 3, right? If client doesn't see it affecting it, then it didn't happen. Client doesn't care about it, as long as it doesn't affect the experience.
Brett McBride 00:27:51 Yeah, well, that's true, but… but… but also, interesting things might happen that… Yeah, that's why it's interesting.
Sergey 00:28:00 It's… that's what I'm saying.
Brett McBride 00:28:02 Yeah, yeah, yeah.
Sergey 00:28:04 How to present it, so it…
Both points of view can be, you know, you can look at it from this angle and from that angle, yeah.
So maybe child spends, and you can say this is the… until the response was sent, and this is a post-response processing, then people can just concentrate on the first span. Maybe that will be the simplest solution for now.
Brett McBride 00:28:27 Mmm.
Sergey 00:28:30 Yep.
But that will require additional thinking, because it's not clear when you create this additional spawn, because it seems that…
It's kind of like, it should be kind of like some kind of, like, bag for… for anything that maybe possibly can be done, but maybe nothing is done in some cases after the response is sent.
So it's…
Less clear, you don't have a clear kind of, like, entry-exit for that part of work that can happen after the response is sent.
So maybe you need to create it on demand, kind of like just a… Umbrella span that will…
Under it, hold everything that happens after the response is sent.
I don't know if it's technically how easy it is to do, can you easily detect this response is already sent?
Brett McBride 00:29:16 Oh…
Sergey 00:29:17 Maybe the simplest solution is to just go with the root span that you suggested, and then let's wait if somebody will even care and say, okay, I want these two things to be split, then…
Then it might be worth spending time thinking how it's bigger.
But it sounds like, yeah, what you proposed at first probably you should cover, and then we can revisit it based on the, you know…
So, I will write myself to do, maybe, because I was interested in… to the truth, I was, kind of, like, was interested to have, these two things unified, this root span… outer root span creation.
Because,
sometimes I want for my testing to pin something on the root span, and we don't have this API to easily obtain it, but for root span, your implementation, Brad, you do have API and SDK that can… you can obtain that root span.
via the API.
Brett McBride 00:30:04 Yeah, do you mean the local route span?
Sergey 00:30:06 Yeah, local respond, yeah.
Brett McBride 00:30:07 Yes.
Sergey 00:30:08 instead of us implementing that alternative API, maybe we can just unify and kind of, like, integrate with that.
God.
Brett McBride 00:30:16 Yeah.
Sergey 00:30:16 Anyway, what is the reason that you… you don't have it in main, right? You didn't release that feature, local load span.
Brett McBride 00:30:23 Yeah, yeah, yeah, it's.
Sergey 00:30:25 It's a list, it's an…
Brett McBride 00:30:26 It was marked experimental for a while, but it's now marked stable from, like.
Sergey 00:30:31 Okay, so it is part of the release. Okay. So, I will take a look how maybe we can integrate with that, and
But yeah, but like you said, for it to work out of the box, they will need to use extension.
Would it make sense to port it to…
To have it as part of the existing extension?
Brett McBride 00:30:52 I think we can just say, so long as a root span
As long as the root span created from the EDOT extension is… sort of uses the OpenTelemetry
APIs to create that root span, then it should be accessible through… through local root span.
Sergey 00:31:18 Yeah, but I was wondering, if Rootspun is created using your implementation.
Will it also cover those things that happened? Because you closed the spawn… on the shutdown, right?
Brett McBride 00:31:32 Okay. Yes, we do. Yes.
Sergey 00:31:38 So technically… Yeah, we had a shutdown handler, yes.
So technically, it's possible, but you're saying the additional work is needed here if we want to integrate that Laravel information into the already existing local root span instead of creating a new root span?
So maybe integrating them somehow?
Brett McBride 00:31:56 Yeah, what I'm suggesting is… is… is a… probably a change to the way that we do
Root server spans for auto-instrumentations, which is…
We could do it one of two ways. We could either say.
If there is already a root span that is a…
You know, a recording span, it's a server span, or whatever we check. Then instead of creating a
Spain, Instead of creating a root span, we just mutate the existing root span,
But then we may also need a fallback of, well, if you don't have something installed that's automatically creating that root span, then we do need to
Sort of, create that root span manually, well, through auto-instrumentation.
Sergey 00:32:49 Right. Is it possible that it… is it possible to call one framework in the context of another framework? Like, is it ever will be incorrect to do it like that? Like, is it possible that you suddenly, in the context library, were called into something, like, slim, and it's supposed to create a separate root span, not to try to merge whatever it wants into the existing…
Brett McBride 00:33:08 Wingspot, no.
Sergey 00:33:10 No, usually you use exclusively only one framework.
Brett McBride 00:33:14 Yeah. Pizza.
Yeah, I think so.
Okay. Excellent.
Sergey 00:33:18 Yeah.
Brett McBride 00:33:19 Okay, that might be interesting.
Sergey 00:33:22 So… Yeah, I mean,
It's somehow related to the… to the work that you did on the… how you called it? Also, you called it… how you called this ability of, kind of, like, emerging, different layers of the same, kind of, like, whole…
you have something like that, right? Let's say, for example, if you call high-level API, and it uses lower level, let's say, instrumentation like HTTP calls.
You had the.
Brett McBride 00:33:48 Mmm.
Sergey 00:33:49 ability to Agents.
Brett McBride 00:33:50 I think you called it span suppression?
Sergey 00:33:53 Suppression, yeah, yeah, suppression. Yeah, so for some reason, I was thinking about compression, but we have.
Brett McBride 00:33:58 Yeah.
Sergey 00:33:58 feature spun compression, which is completely different. It compresses, like, end query issue.
So…
Brett McBride 00:34:04 So they don't…
Sergey 00:34:04 It's somehow similar to what you want to do here, right?
In that sense. Like, you essentially want to…
Brett McBride 00:34:11 No.
Sergey 00:34:12 and this autolocal expand together, like, in the same way as you want to merge in that suppression, you want to merge, like, low-level HTTP with higher level, let's say, something that goes into HTTP.
Brett McBride 00:34:25 I was probably thinking a little simpler than that in my mind, which is almost an if statement. You know, if there is already a root span, modify that root span. If there isn't.
Create it, as you… as you do already.
Sergey 00:34:39 Yeah, I agree with you, like, if that feature is not ready yet, there's no point of blocking on it and waiting until it's done in order to do this. This one is definitely a more specific case that can be done much easier, yes.
Brett McBride 00:34:52 And also, span… I don't think that's quite the purpose of span suppression.
either. That's just to…
To suppress, you know, to stop duplicates, not to… not to try and, sort of, merge them together into… into one space.
Sergey 00:35:06 When you say duplicates, I thought that you meant it, like, in the sense that you have higher level of technology that is also instrumented, and then if it goes into low layers that are also instrumented, you don't want to see lower layers, right? You only want to see higher level instrumentation creating span.
Was that the use case that you wanted to solve?
Brett McBride 00:35:26 Yeah, well, yes, yes, I think so, yes. So, maybe an example would be we have PSR18 auto instrumentation plus guzzle, plus curl, which is… which is a real situation, and we don't want
you know, three spans for one HTTP client making a request. That's sort of the use case for span suppression.
But really, that's just… That's just picking the… picking the top one and… and hiding the… the…
Sergey 00:36:02 When you say picking the top one, you will pick them, let's say they should belong to some kind of, like, same category, right?
Brett McBride 00:36:09 Yay.
Sergey 00:36:09 So in that sense, you can say that this is a particular case of that, but instead of HTTP, they are local root category, right? So if you have local root and you want to create local root, first you need to check if there is already local root, don't create it, just merge with it, right? Essentially.
Because curl, you want curl to create that HTTP span if there is no guzzle, but if there is guzzle, then curl should merge with it, or… not to create its own span. So, essentially, similar things. The question is, if that feature is, is,
you know, it will take longer, then I agree that it's easier to do this one by itself, and then,
Maybe merge it when that feature is.
Brett McBride 00:36:49 Yeah, look, and, and… think. I think that the difference between these two examples is that,
Creating an auto-root span doesn't have as rich
of, information available as, you know, Laravel
you know, like, we don't have… we don't have routing at that point. We don't know…
you know, we can't… we can't give it a good name, because we don't have that level of information, because we don't have routes. That's probably the main one, actually, is… is… is having routes. But, you know, there may be other metadata that we can get once we know that it is
a Laravel application that we don't know, you know, generically looking at, superglobals.
Sergey 00:37:41 Right, man. Yeah, yeah, I mean,
Yeah. Yeah, I agree, like, it's each case, but if you try to solve it generically, like, the question will always be, like, is it always the case that higher level has always more information than lower level, or the other way around? Like, in case of Laravel, it seems that Laravel will always have more information, so it probably should always merge its information
local span, but what about all this Gazel versus kernel? Maybe sometimes Gazel will have,
You know, top level will actually be.
Brett McBride 00:38:13 Ew.
Sergey 00:38:14 richer, have richer information than lower level. So, I guess if you want to make it generic, you will probably allow merging in both directions, right? The question is how each of them, if they're not aware of the second side, will be able to, you know, kind of, like, arbitrage it, like, who decides what should be merged with what. That's an interesting question.
But… Yeah, I agree with you.
Brett McBride 00:38:35 Even though we've been…
I don't know whether we've even considered that for… I mean, there's… there's sort of two span suppression strategy pull requests out there. My original one and Neve.
has a draft of another one, as I remember. But I don't… I don't think that either of them
Sort of tackle the use case of…
Sergey 00:39:00 What's the difference between…
Brett McBride 00:39:01 This is true.
Sergey 00:39:01 What's the difference between them?
Brett McBride 00:39:04 Oh, his is better.
I think… I think mine was probably a bit… well, I think it worked, but it required more…
Sort of more work to make it sort of more code, but for an instrumentation author.
Sergey 00:39:25 But the outcome in both cases is that lower level is completely discarded. There is no margin involved, right? So the top stays as it is, and lower… the lower level just being eliminated, and that's the…
That's the outcome. And you're saying in this case, we actually would want lower level to contribute to existing upper level, okay.
Brett McBride 00:39:45 Yeah, yeah, which is sort of… it's different APIs as well.
Sergey 00:39:50 Yeah, yeah, I mean, I agree with you that it all becomes a question of, will it be over-engineering to somehow combine these two things together, or is it okay to keep them separate? I can see benefits to both, like,
I agree that, use case is a little bit different, but although, again.
If you are into engineering, you can see similarities between them, but…
Brett McBride 00:40:12 Yeah, one thing I would point out, though, is that the spec disallows having
To, service bands within a…
You know, within one section of a trace.
So… so we definitely need to either discard or merge to… if we've got… or, well, I guess the… the APIs…
Sergey 00:40:35 I guess you will have to change those instrumentations that try to create, like, root span frameworks. They will not directly go and create a root span, they will use some alternative API to just query, kind of like, give me existing root span, or create a new one, and then they will kind of, like, work on top of it.
So, probably, but I don't know, I'm not that, maybe there is a…
better way to, you know, phrase it in API, you know, if it's a good idea to even add this special API.
So… Yeah, I guess.
Brett McBride 00:41:08 Yeah, yeah.
Sergey 00:41:08 So for me to see how this implementation anyway, maybe to get some inspiration from that.
But, in this case, I don't think at any point of time you do need, like, to spend existing, right? Like, because you can change the Laravel or other frameworks of simplification, they will just…
Brett McBride 00:41:26 Obtain the existing spawn and mutate it without creating a second one.
Yeah, yeah, and I think… I think we're right. I think we've got all of the APIs that we need to do that. The other key bit would be…
For the post hook to know… That there wasn't a…
span created from the pre-hook to shut down, because the way that auto-instrumentations tend to operate is pre-hook creates a hook, activates it, post-hook,
Sergey 00:41:58 Right. Gets the issue.
Brett McBride 00:42:00 Active span encloses it.
Sergey 00:42:01 So, for you to… for you to be completely sprint, you need to do some kind of, like, reference counting here. Like, are you the owner?
Brett McBride 00:42:09 Boy.
Sergey 00:42:10 only the user, but if you don't want to overcomplicate it, it's probably get… yeah, it probably would be easy to return some kind of flag that you don't need to close the spawn you obtain.
Brett McBride 00:42:19 Yeah, and we can… we can do that, I think, because… because Scope…
Also, it can act as storage, so you can actually pass things between a pre and a post hook.
Sergey 00:42:35 Which part can access storage? Sorry.
Brett McBride 00:42:38 Scope. Scope is the object that is, is returned when you activate.
context.
And it's the… the thing through which you detach… detach context, so… so I think all the… all the bits are in place that we could do that.
Sergey 00:42:59 Yeah, I saw that it's a really advanced system that you have those guys. What do you recommend to read, like, to understand this relationship between spawn, scope, context? Is that something that's worth reading the spec, or is it better to just look at the code and, because that's something I need to understand better?
Brett McBride 00:43:16 Most of it's…
Sergey 00:43:18 concepts.
Brett McBride 00:43:19 I think that the OpenTelemetry spec covers most of it.
There are some… there are some added complexities beam.
our context implementation that are strictly part of spec.
Such as… you know, the bit I just mentioned, you can use, Scope to store things.
Yeah, but I mean, it's… it's… it's fairly closely aligned to what Spec talks about.
Okay, nothing.
Sergey 00:43:51 Look at that.
Brett McBride 00:43:51 Yeah, and spec certainly talks about, you know, when you activate a span, you should get some kind of guard.
Or, you know, a guard. Guard is the right word. You know, through which you can then detach that context, and that's probably come from, sort of.
you know, Rust, or Go or something.
Sergey 00:44:10 Guard in the sense that if you live in those languages that track scope, then they will automatically destroy that guard, and then they will close the spano. Yeah.
Brett McBride 00:44:21 Yep, that's… that's the pattern. Yeah, so we don't have that exactly. We do actually have to call detach.
Sergey 00:44:28 On it, because it doesn't… So, BHP, you have destructors, but they're not reliable.
Brett McBride 00:44:33 Dude, that's…
Sergey 00:44:34 Play with that.
Brett McBride 00:44:35 Yeah.
Sergey 00:44:36 It depends on the optimization level, I think. I tried to play for testing when I wanted to kind of, like, automatically add the context, like, have this kind of, like, debugging facility when, in each context, you can add some… some kind of, like, variables or whatever you want to track, and then kind of, like, pop the frame automatically when this context goes out, like, when functional, so…
But it's not reliable, it's, sometimes it calls instructors, sometimes it doesn't. I guess it depends on optimization levels, or maybe on how the GT and the code.
Brett McBride 00:45:05 So yeah, you cannot rely on the fact that destructor will be called.
Interesting. Okay, I wonder if that's why we have a detach method.
Sergey 00:45:17 You mean, like, in general, in spec?
Brett McBride 00:45:19 True.
No, well, no, in PHP's implementation.
Sergey 00:45:24 What do you mean, wonder? You already inherited it? You were not the one that implemented it?
Brett McBride 00:45:29 No, no, no, no, it was like that when I got here.
Sergey 00:45:35 Oh, that is.
Brett McBride 00:45:36 it's barely changed, you know, in my… I know that Neveh has worked on it quite a bit, but I think a lot of it was in place even before he
Before he was… was contributing.
Sergey 00:45:49 I see. Well, what I can say is that in 7, it was more reliable, like, this facility of working with, with frames, I could rely on this active being called, but I guess they probably implemented maybe much more optimizations in version 8, and it became much less reliable.
It's…
So, you cannot learn distractor VIN call.
Yeah, so…
So, yeah, definitely, for languages that, you know, are garbage collected, you… you have to have ability to do it manually. Most cases, you will do it manually.
If you want it to be 100% reliable.
Brett McBride 00:46:26 Yep, I might just document this discussion in the… in the minutes, because it's been interesting, and I do feel it's something we, we should probably look at for auto-instrumentations, because it…
I think I prefer the pattern where, you know, a root span is reliably started for you.
And then you're just adding extra information to it as it… if and when it becomes available.
And petite…
Sergey 00:46:58 The only concern I would have is, what do you do about this Octane thing, right? About all these frameworks that essentially have multiple logical root spans during the same request, like, let's call it physical PHP lifecycle root span, right? So you don't want to connect those, because that initial root span that you had for
For we need Archer down, that's completely meaningless in the context of, like, React, PHP, Octane, or whatever, that runs multiple logical requests in the same context. They might even run multiple requests at the same time, technically, right? They might have multiple requests in flight.
At the same time, so… Completely unrelated to each other.
So…
Brett McBride 00:47:40 fruit.
Sergey 00:47:41 So that's something to consider. Again, if API is kind of, like, hides this, you can obviously… but, I mean, you cannot always rely that it exists, because, I mean, unless you implement it as part of this instrumentation of Octane or React PHP,
But technically, it will be then implemented in instrumentation, not by SDK, right?
Because instrumentation needs to understand what is the entry point, when does the processing of logical request start and end, right? And at that point, you will create… but then it will coincide. You will essentially coincide both the
Creation of the span for the framework and the local root span, because this is knowledge that is specific to this framework.
Brett McBride 00:48:24 Yeah, and so perhaps we have an Octane-specific,
auto-instrumentation that does something like auto-root span, you know, I'm just…
Sergey 00:48:34 But what I'm saying is that relying on the fact that you.
Brett McBride 00:48:37 Always great.
Sergey 00:48:37 in SDK, and then instrumentation can rely on it, it can be a little bit shaky in that case.
Brett McBride 00:48:43 Yeah.
Sergey 00:48:43 You need the instrumentation knowledge.
Yeah.
Brett McBride 00:48:47 That's true. And so maybe, I mean, you sort of hinted before it, you know, maybe we have a different API for, you know, like it's called, maybe create, root span.
which, you know, here's all the information that I want to apply, and it's kind of… yeah, it does feel a bit like merging, and it's… and it kind of does a… if there's already a local root span, take these parts and apply it. If there's not, then just start a whole new…
Sergey 00:49:14 Yeah, although in this case, it's even more complex. So, to tell you the truth, if we want, like, to be 100% sure on this API that it covers, it's probably better to run those two use cases, like Laravel in the case of regular PHP FPM,
and Laravel Octane, and to see… like, I mean, I definitely would not say that this APHI… this API, something that definitely works if you didn't try it in this context of React, PHP, or Octane, maybe both, just to make sure that they cover both, because,
Like, it's not even about merging in the case of Octane, right? Because you're not supposed to merge anything with one that was created by Aranitar Shadoun, because that's completely irrelevant. That's just long-running request that just encompasses
all the CLI running process, right, that inside of it runs multiple logical requests. So you need to create root span for that logical request only, not to try to merge it with the one that you created for Aranith Archa down, right? That one is not even interesting, you're not supposed to even send it out.
Because.
Brett McBride 00:50:16 That's weird.
Sergey 00:50:16 Maybe, you know, it might be an hour-long spend that is… Just shows how
This process lived, and stuff like that.
Brett McBride 00:50:24 Yep, so I've tackled that in my Rust implementation by just having it, like, an INI setting for, you know, if you're running Octane or Roadrunner or something, then don't start an auto route span. Like, you have to…
you know, you have to start it in some other way, because rinit and rhutdown aren't reliable in those long-running processes, or they don't represent a
An actual user request being processed.
Sergey 00:50:52 Yeah, yeah, I mean, yes, it's a simpler approach, I agree with you that initially, it might… it may be just… will require manually from user to configure, that if they know that they're using something that makes this RNA tarsha down spawn obsolete, not interesting, then don't create it.
But then, yes, then I agree with you that this API that will automatically detect if it exists, then…
But if you want it to be completely automatic, not even requiring a user to manually configure what kind of, you know, PHP runtime they are using.
Then, if you detect it, then you can essentially… because you do detect it, right? You have instrumentation of octane.
Brett McBride 00:51:28 You know, what you can detect is you look up the server API. That's how I did it in Rust. I didn't… I didn't…
I misled it before, so… so I think that the check is literally, if the server API is CLI,
Don't start an auto route span.
Sergey 00:51:46 In some cases, you do want to start it. Like, if it's a regular CLI, like Laravel Artisan? What is that? Like, if you just run some command, and you do want to monitor it, then if it's just a classic CLI, not a long-running, like, Octane thing that serves requests.
But just, yeah. We do monitor CLI as well, right? With the regular, like…
Not just the…
Brett McBride 00:52:11 Everybody.
Sergey 00:52:12 Questrant.
So yes, so let's say if you… if you're running Laravel Artisan, then you do want to create that root span, right? So it's kind of like,
I guess you will need this kind of, like, instrumentation from Octane to tell you that, okay, the Octane is detected, then don't… or at least don't send it out, like, even if you create it, it doesn't matter, but it's probably…
like you said, if you don't want… if you want to avoid the situation that you have a multiple service… by the way, regarding multiple service spans, I'm not sure how you can avoid it in this context of Octane, because if I understand correctly, in Octane, you can have multiple requests at the same time going on, or maybe I'm understanding it wrong.
Maybe, maybe in Octane it's not that complicated. Maybe in Octane it's impossible. Yeah, probably not, because that would be impossible to program from PHP point of view, because you don't have ability… it's not like threads that you can localize this request some context. So I guess, in React PHP, it's definitely possible, right? Because it's all up to you, you can…
You can accept those requests, and if you keep all the context in your objects, then you can have multiple requests. It's like Node.js, right? PHP is like Node.js.
completely all in user context, and you decide how you interleave those requests, and if you have a completely asynchronous I.O,
Right? If all your requests are asynchronous, then, yeah, you can have multiple requests at the same time going on, right? You will just react to the callbacks when the I.O. is complete, you will fetch back the context in which it was made, and you will proceed with the
with the processing of that request. So, yeah, so it's,
And I guess fibers will bring you to the same situation.
Brett McBride 00:53:52 Card.
Sergey 00:53:53 Oh, yeah.
Brett McBride 00:53:54 Yep, and I was just about to mention fibre, so when you're next reading the… our context implementation, you'll see that some other non-standard things in context are, like, fork.
forking context, and there's a couple of other methods, and… and we use FFI to hook into when context forks and, sorry, when
Fibers, fork and…
do whatever they do. And our context is able to sort of follow. You can have multiple contexts on the go for your different.
Sergey 00:54:35 And this is something that you think doesn't exist in the spec itself, ability to kind of, like, have multiple…
Brett McBride 00:54:43 Look, it… It's probably implied in the spec, but our implementation is, respect.
Sergey 00:54:52 Similar thing.
Brett McBride 00:54:53 Make sure we'll go down to that level of detail.
Sergey 00:54:56 Right, it's interesting, because in Java, for example, they now introduced the concept of fibers. They have these lightweight threads that… it is essentially the same thing as PHP fibers. It's different, like, for example.
like, from coroutines, like in C++, where you don't have any stack. That's, like, stackful, things that they simplify for a programmer, obviously, but…
I think in .NET, there's stackless, they don't have the state, but but the same concept will still apply. You still need the ability to forward the context, and kind of, like, say, okay, this happens in the context of this request, and it's kind of, like, at the same time.
Yeah, we'll have to read it to get up to date, but, yeah. So, I think before we go, like, that would be an interesting project to take, definitely would be glad to cooperate in that.
But I think to become, like, it's better to try it out on, like, at the same time on… on couple, like, use cases, like regular AOL, Octane, and maybe React PHP, to be sure that you're covering all these bases,
To make sure that the API is suitable for all these use cases, yeah.
Chris Lightfoot-Wild 00:56:04 I did have one other question, or thought on that. Like, are you… I thought we couldn't change certain things on the spam, what's the set, or have a bad.
Brett McBride 00:56:12 There are… yeah, you're right, there are limited things you can change, but you can update the name, you can add attributes.
Chris Lightfoot-Wild 00:56:19 Can you remove attributes as well then, if that's the case?
Brett McBride 00:56:24 Sorry?
Chris Lightfoot-Wild 00:56:25 You can modify attributes, or you can only add… it's only additive.
Brett McBride 00:56:28 That's a good question.
Sergey 00:56:31 But you cannot change the name. Name is… should be cra… should be.
Brett McBride 00:56:34 No, no, you can change the name. You can definitely update the name.
Sergey 00:56:37 Okay, so you can update, like, you can use Route as a name after you discover it.
Brett McBride 00:56:43 Yes, and we actually do that anyway in a lot of instrumentations, because… because routing often happens after, you know, the application first bootstrap.
Sergey 00:56:54 Wasted ruins.
Brett McBride 00:56:56 Yes, so updating a name, definitely, adding events, adding attributes.
Yeah, I think that the spec encourages you to add all attributes possible as soon as possible, so that they can be used to make sampling decisions, but
You can certainly add them after the fact as well, after it's been started.
Chris Lightfoot-Wild 00:57:23 Maybe if you had the same pre-existing attribute, it presumably it just overwrites rather than rejects.
I don't know.
Brett McBride 00:57:30 Yeah, it wouldn't reject.
Chris Lightfoot-Wild 00:57:32 Null ify that out to essentially drop that attribute if you wanted.
Brett McBride 00:57:39 Don't know if you can drop an attribute. Maybe.
Haven't tried.
Sergey 00:57:46 But, like, doing it like that, discovering it later, if you want features, like, for example, when you can say, okay, drop all the… all the traces with this, for example, entry point, right? That would make it a little bit more challenging.
But, I guess…
Brett McBride 00:58:03 You'd have to do that. You can do that, tail-based sampling in the collector. We wouldn't… Yeah, I don't think we should try to do that in our SDK.
Sergey 00:58:17 Okay, okay, maybe. Yeah, maybe it's better to be…
defer to other stages, yeah. Okay. Okay, yeah, definitely, definitely interesting stuff.
Chris Lightfoot-Wild 00:58:33 I've asked a lot of questions as well that I've always, pondered, Sergey, so thanks for that. Scope and context, I've still not fully got my head around.
Brett McBride 00:58:41 No, it's…
Chris Lightfoot-Wild 00:58:44 I can imagine the span now, because I've seen it in, like, a JSON format, but the things that seem like a… yeah, I'm not quite there.
It'll be interesting to hear what your take is on it.
So… Even if.
Brett McBride 00:58:58 Yeah.
I mean, I kind of think of context… oh, and there's context storage as well, there's a whole other…
There's a whole other bit for you to investigate next time you're bored, Sergei. And that's… I think that's…
that's an abstraction to help us deal with… with fibres, and I think that's how the… that's how the sort of switching and forking
It works, but… Yes, it's very, very.
Sergey 00:59:26 For example, I'll give you an example of when I tried to… why… I think I need to beef up my knowledge on this. Like, for example, when we implemented this inferred spans feature, so this inferred spans means that we create spans based on the stack traces that we take periodically, right?
So, we essentially create spans out of the scene error just by profiler taking periodic snapshots and seeing, okay, if this stack frame is still… if this function is called… is still on the… on the stack trace, then we will create a span from it, right? The first time we saw it and the last time. So, essentially, we create kind of this inferred spans, they call.
So, when I try to, during testing, to add some information to this response that will help me, essentially we have this test that we call component tests, right? We have a separate process running that runs the application code with the instrumentation, and then we send this information back to the process with PHP unit that will
run all the asserts, right? And check the information derived from the collector, or to collector from SDK, and versus what was supposed to happen. And what I tried to do is that I wanted to attach some information as a kind of, like, custom attribute to the spawns.
So I can verify that… let's say, for example, timing, right? I know when function started, when function ended, so obviously this inferred sponge can only be inside of that time frame, right? It cannot go outside of that time frame.
But it's… I tried to add this information, so I tried to find those spans, like, to get current span, so I thought I will add this, all this information, for example, to root span, right? So I can easily find it, because I couldn't just attach it to the any span, to the current span, because our inferred span implementation, it can possibly drop spuns. It tries to kind of, like, merge them.
And essentially, it drops some of them when it merges them.
So…
That was a problem. If I attach to the wrong spawn, it can be dropped. I will not see it in my PHP unit context. So I tried to walk the context,
kind of, like, chain to find the root spawn and attach all this payload to it, so, because I always knew that it will be sent out, and I could not do it. Like, I tried to play with API, and I didn't find any convenient way to go up the chain of these contexts and find the root context.
Brett McBride 01:01:38 I also have tried to do that, and I couldn't do it either, because.
Sergey 01:01:42 Not really, it's not that simple.
Brett McBride 01:01:45 No.
Sergey 01:01:45 That's why I wanted to…
Brett McBride 01:01:46 that API that you had for the local root span. And that's why… that's why I eventually did local root span.
Sergey 01:01:54 I don't know if it… do you think it's a good sign that such a simple… maybe it's good, because then it means that you should not assume too much about the structure of those contexts.
But I would assume it should not be that hard to walk this, essentially, tree and get to the root of the tree, right? Why… why API doesn't allow that? I don't know if maybe it's not a popular use case, doesn't everybody care about it?
Brett McBride 01:02:15 I don't think it is, and the only reason you'd want it do it is…
well, the only reason I could come up with anyway was to get to the root span, and we can do that more simply.
Despite, well, the implementation that we have, but… but yes, I… I also…
naively thought it would be… it can't be that hard to just traverse back up the storage. I guess maybe they don't want to allow that, because it's possible that you have these spans existing in different processes, right?
Sergey 01:02:45 So just the fact that you have error. They didn't want to… because obviously, if you allow this an API, then you can encounter use cases that will be… in which it will be hard to support it, so they want to minimize the API, right?
Brett McBride 01:02:59 I think so, and I think it's to discourage abuse as well,
You know, this is the same reason that you're not meant to be able to read
information back out of spans, so that people don't abuse it to, you know, store business data. You know, I know that this span's going to be available when this function next runs, I'll just use this as… abuse it as storage.
Sergey 01:03:24 That's interesting, yeah. I thought you will say that you should not do it, because in case it's sampled out, you will essentially get some kind.
Brett McBride 01:03:31 I, like, died.
Sergey 01:03:31 that doesn't hold any of this information, so you cannot reliably even do it.
But, hmm, okay. Yeah, interesting. Although, wouldn't you say that this, SQL commentator thing, it kind of, like, gets into that area a little bit? Kind of, like, mixing business stuff with, you know, monitoring itself?
Kind of, like, a little bit,
Maybe I need to read about it, maybe I'm mistaken here.
Brett McBride 01:03:55 No, I mean, it's… it is kind of, you know, distributed context.
propagation.
Sergey 01:04:05 Okay, so you're just riding on this feature of database.
Brett McBride 01:04:07 Yeah, it just… it just… it's just… they just use comments as… as the mechanism where… where we use, you know, HTTP headers, because databases don't have.
Sergey 01:04:19 Have that concept.
Brett McBride 01:04:21 At least not… not universally.
I don't know, I wasn't… I was… I wasn't… I'm not…
I'm not thrilled by the implementation that they have now, because they've…
I don't know. I just… I don't think that they're thinking big enough that, you know, we're…
you know, OpenTelemetry should probably be imagining a future where databases do support,
you know, sending this extra metadata, and you can generate open telemetry out of a database and have distributed traces, you know, cross in…
Sergey 01:04:55 Does it preclude from that? Like, the current implementation Just the fact… I mean.
You mean it doesn't attach it in a way that it can be automated, this whole thing? Like, let's say eventually you do have some component that can… that knows how to monitor database, and it can produce some information out to database that you can then match these comments from those two sites, from client side.
Would it be possible with current interpretation, or…
Bona.
Brett McBride 01:05:23 I mean, I suppose if…
If, if an in-database instrumentation could read and parse those comments, then yes.
But I just feel that there could be a better transport.
Chris Lightfoot-Wild 01:05:37 It doesn't really work with, like, prepared statements either, does it? If you, like, prepare an insert.
Brett McBride 01:05:41 No, it's a.
Chris Lightfoot-Wild 01:05:42 will there.
Brett McBride 01:05:43 That's another gotcha, yeah, it destroys prepared statements. Yes, yes, you're right, it doesn't, it doesn't work with prepared statements. Yeah, which is, yeah, another problem, and another reason why
you know, I think it's a… It's a… Not a very good.
Sergey 01:06:02 Bent away.
Chris Lightfoot-Wild 01:06:02 Shoehorned in.
Sergey 01:06:04 So maybe the better way would have been to get some ID when the response is returned from database, and you can store this ID in the span, and then it can be matched against database side. Maybe that would have been a better way than try to
To, to force this, this direction.
Brett McBride 01:06:23 Yeah.
Yeah, I mean, look, I suppose the history of it from reading
tickets anyways, that there was already a Google product that did this, and they didn't want to support it anymore, so they donated it. But we've…
But we've just taken it and used it as is without
Without thinking about how to improve it and make it more… OpenTelemetry.
Sergey 01:06:52 So it will only work if you're building a query textually, like, it will not work with prepared statements.
Brett McBride 01:07:00 I don't think it works with ProPets.
Chris Lightfoot-Wild 01:07:03 It has to come to the end of the statement, isn't it? So, with the prepared one, I'm sure it's, like, only once it's set, and then…
Every time you…
Sergey 01:07:12 That's strange, you can provide parameters, bind parameters to prepare statements, so a comment cannot be binded to a particular execution of the statement.
Brett McBride 01:07:22 I think you can find a comment, no. No.
Sergey 01:07:27 Okay. And then the usability with… because if I understand correctly, from security point of view, you should always use prepared statements, you should not try to construct queries textually, right?
Brett McBride 01:07:36 Hmm.
Although, I suppose if we just used a trace ID and not a span ID, then you at least… like, that's stable for…
That stable provided the sh… Prepared statement is only used within the context of one user request.
Because otherwise, the… The… the bind, and the… therefore the…
Sort of the propagated context is only relevant for…
Whichever trace happened to be running when the statement was prepared.
Sergey 01:08:15 Right, yeah, but how are you gonna pass it to database? Sorry, Chris?
Chris Lightfoot-Wild 01:08:20 No, just saying that you talk about the Octane thing and the local route span, but, like, almost subrequests, if you were doing that with a database connection where you'd prepared a statement first, and it was, like, spanning multiple, kind of, requests, it would all cock up as well, wouldn't it?
Brett McBride 01:08:37 Yeah, it would.
And so that… that's… that's… yeah, that… it's just not…
Sergey 01:08:42 Is that… is that a… is that a good practice in Foctane, kind of like, models like that, that can survive end of the request? People keep data, like, prepare statements, they… they cache them, and they keep them between requests?
Chris Lightfoot-Wild 01:08:56 With Octane, it's to try and get, to prevent Laravel booting from cold every time, isn't it? So it keeps, like, different connections and things open. And, like, that's what the… in the service provider, you can, like, scope something in a container.
Where it gets reset between requests, or you can have a singleton where it's, like, you know, long-running.
Until the application dies.
Sergey 01:09:19 So it just seems like there's a lot of gotchas.
Chris Lightfoot-Wild 01:09:21 But, you know, as long as, I guess, it's advertised on the tin.
That, you know, there's danger to using it.
Brett McBride 01:09:30 Yeah, or just that it could be misleading, but…
I don't even know what you do with the…
you know, once you've got these, these comments in your SQL query, you know, I don't know if there's… there's other tooling that can then
generate… Data out of your database logs.
to tell you about statements and link them back to OpenTelemetry. I don't know how any of that.
Chris Lightfoot-Wild 01:09:56 I'd seen something possibly that was suggesting that it might be useful for a database admin that's, you know, got a slow query log, and goes, hey, this query is slow, but you've got this comment on the end of it that might.
Brett McBride 01:10:07 Thank you.
Chris Lightfoot-Wild 01:10:07 The programmer some further context to unlock some more…
Brett McBride 01:10:11 True.
Sergey 01:10:12 We think they will do it manually, they go to the slog, fetch the IDs, or they need to write some ad hoc thing that will
Official.
Chris Lightfoot-Wild 01:10:19 Part of the suggestion that I'd read, rather than it just being part of, like, first-party support in the database engine, which would be the best way, wouldn't it? If there was… when you're preparing the statement, there's some, like, meta layer to that, you see, and with tracing, and yeah. Better yet, at the execute.
Yeah, yeah, absolutely.
Brett McBride 01:10:37 Gus prepares Yeah, simple comments are not… not… not the right way, in my opinion.
It's just, yeah.
Sergey 01:10:48 Okay.
Well, good discussions. Well, what time is it for you, Brad?
Brett McBride 01:10:53 It is 10 minutes past 11pm, bedtime. Bedtime is what it is.
Sergey 01:10:59 That's not as bad as I thought. Apologies.
Brett McBride 01:11:01 No, I'm not joking.
Chris Lightfoot-Wild 01:11:03 So you're taking vacations, so you will be on this, or you're just switching jobs, or…
Brett McBride 01:11:10 No, I'm not switching jobs, I'm, I'm parenting.
Sergey 01:11:14 So okay, so you're reducing your presence at topical entry for your children.
Gotta switch.
Brett McBride 01:11:20 Yes, yes, that's right. So, look, I'll still be around. I'll show up to SIGS and, you know, merge pull requests, but, well, we'll see how bored I get. Maybe I'll be around a lot.
Sergey 01:11:32 No, it's good, I mean, I guess,
Definitely, we'll see how we'll pick it up, you know.
Yeah, we cannot rely on you, Carrie, to enjoy life as well.
Definitely will try to not disappoint you.
Brett McBride 01:11:46 Excellent. I'll be keeping an eye on you anyway.
Sergey 01:11:50 Good, good. Okay, so when do you plan… when does it start?
Brett McBride 01:11:54 Oh, sorry.
Sergey 01:11:55 of your life?
Brett McBride 01:11:56 Three… you know, we've got 3 weeks.
Sergey 01:11:58 Is that right?
Brett McBride 01:11:59 starting my… I guess I'll call this… Yeah.
Chris Lightfoot-Wild 01:12:04 Is it worth pointing on the next agenda to cover anything like that, obviously, just to highlight,
you know, if… if anyone else comes up in your absence, maybe Bob, Bob doing more releases or something, just to plan in for that.
Brett McBride 01:12:18 Yeah, yeah, I mean, releases aren't hard, they're, you know, I've got all the tooling set up, so all those things are pretty…
Sergey 01:12:25 Do you think it might be useful for you to write down, like, what responsibilities you would like other people to pick up, and try for us to see how we divided them?
Brett McBride 01:12:34 Yeah, it might be. Yeah, that's probably a good…
Sergey 01:12:38 Because you do stuff periodically, maybe it's not always, just so we don't, you know, miss it, and not understand why something doesn't happen that happened before by itself, seemingly, right?
By itself.
Brett McBride 01:12:49 Yeah. Look, mostly… most of the magic is just doing releases, and…
Sergey 01:12:55 Hmm.
Brett McBride 01:12:55 And, probably the most involved bit is when a new contribute module drops. And it's not that many extra steps, but… but, you know, you have to create
create a repository in… in GitHub, and create an entry in Packages so that it can be downloaded, and yeah. Like, it's not too onerous, but,
Sergey 01:13:19 So maybe you can just list those, responsibilities, then we can divide, maybe we will sit down, each of those people that we'll pick up, we'll sit down with you, those steps that are not documented, we can document them, and have them kind of, like, already documented, and then whoever does it.
Brett McBride 01:13:34 Yeah.
Sergey 01:13:35 We'll be able to just follow the steps.
Brett McBride 01:13:37 Yeah, look, I feel like they are documented, but it would be great to have someone test that documentation.
And… and see if it works, because I… I…
Yes, I have a terrible memory, so I do write things down and follow my own instructions, which is good.
So, I think they work, but… but yes, it would be good if,
Look, it'd probably have to be Bulb.
Otherwise, Chris, maybe you're up for a promotion, to a maintainer for extra privileges.
Chris Lightfoot-Wild 01:14:14 Well, maybe we can discuss it, further and see what officers.
Sergey 01:14:17 Yeah, definitely.
Chris Lightfoot-Wild 01:14:17 Yeah, let's.
Sergey 01:14:17 Let's discuss it at the next meeting.
Definitely need to pick up the slug, yeah.
Brett McBride 01:14:22 Yeah.
Chris Lightfoot-Wild 01:14:22 Moved again.
Brett McBride 01:14:23 Yeah, yeah, yeah.
Sergey 01:14:23 Right, yeah.
Brett McBride 01:14:24 Yep. But also, if… if… if…
you know, disaster happens, I'm really not very far away.
Sergey 01:14:33 Well, you're literally fireware, but I'm just gay.
Brett McBride 01:14:36 Yeah, yeah, yeah. I'm not far away from this computer.
And I don't want my skills to atrophy.
I'm away, so… I'll still pop up.
Sergey 01:14:46 Brian, yeah.
Don't worry, we will probably supply enough stuff for you not to atrophia, that's… Good. Alright.
Brett McBride 01:14:54 Well, let's call it. I'll just update the, update the minutes, just with a bit of what we just talked about with… particularly around route spans, and…
And possibly how we can do that better.
For things like Octane and… Yeah. Otherwise, I will see you next week.
Chris Lightfoot-Wild 01:15:15 See you later. Thank you, guys.
Brett McBride 01:15:16 Excuse me.
Chris, thanks, Igmy. Bye.
Sergey 01:15:20 Bye.
