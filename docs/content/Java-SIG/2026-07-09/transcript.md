SIG: Java SIG
Date: 2026-07-09
Duration: 38 minutes
============================================================

## Zoom Recording Transcript

**Jack Shirazi** 02:14 So.
We are in one position to manage it from 0 s. We do need more contact with you.
Let's see.
**Trask Stalnaker** 02:28 Hey, folks.
**Bruno Baptista** 02:36 Hello.
**Jack Shirazi** 03:05 If this is this without.
I don't know, I wouldn't And there's just a little bit of a layer of not transition in the Philippines.
Yep.
**John Watson** 03:18 Hey, Jack Shirazi, you have a hot m.
**Jack Shirazi** 03:20 And so now we'll consider for me transitioning to you, Ms. Adam. Thank you.
**Jason Plumb** 03:34 Day. But here is Emily Fang reports Iran and the Us. Are.
**Trask Stalnaker** 03:41 Well, let us… Start with… The three oh.
Release status… Where's far from I just would take… Oh, yes, yes, I saw this. I think we will be able to… I think once we mark them all as deprecated, then this will be covered by… removing deprecated code.
I left it open.
Because I just opened this… PR… yesterday… To deprecate Config.
Properties, and… the last two… Places I found… Now… I remember… Gregor, we had… We discussed this before, that we're not going to kind of force everyone into declarative config in…
**Gregor Zeitlinger** 05:17 All right.
**Trask Stalnaker** 05:18 3-0.
And so we bumped this, but I'm actually… Wondering, like, I think we… that doesn't… I'm not sure that means we can't remove These still in 3-0.
**Gregor Zeitlinger** 05:35 And I think you're right.
We're not taking anything away if we remove that, because you can still get the values.
**Trask Stalnaker** 05:45 Okay, great, great. Just wanted to make sure I was not — How does this, how does this work?
No?
Refresh… There we go.
Okay, cool.
So… I'm going to actually mark this PR as… closing this issue.
And then actually removing the code is covered by the other issue of removing deprecated code.
**Gregor Zeitlinger** 06:32 You mean remove it now?
**Trask Stalnaker** 06:35 No.
I mean that the actual, Well, I won't do this. That'll be confusing.
What I was going to do is… says this… No.
**Gregor Zeitlinger** 06:55 You mean at the deprecation comment?
**Trask Stalnaker** 06:59 yeah, so removing support once they're all deprecated.
Like, here, this is covered by… Remove deprecated code. Right, right.
So I'll wait till I merge that PR later. I saw that Laurie already reviewed it.
Yeah, this one, still running just some, Copilot queries to… Find… Places where maybe it's not… completely following the semantic conventions. I have a couple Minor edge cases around batching that, I will… Still, finding… So I'm gonna leave that one open.
But I think hopefully by next week's meeting, this one will be closed.
And then our release will be… the final 2X release will be The week after that.
**Gregor Zeitlinger** 08:26 Trask, did you see that I re-tagged some of the… Frio, PRs to, 2.30, we did that last week, and you weren't there. Just wanted to make sure that you saw that.
**Trask Stalnaker** 08:41 Oh, OK. Let's see.
Okay.
Great, yes, I've looked at this for… yeah, I've looked at… These… these two… Need approvals still, Sylvain, probably if you have a chance, I think you were reviewing this one already.
And… I don't know who wants to… Bless.
Looks like Lori was… Looking at this one.
Cool.
And I'm not seeing any more of the invoke dynamic… Issues here… does that mean that they're… Yeah, what's the status there?
**Sylvain Juge (Elastic)** 09:41 Yes, so there is one PR because like this view is filtered on issues. So there is one PR.
**Trask Stalnaker** 09:47 Oh.
**Sylvain Juge (Elastic)** 09:48 To modify documentation.
And I think a few others have been moved to 2.30, because it's about, like, removing and migrating, Methods.
**Trask Stalnaker** 10:04 Okay.
Switch… okay, this is the doc PR, okay, great.
**Sylvain Juge (Elastic)** 10:08 Yeah, it's the dock and like switching it by default, which means it would be used most of the time.
**Trask Stalnaker** 10:17 This.
Oh, oh, I understand. Yes, yes. Can we switch it?
by the… can we switch it by default under the V3 preview?
**Sylvain Juge (Elastic)** 10:29 Yes, this is what this VR does. And but it's a bit hackish because, we need it quite early.
So…
**Trask Stalnaker** 10:40 So we can't call our regular…
**Sylvain Juge (Elastic)** 10:44 So I managed to do it, but it's not very pretty.
**Trask Stalnaker** 10:53 So does that mean we can merge this… For 2.30?
**Sylvain Juge (Elastic)** 11:05 Yeah, I think so.
Minus the fact that the documentation, refers to, like, 3.0, I think, so…
**Trask Stalnaker** 11:15 Okay, maybe… maybe split it into two PRs?
One for the code change that we can merge in 2.30.
And one for the documentation that we would wait for 3.0.
**Sylvain Juge (Elastic)** 11:34 Okay, maybe. I'll check that, so.
**Trask Stalnaker** 11:42 It would be nice… yeah, I like this idea that the last 2X release is mostly, like, if you run it in V3 preview mode.
It's pretty much the same as 3.0.
wherever we can.
OK, cool. It looks like there's — Let's mark this.
as… 2 30.
2, 30.
So, a virtual usage checker by… This field usage checker is Laurie. No, Laurie.
Yeah.
Oh, yes, the last thing I wanted to do.
Let me bump. I'm going to go ahead just so I don't forget.
Bump to 2, 30.
Gregor, a question related to that discussion we had before about declarative config.
About… not forcing people into Declarative Config in 3.0.
There were… I remember Lori mentioning there were some things that we deprecated, maybe that we… Could undeprecate? Should undeprecate? Do you remember this?
**Gregor Zeitlinger** 14:47 I do, yeah,
**Trask Stalnaker** 14:49 Do you happen to know, remember, remember what those were?
**Gregor Zeitlinger** 14:55 Just a second. I can look it up.
**Trask Stalnaker** 15:04 I can make a note. We can do that async if — It's… all of that.
**Gregor Zeitlinger** 15:11 I already have it. It was really just a second.
Config properties util.
**Trask Stalnaker** 15:21 Oh, yes. Properties, util.
**Gregor Zeitlinger** 15:29 I don't remember if we had a conclusion. Laurie, do you remember?
**Trask Stalnaker** 15:36 Laurie's not. Oh, he's.
**Gregor Zeitlinger** 15:38 I'm not on the call.
**Trask Stalnaker** 15:39 Yeah.
**Gregor Zeitlinger** 15:46 So there are arguments for and against, but I have to recollect, I don't have it at the top of my head, what my final verdict would be.
**Trask Stalnaker** 15:57 Yeah, yeah.
**Gregor Zeitlinger** 15:57 Opinion, then, Just feel free to do so, because there are arguments either way.
**Trask Stalnaker** 16:04 Okay.
Let me open an issue so we don't… Get… Last, oh, let's put that actually in the three on the issues.
It's confusing the issues labeling them as 3.0, but really we should try to get it into I guess, and deprecate doesn't — yeah, that's fine.
Yeah, I…
**Gregor Zeitlinger** 16:45 And that's not.
**Trask Stalnaker** 16:47 Correct.
**Gregor Zeitlinger** 16:48 It's not necessary for 3.0 because it's not going to affect Anyone, materially.
**Trask Stalnaker** 16:57 Right, right.
You had… Oh, yes, for distros, you had, for example, a PR… And maybe this is… Slightly beyond, but it's sort of related to 3.0, because we… The… Yeah, the… Right.
Yeah.
I don't know if you're… Prepared to kind of talk through this.
Let's add this to later on in the agenda. We can come back as a dedicated topic.
how distros support both.
Anything else for the 3.0 release?
That either I'm missing or that anybody wants to raise or ask about?
**Bruno Baptista** 18:26 Yeah, I have a question.
So, I wonder if we could include the… the removal of Jackson from the exporters as well.
**Trask Stalnaker** 18:51 So, let's see… We don't have Jack here, but this has… Looks like this has very good support, so I would tentatively Guess that this will be in the next… Next week's… a week from tomorrow's release?
but, I would… Defer to Jack and John here.
**Bruno Baptista** 19:22 Okay.
**John Watson** 19:23 I think that we should plan on this going in.
I think Jack is planning on doing the release. He's got plenty of approvals.
**Trask Stalnaker** 19:34 Which would mean, as long as it's… Bruno, as long as it's in… This month, or next month's SDK release.
Then it will be in the 3.0 next month.
3.0 instrumentation release.
**Bruno Baptista** 19:51 Okay, okay.
That's what I would like to have, yes.
**Jason Plumb** 19:57 The agent still has Jackson dependencies though, right?
**Trask Stalnaker** 20:03 Yeah, but Bruno, Bruno is, Quarkus is using.
**Jason Plumb** 20:06 Yeah.
**Trask Stalnaker** 20:08 Yeah, yeah, not using that.
And those are… Shaded and hidden and.
**Jason Plumb** 20:15 Yep.
**Trask Stalnaker** 20:15 Yeah.
Cool. Let's move on to Sylvain's topic.
**Sylvain Juge (Elastic)** 20:28 Yes. So, a while ago, we got a few PRs and issues related to trying to validate JMX metrics.
And so the main issue is they are not being defined in semantic conventions. And in the past, it was not possible to use Weather with different registries, but we now have the ability to aggregate multiple registries.
I started opening a PR.
to do two things. So, first, to, like, generate a kind of local registry for JMX metrics directly into instrumentation, where most of the metrics are being defined, and then to apply the weather. So whenever we run integration tests to capture JMX metrics, just use the weather live check validation just to make sure the metrics are working properly.
So doing this, I already managed to find one inconsistency in, JVM metrics.
Where, like, the unit was just off.
Yeah, it was a counter instead of, like, an up-down counter.
And so I was wondering, like, what are your thoughts on having like kind of YAML registry as part of instrumentation? Should it be in a separate repository or.
Or what are your thoughts generally about this?
**Trask Stalnaker** 21:49 I love it, and I think it should be.
Co-located with the instrumentation.
Same, or…
**Jason Plumb** 21:58 on to that. Yeah.
**Trask Stalnaker** 22:00 We could potentially, if we wanted to have a central place in this repository.
would make sense also. I haven't thought too strongly, but we can definitely land it in this location For now, and as we evolve, if we find that it would be better to have a central folder in this repo, we could do that.
Because there are some shared… there's definitely some shared things in this repo.
**Sylvain Juge (Elastic)** 22:32 No.
And so, one thing that could be somehow confusing is… It tends to overlap quite a lot with all the integration tests we have about the metrics, because we mostly check, like, what is the shape and attributes of the metrics.
So, it applies similar tests, but one thing that we can't easily do with this, at least not without splitting in multiple registries, is Dealing with different versions.
Because, for example, like, for Jetty, for, like, I think it's for Jetty 12 and Jetty 9, we don't capture exactly the same metrics, so it means maybe we'll have to split in the registry in two sets of metrics, and only load the relevant one for testing.
Whereas in… integration test, we can easily implement a switch and assert different metrics.
**Trask Stalnaker** 23:24 Now, different… Do you mean, like, attributes present in the same metric?
Or actually — because I wouldn't expect different metrics to be a problem as long as the YAML was a superset.
**Sylvain Juge (Elastic)** 23:42 Yeah, I think in this case it's like different metrics for J.
**Jason Plumb** 23:50 So why is it a problem to have both versions defined?
Oh, yeah.
**Sylvain Juge (Elastic)** 23:55 Okay, so basically the way the weather is being used, so it generates the result as a very large JSON that we can pass. And the test is basically asserting, okay, here is a list of all the metrics we expect, and we expect to have all of them, just to be sure we cover everything.
Cool. Maybe to mine, I'll.
**Jason Plumb** 24:15 Yeah, for the test, for the automated test generation.
**Sylvain Juge (Elastic)** 24:18 Exactly. So if there is, for example, like a registered metric that is part of the registry but is not being reported, it could be considered to be an error. But maybe it's something we can improve later on.
**Trask Stalnaker** 24:35 I see. Now, is that part of Weaver, that it automatically Expects all of the metrics to be there, or that's something that… Kind of, you've encoded in here…
**Sylvain Juge (Elastic)** 24:49 Yes, so this is something that is coded, here, because So, basically, the assertions, in order to make it a bit generic, say, okay, like, everything that starts with, like, a prefix, for example, like tomcat.something, should be, like.
both defined in the registry and we should have values being reported for them.
Which, I'm not sure of how it will go, because, for example, like, for some metrics, I think for Kafka, we are not really able, like, to produce, so, to produce those metrics, but we can always register them.
**Jason Plumb** 25:23 Seems like maybe, like, an over… like, having kind of a customizable override, or… do you have a sense of, like, how many… cases of these version problems exist? Is it, like, a dozen?
**Sylvain Juge (Elastic)** 25:37 Maybe a dozen, yeah.
**Jason Plumb** 25:39 Yes.
**Sylvain Juge (Elastic)** 25:39 That much, yeah.
**Jason Plumb** 25:40 And maybe just, like, having a way to, like, sort of manually override or manually customize those.
**Trask Stalnaker** 25:48 And did you… let's see… oh, okay, so it is integrated into the existing Test.
**Sylvain Juge (Elastic)** 25:56 Yes.
**Trask Stalnaker** 25:58 So we run… I was just… Thinking whether that it's important to… But… Validate the… that all the metrics are present.
Since the tests do have validate, do validate the specific metrics that we care about, I assume.
But the Weave… adding the Weaver live check is… sort of… I'm thinking of that as just being layered on top of the… our existing tests.
That just ensures that all the metrics that are omitted conform to the YAML.
**Sylvain Juge (Elastic)** 26:43 Yes. And it also ensures that we have the proper registry and semantic convention for the metrics we report.
**Trask Stalnaker** 26:51 Yeah.
Yeah, yeah.
Yeah, so I'm not sure how important It is to do the… for it to be the complete.
Set.
And maybe we might be able to relax that.
If it helps.
**Jason Plumb** 27:11 It's pretty nice, though, because it also helps to verify that we don't have definitions that aren't real, right? That there's not just, like, fluff in the YAML.
**Trask Stalnaker** 27:21 Yeah. Okay.
True.
Yeah, I guess maybe for other… Yeah, sure.
I like it.
**Jason Plumb** 27:36 I think this will make Anton very happy too.
**Trask Stalnaker** 27:45 Cool. Yeah, yeah, no, this is really, this is really cool. I would love to see how this, you know, how we can extend this to other all of… basically all of our experimental metrics.
And that might be a path for us. Right now, we hide a lot of things by default.
behind experimental flags.
A lot of, like, framework-specific attributes. Basically, anything that's not in the semantic conventions.
We hide behind experimental attribute flags.
So, like, the courts… Job name came up, on a recent PR.
And that's a great attribute to include by default.
But since it's not in semantic conventions, our policy has been to hide it behind an experimental flag.
And maybe we say.
As long as we define it in… Our semantic conventions now in this repo, that would… Give us a path to, Emitting some of those by default.
**Sylvain Juge (Elastic)** 29:04 Yeah, that's exactly the idea. So, for example, for JMICS metrics, I was thinking about Having a single toggle, where instead of saying which system do we want to capture metrics for, just to say, I want to capture all stable metrics, or all stable and experimental metrics, and then We would automatically get all the metrics we can instead of having to define which metrics sets do we want to enable.
**Jason Plumb** 29:27 It's, like, depending on what end beans are available, or.
**Sylvain Juge (Elastic)** 29:30 Exactly.
**Jason Plumb** 29:30 Yeah, yeah.
So this is a little bit off topic, but our agenda is fairly light. But was there some guidance around like bridging existing metric systems into OTEL and like whether or not those should have semantic conventions? Am I just making this up?
Like, was there some, like, spec-level guidance around bridging?
**Trask Stalnaker** 29:54 I'm not sure if it ever got in through a PR, but there's kind of a de facto issue that — or a de facto comment from Jack that I could probably dig up somewhere, but it was basically saying that we shouldn't try, like, it was around, like, the Kafka ones.
**Jason Plumb** 30:15 Yes.
**Trask Stalnaker** 30:15 We shouldn't… try to… define… You know, we should just bridge if it's from another metric system.
but I… And we could have done the same for JMAC, But we're… this is more… I see this as less a bridging of all… like, we're not bridging… we're not… taking all JMX metrics.
**Jason Plumb** 30:45 Right.
**Trask Stalnaker** 30:46 We're… this is kind of like a curated…
**Jason Plumb** 30:50 Right, but if you just pick one of the systems, like Tomcat, right, we are kind of bridging Tomcat metrics into OTEL.
I mean, kind of.
**Trask Stalnaker** 30:58 A very limited set of them. Yeah.
**Jason Plumb** 31:00 And so for that, I mean, I like having these semantic conventions here.
But, you think in that case, then that's how you kind of… Why it's different than the Kafka ones is because it's not just like blanket bringing over everything. It's.
It's custom and explicitly desired.
Metrics.
**Bruno Baptista** 31:23 There is another case, so the micrometer matrix, we have a bridge for it.
**Jason Plumb** 31:28 Mmhm.
We do, and we don't have any semantic conventions to find for those Unless they happen to be the some existing ones like heap.
Okay, this is cool.
**Sylvain Juge (Elastic)** 31:50 Thanks.
**Trask Stalnaker** 31:51 Yeah, definitely.
Let's… Move on and talk a little bit about Gregor.
Maybe you can, kind of… Give us the overview of… what you've been… Experimenting with for supporting both.
of these at the same time in distros without, I know, without having duplicative paths.
**Gregor Zeitlinger** 32:27 Yeah, sure. Should I just share my screen, show how it's working?
**Trask Stalnaker** 32:34 Yeah, that'd be great.
**Gregor Zeitlinger** 32:44 Can you see my screen?
**Trask Stalnaker** 32:47 Yeah.
**Gregor Zeitlinger** 32:49 Okay, so I think maybe I have renamed the class already and the PR, but the mechanics is the same.
So you have an object and then you say what default values you want to have. And by default, I mean if the user is going to override it using a system property or in the YAML file.
then they have the power to do so. That's why it's a default value.
And this is a syntax that is leaning towards the declarative config shape.
And that is.
to have a common feel with the instrumentation with the Java agent repository, where we have also use the declarative config API as the common API, regardless of whether you actually use declarative configuration under the hood.
**Trask Stalnaker** 33:55 And so, I think one of the… the main thing I was confused on the… that PR… Was the declarative config grid.
I… that one, I thought we were hoping to… remove and… only have the… One bridge.
From… basically, from…
**Gregor Zeitlinger** 34:26 Yeah, you're right. Declarative Config Bridge was the first Iteration of the bridge, which, made you, use the old syntax, and then we got the new one that makes you use the declarative config syntax.
But this is, yet another bridge because it is, Doing the bridging the other way around.
So it's not reusing the first one.
**Trask Stalnaker** 34:56 Oh, I see, it's just… it's reusing that existing module.
But not… it's not realiving the bridge there. Right.
**Gregor Zeitlinger** 35:08 Yeah, and if the location is in question, then we can just put it somewhere else.
**Trask Stalnaker** 35:15 Okay, I missed that. Thank you.
**Gregor Zeitlinger** 35:21 Yeah, I think I don't need to share more, because this is really giving you how it's used.
**Trask Stalnaker** 35:34 There was one other… Yeah.
PR might help to related. Let me put it in.
or I can share… This one… from a… Let's see… Okay, this one wasn't related to declarative config groups, this was related to… Basically, being able to have custom… Mappings. Distros to have your own custom mappings.
**Gregor Zeitlinger** 36:25 Right.
**Trask Stalnaker** 36:29 Okay. And, have you… Needed this… I saw it.
**Gregor Zeitlinger** 36:42 Okay.
**Trask Stalnaker** 36:43 Bob.
**Gregor Zeitlinger** 36:45 It's been a while since I looked at it. It looked fine, but cannot answer you any more specific questions about it.
**Trask Stalnaker** 36:53 Yeah, yeah, yeah. Let me just ask, Okay. I… It makes sense to me, it makes sense why you might… Need that, I think. I just want to make sure we have the actual… actual need for it.
**Gregor Zeitlinger** 37:23 -Hu.
**Trask Stalnaker** 37:26 Cool. I think that… Makes sense. We are out of topics.
Anybody… Anything they want to discuss?
Otherwise… Let's get some time back.
**Jason Plumb** 38:00 I'm okay with that.
**Gregor Zeitlinger** 38:02 Okay.
Have a great weekend.
**Trask Stalnaker** 38:05 Forever.
Bail.
**Jason Plumb** 38:07 There you go. Thanks everyone.
