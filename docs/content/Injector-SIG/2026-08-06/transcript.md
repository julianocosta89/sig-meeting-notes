SIG: Injector SIG
Date: 2026-08-06
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Antoine Toulme (Splunk Inc.)** 01:22 Alright.
**Michele Mancioppi (Dash0 Inc.)** 01:23 Hey, Jay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 01:27 So…
**Antoine Toulme (Splunk Inc.)** 01:29 So…
**Michele Mancioppi (Dash0 Inc.)** 01:30 What is this rain tank incorporated that I see in your…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 01:37 hearing this. So, naming's hard, I guess, for companies. Have you ever seen, Hound Technologies, and Honeycomb people? It's like that type of situation, where it's like, Hound Technologies DBA doing business as Honeycomb Inc. So, like, Rain Tank is, I guess, the formal corporation. And then, you know, I think Grafana is either a child company, or the, like, the name that it's operating under.
**Michele Mancioppi (Dash0 Inc.)** 02:12 Oh, yeah, no.
**Antoine Toulme (Splunk Inc.)** 02:14 I did not know that. Thanks for explaining.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:18 Yeah…
**Antoine Toulme (Splunk Inc.)** 02:21 Alright, what you got today?
Let's do the same game we just did, Had the duck up…
**Michele Mancioppi (Dash0 Inc.)** 02:35 Look, you know what Antoine dropped on the packaging SIG?
You know what they did?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:40 No.
**Michele Mancioppi (Dash0 Inc.)** 02:41 He wants a package, system package, for the GMX scraper.
**Antoine Toulme (Splunk Inc.)** 02:45 Ayy.
Well, he didn't… I don't think Cector Jack commented on that issue back then at all.
I'm curious what you think, Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:56 you know, as a standalone thing, because, you know, it's… it's kind of problematic, right? Don't they want to kick it out of the collector?
**Antoine Toulme (Splunk Inc.)** 03:05 Oh, it's done. It's been kicked out of the collector.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 03:08 Alright, so it's out of the collector, it's kind of silly. It's bundled in with the Java agent, but it seems kind of silly just to, you know, instrument an app for the purpose of monitoring some other, JMX application.
So, like, you kind of… there's a lot of incentive to run it as a standalone thing.
**Antoine Toulme (Splunk Inc.)** 03:28 Yeah, that's why it's… it's… then the question's like, how would you make it easy for someone to do that with minimum amount of first, right? So… If you were to run this thing as a service on your box.
How would you go about it?
If I give you a Debian or RPM package for it, wouldn't you like that? Wouldn't that be helpful?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 03:45 Yeah, like, what's, what's the idiomatic way to package up, sort of, standalone Java applications? Because that's what this is, right?
**Michele Mancioppi (Dash0 Inc.)** 03:55 It's APG install. There is a JRE in main for Ubuntu and Debian, because there are other applications in main that depend on Java.
**Antoine Toulme (Splunk Inc.)** 04:07 Here we go.
So, we recommend that you install that. It's not mandatory.
Because maybe you installed JavaSMOs away.
We start the thing as a service, and there's a rich Java to pick whatever Java is around.
And we take a config file, or some service… the service file is going to take the configuration in some ETC folder, and load that up, and you're going to go connect to some place.
And you're going to assume that there's a collector nearby that has a 3417 open to send all the SLP data.
**Michele Mancioppi (Dash0 Inc.)** 04:41 It is the same, the same assumption that you have in the other system packages.
Since the collector is not yet part of the family.
Yeah, it's gonna be fun.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:54 So… There's a, I forget, I haven't done this in a long time. There's two ways that you can produce a, a standalone Java executable.
there's, GrowlVM, which you could explore, so bundling that up in Growl, or there's this other thing called, J-Link.
Have you heard of that?
**Antoine Toulme (Splunk Inc.)** 05:16 But, sir, no. Please.
**Michele Mancioppi (Dash0 Inc.)** 05:18 And neither are good, yeah, regulated industries, because of FIPS.
**Antoine Toulme (Splunk Inc.)** 05:23 No, just a shady job, we're good. I mean, we just want to take whatever is already published by the contrary people.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:30 I don't know, I'm just saying, the contrib repo, like, you know, it could… I'm not sure how much love that gets, you know? Maybe it's not doing it as well as it could, like, you know, it removes the dependency if you sort of can publish it as a standalone binary, a standalone executable, right? So that helps.
But either way, you know, I guess my… I don't have a negative initial reaction to the idea of having a package for that.
It seems kind of niche, I guess? It's like, it's niche and it's not, like,
**Antoine Toulme (Splunk Inc.)** 06:02 it's.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:02 You know…
**Antoine Toulme (Splunk Inc.)** 06:03 That much, because you guys removed the GMX receiver, like, there was a big effort from folks to say, this is disgusting, the collector is running Java to run a GMX receiver, to run a jar, to get the data.
And I agree, I don't like it, right? But now, what is the idiomatic way for people to do that without breaking the, you know, 3 hours of sweat of writing their own script?
Because they don't want to do it. They don't… people do not want to spend time on installing jars. They don't want to.
**Michele Mancioppi (Dash0 Inc.)** 06:33 It is an infinite pain on the backside to do all that setup, yes?
But, I mean, Jack, you used the word niche.
You know what was the second thing that Antoine said?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:43 Phillips.
**Antoine Toulme (Splunk Inc.)** 06:44 Oh, ugh.
**Michele Mancioppi (Dash0 Inc.)** 06:45 There is also the MQ tool something.
**Antoine Toulme (Splunk Inc.)** 06:51 But that is closer to my heart, right?
That is… Right now… the main thing I would like to make sure we do that for is that it would make it a bit more installable for people who have no idea how to use it. It needs to… It's really hard for people to try to use it today.
Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 07:10 I'll close.
**Antoine Toulme (Splunk Inc.)** 07:10 niche.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 07:11 Antoine, can you remind me, the JMX receiver has to be implemented in Java because it uses, like, Java serialization, right?
**Antoine Toulme (Splunk Inc.)** 07:20 Yes, correct.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 07:21 Alright, so, okay.
**Michele Mancioppi (Dash0 Inc.)** 07:22 There are libraries for that, but the amount of work to re-implement a GMX scraper, it's insanity.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 07:28 Right, right.
**Antoine Toulme (Splunk Inc.)** 07:29 Yeah, they just don't do it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 07:30 Yeah, because, you know, it just, like, it totally is a collector-receiver, like, in every way, except for what you just said, that, like, re-implementing it is insanity.
But, like, conceptually, it just makes sense as a collector-receiver. I just wonder, like, the, and we don't have to linger on this too long, but it's like, you know, putting it in Java Contrib isn't quite doing it justice, like, for, you know, sort of its relevance and the attention that it deserves, like.
**Antoine Toulme (Splunk Inc.)** 08:00 No, I don't know about that. Yeah, you tell me.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:03 I don't know, so, you know, I don't think the Java Contributory Poe gets that much love. Like, sometimes we forget to do a release of it, and, like, somebody has to remind us. And, you know, for comparison, we never forget to do a release of Java Core or Java instrumentation.
**Antoine Toulme (Splunk Inc.)** 08:21 Okay, that's understood. But I think that might actually help you… help change a little bit that stance, if you have more people using it, because it's easier to install, and you'll get more population of people who want fixes.
It's… it's such a little piece of software, like, compared to some of the stuff we ship, frankly. Yeah. Like, I'm not too worried about it, frankly.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:43 Alright, alright. I was just wondering if, like, you ever entertained the idea of having, like, a dedicated repository for it.
**Michele Mancioppi (Dash0 Inc.)** 08:51 Better and better.
This is getting better and better, later.
**Antoine Toulme (Splunk Inc.)** 08:57 No, I don't have… I don't have, I don't have the expectation that it should go and get its own. I think if someone cares about this, it would be Sylvain, the guy who's actually maintaining the JMX creeper, he's from Elastic, he's been working really hard on it. Yeah. But one thing he's done really well is that he's pushed up all the semantic conventions all the way to the Java Core repo, right? If I understand correctly.
It's been moving a lot of that around, and it started to use Weaver for the metric definitions of the scraper.
Jason plungeoned to me by Evan.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 09:30 I don't know what you're referring to with that, like, what's the… like, what semantic conventions have moved to core? I'm not sure what that's referring to.
**Antoine Toulme (Splunk Inc.)** 09:39 Okay, I'm not… I'm not sure. I think Jason mentioned something in passing to me that… When I built the IBM MQ Metrics thing in Contrib, I made sure to have a Weaver model that I use to generate Java code in the documentation of all the metrics. This way, I have some sort of a way to kind of articulate what it is we're going after.
It's kind of neat. And actually, that's a good reason why it's in contrary, because, like, the guy's like, this is a good way to build.
Use that.
And I think I've heard from, from Jason Plum that there was a similar effort around some of the definitions of all the metrics that come as standard.
For, for the scraper, because they're used in other places as well.
I'm not sure.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:24 I might have missed that.
**Antoine Toulme (Splunk Inc.)** 10:27 Yeah, I mean, I'm going by memory, so… Okay, so, anyway, Anything for today, for this Injector discussion?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:39 Oh yeah, the topic that we're all here for.
**Michele Mancioppi (Dash0 Inc.)** 10:42 Antoine, every week you come in, and you promise that you're gonna have an update by the end of the day about S390X.
**Antoine Toulme (Splunk Inc.)** 10:48 These updates, I have no updates, because those guys don't respond to me.
Thanks for reminding me that I need to go and tier a new one to someone here. It's just… Yeah, last ask is on the 3rd of August, asking, got an update.
from Jeffrey Sika, who's responsible for head of projects at CNCF and does not answer.
Let me ask again… Hey, folks over here are asking… So open up dates again.
Peace.
Next, next step for me is to ask for his, signal contact, and start to DM the guy.
And that's what I have.
**Michele Mancioppi (Dash0 Inc.)** 11:47 There's a little bit more going on. Diego is working on, the documentation for, the OpenTelemetry.
No, Diego's doing it for packages.
And Jacob asked for… to take it for the OpenTendra.io website.
So we should have, docs on the website at some point.
And I need to do some cleanup, when, the PR that, made, the version of the minimum version of the net runtime to Inject.
I misplaced the logic in the room module.
So there is some stuff that is, it works, but it's not kosher, like clean.
I'll clean it up.
**Antoine Toulme (Splunk Inc.)** 13:01 It's cool.
Alright, let's put that in the agenda, just some notes, right? So, still no news.
S39TX.
Diego is working with the packaging, so… Okay.
**Michele Mancioppi (Dash0 Inc.)** 13:22 is working for the Injector.
**Antoine Toulme (Splunk Inc.)** 13:25 Undie… On Python for the Injector?
**Michele Mancioppi (Dash0 Inc.)** 13:29 The documentation for the Injector.
**Antoine Toulme (Splunk Inc.)** 13:31 One of the conditions is used.
**Michele Mancioppi (Dash0 Inc.)** 13:32 I'll be able to do it.
**Antoine Toulme (Splunk Inc.)** 13:34 Okay, thank you.
And Okay, you wanted to mention something also. We had a revert this week about an upgrade of the Python instrumentation package, because it broke stuff.
**Michele Mancioppi (Dash0 Inc.)** 13:47 Yeah, that, that is very upsetting.
I spoke about it at length with Jacob. There is, I think, this is something that… it's not really Injector-specific. If anything, it feels more like packaging slash stable by default.
The problem is that the elastic folks have, Decided to discontinue an instrumentation packaging contrib.
**Antoine Toulme (Splunk Inc.)** 14:16 Cool.
**Michele Mancioppi (Dash0 Inc.)** 14:17 The, that has two issues. One… If you are using an old version of the Elastic Client.
You cannot get an updated version of the instrumentation, so you cannot have the instrumentation anymore. If you have an Elastic client without native instrumentation, you are locked out in the cold.
And, it breaks the entire, release train.
Python, because when contribute releases, it makes a new version for every single package.
And, the way that packages work, they pin specific versions of the SDK, So now you can no longer… have… you can no longer mix versions of Python instrumentation releases.
Because they conflict.
on the version of the SDK they're bound to. So that is an entire…
**Antoine Toulme (Splunk Inc.)** 15:18 That's the.
**Michele Mancioppi (Dash0 Inc.)** 15:20 That I believe we will, get into, through other language SIG as well.
This is one of the reasons why.
the work for automatic injection needs to have liaisons and joint ownership with Language 6.
Because if you live in the world of ppinstall, I can't imagine how you could think that what the Python SIG did is acceptable. If you live in the normal world of people that have great stuff, no, it's not.
**Antoine Toulme (Splunk Inc.)** 15:52 Hmm.
**Diego Hurtado** 15:55 Boop.
That's something I wanted to discuss. You mentioned about other language SIGs, this can happen anywhere else.
in the… in other packages, in other languages, can happen in Java, or… Or, I don't know.
**Michele Mancioppi (Dash0 Inc.)** 16:12 Never, never enough.
Java, not so much, because, like, 99% of the people are not using the contributor repo and the SDK, they're using the Java agent. And the Java agent is as monolithic a release as you can imagine.
**Diego Hurtado** 16:25 Okay, fairness.
**Michele Mancioppi (Dash0 Inc.)** 16:25 Every other language, it is a potential issue.
**Diego Hurtado** 16:31 So, the… There is also… Okay, the reason why, the people that Elasticsearch removed, just decided not to make any more releases of this, because they included, instrumentation in their own client.
Which is something some people want to do.
**Antoine Toulme (Splunk Inc.)** 16:54 Excuse me.
**Diego Hurtado** 16:54 In fact, some people in the OpenTelemetry project consider that to be actually the success of a measure of success for the OpenTelemetry project. What I'm trying to say is that there is A motivation for this to happen, which increases the risk for us.
this happening again. That's what I mean.
So I think we need a plan.
**Michele Mancioppi (Dash0 Inc.)** 17:23 I believe what we need is, is policies that should be structured around stable by default.
Right now, there is no consistency in the way that release trains happen.
between different language SIG implementations. Some are utterly broken, like the one of Python. Others, like Java, they never had a problem, because the delivery mechanism is… Fetally atomic.
**Antoine Toulme (Splunk Inc.)** 17:46 Yes.
**Michele Mancioppi (Dash0 Inc.)** 17:48 That is something that we should have better policies in the Lagnos 6 that work both in terms of upgrades and in terms of automatic injection. Otherwise, we feel the pain in the packaging.
An Injector itself.
**Antoine Toulme (Splunk Inc.)** 18:03 Besides…
**Michele Mancioppi (Dash0 Inc.)** 18:04 Yes, of course.
**Antoine Toulme (Splunk Inc.)** 18:07 How would you… how do we go about setting that tone in that discussion with the language SIGs? Do we… Do we want to go first to just talk about that with Python and just make it about Python, or is there a bigger discussion that we're not having? Is it a discussion for Tuesday morning? A Tuesday night for you guys?
**Michele Mancioppi (Dash0 Inc.)** 18:28 I believe that this belongs in the stable by default, so it's split in governance committee and technical committee, and then set down policies about what you are supposed to be able to do.
What is supposed to going to happen when you retire on instrumentation?
**Antoine Toulme (Splunk Inc.)** 18:46 Yeah.
So…
**Michele Mancioppi (Dash0 Inc.)** 18:48 The specific mechanisms, that they may depend on the language, but you should never leave users in the cold if they upgrade OpenTelemetry and not the instrumented library, because this is precisely what happened in Python.
**Antoine Toulme (Splunk Inc.)** 19:06 Discussion. Goodbye.
**Michele Mancioppi (Dash0 Inc.)** 19:07 People have reasons to pin, for example, specific versions of the Elasticsearch client.
**Antoine Toulme (Splunk Inc.)** 19:13 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:16 That implies that… You have to maintain instrumentation indefinitely, though.
**Diego Hurtado** 19:22 Mmm…
**Michele Mancioppi (Dash0 Inc.)** 19:24 necessarily.
**Diego Hurtado** 19:26 In the… in the sense that… the… The problem with, that we're having here is that, in theory, the Elasticsearch, instrumentation could just… Remove the strict requirements it has of… of other OpenTelemetry components.
So that other instrumentations that are still being upgraded can play along with it in the same… in the same environment, right?
Which is something the… That… It's fine. I mean, it, it should not break, because, the OpenTelemetry components themselves, right? That's the thing that we have under our control. It makes the least sense.
When it breaks like that. So… That's a… In the OpenTelemetry Python project, we, in my opinion, have been… Pinning dependencies unnecessarily.
So that we end up causing these problems.
Because… Either everything moves together, Or… nothing moves together, right? So… And that is a problem that we created for ourselves. We don't need this,
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:57 Yep.
**Diego Hurtado** 20:57 strict painting, which is something I'm gonna discuss with with them.
In 8 minutes.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:03 Yeah, so the Elasticsearch Python client has pinned dependencies on certain versions of OpenTelemetry.
**Diego Hurtado** 21:10 Exactly right, yes. It says,
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:13 And does it depend on components besides the API as well?
**Diego Hurtado** 21:17 Yeah, it uses… it definitely uses other packages, that are… that you… you could, logically consider them to be part of the API, right? It shouldn't be a problem. The problem is that it, it sets, A hard painter.
Which is, what's causing this issue. So… So yeah, I'm gonna, let them know that, and, And the least thing, the minimum thing, I'm not saying this is sufficient, but this is necessary, is for them to create a last new release of Elasticsearch.
Instrumentation that removes those dependencies.
So that at least we get a fix For this particular situation that we're having.
Yeah. Which doesn't mean it's the complete solution, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:19 Right, but just going back to what Michele was saying, like, originally, so, you know, no matter… you're saying something to the effect of, like, you know, let's say you're on any version of of the Elasticsearch client, even one that preceded their native instrumentation. You should be able to upgrade your, your OpenTelemetry Python instrumentation without being impacted. And that does imply that you need to maintain, instrumentation in the Python… in OpenTelemetry Python for that Elasticsearch client indefinitely, which I think is… which is in tension with, you know, the stated goal of the project, which is to proliferate, you know, native instrumentation everywhere.
**Michele Mancioppi (Dash0 Inc.)** 23:02 Yeah, I profoundly…
**Diego Hurtado** 23:03 Yes.
**Michele Mancioppi (Dash0 Inc.)** 23:04 the native instrumentation angle, because it sounds good, but it's entirely impractical. But the problem, the thing is, you don't need to maintain instrumentations forever. You need to provide an opportunity to keep the last one that works.
Because if the client doesn't change, the instrumentation doesn't either.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:24 I guess it depends on how you bundle up those instrumentations. Like, in the hotel Java agent, everything's monolithic, as we've talked about. So, like, you know, there is no way to maintain some old one and also stop publishing it. Those things are fundamentally in tension with each other.
But maybe in a situation like Python, where it's, like, you're not bundling all the instrumentations together in, like, a monolithic artifact, maybe there's something possible.
**Michele Mancioppi (Dash0 Inc.)** 23:50 I also.
**Diego Hurtado** 23:51 It is…
**Michele Mancioppi (Dash0 Inc.)** 23:51 I don't remember particular cases where the job agent dropped Instrumentations to the floor.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:58 You don't remember that?
**Antoine Toulme (Splunk Inc.)** 23:59 Mom.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:00 Well, so, like, the way that we would solve this isn't to, like, say that we can never stop dropping instrumentation. The way that we would solve this in Java would be, like, we're gonna wait for the major version, and then we're gonna drop the instrumentation.
**Michele Mancioppi (Dash0 Inc.)** 24:13 Yeah, fine, but that's a major version, right?
within 0.64B.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:20 Yeah, I think, you know, my opinion is very strongly that other languages should try to emulate the Java Agent's release strategy, which embodies, like, you know, the schedule, the use of SEMConf, all the things, so…
**Michele Mancioppi (Dash0 Inc.)** 24:40 And that, for example, what you said, also aligns with packaging, because the moment that… you drop a new major release, we cut a new version of the packaging interface. Now it's OpenTelemetry Java 2.
And then, the migration, with breaking changes in terms of your coverage.
It's something that you need to opt in specifically.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:01 Yeah, so it's like… it's almost like Python, misinterpreted SEMConv. Like, so there's like a… there's a contrast between how the packaging SIG interprets SEMConv and what you're allowed to do in a minor version, and what Python interpreted that it was allowed to do in a minor version, and they disagree with each other.
**Diego Hurtado** 25:19 Sir, what do you mean, Jack? I don't…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:22 So Michele was talking about how, you know, you know, if the Java agent were to drop an instrumentation, we would do so in a major version, and then the corresponding Java package that, the packaging SIG publishes would publish a new major version in lockstep, so everything would be consistent.
Like, you drop the instrumentation in the Java agent major version, and, you know, you bump the Java package major version as well, and everything's fine, because, you know, users expect breaking changes in major versions. But in Python, something different happened, and, you know, in a minor version, Python stopped publishing an instrumentation, which, which the packaging SIG… the packaging SIG mirrors the Python's versioning strategy, and the SIG is looking at this, this removal of an instrumentation and saying, like, hey, this is a breaking change. So there's a disagreement about what you're allowed to do in a minor version.
**Diego Hurtado** 26:15 None… I mean… What happened is that the… The instrumentation did not get a new… Release.
**Michele Mancioppi (Dash0 Inc.)** 26:30 Yeah.
**Diego Hurtado** 26:31 And, And that's… that could have been perfectly fine.
That would not have caused this issue if it wasn't for the fact that, the… that… every instrumentation has a hard pin to another OpenTelemetry component.
It doesn't really matter if… It was, they are using, Mayor… Or… a 1 as the first number, or a 0 in the first number? It would have happened the same.
What I'm trying to see…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:15 Yeah, no, I get what you're trying to say, and I think there's a… I think there's probably… those are, like, two different ways to solve it, and so, like, one way to solve it would be, like, Python never stops publishing an instrumentation in a minor version, so it only… it always waits till it bumps to a major version. And the other way, which I think is more permissive, which you're describing, is, like, the… Python Elasticsearch client instrumentation, Could, before it stops publishing, make sure that it publishes with permissive pins.
Right? Without pinned dependencies, so that, like, it could continue to be used, you know, with other Python versions that, that did not match it, right? So it didn't have that conflict.
**Michele Mancioppi (Dash0 Inc.)** 27:59 That, the latter one, While technically workable.
creates a huge amount of confusion on the end user side, because when you see that your PPAD crate is upgraded, all the packages in lockstep, except that one.
Then you have a major WTF.
And then you need to go and look up, okay, why didn't this upgrade?
How do you figure it out? It's not going to be in the last package, so… where do you find it out? As a user, are you going to think to go and look at the OpenTeleNetry Python contrib, or at the notes of the SIG and find out that that is no longer published instead of being a bug?
I mean, one is better for the end user than the other.
**Diego Hurtado** 28:46 Well… Well, I gotta go to the Python SIG, but…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:50 as well. But yeah, I think there's a conversation here about just, like, open telemetry-wide, like, what the mechanics are, what you're allowed to do in minor versions for these instrumentation bundles.
**Michele Mancioppi (Dash0 Inc.)** 29:01 Yep.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:03 Alright, see ya.
**Diego Hurtado** 29:03 For two, boogie.
**Antoine Toulme (Splunk Inc.)** 29:06 B.
