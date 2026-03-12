SIG: Java SIG
Date: 2025-08-14
Duration: 54 minutes
Zoom Recording URL: https://zoom.us/rec/share/YIwlXYiRRwUVt99I8RbsfXBNV2L2sy1csLc8UECwXSbnNhdRnqq-dZNxwDFwvUT0.d2xF3IZclzzOgtkq
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 01:00 Hello!
**Trask Stalnaker** 01:59 Hey, folks.
**Jason Plumb** 02:03 Hello!
**Jay DeLuca** 02:06 No.
**Trask Stalnaker** 02:14 Jason… I did not follow the 200-plus, comment thread about the release problems last week.
If you have a summary of anything that I should look at.
**John Watson** 02:33 It was a, … I think we hit every step on the way down, is what happened.
**Jason Plumb** 02:40 It was fine. I mean, you know, I think… Did we end up concluding, John, that maybe we merged one of the PRs too early?
**John Watson** 02:49 No. I think in the end, I don't think we necessarily know that was the case.
**Jason Plumb** 02:56 There was definitely….
**John Watson** 02:58 So it started out… started out with the fund that the build started failing because some… a collector change happened that broke.
**Trask Stalnaker** 03:06 Whoa.
**John Watson** 03:07 Yes, yes. And there's an item on today's agenda for that.
To talk about what to do about that. So that's where things started.
And then we ended up having.
**Jason Plumb** 03:18 And Jay helped out with that, right? So thanks for that.
**John Watson** 03:21 Yeah, yeah, yeah. We got that one sorted. We got it sorted out. But, I mean, sort of. I mean, we basically just commented out the failing assertions, but we need to discuss what we really should do with that. But then the bigger thing was we ran into lots of problems around the automated … updating of the API diffs.
**Trask Stalnaker** 03:44 Hmm, okay.
**Jason Plumb** 03:47 And I think it was the case that the stuff that was in main on head was already wrong before the release started. Was that true?
**John Watson** 03:55 No, no, it was the… during the release, you merge one that basically then gets updated after the release is actually in… Maven.
Has been….
**Jason Plumb** 04:08 Right, so that's the one that… that's the one that… That's the one that we merged too early, maybe.
**John Watson** 04:15 Well, I don't… well, but if that's the case, then we need to update our instructions, because it's the….
**Jason Plumb** 04:21 That's what I'm wondering.
**John Watson** 04:23 But I'm not sure exactly how it's supposed to work.
So, the process you do is you run the release job, and it creates some PRs.
**Jason Plumb** 04:31 Yep.
**John Watson** 04:32 And… one of those PRs updates documentation, and updates the API docs.
**Jason Plumb** 04:41 In Maine.
**John Watson** 04:43 in Maine. Well, if you merge it.
**Jason Plumb** 04:46 Yeah, yeah.
**John Watson** 04:47 It updates them against main, that basically ends up with the previous release against the snapshot.
**Jason Plumb** 04:54 Right.
**John Watson** 04:54 previous release against the snapshot, not the current release against the snapshot.
**Jason Plumb** 04:58 That's why you need to wait for… yeah, so that's why you need to wait for the current release to be updated, otherwise you skip one, right?
**John Watson** 05:07 Right, and then once the release has been… shows up in Maven Central, there's another PR that gets created that updates the API docs to point to the current release against.
**Trask Stalnaker** 05:19 I thought I tried to… yeah, it doesn't surprise me that there's… something could be buggy, because I definitely… I was trying to simplify this recently by combining it all into one PR.
That would wait for… So it's supposed to wait for, ….
**John Watson** 05:41 There's a previous PR that gets created that updates it with… in a different state.
**Trask Stalnaker** 05:49 Mmm, what is that PR?
**John Watson** 05:52 They actually just the… I think the first… the first one that happens does that.
**Trask Stalnaker** 05:59 Oh, the prepare one.
**John Watson** 06:01 Yeah.
I think.
**Trask Stalnaker** 06:04 Yes, prepare… So this one is going to… Yeah, this is going to update the version.
In Maine.
Which also then, part of that, updates the API docs.
**John Watson** 06:23 just kind of.
**Trask Stalnaker** 06:24 Oh, it does? Oh… Okay, that… Probably….
**John Watson** 06:33 like, the build will just run and update the API docs, and then we… this… the… this thing adds stuff to the… and pushes it as a new… Commit.
**Trask Stalnaker** 06:45 I see, so if I look….
**John Watson** 06:46 So it ends up… the API docs ended up in a weird state before the final release is actually in Maven Central.
And so, we could… if we had had… if I had had access to just override the things and just merge stuff, we could have got it corrected really fast. But we had.
**Jason Plumb** 07:10 Yeah, Tras… Trask, if you pull up 7551… PR… That's the one that I had to sort of, like, manually cobble together to do the right thing.
**Trask Stalnaker** 07:26 Okay, but I wanted to look at this one, because this is the one that updates… this is part of the prepare side that.
**Jason Plumb** 07:35 This is our first.
**Trask Stalnaker** 07:36 PR.
And did it update? I didn't think… oh, oh, oh, yes, yes, yes, this is acceptable.
**John Watson** 07:44 This is the one that then ended up making it impossible for us to… get….
**Jason Plumb** 07:49 Because it's going 154 against 152.
**John Watson** 07:53 Yep.
**Jason Plumb** 07:55 Which is not what you ever want.
**John Watson** 07:58 Yeah, this is not.
**Trask Stalnaker** 07:59 library.
**John Watson** 08:00 This is not a valid state, right?
**Jason Plumb** 08:01 Yeah.
Exactly, so this is the one that I think I superseded. Like, I did it manually to get things realigned.
**John Watson** 08:13 Yeah.
**Trask Stalnaker** 08:14 I'm just confused, because this is what we've been using… let's see what we're doing in… Instrumentation repo. I'm not sure why that's an invalid….
**John Watson** 08:26 Well, I mean, it's not… it's just.
**Jason Plumb** 08:28 What am I doing?
**John Watson** 08:28 52 against 154 snapshot is just a… that's a funny thing, and it ends up getting merged. Then when you want to run the actual… like, after the fact, the one that you put together then can't be merged.
Like, it always… Oh, because there's conflicts? Because there's conf… yeah, there's conflicts, exactly.
**Trask Stalnaker** 08:46 I see, yeah….
**Jason Plumb** 08:48 But also, we don't run API… Compare in instrumentation, do we?
**John Watson** 08:53 Yeah, yeah.
**Trask Stalnaker** 08:54 We do, yeah, so this is the one I wanted to look at.
… And instrumentation, yeah, so we do the same thing.
**Jason Plumb** 09:04 18 versus an instrumentation.
**Trask Stalnaker** 09:05 Yeah.
**Jason Plumb** 09:06 Yeah.
**Trask Stalnaker** 09:09 Yeah, and it doesn't cause us problems.
But yeah, let's, we'll just, next time, maybe, Jason, have you do it, but I'll be hopefully not on vacation, so I can… Yeah, that's cool. …track and see where, where and why it's failing.
**Jason Plumb** 09:28 That's cool.
**John Watson** 09:29 We ended up sorting it out in the end, but….
**Trask Stalnaker** 09:31 Yeah, yeah.
**John Watson** 09:32 Sometime.
**Trask Stalnaker** 09:34 Thank you, huh.
**Jason Plumb** 09:34 There were only that many messages in that thread, because John and I bandared a lot.
**John Watson** 09:40 also true.
**Jason Plumb** 09:41 As we… As we do.
**Trask Stalnaker** 09:46 Alright, Gregor… impediments to dynamic loading for Java Agent.
**GZ Gregor Zeitlinger** 09:54 Yeah, this, it's a question because, our friends in Obi, are asking about this, because they're wondering if they can contribute, More to making Possibly everything, dynamically loadable.
**Trask Stalnaker** 10:15 And so, by dynamically loadable, you mean specifically attaching the Java agent to an existing running JVM?
**GZ Gregor Zeitlinger** 10:24 Yes.
**Trask Stalnaker** 10:24 Attaching it at startup.
Yeah, so we have an issue that… Discusses that.
**Jason Plumb** 10:38 People still want this in 2025, huh?
**GZ Gregor Zeitlinger** 10:42 More than ever.
And it seems that this is not going out of JVM anytime soon.
**Trask Stalnaker** 10:56 So… I would point the… I mean… Oh, let's see it.
To… there are some basically fundamental, like, issues that would need to be… Like, we'd need to have some seriously updated testing for this.
Where all the instrumentations run once to load all the classes, and then… Attached dynamically and rerun.
Right. If… if you could do that, and prove out that it works, then… We might be more… interested in supporting, but there's a lot of… there's probably going to be a lot of edge cases. For example.
You know, some of the things… we instrument when, like, the GRP Server Builder is first created, the build method.
Right? And so if we attach later, that build method has already been called.
So we would actually need a whole different instrumentation approach.
In order to make it work.
Certainly, I mean, anything's possible via bike code instrumentation, but it's not quite so simple in some of.
**GZ Gregor Zeitlinger** 12:18 Nothing is simple with bytecode manipulation. I was just wondering if… what the known patterns are that make it hard. And the builder one is a really good one.
Yeah, the issue.
**Trask Stalnaker** 12:35 Yeah.
**GZ Gregor Zeitlinger** 12:35 It's from Nicola, who has asked about this, so it's exactly that.
**Trask Stalnaker** 12:44 Yeah, and I don't know, I mean, I don't know how hard it would be to… Update the tests… but that would be cool, like, to try if you wanted to see how many Already pass versus fail, the integration tests.
If you could… basically run the test, but allow it to fail so that it warms it up, and then dynamically attach the Java agent.
**GZ Gregor Zeitlinger** 13:18 Yeah, okay.
**Trask Stalnaker** 13:19 Thanks.
Yup.
John!
**John Watson** 13:29 Yeah, so this was coming out of, you know, what happened last Friday.
So, we have a test in the Prometheus module that tests Prometheus against the collector, and a change got made to… and we are using the latest collector release. So we have… we don't have it pinned to a very specific one, we are using the latest collector release.
… And the test was making assertions that broke because the collector implementation changed and stopped writing scope, name, and version.
So the real question is, what is the goal… what is this test for? Are we trying to detect changes in the collector and make sure that we're aware of them, or are we trying to verify that our Prometheus thing is doing what it should in relation to what the collector does? Because… If we are dependent… if the collector changes, Which… it did.
Should this test fail, or should we pin our collector release to a very specific version so that the test is reliable?
And I don't know, I don't honestly have any idea why… what this test is about, and what its purpose is.
But depending on the… if we want to be detecting changes in the collector.
Then this test will occasionally break, and we'll have to figure out what we want to do with it.
**GZ Gregor Zeitlinger** 14:59 All pinning is better either way.
**John Watson** 15:02 No, because then we won't know if the collector changed, and that we're no longer using… we're no longer… like, we're maybe no longer doing what we expected we were doing. So I don't think….
**Trask Stalnaker** 15:13 I think what Gregor is saying is, pinning it, but have Renovate automatically update.
**GZ Gregor Zeitlinger** 15:18 Alright, Dan.
**Trask Stalnaker** 15:21 That way, you're… you always get the latest, but it'll… you'll see it fail in that PR, so it won't break main.
**John Watson** 15:30 So, can Renovate dip into this code where the version is inside the actual test code?
**GZ Gregor Zeitlinger** 15:37 You can do anything with Renovate. You can have regular expressions to do that.
**Trask Stalnaker** 15:46 Here's a… cool thing I was adding to… I'm… want to test out here, and then I'll add elsewhere, but… … So this is kind of what Gregor's talking about. You can, … Add these custom regexes to the renovate configuration.
And then in our build, for example, I want to have it… we always forget to update the… to the latest Java version that we're running again, start tests, and so this will make Renovate aware and auto-update that version.
But that doesn't solve your other problem.
**John Watson** 16:29 Well, no, I mean, I think this would, because inside the… well, you'd have to… inside this code, like, up… if you look up at the top of this class.
There's a hard-coded version in, that's being pulled in Right there, collector image, that.
… So, if we could use Renovate to update this….
**GZ Gregor Zeitlinger** 17:00 Yeah, that works.
**John Watson** 17:07 Because right now, we're just pulling in latest.
**Trask Stalnaker** 17:09 Yeah. So at least you won't be surprised by… Sudden break-in.
**John Watson** 17:14 Especially when you're trying to do a release.
**Trask Stalnaker** 17:17 Yeah.
**John Watson** 17:18 Yeah, exactly.
Yeah, so… so maybe if you could put a comment, or somebody could put a comment on that issue, and we could then… somebody could put in a PR to do that, that would probably be the best solution. I agree.
**GZ Gregor Zeitlinger** 17:33 I can take that one.
**Trask Stalnaker** 17:37 Awesome.
But John, does that… I mean, still, we'll need to… we'll probably wanna… we'll need to fix it with the latest version.
**John Watson** 17:48 Well, I mean, that… fix it, that's what is… the comment out is the fixing of it at the moment.
**Trask Stalnaker** 17:54 Oh, okay, so we're okay for just… we don't care about this code, we can just delete it?
**John Watson** 18:00 I mean, assuming the… assuming the collector… well, so I think that, Jay, you put in some comments, I think, in that the issue. It looked like the collector made some changes and then reverted them?
Because it was breaking… something?
And that they're probably going to come back?
From what I was reading?
But it was hard to tell.
And I'm not exactly sure why they removed the scope name inversion. Like, it was their….
**Jason Plumb** 18:32 Because they're on the resource.
Or, sorry, the scope. They don't need to be on the data points, because they're already on the scope.
**John Watson** 18:41 But it sounded like they were… removing them broke people in some way.
Or adding the… I don't know, anyway.
**Jason Plumb** 18:50 I mean, every change will break somebody, right?
**John Watson** 18:53 Yeah.
Anyway, I think… Deleting them is probably.
**Trask Stalnaker** 18:58 your main….
**John Watson** 18:59 I don't know. I'm not sure. I don't know enough. I don't know enough. I don't know enough to know whether it's good or bad, or whether this is a problem, or whether we're now going to be… like, our users are going to be broken because this is not there. Just don't know.
**GZ Gregor Zeitlinger** 19:11 This is a new, … specification that says that OtelScope name must be promoted in Prometheus, but it has been added recently, and I guess it was reverted in the collector because of some problem, but it will be back at some point. It's just a matter of when, and until then, we can just leave it commented out.
I, I would suggest.
**Trask Stalnaker** 19:32 And… Gregor, will this then… The scope name and scope version would then show up on the Prometheus infometric.
**GZ Gregor Zeitlinger** 19:43 No, it is, put in the resource, in favor of the infometric, because Infometric was too complicated to use for most people. That's the bottom line.
**Trask Stalnaker** 19:57 Oh, how are… I thought the infometric was the Prometheus way to get resource attributes.
**GZ Gregor Zeitlinger** 20:05 Right, and in theory, this all works fine, but it's quite complicated to use, because you need to use joins if you want to do the simplest thing, and users are are just not satisfied with that behavior, and so more and more things are being transferred to a resource to have an easier user experience. That's, like, the general trend.
**Trask Stalnaker** 20:31 Okay, is there already a replacement for the infometric, or for passing resources?
attributes to Prometheus. And so this is for the infometric, there is, there are….
**GZ Gregor Zeitlinger** 20:46 more infometrics. The scope infometric is basically useless, but the, like, the target infometric, this is still being used because it has all the resource attributes, and only the most important resource attributes are being promoted to resource Attributes, to cover the.
**Trask Stalnaker** 21:05 Oh, okay.
**GZ Gregor Zeitlinger** 21:05 use cases.
**Trask Stalnaker** 21:06 And so they're just dropping the scope name and scope version, because they're just not useful enough to… be passed.
**GZ Gregor Zeitlinger** 21:17 To be put in the info… in the scope infometric, right?
**Trask Stalnaker** 21:20 Yeah. Okay. Okay.
So, yeah, so it sounds like we can… Just… sounds like it's okay to just remove those, and there's not a replacement for that verification.
**GZ Gregor Zeitlinger** 21:37 Well, what is commented out here is the resource attribute, if I get this.
Correctly. And that is what was rolled back, but what will be there again in the future.
**Trask Stalnaker** 21:52 … This might be a resource attribute? These are resource attributes, the hotel scope name and scope version.
**GZ Gregor Zeitlinger** 22:01 Oh, sorry, no, it's not a resource attribute, because.
**Jason Plumb** 22:04 Data point attributes.
**GZ Gregor Zeitlinger** 22:05 No, yeah, it's… it's on the… it's on the primitive attributes, yeah, sorry about that.
**Trask Stalnaker** 22:11 Okay.
**John Watson** 22:12 Is there… well, I guess the question is, is there something different that we are supposed to be doing That we're not.
And that this test failure uncovered. That we should be.
**GZ Gregor Zeitlinger** 22:24 You know….
**John Watson** 22:25 A different assertion now.
Like, do the OTO name and version, are they nowhere now?
Or is there a place where we can assert that we have… they're in the right place?
**GZ Gregor Zeitlinger** 22:38 So I think this is quite unrelated to what we're doing, because it's quite clear that we want to put it in the OTLP payload, and that is all we should actually care about.
I would say we don't care how the collector is transforming it, and I'm not even sure why we have this test either.
**John Watson** 22:55 Yeah, that was kind of the… that was really the basis of, like, what are we trying to test here? I'm kind of confused.
Like, we plug in the collector, and we send data to it, and we verify that the data we sent to it is the Or the data that comes out of it is… I, yeah, I'm confused.
**GZ Gregor Zeitlinger** 23:14 So basically, we're testing that we're still speaking the same language, and that the OTLP we are sending can be understood.
… But maybe this is overkill.
**Trask Stalnaker** 23:27 Looks like just a very basic integration test that's just like, hey, happy path works.
Yeah, because it's definitely not testing, like, all of the different combinations and all of the stuff that are normal, like, Prometheus exporter tests test.
**John Watson** 24:07 Good old AI Gregor.
**GZ Gregor Zeitlinger** 24:10 I hope he will do it better than I do.
**Trask Stalnaker** 24:18 I'm pretty sure I asked… … AI to do this one.
… But it took several.
Did it wrong several times.
Or at least to get it… at least for me to understand what it was doing.
**GZ Gregor Zeitlinger** 24:37 Yeah.
The new Chet GP.
**Trask Stalnaker** 24:39 Oh, no.
**GZ Gregor Zeitlinger** 24:42 The new ChatGPT is quite good, but I don't know if it would get this one, right?
**Trask Stalnaker** 24:48 You know what? It actually… I remember now. It actually got it… it was… it did fine on this. What happened, though, is I was testing it on my fork.
And… it wasn't working on my fork, Because… of this… This rule here, which says group all major updates once a week.
And so I'm like, it's not updating my Java version in my fork, and I could not figure that out for the longest time. I finally cloned the Renovate repo and asked co-pilot over there in that… in my checkout of that repo, what was going on, and it was able to finally… Figure it out.
All right, Gregor, more, attribute… renaming attributes….
**GZ Gregor Zeitlinger** 25:47 Yeah, you tagged me in this one. I thought, it's too difficult for me to figure it out.
**Trask Stalnaker** 25:52 Aww.
**GZ Gregor Zeitlinger** 25:54 Because it's about, breaking change in semantic conventions in a contrapt rep repository. I don't know if we've… Had that, or if we… Have a policy for that.
**Trask Stalnaker** 26:10 So, is… are we using… Which specifically… let's see… So, our current resource, Azure resource… Uses a different name.
**GZ Gregor Zeitlinger** 26:34 I think otherwise we would not have this issue.
**Trask Stalnaker** 26:41 Oh, I thought that this was just trying to add, … some missing things to the semantic convention repo that were already being used.
Only change that has occurred. Oh, I see. Is this what you're talking about? App.service to app underscore service?
Gotcha.
… I mean, we are… allowed to, because this is… Alpha?
We just need to, you know, call it out in the changelog.
I see. So this is what we would change here.
Yeah.
That's okay.
**GZ Gregor Zeitlinger** 27:34 Okay.
**Trask Stalnaker** 27:35 We just need to call it out in the changelog.
**GZ Gregor Zeitlinger** 27:39 Alright, that's easy then.
**Trask Stalnaker** 27:49 Antoine, are you here?
Don't.
Let's see, Antoine. ….
**Jason Plumb** 27:59 I can pretend to be him.
**Trask Stalnaker** 28:00 Yes.
**Jason Plumb** 28:01 Sure.
**Trask Stalnaker** 28:03 You gotta use the awesome, French accent, though.
**Jason Plumb** 28:07 Yeah, I was gonna say, just pretend I'm doing, like, a really offensive, like, over-the-top French accent. … I think he probably just wants to nudge this one and see where we're at with this. I know that we put a milestone on it last time.
So, I think it's slated for… it still doesn't have a green check, though.
….
**Trask Stalnaker** 28:26 Oh, okay. Yes, that's okay. I, … when I put the milestone on, I'm basically saying, okay, it's been….
**Jason Plumb** 28:38 Goodbye.
**Trask Stalnaker** 28:38 and… Approved… approved by the component owners, and….
**Jason Plumb** 28:42 Great.
**Trask Stalnaker** 28:43 I'm just kind of letting it… sink in, but I will merge it. And actually, it's been… There's been enough time here, let's just… Get this in.
….
**Jason Plumb** 28:58 May we… Thank you.
I don't know any French, by the way.
**Trask Stalnaker** 29:12 Oh, yeah, speaking of which, it is release week. Okay, I gotta get on that today.
Let's… Insta… instrumentation release.
**Jason Plumb** 29:29 Just because we're talking about releasing, … Jay, you were on that thread about OKHTTP and the change breaking us in Android, blah blah. It looks like we've got that ironed out, so just… just to circle back on that.
**Jay DeLuca** 29:44 How it looks like if… if someone else outside of Android comes to us with similar issues, it looks like there's some… trickery we can do in the Gradle configs to tell it to use the other one. That's the, kind of the go-to.
**Jason Plumb** 29:59 Exactly.
**Trask Stalnaker** 30:01 Thank you, Laurie.
Oh, what did… this is… No, probably not.
Any PRs?
In the instrumentation repo that… People want….
**GZ Gregor Zeitlinger** 30:34 Robert had a bug, which I just apparently fixed, it's, and I want to add that. Do we have a milestone?
**Trask Stalnaker** 30:43 Yeah.
**GZ Gregor Zeitlinger** 30:46 The 19?
**Trask Stalnaker** 30:47 Oh, was that the lot? Yeah, yeah.
**GZ Gregor Zeitlinger** 30:53 Yep, I did that.
**Trask Stalnaker** 30:54 Yep.
Okay, perfect. Yeah, just if anybody has anything else… Either, if you have permission, add the milestone, otherwise, just ping… Ping me.
….
**GZ Gregor Zeitlinger** 31:13 Alright, ….
**Trask Stalnaker** 31:16 Gregor… Naming of… okay, I can… or I'll let you. We had a good discussion… Do you want, … Give the overview here.
**GZ Gregor Zeitlinger** 31:32 Right, yeah, this is a declarative configuration, which we discuss usually in the meeting before, but I'd like to have some more feedback here, because naming is, like, the hardest thing. And here, we have a property that applies both to the agent and the spring starter, and so far, it is grouped under the comment section.
And Trask pointed out, that, Having things under the comment section can be confusing if it applies, only sometimes, because, library instrumentation will not Respect of the enabled flag.
But the agent and the spring starter would.
… So then we started to explore some alternatives.
… And, the default enabled is actually what kicked us off, but then the discussion turned into more, like, how would we group this so that it's intuitive to understand that we have properties, that control… that in the agent you can enable an instrumentation. And, the same would be true for Spring Startup, but then it would be, under Springs… And so.
**Jason Plumb** 32:57 No.
**GZ Gregor Zeitlinger** 32:58 Here is a top-level, … top-level node in YAML. What is not instrumentation is SDKs, so that is how the file is structured.
And, … Then, we have agent, and then again instrumentation, which, feels like a bit redundant, but it, on the other hand, it captures, Top….
**Trask Stalnaker** 33:36 We're losing you a little bit, Gregor.
**Jason Plumb** 33:39 choppy.
**GZ Gregor Zeitlinger** 33:42 Then, just kick it away while I'm… I'm repairing my Wi-Fi.
**Trask Stalnaker** 33:48 So this is, our proposal, … Yeah, so the downside is it feels a little redundant there. The upside is we tried to put these directly under agent, and then it wasn't really clear, like, what was it the default enabled of?
… I guess maybe these could be… bumped up right under agent, and … Default instrumentation enabled something else, but this kind of groups them okay.
It's also not a super… Common thing that at least we don't really recommend.
I'm mucking around with enabled and disabled stuff too much, other than, like, to disable, you know, some… something that's noisy that you don't want.
….
**Jason Plumb** 34:48 Why is that… why… I'm sure I missed this and it was discussed, but why is it called default enabled?
Like, why do we have the word default in there?
**GZ Gregor Zeitlinger** 34:58 Because.
**Trask Stalnaker** 34:58 Yeah.
Go ahead.
**GZ Gregor Zeitlinger** 35:03 Because it applies to all instrumentations without enumerating them. So, what you can do is you can disable all, and then selectively enable them if you set it to false.
**Jason Plumb** 35:16 Got it, okay, okay.
**Trask Stalnaker** 35:20 And it's to match… Today, we have, let's see, probably… Here, default enabled. Yeah, so it's basically this.
And so….
**Jason Plumb** 35:38 with….
**Trask Stalnaker** 35:39 what my… what I was asking, what kind of started this was that I… didn't love it being right under common. We have some other things under common.
If we look at configurations….
**GZ Gregor Zeitlinger** 36:03 No, I think you don't have it there, because it's the Java part.
**Trask Stalnaker** 36:09 Oh, okay.
Thanks.
….
**GZ Gregor Zeitlinger** 36:15 But what you have is, statement sanitizer enabled for everything database-related, I think that's one.
**Trask Stalnaker** 36:25 Yeah, and so those, … If we look at, like, Java Common here, you know, we might have Sanith Tizer… Something like that.
And these apply also not only in the Java agent instrumentation, but in library instrumentation, native instrumentation can all support that.
… the reason I was… Hesitant to put… Default enabled here.
Is that… This is only respected by… our, like, distros, the agent and the spring boot starter.
But it doesn't… it wouldn't affect people who are using the SDK and library instrumentations, or native instrumentations.
And so that's kind of what….
**GZ Gregor Zeitlinger** 37:26 I'm wondering about the enabled, though. If you, like, have native instrumentation, would you want to use the enabled flag to disable?
an instrumentation for, I don't know, OKHTTP?
Does not seem, too weird to do so.
**Trask Stalnaker** 37:50 That's a good point. It does… yeah, like, you would want to have some way, and having a common way.
to disable it.
is… Nice. I don't know about the default enabled, but definitely I… That's a good argument for… … Okay, CPP… Enabled. False.
So, I mean, we could keep all… we could keep the individual enabled, disabled, under… here.
We don't really… we don't respect it today in our library instrumentation, but potentially we could.
And just have the… I guess default enabled could even make sense.
**GZ Gregor Zeitlinger** 38:56 It's kind of hard to know.
**Trask Stalnaker** 38:59 Yeah, do you think that's a cross-language?
… Question, like, should we raise that in the configuration?
Sig, then….
**GZ Gregor Zeitlinger** 39:14 I… I don't think so. So, … Having the concept of individual instrumentations is nothing that exists there so far, so… configuration that is cross-language is more on the conservative side. So, things like HTTP settings, where we clearly define One concrete use case, but… Enabling instrumentations, that would take it to another level than it is right now.
**Trask Stalnaker** 39:50 I'm… For listing specific instrumentations over there, definitely, but maybe a pattern where, like, I'm… Assuming that, let's see, instrumentation… Here, general, we've got….
**GZ Gregor Zeitlinger** 40:09 Put this on the side.
**Trask Stalnaker** 40:10 So, like, example here, I think, is… like… Supposed to be an instrumentation?
With different properties.
Configure the instrumentation corresponding to key example.
So, I mean… We could have… Optionally, like, if it did support an enabled flag, you could have enabled here.
**GZ Gregor Zeitlinger** 40:37 Yeah, except that it would be disabled, because… This is following the convention that everything that's not specified is false.
**Trask Stalnaker** 40:46 Right, right.
**GZ Gregor Zeitlinger** 40:48 convince, I suppose.
**Trask Stalnaker** 40:50 Which is okay. Also, I mean, a disabled… True, you would add.
**GZ Gregor Zeitlinger** 41:02 But then you would also have to talk about the concept of, if instrumentations are enabled by default, and I don't know if there are even more things, … I don't know if all the other languages would also… be able to follow this pattern, I simply don't know.
**Trask Stalnaker** 41:32 Okay.
… Yeah, what would you normally do if you didn't… if you wanted to disable all instrumentations I see, the default. You would want default if you wanted… it's like if you're debugging something, I guess is the main use case, where you want to disable everything and just enable one thing.
**GZ Gregor Zeitlinger** 41:52 Hmm.
**Trask Stalnaker** 41:54 So maybe not super….
**GZ Gregor Zeitlinger** 41:57 I'm Northern.
**Trask Stalnaker** 41:59 … Let's… Thick on that a little bit more, Gregor, because it's a good… You brought up a good point that it may… could make sense under those individual instrumentations. I was thinking it didn't make sense under them.
But, especially native ones… that are on by default. You want to have some way to turn them off that's not….
**GZ Gregor Zeitlinger** 42:33 necessarily programmatic. Huh?
**Trask Stalnaker** 42:39 Okay.
….
**GZ Gregor Zeitlinger** 42:41 Are you, … Sorry.
**Trask Stalnaker** 42:42 Let's….
**GZ Gregor Zeitlinger** 42:43 Would you, be fine with, splitting that question off and just removing that from the PR?
**Trask Stalnaker** 42:50 Oh, I see. Yeah.
**GZ Gregor Zeitlinger** 42:52 Yeah, yeah, that's a good….
**Trask Stalnaker** 42:54 Idea.
**GZ Gregor Zeitlinger** 42:55 Yes, I drops down.
**Trask Stalnaker** 42:57 If that… if that's splittable.
**GZ Gregor Zeitlinger** 43:00 Yeah, I would just remove that line, and, I mean, the… The thing is not ready anyway, so, … we are just removing that line and creating a new issue, then at least we could progress on other areas that depend on this PR.
**Trask Stalnaker** 43:18 That sounds like a great idea.
**GZ Gregor Zeitlinger** 43:23 Thanks!
**Trask Stalnaker** 43:30 Jason….
**Jason Plumb** 43:34 Yeah, I just wanted to make sure that people were aware of it and thinking about it. These two… I'm just wondering if maybe… I don't know, like, maybe the Shadow benefits from having Gradle 9 in there first? I'm not sure, but Sylvan took some time and looked at it and kind of got stumped. I haven't had any cycles to look at it, but… It's gonna be some work, I imagine.
**Trask Stalnaker** 43:56 Yeah, I banged my head against it for a little bit.
**Jason Plumb** 43:59 Yeah.
**Trask Stalnaker** 44:00 I bisected the, Gradle, I mean, the shadow, repo to see which commit introduced the problem for us.
**Jason Plumb** 44:11 Yeah, yeah.
**Lauri Tulmin** 44:12 Did you find it? I think it was somewhere between RC1 and RC2.
**Trask Stalnaker** 44:19 It was, … So, it seemed like… yeah, let… let me… Find… Oh, no, it's not letting me… Yeah, I will dig that up, I… Have it on my remote.
Desktop.
**Lauri Tulmin** 44:41 To me, it looked like that there is some sort of behavioral change in the Shadow plugin.
It might be that it's their bug or something.
**Jason Plumb** 44:52 The changelog is massive.
**Lauri Tulmin** 44:53 Anyway, the shadow thing is… like, it's business as usual. The shadow thing is probably hard, but … The Gradle update itself, it's going to be way harder than that.
So, if anybody.
**Trask Stalnaker** 45:08 Yeah.
**Lauri Tulmin** 45:09 But then, … I'm pretty sure they're all, like, … Many small failures.
There.
**Trask Stalnaker** 45:18 Yeah, aren't they enabling the, like, things have to be configuration cache?
Has to be supported now.
**Lauri Tulmin** 45:28 I think the… probably the scariest thing is that, … Some old plugins will stop working.
And, like, for example, I don't know, like.
maybe, like, if something like the Spring Boot plugin that we use for, like, building version 2, Which is probably quite, like, a bit older.
**Trask Stalnaker** 45:51 If that one stops radius.
**Lauri Tulmin** 45:53 Then that's going to be a major headache for us.
Probably also, I don't know, quark or stuff, if that doesn't work, then well… I think… Probably easiest to just delete that instrumentation.
**Trask Stalnaker** 46:09 … Yeah, I think I… I think I made that choice just to delete some, old tests, ….
**GZ Gregor Zeitlinger** 46:23 That's cool.
**Trask Stalnaker** 46:24 I think I updated….
**GZ Gregor Zeitlinger** 46:27 Yeah, yeah.
**Trask Stalnaker** 46:30 Maybe not.
I think I was trying, at least.
**GZ Gregor Zeitlinger** 46:34 Essen calm down.
**Trask Stalnaker** 46:39 Operation… Oh, no, I never succeeded over in our distro either. But yeah, I think I got far enough to run into that same problem, Lori, of the old Spring Boot. Oh, yes, I know what I….
**GZ Gregor Zeitlinger** 46:55 Who knows?
**Trask Stalnaker** 46:56 I was able to work around that a little bit, the plugin, at least for the tests, the Spring Boot plugin.
Just not using the plugin, and just using the dependencies directly, basically kind of rewriting the test to use dependencies.
**GZ Gregor Zeitlinger** 47:10 Wrong.
**Lauri Tulmin** 47:11 I think that's definitely one option.
But we also have some, like, native compilation stuff going on there. I hope that won't be causing some issues.
**GZ Gregor Zeitlinger** 47:22 Prices need to know, Dr. P.
**Trask Stalnaker** 47:24 Yeah.
**Lauri Tulmin** 47:25 Yeah, I'm… I'm pretty sure that whatever is going on with the shadow plugin, it's going to be peanuts when compared to the actual Gradle update.
**Trask Stalnaker** 47:35 I would have thought so too, but, like, I mean, we've… like, I've probably spent, you know.
6 hours on, you know, like, off and on, like, trying the, Gradle plugin. I know, what, and now a couple other people have, too.
**Lauri Tulmin** 47:54 Yeah, I also spent time… I got rid of the circularity, but I ran into another issue.
**Trask Stalnaker** 48:08 All right.
**Jason Plumb** 48:10 Just wanted to make sure that we were thinking about it. That's the only reason I put it in the agenda.
**Trask Stalnaker** 48:19 Thinking slash scared about it.
**Jason Plumb** 48:21 Yeah.
I think we got Gradle 9 on the Android, no problem, I think.
Is that true?
**Trask Stalnaker** 48:31 You know the one that I was surprised about… is… One of these… Backwards.
One of these simple repos… Oh, it must have been semantic conventions.
Oh, finally did get it. Gradle 9, okay.
Yes, but it was running out of memory, … After updating to 9, but I guess… Okay, just had to give it more memory. Okay, never mind.
But yes, I struggled with this one for too long, also.
**Jason Plumb** 49:21 I put a link to the Android fixes for Gradle 9 in the agenda doc. I don't know if it's helpful, I mean… I'm sure it's a fraction of what the work we have here.
We had some, configurations that were being added explicitly to their container. Yeah, this part, like, But… The documentation says that you don't have to call add, like, the act of creating also adds it to the configurations. So that was, like, something that was broken, we just didn't have to call add.
**Trask Stalnaker** 49:54 Nice.
**Jason Plumb** 49:56 Yeah, it's pretty, pretty minimal.
**Trask Stalnaker** 50:02 Lori… I started… Oh, go ahead.
**Jay DeLuca** 50:06 I was gonna say, I started on the core, the SDK as well. I have a PR up, but I got it to build locally, but there's a bunch of, like, check-style Failures now.
I have to… Jump back into it, but… It's in a draft, if you just look for me.
**Trask Stalnaker** 50:29 Oh, okay.
Nice.
Oh, yes, hey, the same copy-paste.
**Jay DeLuca** 50:38 But yeah, the Google Protobuff plugin, like, I think, like Laurie said, that… that no longer was supported, so I had to update that. I don't know if that is leading to some of the… check style errors, I'm not… I'm not sure yet, but….
**Trask Stalnaker** 51:00 Cool. Lori, do you… are you getting these admin… PRs… Do you see this?
**Lauri Tulmin** 51:15 I think I saw this.
**Trask Stalnaker** 51:18 Okay, okay.
… Yeah, if you can take a look, I want to… So I've been having trouble, like, all across OpenTelemetry with these, We're kind of having trouble with… in this. This is, for folks who haven't seen it, this is, … IAC infrastructure as code, Terraform repo for, managing the repo… GitHub repo settings.
So, for example, Java… … Like, it's all defined what the settings are and branch protections.
**Jason Plumb** 52:05 This is, like, one of the only… this is one of the few private repos that are out there in OpenTelemetry, right?
What's the reason why it's private again?
**Trask Stalnaker** 52:15 I'm… Abundance of caution.
**Jason Plumb** 52:18 And, like, it doesn't need extra eyes on it, like, he'll get a bunch of random PRs otherwise, probably.
**Trask Stalnaker** 52:26 More… it was really just, out of abundance of caution, because there's a pretty high level, token that we use that has permissions to update all the repo settings.
And so, while… It's secure, to the best of my knowledge.
**Jason Plumb** 52:51 Like, if it did get divulged through an action or something, then… yeah. Okay. I get it. Hey, look who showed up!
**Antoine Toulme** 52:58 Hey.
I ditched the operative seek for you all.
What buttons you are.
**Jason Plumb** 53:04 We already talked about your thing.
**Antoine Toulme** 53:07 Okay.
**Trask Stalnaker** 53:07 immersed it.
It's merged.
**Antoine Toulme** 53:10 Huh.
Gotcha, guys.
Alright, cheaters.
**Trask Stalnaker** 53:18 Anyway, I'm sure.
**Antoine Toulme** 53:20 Before you guys rise up on me and revert it? Okay.
**Jason Plumb** 53:24 Sorry.
**Trask Stalnaker** 53:27 So I've been having trouble with these, we've been having trouble with the branch protection rules because they have to be in a specific order.
They're order sensitive, which is really annoying. So I'm trying to come up with a better way, and I think I was testing it out. I broke contrib last night, sorry, Lori, with the EZCLA check, but I think I got it, fixed now, and so with using rule sets for the easy CLA protection, the fallback, then we can ditch … We can ditch the… Branch protection rule for it, which then we don't need to worry about the reordering, because that's the one that always causes problems with the reordering, because that one has to be last, since it's a catch-all.
Alright, … Anything? Anybody else? We've got 2 minutes left.
Any last topics?
Thoughts, opinions?
Alright.
See y'all next week.
**GZ Gregor Zeitlinger** 54:47 2….
**Robert Niedziela** 54:48 Leo.
