SIG: Ruby SIG
Date: 2026-03-17
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Kayla Reopelle 00:01:31 Hi, Arjun, how are you doing today?
Arjun Rajappa 00:01:34 Hey, hey, later.
Doing good.
Kayla Reopelle 00:01:39 Glad to hear it. Hi, Rob!
Robb Kidd (he/him) 00:01:42 Hello!
Kayla Reopelle 00:01:52 I'm about 2 minutes from my destination, where I can more thoroughly start the meeting.
Buhman.
Robb Kidd (he/him) 00:02:00 Nowhere.
Kayla Reopelle 00:02:00 If anyone else wants to kick things off and get there, please feel free to go.
Robb Kidd (he/him) 00:02:07 I don't feel qualified to kick anything these days.
Daniel Azuma 00:02:30 Hello?
Robb Kidd (he/him) 00:02:36 Hi.
Daniel Azuma 00:02:49 Sorry, trying to figure out my camera here.
There we go.
Robb Kidd (he/him) 00:03:01 Welcome.
To being visible.
Kayla Reopelle 00:04:47 Okay, thanks for everyone's patience. Sorry, that took me longer than I thought.
Let's see… would someone else be up for sharing their screen today, since they need to leave early?
Daniel Azuma 00:05:06 Or I can try doing that, if I can figure out how.
window… Shit.
Kayla Reopelle 00:05:36 Thank you.
So I don't have much of a spec sig update today. I went to the beginning of it, but then something else came up, and so… I wasn't able to stay. Was anyone else there, or… I mean, do we want to take a minute to look at the notes? I think we've got a decent agenda.
So we could go either way.
Robb Kidd (he/him) 00:06:10 Looks like we'll skim.
Kayla Reopelle 00:06:12 Perfect.
Daniel Azuma 00:06:21 Interesting. Anyone?
Robb Kidd (he/him) 00:06:34 I see comments about always record sampler and a tracer enabled that might affect things, and… Core?
Kayla Reopelle 00:06:44 Where was that?
Robb Kidd (he/him) 00:06:45 The third bullet on today's agenda from Carlos, one minute, FYI, a pair of stabilization terms.
In the spec sig?
Daniel Azuma 00:06:55 Oh, the specs here.
Through Bullet.
Robb Kidd (he/him) 00:06:59 Carlos 1-minute stabilization term, just from always recording.
Kayla Reopelle 00:07:02 What's happening.
Robb Kidd (he/him) 00:07:03 and Tracer-enabled.
Mixed mud.
Kayla Reopelle 00:07:06 I was there for that bit, and it just sounds like these specs have matured to the point where they have enough prototypes that I think they're going to move forward.
They'd be new features for us, but new features we should probably pay attention to for Core.
Tracer Enabled already has an issue that was made for it a few weeks ago, and, I don't think we have one for Always Record yet.
Robb Kidd (he/him) 00:07:30 Boop.
Context, scope, attributes.
It's good to want things.
Kayla Reopelle 00:07:58 Indeed.
Okay, well maybe… should we take a look at some of our other points?
Sure.
Schwan, I see that you added something for core?
Xuan Cao 00:08:19 Alright, yeah, basically, for the, examiners, now most of the language has the exemplars for the metrics, this update, is for the visual example about the implementation. As you can see, it… the trace and then the matrix is curated, and you can… based on the Grafana dashboard, For each metric, you can link to the trace?
And, yeah, this is just, iTempo.
So, hopefully you can get some, eyes on this, PR. It's sitting a long time, Kayla Reopelle 00:09:06 Nice, thank you. Those visuals were really helpful.
Yeah, it's been a while since I've looked at this, but, I had that as next up on my core PR reviews.
Yeah, I can look at this one this afternoon.
Okay… Any… any other points about CORE before we move into the… Points on contribib?
Robb Kidd (he/him) 00:10:07 Encore, Hispanic Conventions?
Kayla Reopelle 00:10:10 Oh, yes, thank you.
Robb Kidd (he/him) 00:10:12 a looming PR that I'll submit, that'll open today, that will change the templates For generating, Mostly around the doc comments for the yard documentation. I think the shape… the shape of the data structure of attributes and metrics, the deprecated key and the attributes and the examples key on those things have gotten more complicated since I initially wrote them.
or updated those attributes, for Weaver. Yard documentation looks weird. I'm going to simplify the template so that the yard documentation does not look weird. So it's kind of a minor update, because it's just yard docs. I don't even know if anybody reads the yard docs, but… It'll be… it'll be an update. And I don't know if that'll bump the set to do the release.
That you were trying to do?
Or if we'll still have… Kayla Reopelle 00:11:08 Yeah, I mean, I guess if we wait, because I don't think it's really time-sensitive, if you wanted to submit that PR and then include a reversion to 136 or whatever in, the version RB file, then we could… two birds, one scone it, and… just release that as part of the 137 updates, and I can go back and… Robb Kidd (he/him) 00:11:30 I'm not entirely certain of the details on that, but maybe I'll open the PR with just… it's okay, I'll open the PR with just the template update, and then, whoever. I'll leave it open to push from maintainers, or somebody can comment on the change that needs to be made to do the revert, and.
Kayla Reopelle 00:11:47 Okay, perfect.
Robb Kidd (he/him) 00:11:48 Happy to do that, too.
Kayla Reopelle 00:11:52 And yeah, just on the topic of semantic conventions, wanted to call out, I'm leaving it closed for now, but I have a… or draft for now, but I have a PR… to use Renovate to update the semantic conventions gem from here on out, like, once we catch up to the latest version. I do think we should probably do releases for the versions that have existed since our initial revamp.
But, yeah, but this should be available. So, if anyone wants to take a look at it in draft mode, it's here. I don't think it's gonna change a whole lot.
But, yeah, just waiting. It will only… release the latest version. Like, we can't get it to go back and release earlier versions, so no need to really open it until we're caught up.
Robb Kidd (he/him) 00:12:40 Okay.
I think all the more reason to make the template simpler.
Kayla Reopelle 00:12:47 Yeah, yes, right.
Robb Kidd (he/him) 00:12:49 As the shape of the data that's in the semantic conventions models seems to change, like, let's not include that stuff that keeps changing shape.
I might look for a way to link back from the generated code docs, like, the yard doc content to link back to official Semantic conventions. Like, if you would like to know more, it's over the… the actual source of truth's over there.
Kayla Reopelle 00:13:13 Yeah.
Robb Kidd (he/him) 00:13:15 Cool.
Kayla Reopelle 00:13:16 Cool, thank you.
Yeah, I can… Hop on this next one then, unless there's anything else for CORE that people want to chat about?
Daniel Azuma 00:13:37 But were there any other, decisions we had to make around the way that the release was gonna be handled for that?
Kayla Reopelle 00:13:45 Oh, that's right, the tiny, teeny versions was another thing that came up in Slack yesterday.
Robb Kidd (he/him) 00:13:54 I was calling them micro versions, because I think sometimes patch is called tiny, but fresh level of versioning.
I don't immediately know how the Ruby ecosystem will treat a fourth level, a fourth segment of version. Gem… like, the core Ruby gem version class seems fine with it, and will do… Kayla Reopelle 00:14:14 Yeah.
Robb Kidd (he/him) 00:14:15 Comparison math with it just fine.
There's not a… go ahead.
Daniel Azuma 00:14:19 Yeah, sorry, there are plenty of gems out there that have 4 levels of virtue.
Robb Kidd (he/him) 00:14:24 Okay.
Daniel Azuma 00:14:24 It does work fine, so yeah, I think it's fine.
Robb Kidd (he/him) 00:14:29 That is a pattern that I've used for, when I was doing more infrastructure work, and we would make packages of some other project, the other project had a version, and then… Our… the code that we would package that thing with would itself, like, we'd iterate on it, and we would have to produce a new package.
But it still contains the same upstream version.
That we would just put a fourth layer on there of, like, this is… Upstream version .1, which… that fourth level are the iterations we've taken to Fix our packaging and release of it.
It hangs together just fine, so we could document that the first three are the packaged semantic convention version, and then the gem itself has some iterations on it, because sometimes things get messed up and release, and you gotta, like… Update the release code, and do a new release, and you already burned a version number, so that's a way to manage it.
Yeah, it's an okay pattern.
Daniel Azuma 00:15:31 Yeah, I think it totally makes sense, yeah, especially, yeah, if we update the way that our, we express or document the semantic conventions or whatever in our generator, then yeah, that's… I think that, so the existing version comment, the release system assumes that that is the GEM version, not the semantic convention version. So I, I think if… I think it might make sense to have a constant that does all… that does represent the actual semantic convention version that we are using, so it's probably… we should probably have a separate constant, two constants, one for the JAM and one for the, Robb Kidd (he/him) 00:16:12 What upstream version are we tracking, and then what version are we on?
Daniel Azuma 00:16:16 Yo.
Robb Kidd (he/him) 00:16:16 Yeah.
Daniel Azuma 00:16:18 Yeah, so that would probably, alleviate the confusion that we have right now with, you know, do we update that version constant or not in the rake file?
Robb Kidd (he/him) 00:16:35 Let's maybe keep that separate from my template stuff.
Kayla Reopelle 00:16:42 Yeah, that's the template.
Robb Kidd (he/him) 00:16:43 So the template updates and the revert, just to get us back to, like, a clean state.
Maybe catch up.
Kayla Reopelle 00:16:52 Yeah.
Robb Kidd (he/him) 00:16:53 So that we're caught up.
We could tell Renovate to… then we could bring in the Renovate.
Kayla Reopelle 00:16:57 Yeah.
Robb Kidd (he/him) 00:16:58 Automation. And then we can consider, like, or, should we solve the versioning before we automate?
Ariel @arielvalentin (ATX, USA) 00:17:04 Updates. Rob, I was gonna say that, isn't that the schema URL?
Like, the version of the… Robb Kidd (he/him) 00:17:11 Version of the Fnatic Convention.
Ariel @arielvalentin (ATX, USA) 00:17:13 Should be refined.
schema URL, so that might be a separate… Okay.
Robb Kidd (he/him) 00:17:18 constant.
Ariel @arielvalentin (ATX, USA) 00:17:19 Versus the version of the gym itself.
Robb Kidd (he/him) 00:17:25 That's… yes. So, that's another reason why Daniel's idea is a good one to have somewhere, probably… I don't know that it needs to be a constant in the gym.
But… it does… that version, not the version of the gem, but the version of the semantic conventions that's being packaged, needs to be represented in the schema URL in The code that's produced.
So, so long as we've got that value of just the upstream version.
Whether it's used in the templates to produce the code that would have a schema URL represented, or it's a constant in the code that the schema URL is built with.
Implementation to be determined, but yes, that version, that's not the library version.
Is important to keep distinct.
Ariel @arielvalentin (ATX, USA) 00:18:23 May I derail the conversation into something related?
Robb Kidd (he/him) 00:18:28 Love derailments.
Ariel @arielvalentin (ATX, USA) 00:18:29 Which is, we don't have instrumentation scope attributes available yet, which includes the schema URL, That's something we're behind on.
It'd be nice to have that in.
Robb Kidd (he/him) 00:18:42 I think that there's work in flight?
Kayla Reopelle 00:18:44 Yeah, that's right. We had to table that. We reopened the old PR, and then… Things got really busy, and I didn't get a chance to look at it.
Ariel @arielvalentin (ATX, USA) 00:18:54 I think Robert Lawrence also opened one up, but I think he closed it all.
Kayla Reopelle 00:18:57 Oh, interesting. Okay.
I do think that would be a nice thing to add, especially before we remove our semconf opt-in environment variable.
For HTTP libraries.
Robb Kidd (he/him) 00:19:15 I'm willing to argue for time to work on that, if… I don't know that I am smart enough to do it on my own, though.
Ariel @arielvalentin (ATX, USA) 00:19:22 Why argue? You know, give it to the, you know, the robot clanker thing there, and, like, auto-generate this code. We don't have the markdown… agent's markdown and the prohibitions yet, right? Just… Robb Kidd (he/him) 00:19:34 We haven't prohibited it yet.
Ariel @arielvalentin (ATX, USA) 00:19:36 So, let's just crank them out.
Robb Kidd (he/him) 00:19:38 No, it's not just, I know a guy. I know a bot.
Ariel @arielvalentin (ATX, USA) 00:19:41 Yeah, no, no, it reminds me, we have to add the… the… sort of, like, suggested templates, the agents marked down, and the, Whatever other configurations that are necessary in the repo, you know.
People kind of agreeing on the one that's in the collector right now, so we might as well.
Kayla Reopelle 00:19:59 Hmm.
Ariel @arielvalentin (ATX, USA) 00:20:00 Bring that one over as well.
I keep putting all these things out there, like… Suggesting that I'm not gonna do… I'm just kind of putting it out there to find inspiration in others and inspire others to take these tasks on.
Robb Kidd (he/him) 00:20:15 Well, I'm, I'm, I'm interested, and it's, I think… I can get the time to work on this stuff. I don't know that I'll be able to work on it. I don't know that I'll be able to deliver by myself, but if somebody wants to… If somebody else is interested, and we can, if not pair, at least pay attention to each other's PRs. I promise to pay attention.
Ariel @arielvalentin (ATX, USA) 00:20:38 I am interested, because it directly impacts us, because we want to stay on older conventions, and so having the schema URL in there to allow me to downgrade attributes.
Robb Kidd (he/him) 00:20:48 To declare what versions you're… yeah.
Ariel @arielvalentin (ATX, USA) 00:20:51 So, I'm very interested in that feature being implemented.
Robb Kidd (he/him) 00:20:54 It's also pretty much a prerequisite to that scope-level attributes that.
Kayla Reopelle 00:20:58 Yeah.
Robb Kidd (he/him) 00:20:59 talked about at the SpecSIC.
Well, I'm willing to work on it, if.
Kayla Reopelle 00:21:08 Cool. I should have bandwidth to help out. I will be out next week, but, after that, I should be relatively stable.
Robb Kidd (he/him) 00:21:39 Ugh.
How does out debt work? I know that you all are just watching me flail in here.
Kayla Reopelle 00:21:46 We can start talking about the next one.
Robb Kidd (he/him) 00:21:49 Just please.
Kayla Reopelle 00:21:49 When you're typing. So, switching to our spec mocks, this was, like, a little… investigation into how OTEL likes to deal with fossil scan failures and licensing issues.
In addition to just the question about whether we want to use RSpecMOCs more fully.
For that first question, the licensing issue.
It seems like there's a process in place where we could submit, an exception, if we do want to use this library, we may need to submit an exception for some other things, too, like yard, but there still is a lot of ambiguity about, like, how much… Care and attention needs to be made to, like, test slash development dependencies versus dependencies that we actually ship with our code.
The other thing that was really strange is that when I dug into not only this package, which DIFLCS is the one with the GPL2 license.
But also RDoc and YardDoc. None of them actually had, like, strict GPL 2.0 licenses. I couldn't even find one at all in relation to… Robb Kidd (he/him) 00:23:02 I was looking at them, and they both looked… and they both… the yard looked like MIT, and I don't.
Kayla Reopelle 00:23:06 Yeah, fuck.
Robb Kidd (he/him) 00:23:08 The fossa would trip on it.
Kayla Reopelle 00:23:10 So that's, I guess, a different, you know, question that I need to explore, is just, why is it tripping on this at all? Because we may… we may not need to get an exception in the first place. I think diff LCS, which is the RSpecMox dependency, is maybe the only one that could have an argument, because it was originally… Robb Kidd (he/him) 00:23:30 Cross-licensed MIT… Kayla Reopelle 00:23:32 GOPT.
Robb Kidd (he/him) 00:23:32 two and something else, I think maybe commercial. There was a third, and they noted that it couldn't be pure MIT, because the implementation was, like.
Is a reimplementation of a… Kayla Reopelle 00:23:46 Yes.
Robb Kidd (he/him) 00:23:46 Perl slash GPL2 licensed algorithm.
So that oughta get a… we oughta be able to get a waiver.
But also, we don't redistribute it, so I think… No.
My opinion… having just looked at this yesterday, because I started commenting on the PRs and realized that I was kind of coming in ignorant. I started looking, too.
And… A challenge is that the FOSA tool uses GemfileLock, but the Gemfile Lock Like, doesn't really distinguish between development versus test requirements.
Kayla Reopelle 00:24:26 Mmm, Robb Kidd (he/him) 00:24:27 Whereas the gem file does, and when you bundle install, the bundle installation can be scoped to groups of gems, but… If this fossa tool doesn't care and just uses gem file lock and then follows that tree, it doesn't distinguish I need to learn more about the faucet tool.
Kayla Reopelle 00:24:47 Interesting, and… Robb Kidd (he/him) 00:24:48 and see if its support of Ruby could… Like, tell it not to care about development dependencies.
But I only just started looking at it yesterday.
Oh my god.
Kayla Reopelle 00:25:02 Well… Robb Kidd (he/him) 00:25:03 Happy to look and… Kayla Reopelle 00:25:04 Yeah, we already have a script, that, Arjun wrote, to help us with FOSA and, like, looking at the gemfile.locks, so I don't know if that could be tweaked, maybe we only install… You know, not our dev dependencies with that, or something.
Robb Kidd (he/him) 00:25:22 baby.
Maybe. It, it depends on whether… because, my glimpse at how Fossa looked is Fossa needs a gem file lock.
I don't know that a bundle install is required.
I don't know, I'll look, I'll learn more.
Kayla Reopelle 00:25:39 Yeah, yeah, check it out.
Robb Kidd (he/him) 00:25:40 But I couldn't figure it out.
Kayla Reopelle 00:25:42 She learned.
Robb Kidd (he/him) 00:25:43 And I have been… I have comment… I've gone on record as unconvinced that we ought to check the gem file locked in to appease the fossa scanner.
But I think the more I look into it, I can see the sense of that, so… The new maintainer that's joined us, who's had a bunch of work with the submitted a bunch of PRs to… to do the gem file lock check-ins.
And then making Renovate or Dependabot keep them up to date? Meh, I'm closer to being convinced.
I'm more… I'm… I'm less… I'm convinced that I was.
If that makes sense.
Starting to see the sense.
But yeah, I'll take a look, at… At what options we have to appease the fossil scanner.
Kayla Reopelle 00:26:32 Cool, thank you.
Ariel, do you want to roll in? I only got 5 minutes left, that I can chime into things on.
Ariel @arielvalentin (ATX, USA) 00:26:50 Sorry, is this for the contrib?
Kayla Reopelle 00:26:53 Yeah.
Ariel @arielvalentin (ATX, USA) 00:26:53 contribute.
Kayla Reopelle 00:26:54 The one you just added.
Ariel @arielvalentin (ATX, USA) 00:26:55 I do wanna… ask the crowd, though, that's here, because I don't think that's an open question for me, is do we want to actually expand our usage into RSpec MOX? I know we were using it in several places, or should we stick to using mini test doubles?
And… Not include another dependency on another gem.
I don't know… Kayla Reopelle 00:27:21 I was like… Ariel @arielvalentin (ATX, USA) 00:27:22 we were using, like, a mix of the two, and so I was like, okay, well, Allspract Monks is used more, so I had put together a PR to… Move them all over to make the Mini Test 6 test pass.
And then James followed up with some more.
some more PR, so… I wanted to get an opinion from the group.
Kayla Reopelle 00:27:46 For me, style-wise, I'm comfortable with either, as long as it's consistent, that just makes it easier to write the tests.
I think if we wanted to keep Minitest mocks, we would still have to add another library anyway, since it was pulled out of Minitest 6, and it's in its own separate gem now.
Robb Kidd (he/him) 00:28:04 Does it use DIFLCS?
Kayla Reopelle 00:28:06 I don't know.
Possibly? I don't know.
Robb Kidd (he/him) 00:28:11 We could sidestep the whole licensing thing if we, If we don't bring that in.
Kayla Reopelle 00:28:16 We could. And then we have the simpler questions to answer for RDoC and YARD.
I don't know… yeah, I don't… I haven't worked with RSpecMox in a really long time, so, you know, it's… it's something that I just need to adapt to regardless.
What do other people think?
Robb Kidd (he/him) 00:28:40 I don't have an informed opinion about caring about which one… I don't know which one would be better. Consist… I… I'm… without an… without using either, I would… my default would be, we should be consistent.
And… Use one.
So that's the best I got.
Daniel Azuma 00:29:05 I think likewise from me. My default for most things is to use Minitest unless RSpec is necessary. I'm not… Yeah, I'm not informed enough about our tests to know whether RSpec is necessary.
Ariel @arielvalentin (ATX, USA) 00:29:26 Okay, so I'm gonna see if I can run it through the clanker, and instead of doing the R-SpecMox one, we'll see if Minitest Mox gives me… you know, if Copilot knows how to regenerate everything with, mini-tests, and then… We'll compare the two, and… See how we want to move forward, I don't see a dependency on… Diff… what is it?
Kayla Reopelle 00:29:49 If LCS?
Ariel @arielvalentin (ATX, USA) 00:29:50 with LCS, so… that's, like, you know, plus points.
Robb Kidd (he/him) 00:30:07 Sure.
Kayla Reopelle 00:30:09 I… I should sign off. I'll watch the recording to catch up on everything else.
But, yeah, it was nice seeing everyone!
Ariel @arielvalentin (ATX, USA) 00:30:16 Don't forget to like and subscribe.
Kayla Reopelle 00:30:20 I shouldn't.
Ariel @arielvalentin (ATX, USA) 00:30:23 I guess that puts me next up on the conversation. So… this PR was opened up, specifically around Avoiding, or, like, omitting exceptions?
From… that are sort of, like, commonly raised errors, I guess?
That are part of the… some uses of Active Record. I don't know if you've… if you could follow that.
Yeah, let's follow this link. So, this, person just submitted this PR thing yesterday, and it was, you know, there's all these cases where, Spans are getting marked as aired.
But it's kind of like using… You know how Rails uses a lot of exception handling as flow and control?
And they feel that it's unnecessary to record these specific use cases as exceptions.
And, instead allow them to propagate through without an issue, and leaving the spark… the spans left as unset.
Right now, they're being set as aired.
Because of the way that the in-span helper works. InSpan will… rat… well… We'll handle any exception.
Append it to the span, and mark it as an error, and then re-raise that error.
So, if we take a look at what the implementation looks like… it's kind of, you know, adding this, like, allow, you know, this sort of allow list, I suppose, and then every time an active record operation is performed, it's gonna… Run through that list to see if there's anything in there.
It's gonna look at It's gonna look to re-raise the exception, otherwise it's gonna bypass it, and it's kinda like, oof.
This is gonna get sprinkled in a bunch of places.
And, maybe, perhaps, we should be rethinking, or changing the API that's available through the API gem for that helper, that in-span helper.
To say, like, hey, look, you're gonna… Allow for certain exceptions to be ignored.
When you're recording this, or don't record exceptions at all, just propagate them.
And let something higher on mark a… Our span is, As having aired out.
That's kind of, you know… kind of what's on my mind here, because I don't think that this is… It's good to sprinkle this around.
Instrumentation, specifically.
Robb Kidd (he/him) 00:33:46 I'm… hmm.
I'm coming cold to this issue, but having looked at the… Having looked at the issue that this PR is… trying to address. The concrete use case is coming from, Our friends at Mastodon.
Ariel @arielvalentin (ATX, USA) 00:34:04 Yeah.
Robb Kidd (he/him) 00:34:05 Who are looking at a trace.
Ariel @arielvalentin (ATX, USA) 00:34:08 Yup, where… Robb Kidd (he/him) 00:34:10 Subspans in the trace have errors.
Ariel @arielvalentin (ATX, USA) 00:34:12 Exceptions.
Yup. But… Robb Kidd (he/him) 00:34:14 The root span is successful.
And my, sort of, like.
Tracing Purist Heart says that recorded what happened.
There were exceptions in the lower-level child processes of this overall trace, but the overall trace succeeded.
Ariel @arielvalentin (ATX, USA) 00:34:34 Right.
But it also… but there's, like, 3 things that are, I think, coming to mind here.
One of them is, idiomatically, a lot of people are using exceptions for flow and control.
And so, it's like, they don't necessarily want to record the exception.
Because it's not really an exceptional case for them. It's kind of the regular flow and control, they're just using exceptions.
to… Moving to the next stage.
Robb Kidd (he/him) 00:35:02 ActiveRecord shouldn't be using this for phone control. It's where I go, but I know that… That's all.
Whistling in the wind there.
Ariel @arielvalentin (ATX, USA) 00:35:09 and we're automatically setting a span to an error every time an exception is recorded, which is not part of the specification, and not part of the API. Like, you can record an exception and leave a span unset.
As far as I understand.
And so I think one of the problems that's happening is that it's… Recording the exception and sending this ban as error.
through the in-span helper, which is making our friends at Macedon see the trace and be like, wait a minute, I've got all these errors that are happening in the trace, but everything is just fine.
And I'm not trying to propagate it anywhere, because it's kind of normal.
So, you know.
I guess I'm proposing, like, some of the options there would be, okay, we could tell them… Don't use the in-span helper.
Or, we make an adjustment to the in-span helper that's like, should you record… should you… Record a status?
Robb Kidd (he/him) 00:36:10 Treat exceptions as everything.
Ariel @arielvalentin (ATX, USA) 00:36:11 errors or something like that?
Right?
But then, you know, there's the nuance here of it saying, like, there's only specific errors in an allow list.
And do we have the… sort of, like, the hierarchy of errors, right? You know how ActiveRecord has its… air, and then there's, like, this tree of children, and it's like, well, one of the ancestors, or one of those an exception that I… Is that really the exception? Like, if this resulted in, not record invalid.
But rather, you know, statement invalid because of a, you know, Driver connection error.
Should that be marked as an error?
In that particular case, right?
I'm not coming here with answers, I'm just coming here with problems.
Robb Kidd (he/him) 00:36:59 Yeah.
Some options that I can spitball are a just straight-up bull of, Exceptions are exceptional. Default, true.
And then that would mean… A span is marked as error, if there is an exception.
And you could choose to set it to false.
If… If… and it's just a… there's no, like, allow list, in that option.
there's the allow list option, which could take Discrete exception classes, or… An exception class and its descendants.
Which… Involves a little bit of processing of iteration.
But, it's not… awful.
Or there's lambdas of… you give me, like.
if you… if you put how to treat exceptions, you give me a lambda or a proc, I will process that proc for a true or false, and… That's the handing the instrument or a footgun.
Actually, even end users who might not know that it's a footgun. That if you put complex logic into this lambda, you are incurring Compute cost.
Sure. Whenever… whenever things are happening, whenever exceptions are thrown, you will be… You will be responsible for making this performant.
As performant as you want it to be.
Ariel @arielvalentin (ATX, USA) 00:38:35 All options.
Robb Kidd (he/him) 00:38:36 It's the most flexible.
But the most fraught with peril.
Daniel Azuma 00:38:44 It seems to me that… Just philosophically, who… if, you know, we, we could… we could say, you know, as… as… as… as the OpenTelemers, we say, we have the opinion that, in general, exceptions are exceptional, or, you know, or something like that. We could… we could kind of put… put a foot down as an opinion, and… And say, well, yes, we understand that there are cases where, people do use them as flow control, but we consider that the exceptional case. And therefore, if you want to do that, then you sh… then, you should… then we'll give you the ability, you know, we'll give you the ability to do that for, those exceptional cases. So, I guess maybe I'm, I'm, I'm, I'm advocating for the, For the allow list. Because, I think that's a reasonable way to enumerate the exceptional cases. We would… We would once… real exceptions. Even if there's, you know, there's some… There are certain exceptions that, are used by, you know, record invalids, you know, for certain, for certain cases. There are also going to be other exceptions, system call errors and various things that you probably still want to see as errors.
So… so even… So even when there are those flow control situations, it's still going to be a minority of the exceptions that could be thrown.
So, it seems like we would want, a user, if they want to have those to handle those cases, that they should tell us, okay, which… You know, which cases, you know, here are the… Robb Kidd (he/him) 00:40:57 What exception types do you not consider exceptional?
Daniel Azuma 00:41:00 Yeah, yeah. God.
Robb Kidd (he/him) 00:41:02 I hate that I said that.
Daniel Azuma 00:41:05 So that's… that's why I would… I would… I would say do that rather than have… just have a Boolean, which would do all… all exceptions or no exceptions. Now, regarding your other idea of a lambda… Robb Kidd (he/him) 00:41:19 The lambda?
We've done it in other instrumentations, and I… and I… it's been a while since we talked about them, but I recall us sort of regretting it.
Daniel Azuma 00:41:28 Yeah, I… that… that seems… Overkill?
Robb Kidd (he/him) 00:41:33 For all of the reasons why you were hesitant in saying that, yeah, it is.
Daniel Azuma 00:41:40 Yeah, I… I don't know. Unless we can come up with a… what we think is a common Use case that the allow list cannot handle.
I don't think we… That's… Robb Kidd (he/him) 00:41:54 That's the thing, the Lambda's, like, we don't have to think, like, the Lambda's the… We don't have to think about it.
Right now. We don't have to address all the use cases of… future use cases that we can't think of right now.
One might come along, and then we're like, well, now we have to change the implementation somehow.
But I'm… I'm cool with an allow list at first.
Ariel @arielvalentin (ATX, USA) 00:42:17 Should that allow list be?
Instrumentation-specific.
And then… Handled by each instrumentation.
Or should it be, again, instrumentation-specific.
Passed in as an option to NSPAN.
Or… should Inspan be inlined in these use cases, and be instrumentation-specific?
Or should it be a global value?
That is configured on the SDK configurator.
And it doesn't matter which instrumentation is using it, the SDK configurator will… Kind of injective.
Robb Kidd (he/him) 00:42:59 My initial reaction to global is negative. I do not think that in… all cases of creating spans, you would want this allowless set.
I think. But that's, like, a knee-jerk reaction.
Ariel @arielvalentin (ATX, USA) 00:43:10 Sure, sure.
So it would… so it sounds like we're leaning more towards… Individual places.
Robb Kidd (he/him) 00:43:19 Implemented on in-span, and then instrumentations can choose to… in their use of InSpan, take an instrumentation-specific configuration Option.
And use that configuration-specific… that instrumentation-specific configuration option in their use of Inspect.
Ariel @arielvalentin (ATX, USA) 00:43:39 So, does that constrain… is that to be constraining on whether or not the exception is recorded as an event?
And the span is set to error or not?
Is it just… Sorry, because there's a couple options here.
Is the allow list saying… Bypass recording the exception, recording exception, and Keep the span unset.
Is it saying… Record?
the event, record exception, without setting the spam, Or neither.
Skip recording the event, skip recording the exception… setting the… the… the span status.
Daniel Azuma 00:44:30 The action there is… they… they probably still want to record something, because, you know.
Because these are, these are flow control, you still want to understand what's, you know, what happened.
Robb Kidd (he/him) 00:44:53 Why did it flow this way? And if you don't record the exception, that triggered flow.
Ariel @arielvalentin (ATX, USA) 00:44:57 Right.
Daniel Azuma 00:44:58 So events, but not… but not sets the… but not set it as error.
Ariel @arielvalentin (ATX, USA) 00:45:03 So, this code right here is explicitly saying, don't record the event, because it is handling the exception and returning it, as opposed to letting it flow through the in-span helper that records it and sets the status.
Robb Kidd (he/him) 00:45:19 So I'd want to… for myself, I'd want to go… I mentioned this in chat, I'd want to go re-read the hotel spec around exceptions, and recording them, and setting spam status relatedly to see what the hotel spec says. We should do… We should do what the spec says.
Or, I'll rephrase, we shouldn't do what the spec says not to do. We got some wiggle room to, like, if the spec doesn't… if the spec doesn't prohibit it, we can maybe make it more user-friendly. There's also a little bit of, once… once I get more clear about what the spec says, do and don't, or should or may.
Depending on the answer there, flows back to… backends ought to… interpret according to the spec. So… There's some negotiation there between… we should record what the spec tells us to record in the way that it tells us to record it.
And if that's resulting in an unpleasant experience in a backend.
Talk to your back-end maintainers, slash vendors, slash the copper.
Which, there's a whole bunch of unknowns, I don't know the answer yet there, but I would default to, let's go run these ideas I'm willing to go read the spec with these ideas in mind and see where I land after refreshing my memory.
Ariel @arielvalentin (ATX, USA) 00:46:48 I'm gonna read this to… I can read this, what is his, I could read this… Out loud.
An exception should be recorded as an event.
Should, not must.
On a span during which On the span during which it occurred, if and only if it remains unhandled.
Robb Kidd (he/him) 00:47:12 Should, if and only if, unhandled.
Ariel @arielvalentin (ATX, USA) 00:47:16 When the span ends, and causes the span status to be… sorry, remains unhandled, and when the span ends, and causes the span status to be set to error.
Robb Kidd (he/him) 00:47:30 I'm gonna have to read this.
Ariel @arielvalentin (ATX, USA) 00:47:31 Super… Super wordy.
Super wordy.
Robb Kidd (he/him) 00:47:40 Okay.
Ariel @arielvalentin (ATX, USA) 00:47:41 So… Robb Kidd (he/him) 00:47:42 Should, if and only if unhandled, when the span ends.
Ariel @arielvalentin (ATX, USA) 00:47:46 Nope.
Robb Kidd (he/him) 00:47:47 And causes the span status to be set to error.
Ariel @arielvalentin (ATX, USA) 00:47:54 Awesome.
Robb Kidd (he/him) 00:47:58 Causes… Ariel @arielvalentin (ATX, USA) 00:47:58 Spence.
Robb Kidd (he/him) 00:48:00 What causes the spend status to be an error.
Ariel @arielvalentin (ATX, USA) 00:48:03 But record exception does not set the span status.
Okay, those two operations are separate from one another.
Robb Kidd (he/him) 00:48:11 separate.
Well, I think it's useful to go and look at Active Record, or at least how this trace is playing out.
if user… in this case, it's user create bang.
calls… UserSaveBang, and user save bang is marked as having an error.
Ariel @arielvalentin (ATX, USA) 00:48:35 Yeah.
Robb Kidd (he/him) 00:48:36 does… I think user's safe. Bang.
Ariel @arielvalentin (ATX, USA) 00:48:42 So, from the instrumentation library's perspective, user-safe Bang is not handling an exception. It's raising an exception.
So, if I were to read this quite literally, it would say, we should be recording the event because the instrumentation didn't handle it.
Robb Kidd (he/him) 00:48:57 Nope.
Or, or… Ariel @arielvalentin (ATX, USA) 00:48:59 Sorry, the library didn't handle it.
Robb Kidd (he/him) 00:49:01 Yeah, the function… Ariel @arielvalentin (ATX, USA) 00:49:02 Yeah.
Robb Kidd (he/him) 00:49:03 function in this case, that… is being… that the span represents. By the time that function exited.
You hadn't handled the exception.
Ariel @arielvalentin (ATX, USA) 00:49:12 Yep.
Robb Kidd (he/him) 00:49:14 I think… Ugh.
Ariel @arielvalentin (ATX, USA) 00:49:18 So unhandled exceptions ought to be set to error, is how I'm interpreting this.
Robb Kidd (he/him) 00:49:27 There's always the, WWJD. What would Java do?
Ariel @arielvalentin (ATX, USA) 00:49:33 Here's the duo drop.
Robb Kidd (he/him) 00:49:34 It's just through the job.
Ariel @arielvalentin (ATX, USA) 00:49:35 Java code right here. You do try, throwable, record exception, sets fan status to error, and that's that. And there is no Java bang, there is no save bang in Java, you know?
Come on, baby.
No, what I'd be interested in is seeing what other libraries have done, so I wonder what other vendor-specific implementations have done to kind of represent this particular use case with ActiveRecord.
Robb Kidd (he/him) 00:50:04 I keep going back to the… The use case is that a backend is complaining about errors appearing in this trace.
Ariel @arielvalentin (ATX, USA) 00:50:12 I'm like, well, the collector removing them.
Say again? Sounds like the collector removing the… On setting the science.
Robb Kidd (he/him) 00:50:20 Or there's… you could do that.
Collector is where we pile all of our hopes and dreams.
Ariel @arielvalentin (ATX, USA) 00:50:25 Of course, right?
Robb Kidd (he/him) 00:50:26 We got corners to cut, let's get the collector to cut them.
Ariel @arielvalentin (ATX, USA) 00:50:30 Would you?
Robb Kidd (he/him) 00:50:35 Yeah.
I get the pain that, that… behind the issue that's being reported here.
Ariel @arielvalentin (ATX, USA) 00:50:45 Totally with you.
I'm not… Robb Kidd (he/him) 00:50:47 And I… Oof. Yeah, let's go take a look at what other, SIGs have done. What other languages have done in their… In providing options, and maybe that's, if there's a pattern growing across different implementations of this Problem, maybe it's time to talk about it.
Ariel @arielvalentin (ATX, USA) 00:51:03 When it comes to Old Tel.
Sikh languages, you know, I feel like there's, like, a little bit of a mix, because in Golang, for example.
Capturing the stack trace is super expensive, and often not helpful.
So, the record exception option has even got a thing like, record the stack trace, like, trace.with stack trace, so it omit the stack trace by default when you record an exception, which is kind of interesting, right? That's not what we do, we're like, we're unwinding the stack all the time.
So you're probably making things slower. But I don't think there's a lot of languages that are like, hey, do you have the same method, only one raises exceptions.
Versus another. So, I think that's just, like, something that's very specific.
to Ruby, unless there's another programming language that does something similar, you know? I was thinking more about, like, Lib Honey, and, like, New Relic Agent, and, like, Datadog, like, what did they do for their customer experience?
You know, what did, the AWS SDK do.
Robb Kidd (he/him) 00:52:09 Answering from the hip, we go… if you put an exception… if it raises an exception, then we… it's an error. An exception occurred, and you didn't answer.
Which goes down to, you're using a framework that is using exceptions for flow control. Why? But we're not going to convince Rails not to.
Ariel @arielvalentin (ATX, USA) 00:52:26 No, yeah.
Robb Kidd (he/him) 00:52:27 Whoa, whoa.
Which goes back to your original question, Ariel. Where… where's… if we were to put in an option, where does it go? Is it… Do we update… if it's Act… if it's Rails, or specifically ActiveRecord, who's choosing to use exception handling as fault control?
Do we just do something with the Rails instrumentation? And… Not make it.
SDK-wide.
I don't know, I gotta sit with this one. This is a good one.
Ariel @arielvalentin (ATX, USA) 00:53:06 No problem. Sit with it, please comment in the PR, or maybe we have a separate discussion about it, but I really could, you know, use some input from folks.
I don't want to accept this PR as is.
Robb Kidd (he/him) 00:53:20 I agree.
Ariel @arielvalentin (ATX, USA) 00:53:24 Okay, and I've, taken up so much of your life.
Robb Kidd (he/him) 00:53:28 I agree with that part. We should… we should figure out how to solve this.
I appreciate them.
Poking us to make us solve it.
Ariel @arielvalentin (ATX, USA) 00:53:37 Yo… Yeah, oh, so, some things to add that, did not come up. So, so far, I've had a very pleasant experience using the merge queue in Ruby Contrib.
And wanted to ask folks, maintainers in, The core repo, if they be amenable.
to adding… yeah, Arun is, like, I think it's, like, midnight where they are. Oof.
Robb Kidd (he/him) 00:54:06 Tonight.
Ariel @arielvalentin (ATX, USA) 00:54:06 Arjunamine, the… I'm wondering if we can add it to core?
Because the merge queue has been, like, pretty nice. It's like, you don't have to constantly be rebasing.
for, merging main in order for you to, get your PR merged, waiting for CI to complete, and so on and so forth. And, I wanted to get folks' take if there was any concern about… Robb Kidd (he/him) 00:54:32 I have to admit that I am ignorant to this merge queue behavior.
Ariel @arielvalentin (ATX, USA) 00:54:38 when you have a set of PRs.
Robb Kidd (he/him) 00:54:39 So I should withhold my opinion, and if anybody's like, yeah, it's great, we could have that conversation, or we could go off on a tangent and teach Rob what a merge queue is.
Ariel @arielvalentin (ATX, USA) 00:54:48 I'm happy to just discuss it, which is… because I… it wasn't my idea, it was James, that was like, let's use the merge queue, and it's, you know… I'm not trying to, like, shamelessly plug features that are in GitHub. But when you have a PR, And you can say, hey, merge it when it's ready.
Right? And then, what'll happen is… Robb Kidd (he/him) 00:55:10 Merge if it, like, it's got approvals, and if all the things pass, merge when it's ready, and then it goes into… Ariel @arielvalentin (ATX, USA) 00:55:16 And then it'll go until right… what happens pre-merge queue is that, assuming that it's in sync with main, it'll just merge it.
But if it's not in sync with the main, it won't, and require you to rebase.
or merge main onto that PR, and then start that, and then it'll run CI again.
Robb Kidd (he/him) 00:55:34 Is it… is NSYNC mean?
The current head of Maine is in your branch's history.
Ariel @arielvalentin (ATX, USA) 00:55:41 Yep.
Robb Kidd (he/him) 00:55:41 Okay. Not that there aren't merge conflicts, it's… Ariel @arielvalentin (ATX, USA) 00:55:44 Right.
Robb Kidd (he/him) 00:55:45 Okay.
Ariel @arielvalentin (ATX, USA) 00:55:46 And so when, if you put things into the merge queue.
GitHub is going to batch those all up into a temporary branch, merge all of those changes together, and then commit those onto main.
And so you're not waiting for CI on each one of the individual things.
for each sync to happen, it's gonna run CI across all of them, run CI in the merge group, and then say, oh, this worked well, and I'm just gonna… and I'm gonna merge it now.
And that has proven to be successful.
How's that merge?
Robb Kidd (he/him) 00:56:17 I guess I could go look at the history of… Ariel @arielvalentin (ATX, USA) 00:56:18 Yeah.
Robb Kidd (he/him) 00:56:19 Contribs… Contribs main.
Ariel @arielvalentin (ATX, USA) 00:56:21 Yep.
Robb Kidd (he/him) 00:56:21 Is that a merge commit of the… Is it, like, squash commits for the… do we squash commits? I can't even… it's been so long since I'd dealt with our… Ariel @arielvalentin (ATX, USA) 00:56:30 Yet, for an individual PR, merges are squashed, yes.
Robb Kidd (he/him) 00:56:35 Okay. For individual… Ariel @arielvalentin (ATX, USA) 00:56:36 R.
Robb Kidd (he/him) 00:56:36 And then a merge queue, taking, like, 5 PRs together.
Those would not be squashed for the… it's a merge commit domain of those 5 squashed PRs?
Ariel @arielvalentin (ATX, USA) 00:56:46 Yup. So if you want to take a look at what it looks like, you know, here's what the history looks like with all of these PRs merged.
And all those Renovate Bot ones were merged as part of a merge queue.
Which is, like… Pretty nice.
Robb Kidd (he/him) 00:57:01 Oh, not even a merge commit, then. It's just… Those commits are played. Okay.
Ariel @arielvalentin (ATX, USA) 00:57:06 Yes, yes, sorry.
Robb Kidd (he/him) 00:57:08 Oh, that's.
Ariel @arielvalentin (ATX, USA) 00:57:09 And so it preserves the history the way that you would normally expect to see it, is if each one of those PRs was merged independently.
Robb Kidd (he/him) 00:57:16 Neat.
And here I say I don't have an informed opinion, because I was just introduced to this feature.
Ariel @arielvalentin (ATX, USA) 00:57:24 hey, 5 minutes… turn it on in Honeycomb, man, you're gonna be… you're gonna make your life.
Robb Kidd (he/him) 00:57:28 It might be, I just haven't been paying attention.
Ariel @arielvalentin (ATX, USA) 00:57:31 Who knows? But if there's no objections, I'd like to try to get that enabled in May, which requires a couple of changes. It's like, we have to allow a new… Trigger.
right, a new, event to be accepted, which is called Merge Group on some of the CI jobs.
Especially the required ones.
So that they run during the merge group.
Second is changing something in Terraform.
to enable merge groups in the repository, and those would be two separate PRs that would happen.
And and then, you know, magic happens after that, right?
Robb Kidd (he/him) 00:58:12 What… why wouldn't we do this?
Ariel @arielvalentin (ATX, USA) 00:58:17 I don't know.
Robb Kidd (he/him) 00:58:18 Yeah.
Ariel @arielvalentin (ATX, USA) 00:58:20 You know? Cost savings, right? It's like, some people just like to sit around and watch the… You know… Watch builds go.
Daniel Azuma 00:58:28 Is there… so, what do… what do we need to do differently to merge a… to merge a PR.
Ariel @arielvalentin (ATX, USA) 00:58:38 Oh, nothing, you do your review, CI will run, you click the button that says merge, add to the merge queue, and it'll add it. And then GitHub keeps track of where that… of that intent to commit.
And if there's multiple PRs that are done together, it'll do them all at once.
Daniel Azuma 00:58:56 Okay, so, so it just replaces the button, text with, you know, from merge this now to add to merge queue. We press the same button, then.
Ariel @arielvalentin (ATX, USA) 00:59:05 Precisely, precisely. And you'll see that right now in… in the contributor bowl is Merge when ready, is what the label of the button is, and when you click it, it'll say, I'm queued to merge, and then it shows you a little icon, and you can click through to see it in the merge queue as it goes.
Daniel Azuma 00:59:24 Got it.
Robb Kidd (he/him) 00:59:25 Let's try it. Is there a way to arrange the PRs?
So that if something goes badly, we change our minds, we could revert and… be fine.
Ariel @arielvalentin (ATX, USA) 00:59:37 Arrange the PRs? What do you mean?
Robb Kidd (he/him) 00:59:39 Well, there are changes to be made to the repo itself, right?
Ariel @arielvalentin (ATX, USA) 00:59:43 Yes.
Robb Kidd (he/him) 00:59:44 Can those changes be easily reverted if we realize that We've made a horrible mistake.
Ariel @arielvalentin (ATX, USA) 00:59:51 Yeah, we have to go into… the Terraform repo, though, which is the OpenTelemetry admin repo.
Where those settings are managed now. You can't log in anymore as a maintainer and edit settings in the repo.
Robb Kidd (he/him) 01:00:07 Are the Terraform… do the Terraform changes require that we are doing merge Kiwi things? Like, could we tell our repo to behave differently?
Without making Terraform changes? Or, like, are the Terraform changes just allowing it to occur.
Ariel @arielvalentin (ATX, USA) 01:00:20 Herbert McGuire.
Robb Kidd (he/him) 01:00:21 it to occur.
Ariel @arielvalentin (ATX, USA) 01:00:22 Allowing it to occur?
Robb Kidd (he/him) 01:00:24 So, we can make the Terraform changes that allow it to occur, and then it's a matter of our CI configuration about whether it occurs, right?
Ariel @arielvalentin (ATX, USA) 01:00:32 No, sorry.
Okay. It's the other way around.
Robb Kidd (he/him) 01:00:37 Let's try it. Having heard about this feature today, let's try.
It's working in… in Contrib.
Ariel @arielvalentin (ATX, USA) 01:00:45 So far, have been successful.
Yeah. Okay.
Robb Kidd (he/him) 01:00:51 Maybe… Ariel @arielvalentin (ATX, USA) 01:00:53 time.
Robb Kidd (he/him) 01:00:54 Maybe… Maybe to get more humans' thumbs approving this instead of just this conversation, there's a… there's a PR we need to the repo, right?
Ariel @arielvalentin (ATX, USA) 01:01:03 Indeed.
Robb Kidd (he/him) 01:01:03 We can get thumbs and approvals on that, and then hold off merging it until the Terraform's been done, right?
Ariel @arielvalentin (ATX, USA) 01:01:08 Indeed.
Robb Kidd (he/him) 01:01:09 Let's do that.
Ariel @arielvalentin (ATX, USA) 01:01:11 Okay, friends.
We are at time, but it was… Look, I've not felt this much joy.
In months.
It is… it is really just amazing to see everybody.
I'm so happy to see every… like, I'm saying the same thing.
multiple times.
But, it makes me feel energized.
To see everybody on the call.
Robb Kidd (he/him) 01:01:38 Yeah.
Hoping to do more of it.
Ariel @arielvalentin (ATX, USA) 01:01:41 Yeah. I got a shameless plug.
Robb Kidd (he/him) 01:01:43 Okay.
Ariel @arielvalentin (ATX, USA) 01:01:44 If you decide that you want to come to Austin March 27th, 26th and 27th.
I will be talking about practical observability for Ruby.
Robb Kidd (he/him) 01:01:53 Okay.
Ariel @arielvalentin (ATX, USA) 01:01:54 And, we'll be shouting out this group of wonderful people that have been volunteering here and helping out.
Making this project go.
Please join us.
Make the trip, drive, fly, whatever, helicopter? I don't know what your… You know what transportation situation is?
Robb Kidd (he/him) 01:02:13 Oh, March, that's coming up fast.
Ariel @arielvalentin (ATX, USA) 01:02:15 Yeah, that's, like, 2 weeks from now. So, like, and I still haven't finished my slide deck.
Robb Kidd (he/him) 01:02:19 No one does.
Ariel @arielvalentin (ATX, USA) 01:02:20 So… Robb Kidd (he/him) 01:02:20 Until the night before, it's fine.
Ariel @arielvalentin (ATX, USA) 01:02:23 We're friends, you know.
I look forward to seeing y'all.
Killer.
If you actually watch this video, I want you to send me a DM.
And say, I watched the video.
Robb Kidd (he/him) 01:02:37 And I'm coming to Austin.
Ariel @arielvalentin (ATX, USA) 01:02:39 And you're coming to Austin.
Okay, my friends.
Take care.
Robb Kidd (he/him) 01:02:44 Bye!
Daniel Azuma 01:02:45 Right.
