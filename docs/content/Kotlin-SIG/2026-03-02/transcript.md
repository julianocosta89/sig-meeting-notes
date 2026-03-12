SIG: Kotlin SIG
Date: 2026-03-02
Duration: 37 minutes
Zoom Recording URL: https://zoom.us/rec/share/9VlmPR7Hb7x994uE1UXaeho06dSD7h2uzj1L_psgSat3YtbTvzXtWB3WvVuAadYK.ys1Q1sQX00726YeQ
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:01 It is such a pain in the ass to manually copy over meeting information into this Outlook calendar that we have.
**Jamie Lynch** 01:09 Oh, really.
**Jason Plumb** 01:10 Yeah.
Like, I mean, I don't know when the last time you used Outlook was, but, It's not… it's not good.
**Jamie Lynch** 01:18 Yeah.
Probably at least a decade ago.
It's… fairly straightforward in Google Calendar, but then the invite changed, so the information's slightly out of date, so that's a pain as well.
**Jason Plumb** 01:32 I think I've got mine, and it's multiple clicks, like, I have to actually open… I can't just, like, you know, preview and, like, open the Zoom link. Like, you have to open the thing, and then… it's like… They make it really a hassle. And also, there's, like, some city truck, like, giant truck outside my house, so… I don't know what they're doing out there.
**Hanson** 01:54 Yes.
**Jamie Lynch** 01:55 Well, I guess I want to push you towards Teams instead of Zoom.
**Hanson** 02:01 keep on adding bits of friction so that you submit. You're like, fine, fine, fine!
**Jason Plumb** 02:09 Oh, it's worse than that, like, people that use it for long enough come full circle, and they're like, oh no, it's actually way better than Zoom, you know, it's like that kind of thing.
Slack, oh, I hate using Slack. You're like, really?
Okay… Well, here we are.
**Jamie Lynch** 02:30 Has everyone got the dock link?
**Jason Plumb** 02:34 Yeah…
**Hanson** 02:37 opening now.
**Jamie Lynch** 02:39 So, I'll just give it a couple of minutes for folks to add.
Yeah, any agenda items, and for anyone else to come along.
**Hanson** 02:51 Still catching up.
I went on vacation sick, I came back sick.
**Jason Plumb** 03:03 Fun.
**Hanson** 03:04 I mean, coughing in Mexico and in the sun is much better than coughing here, so, you know… What can I say?
**Jason Plumb** 03:18 Yeah, at the end of the day, you're still in Mexico, right? So…
**Hanson** 03:21 Yep.
**Jamie Lynch** 03:29 Cool, we could just stop talking through items, and if other points come up, we can add them on as we're going.
That's phenomenal.
**Jason Plumb** 03:39 That sounds good.
**Jamie Lynch** 03:41 Cool. So… First item, so we have a calendar invite now.
with the Zoom link, the Google Doc.
So, that's super helpful.
I think there's just… I think there's also, like, a table on the community repo containing information.
about those calendar invites, and that's not visible yet. So I think that's relying on this PR.
So… I think there was, like, one failing CI check, and a couple of review comments.
**Jason Plumb** 04:27 And I tried bumping it last week just to get some attention there, and didn't get any traction.
**Jamie Lynch** 04:37 So I guess we could… Wait, a day or two… I guess… Would it be possible to, like, push to this PR, or could we create a separate PR to basically do the same, or show a bit of a commit?
**Jason Plumb** 04:55 You mean to be able to commit to this repo?
**Jamie Lynch** 04:58 Yeah.
**Jason Plumb** 05:00 I don't know who the maintainer's on. I don't think any of us three have the ability to commit to that, do we? I don't think so.
**Carlos Alberto Cortez** 05:07 We open some trash.
**Jason Plumb** 05:10 Sorry?
**Carlos Alberto Cortez** 05:11 Is that… I mean, you want to merge this PR?
**Jason Plumb** 05:14 Yeah.
**Carlos Alberto Cortez** 05:15 No, I don't think you have permission for that. I'm probably.
**Jason Plumb** 05:18 You do.
**Carlos Alberto Cortez** 05:18 permission, either. I don't think.
**Jason Plumb** 05:20 No.
**Carlos Alberto Cortez** 05:20 Because, no, I think that the permissions were restricted, because people were afraid that any TC or UC member could call and Press merge on anything, and it's true.
**Jason Plumb** 05:30 Yeah. So, it looks like… it looks like GCTC. If you look at the code owner's file in the root, yeah, it's like…
**Hanson** 05:38 I will double-check again.
**Jason Plumb** 05:40 Austin, yeah.
**Hanson** 05:45 Are there anything else in this repo we want to change, like, as we're waiting for this? Because it seems like this is going to take a while to, like, go through, like, because I don't want to do this, and then a week later, oh yeah, there's something else we need to do, and we'll wait another 3 weeks. Have we gone through the repo and say, hey, is there anything else we need to add?
**Carlos Alberto Cortez** 06:06 Well, I would argue that this is the important part. Any other thing could be probably just additional. Well, yeah, of course, Jamie or anybody else can go and double-check.
**Jamie Lynch** 06:18 Yeah, I think this is the main… Imports in part.
**Hanson** 06:24 Just linking to everything.
**Jamie Lynch** 06:27 But, yeah, I can add a note for myself to go and double-check, if there's anything else that needs changing.
**Carlos Alberto Cortez** 06:34 Yeah, now that you, you mentioned that, there's, I don't know whether it still exists, but we were, in the past, having greetings down somewhere where the maintainers in each repo.
I don't know if we still do that for now, it's repo-independent, you know? Repo-dependent.
**Jason Plumb** 06:54 I don't think it's not centralized, is it?
**Carlos Alberto Cortez** 06:57 I don't think, yeah, hopefully it's not anymore, but it used to be. That would be the only thing I can imagine, besides this.
But hopefully it's not anymore.
Centralized, I mean.
**Jamie Lynch** 07:08 Hmm.
Okay, I guess I'll just wait a couple of days on that, and then…
**Hanson** 07:20 Good evening, folks.
**Carlos Alberto Cortez** 07:22 What?
**Jamie Lynch** 07:23 So…
**Carlos Alberto Cortez** 07:24 I will, I will poke people, and DTC, probably, in case, you know. I will double-check, maybe I have permissions myself.
**Jason Plumb** 07:31 Yeah. I just… I just referenced Alolita in the Kotlin channel, just as a direct, like, hey, come back, please.
**Carlos Alberto Cortez** 07:41 Yeah.
**Jason Plumb** 07:41 But I know people are busy, I get it.
**Carlos Alberto Cortez** 07:45 Yeah.
**Jamie Lynch** 07:49 Cool.
Yeah, next item… just, kind of an FYI to everyone, but there's a blog post for OpenTelemetry I.O, Just basically reannouncing the project now that it's been donated. So, yeah, feel free to have a read around it. I think… we're aiming to get that merged around, like, March 23rd, because I think there's also some marketing that CNCF and Embrace are doing at the same time.
**Jason Plumb** 08:30 Nice. That's awesome.
**Hanson** 08:32 We'll look today…
**Jason Plumb** 08:34 Yeah, I haven't seen it yet, so… Cool.
**Jamie Lynch** 08:43 Yeah, I guess we can move on to the next one.
Yeah, so I'm continuing to work on like, making the API compliant with the spec, so there's a few PRs out around that.
So, if anyone had, like, questions around that, or… Yeah, any, like, concerns? I guess we could cover that now.
The thing I wanted to ask was whether it's worth putting something in my spec compliance matrix.
Now, just so that there's, like, something there, and we can kind of reference it.
**Hanson** 09:22 I think so. I mean, if we have everything locked up, and it's… we have releases, we have… we're listed on the main page, we should be, adjudicated on our compliance. So, I feel like if it's not there, it should be there.
**Jason Plumb** 09:39 Yeah, I think this is a good idea.
It's early, but it's good to be early, I think.
It's good to be able to point at it and say, here's all the stuff we want to work on and get compliant.
**Carlos Alberto Cortez** 09:53 Just to be clear, this is, like, totally empty, just adding blank spaces, right?
**Jamie Lynch** 10:00 So… I'll show you this one. So, it's basically just been on my assessment.
of… what is obviously there. So, like, there's obviously a tracer provider, you can obviously get a tracer, We could leave it totally empty.
**Jason Plumb** 10:21 No, I think, I think what Carlos is asking, if you scroll to the bottom, it'll have the markdown file, and then if you do view file on it… I do a view file on this. Not download the diff, oh no!
And then, I think this is what Carlos was asking, if you scroll to the right, there's… it's not all blank, you know, there's some stuff in here.
**Hanson** 10:43 I mean, if… procedurally, we want to start with all blank, and then have a second commit right at… or a second PR right after, with what we consider to be the current state, then we unblock that first one, and the second one, we could, you know, talk a bit more about it, and then merge it.
That would be fine if that's preferable.
**Carlos Alberto Cortez** 11:05 That's kind of what we had in the past with previous PR that Jimmy had prepared, So, I was mentioning to Jamie that, for some reason, when I was trying to ask questions on those old PRs.
My comments were appearing as pending to be approved.
And legitimacy guy.
**Jason Plumb** 11:24 comments were.
**Carlos Alberto Cortez** 11:26 Yeah, like, for example.
**Jason Plumb** 11:27 Weird.
**Carlos Alberto Cortez** 11:27 regarding active span, yeah, active span, and I was asking, like, hey, I don't think it's exactly that.
Like, can you point me to that code piece? And then it says, like, waiting, you know?
**Jason Plumb** 11:40 In which repo? In this repo? In the spec repo?
**Carlos Alberto Cortez** 11:43 In this big repo, yes, for the PR that Jamie had. Yeah, it was weird, and Jamie couldn't see them. Usually, you know, like… Yeah, well, I could totally see that, yeah. And that happened only once with another person.
And we… but, yeah, in the end, we just created a different PR. I don't know if it's bulk or some specific situation, but anyway, It's up to you. I still have some questions around, context propagation here, so… I guess that my only request could be, like, base… basic stuff that we have seen that works just fine, let's add that. Like, no, create a tracer, create a logger, stuff like that. But parts regarding context propagation, it would be nice if you could leave them out, since I still have some questions regarding that one.
**Jamie Lynch** 12:38 Okay.
Cool, so I guess the conservative way of doing this would just be to create an empty column, and then we can fill out the really obvious stuff that is definitely implemented.
And then… kind of, like, create small PRs for… Well, like…
**Carlos Alberto Cortez** 12:59 I would say that for speed, probably makes sense that you keep this PR just stopped around context propagation, just mark it as Not unimplemented, or who knows?
So we can go ahead and merge this one. I think you, you can… you have in your mind very clear what things are clearly implemented, so just keep them.
And then we can iterate on the context propagation part after. Otherwise, it's gonna take more cycles, and I am afraid it will happen like the last time, you know?
**Jamie Lynch** 13:27 Yeah.
Okay, so you'd be happy to, once that PR has been reviewed, For that to get merged.
**Carlos Alberto Cortez** 13:37 Yep.
**Jamie Lynch** 13:59 Cool. And… yeah, I think that'll be helpful from my perspective, because… That kind of gives us, like, a matrix of… missing features, effectively, and we can maybe even populate for GitHub issues with that.
**Hanson** 14:21 That was great.
**Jamie Lynch** 14:23 Cool. I guess we can talk about release cadence. I don't think… We really covered that when we did the first release, but… what sort of… cadence should we be looking for? Like, is there a standard in OpenTelemetry?
**Jason Plumb** 14:45 You know, I don't… I'm not aware of a standard, but, you know, Java and Java instrumentation release monthly. I know there's other repos that also release monthly. It's kind of a convention, but… I don't think there's anything mandating it. I think the Collector also might release monthly.
**Hanson** 15:06 I wouldn't mind for us, at least initially, when the velocity is, should be pretty high, that we release more frequently. If nothing else, to iron out the kinks in the process. Like, I would love for us to, like, do a patch release, and not, not, not that I want us to do a patch release, but, you know, while not…
**Jason Plumb** 15:26 You want us to have had done one, Patrick.
**Hanson** 15:29 Exactly, I want the ability to click a button and do a release and not have that be a huge ordeal. I mean, I think on Android, people are more likely to adopt new library versions anyway, so if you release every two weeks for Java, I doubt people are going to adopt at that cadence, but for mobile.
that is more reasonable. So, it depends on how much work it takes to do that. And if it's, like, pretty easy, I think I want to do more, and it would be great if some approvers could also, like, get it going, and maybe the… maintainer will do the merge, but we can sort of ditty up that work and have more, more muscles trained, so that we're not, like, dependent on, you know, particular people to do this. So, I vote two weeks.
**Jason Plumb** 16:26 That's cool. I know in other repos, like in the Java core repo, I'm an approver and not a maintainer, and I was able to do the release.
with maybe, like you mentioned, like, maybe there was one step where I needed a little assist from Trask, but I think the rest of it was doable.
As an approver, which is great. I mean… Yeah, so… 2 weeks, to me, does feel a little aggressive.
I… I mean… if… you know, mobile Kotlin users used to getting stuff more frequently, I get it. It's a little bit of a thrash.
And it might make it slightly harder to get bigger stuff stable or kind of done. Not that it's, like, important always to be done with something before you release, but, like, if there's huge chunks, sometimes it's nice to, like.
Be able to say at a given release moment, like, oh yeah, this finishes the work around whatever, rather than it just, like, dragging on across multiple releases.
Do we currently publish snapshots?
**Jamie Lynch** 17:41 No.
**Jason Plumb** 17:42 So that'd be maybe something that would help for people that want to do early integrations, is they can use, like, if we started publishing snapshots, then they could rely on those.
**Hanson** 17:54 And get the, you know, latest and greatest bleeding edge, and be ready for the next release when it hits…
**Jason Plumb** 18:01 Every month or whatever.
**Hanson** 18:03 Yep.
**Jason Plumb** 18:04 What's interesting.
**Hanson** 18:04 What's insane.
**Jason Plumb** 18:05 What's interesting about this project, too, is that the goal is to not really have any other… dependencies, right? Aside from, like, semconv, or… Protos, you know, there's not really a lot of other dependencies.
**Jamie Lynch** 18:20 So we don't…
**Jason Plumb** 18:21 we don't have the same restrict… like, it wouldn't make sense for us to release Android every two weeks, I don't think. No.
Yet. Maybe, maybe one day, but yeah, so it is interesting, like, I… I wouldn't, you know, lose sleep over two weeks. It just seems a little bit… Aggressive.
Especially for a project that has so few maintainers, like, there's so few of us working on it right now that, like, I think… It's a little aggressive.
**Hanson** 18:50 No, I think, I think, I think you're not wrong, especially have… have, snapshots. I think my whole thing is… is… for us to get used to releasing, and get the reps going. But having it monthly, I think, is reasonable, and if there's, like, a dependency that we really want, we could just do a patch release, if it's, like, a fix or something like that. That will also work out some muscles. So, yeah, I have a slight preference for higher cadence.
But, not if it creates overhead, in Thrash, for the bad reasons. But, but having, having a codified process, repeatable, done by other people, If we can do that without having monthly minor releases, or bi-weekly minor releases, then that's fine for me, too.
**Jamie Lynch** 19:46 Yeah, I think I'd agree that around monthly is probably… Goods.
Kind of level, right now.
But I guess we could revisit that in the future.
**Jason Plumb** 20:00 Yeah, we probably don't have a sense yet how much actual human… Attention time it takes, like, that's my… that's currently my unit of currency, you know? Like, if I do the release for Android, I expect to take one to two hours of attention on the thing, and mostly it's just, like, it's babysitting, it's, like, trying not to forget about it while you work on other stuff, and coming back and being like, oh, shit, the build did break, and then having to fix it or whatever, but, you know, usually it's just babysitting.
**Hanson** 20:28 If, if the changelists, changelog generation is fairly automated, if, if the, uploading of the releases of binary candidates, are, are, you know, click of a button, if it's going back and clicking a couple buttons, As long as it's well documented, hopefully, we'll get to a point where… We don't… like, the reps aren't as important, because it's just like, hey, follow these three steps.
**Jason Plumb** 20:55 Yeah.
**Hanson** 20:55 So…
**Jason Plumb** 20:56 I know for a long time in Android, when it was still within Splunk, we would have to do that step where you'd go into Sonotype and, like, manually close the repo, wait for it to show up again, then manually do it. Like, that was such a hassle. And when they finally… I think it was, like, some Gradle… plug-in thing that got fixed that finally allowed it to work. It was just, like, so much nicer.
Oh my gosh.
Yeah.
What a hassle.
Well, the new hassle, if you weren't aware, is that you cannot browse snapshots in Sonotype.
He just kind of, like, we can… We can provide docs and tell people that they're there, but like… You kinda can't go… it's… you can. You have to know URLs, like, you have to guess the URLs.
And then you can grab the metadata file, which will then allow you to construct the actual URL. I mean, Gradle… the Gradle plugins will do that just fine. Like, if you point it to the snapshot repo, it works.
You can depend on the latest snapshot, and it will just work, but you can't go in your browser and sort of casually browse like you used to be able to.
**Hanson** 22:02 It looks like a cron job could just, you know, update that directory listing with, like, well-named file version, or file, you know, structure, and say, hey, is this there, is this there?
**Jason Plumb** 22:11 I mean, I assumed they had something cobbled together like that already. Like, I'm assuming that's how the pages were built, but what do I know?
**Hanson** 22:21 I think at least if we have snapshots, and we have a way for people to know what the latest snapshot is, even if it's just, like, a date format, basically, that would probably be fine.
**Jason Plumb** 22:35 Yeah, and I think we can… let's write down… Sounds like we have consensus around monthly being fine. Let's write that down in the releasing as our cadence, and then maybe just with a little asterisk by it that says, you know, we can release whenever we want to.
**Hanson** 22:50 Yeah.
**Jason Plumb** 22:51 At least for now. Like, we will strive for monthly, we will release more frequently or less frequently when weird stuff arises.
**Hanson** 22:59 At least monthly.
**Jason Plumb** 23:00 Yeah. Caveat.
That's fair.
**Hanson** 23:03 Best attempt.
**Jason Plumb** 23:04 Yep.
**Jamie Lynch** 23:05 Sounds good.
**Jason Plumb** 23:09 But I do think it helps to have that written down, because people will ask about it. Like, people still ask about it in every, every repo. Every open source repo, I see it all the time.
Because they have their pet issue that got fixed, and they're like, oh, when's the next one coming out?
**Jamie Lynch** 23:22 Hmm.
**Jason Plumb** 23:23 So.
**Hanson** 23:24 Well, if we point them to the latest snapshot, like, on the homepage, and this is the latest stable release, you know. Android has a lot of, like, alphas and betas and stuff, like, theoretically, we can tag the dailies, but no, I think Snapshot is just fine for now.
**Jason Plumb** 23:41 Oh, I have something I wanted to ask about.
**Jamie Lynch** 23:45 Let me… let me make sure this is…
**Jason Plumb** 23:53 Let me make sure I can still reproduce this, I bet you I can. I think I was having some weird… this is probably an, like, a JSON problem, but I think I was having, like, these Xcode failures trying to build this thing.
And maybe it's familiar to you, and you can help me with it?
**Hanson** 24:12 you… if you have Xcode installed, you also need to manually select the correct simulators to be installed by default, the iOS simulators. And you also have to have the version that matches whatever that it thinks you need.
**Jason Plumb** 24:28 I've never touched iOS at all, so that's maybe… maybe there's, like, some extensions or other packages I'm missing?
**Hanson** 24:34 It's… it's the simulator. It took me a few hours, if not longer.
**Jason Plumb** 24:38 Can I share, can I share real quick, Jamie?
**Jamie Lynch** 24:40 Cool.
**Jason Plumb** 24:44 You can start.
**Hanson** 24:45 You'd expect Xcode to be installed with the iOS emulators, but they don't.
**Jason Plumb** 24:50 I don't know what I just shared.
Maybe that's the right window? That seems plausible. Okay, yeah, so this is the… This is the thing that was happening, and I get a bunch of these… Does that look familiar?
**Hanson** 25:07 Yep.
That's the first one. There might be a second one after you do this.
**Jason Plumb** 25:15 Like, I think that same command, like, I can't run that, but if I have… I have that somewhere in my path, right? But it's trying to run it from here… I don't know what that is.
Anyway, you think there's some iOS tools? Anyway, I couldn't find any instructions about setting this up in the repo either, so are we lacking something there?
**Hanson** 25:40 Yeah.
**Jamie Lynch** 25:41 Yeah, I'd say so. I guess it's just kind of assumed as a prerequisite, but you've got Xcode installed and a simulator set up. So, yeah, that's a good point.
**Jason Plumb** 25:52 Or even, like, a… like, I have… I think I have Xcode set up.
Like, I… do you know how to tell from the command line?
It seems like this is the thing, right?
**Jamie Lynch** 26:05 Yeah, I'd have thought about Xcode build, if that's present.
**Jason Plumb** 26:10 Look at this, see? Look at this, shh, shh.
**Jamie Lynch** 26:12 I wasn't sure.
**Hanson** 26:14 Command Line Tools is… Hmm, interesting.
**Jamie Lynch** 26:20 So… I know that Xcode command line tools is separate from Xcode BIDE.
So, perhaps you've got the command line in.
Stuff installed, but not big.
Like, OT.
**Jason Plumb** 26:36 I mean, that would be…
**Jamie Lynch** 26:37 line stuff is, like, dense. That's perfect.
**Jason Plumb** 26:40 Okay, that'd be preferred to me, I don't need the UI, because I never want to touch that thing.
Unless I have to. I guess if we have demo apps, maybe it makes sense to once in a while, but… We should… I mean, I guess the takeaway here is that we should… we should clarify, like, we should have a doc that says… in the developing or contributing, like, this is how you gotta get set up as a developer, and you won't be able to do X, Y, and Z unless you have these tools, and like… then I can, as a… if you guys want to take a first stab at that, I can pretend that I'm a user, because I am, and I can try and follow those, and then we'll be on the same page.
If that makes sense.
**Hanson** 27:15 Yeah.
**Jason Plumb** 27:15 Okay.
**Hanson** 27:16 I can try to take that.
**Jamie Lynch** 27:18 Okay.
**Jason Plumb** 27:19 Cool.
Thank you. And I've been… I've been trying to merge PRs, you know, it's slow going, but I'm, you know, I'm chipping away at them. I think, especially with Hansen out last week, it was a little slow going for you, Jamie, so I'm sorry if that's… Frustrating, but we're trying.
**Jamie Lynch** 27:32 That's my problem.
**Jason Plumb** 27:33 Okay.
Cool.
**Hanson** 27:39 Cool. Yeah, gotta get back to those today, or probably tomorrow.
**Jamie Lynch** 27:46 Right, anything else to talk about? Otherwise, we've got 15 minutes back.
**Jason Plumb** 27:53 I think it was pretty good today.
Yeah, I'm glad I remembered that, because I didn't put it on the list, I just remembered, like, I think I had made some changes, or I was trying to verify something, and I was like, I can't even build this thing.
So I'm glad, I'm glad I remembered that, but I don't think I have…
**Hanson** 28:09 The automation requires the simulator, because there's some tests that run on that, and that requires a whole chain of Xcode dependencies. So even if you don't use a UI or anything, you need certain things.
**Jason Plumb** 28:23 Cool, okay.
**Carlos Alberto Cortez** 28:26 I guess that something I can mention is that I was going through the item regarding being able to read attributes and spans.
And yeah, it sounds to me like… Catching the span during the span process, or on the start operation would be, like, a good way to go now.
Hanson, you have some other requirements, or saying that it could be nice to be able to actually get some state from Span. Probably that's something that we can work on as we go on.
That's just my initial feedback for now. I forgot to write that down, but you know, there are so many calls here and there, so I forgot. But yeah, I would suggest that we stick to that for now.
I don't know what other people think here.
**Hanson** 29:10 I… I… I just don't like… having to… so if restricting the modification to within a processor.
if that's, like, the rule, at least the rule is pretty airtight. But to basically say, yeah, there's a workaround, just have a process or keep a reference to an internal implementation, and have that be, like, you know, your access to the modification. It seems… that… I'd rather allow something, explicitly than offer a workaround that does the same thing, but opens up, like, perhaps even more problematic, you know, patterns, like… keep an internal reference, via, you know, an SDK dependency. It's just… it's just so gross to… to me.
**Carlos Alberto Cortez** 30:00 Well, disclaimer, I don't think there's… it's a workaround. Actually, what the SDK is, in theory, allowed to do is very flexible. It's also dangerous, and that's why we don't offer many out-of-the-box processors, and actually, but there's a processor that, in theory, by the way, just to put an example, that, in theory, we will allow, and this will be a spam processor.
that we'll get another spam processor. So you're… you would have a spam processor doing the actual processing, and then the grabber would be sending events regarding the spam lifetime.
And for that, you need to keep a reference to the span, and you're reading stop from the span.
And that's something that has been initially approved, let's say, as an idea to work on.
So it's not, like, misuse of the… of the architecture, I would say, you know?
And the thing is that, on the other hand, I mean, we don't have to discuss that here, it's a super long conversation, like, people… we have been always afraid of allowing people who write instrumentation to be able to check the stage, because then it becomes very, you know, it's very easy to break users, you know? So I guess we have been trying our very best forever, based on previous experiences, to not allow this.
But yeah, anyway, yeah, if you have, yeah, I don't know. The second point that you were making, Hansel, probably just the one I would like to focus on for now, I guess, like, how to make it possible that you… attached state that you can query as a span, as an advanced operation, let's say, that could be an interesting one. Yeah.
**Hanson** 31:41 I think I realize the trade-offs that are being made. I realize what the intention is, and I completely understand it. But sometimes the calculus changes slightly, and since there's already a way of doing this that is, you know, semi-allowed, because if you have SDK dependencies, you're… you should be able to do more. The fact that we have this SDK API probably means it's a… it's… it's… we're codifying this… this privateness into an API. So, I feel that's… I mean, I wouldn't mind writing it down more fully, to fully describe, like, the trade-offs, just so we can, you know, decide with that. But, yeah, I prefer this, since this is, you know, we could make this happen both ways. It's one way is, here's the official documented way, it's dangerous, use it carefully. Here is, well… Yeno.
You could do it anyway.
**Carlos Alberto Cortez** 32:48 Yeah, well… So… On that front, that reminds me that on that API SDK separation, that there's a proposal that somebody did, and I was supposed to take that, but I haven't been busy doing many things. But basically, the idea is that you can attach a state to a span like, in context, but basically, you just keep that private, so the only SDK… the API can write that, but the SDK can consume that. And that could also help you with this approach, because it allows people Anyway, the point is that I'm not saying that specific thing, because it's a long… it would… it would take me so long to explain that, but it's like, there are similar, needs to do that.
And, so it's a valid reason to think about that, it's just that we don't know which one we will go for in the end. But they are similar needs, you know? And I think that they are initially approved as an idea to play with.
Because of these trade-offs that you mentioned, that we are so scared of allowing users to go and read what's happening inside, you know?
**Jason Plumb** 33:51 I will say this topic, I think, touches on something that we had to deal with in Android.
And let me make sure… so in Java, right, we have… we have this class called SpanData, and I think that comes from the spec. It's a spec class, I think. And it's purely readable, right? There's no, like, changing it at this point, it's read-only.
And we made this awesome thing called modified span data, and it extends, or it delegates to a span data, and it allows you to, to change it, which we baked this span data modifier around, which… I think the usages of this today are, like, kind of limited. Like, I don't know that we do a lot of this rejecting spans by attribute value anymore, so some of this might be kind of antiquated.
But the idea was that you could change attributes before export. Like, that was one of the things that we needed to do, because in, sort of, mobile direct ingest kind of situation, you don't necessarily have a collector to put some… filtering or OTTL rules into, so we had to do it client-side. And there was no good, reasonable way to do this using the out-of-the-box Java APIs. Like, we… we needed to catch it right before export, like, after span end, and before export, and there were no good APIs for this. So, this has always felt hacky to me, but it is what we… it's one of the things we have in Android to sort of work around these shortcomings.
**Hanson** 35:22 And I don't think we use it, but… That's a wrapper for an immutable object that allows you to override, which…
**Jason Plumb** 35:31 Yeah. Oof.
Yeah, buddy.
**Hanson** 35:34 Yeah, what I think I'm trying to propose is way less problematic than this. Immutable is still immutable.
Yep.
So, I could… I could, if… yeah, I don't remember if I said I was gonna do it already, but I could… I could write that more fully if it's… if it wasn't fully enough.
To represent this, because it's… it's… it's the least bad way of achieving this, I believe. Otherwise, we just forbid it, because the current ways, I feel like… I didn't even see this one, I didn't even know about that, that existed, but… Yeah, it was like, woof. Never gonna submit that to the spec, so…
**Carlos Alberto Cortez** 36:24 Yeah, it would be nice if you have the motivation, sure, because probably it would be a long discussion, but if you're motivated, I would say, at the very least, initial… That install this in your mind, that would be great, you know?
**Jason Plumb** 36:47 Well, Carlos, shouldn't you be having dinner, like, in 6 hours or something where you are?
**Carlos Alberto Cortez** 36:51 It's almost 7PM here, you know?
**Jason Plumb** 36:55 Yeah, so, like, 5 hours, sorry, I was wrong, yeah.
**Carlos Alberto Cortez** 36:57 Now, Europeans love, at least in this part, to have early dinner. Okay. And the problem for me is that because of that, I had very early lunch, which should have been brunch, yeah.
I don't know, I think in Spain, I was surprised that it's closer, like, to how it's in Mexico, that you have dinner at 9 or 10 PM. But here, yeah, in this Central Europe, some, it's different, yeah.
**Jason Plumb** 37:22 Oh yeah, that's cool.
**Carlos Alberto Cortez** 37:23 I will get a soup later. I will get a soup later, anyway.
**Hanson** 37:27 very efficient.
**Carlos Alberto Cortez** 37:28 No.
**Jason Plumb** 37:30 Alrighty, thanks everyone. See you next time, or see some of you tomorrow.
**Jamie Lynch** 37:35 Thanks. Bye.
**Hanson** 37:36 See you tomorrow, bye.
