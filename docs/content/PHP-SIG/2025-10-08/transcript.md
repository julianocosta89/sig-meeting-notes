SIG: PHP SIG
Date: 2025-10-08
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**Sergey** 01:52 Oh my goodness.
Well… Can you hear me okay?
**Bob Strecansky** 01:59 Yep, can you hear me.
**Sergey** 02:00 As well, yep.
**Bob Strecansky** 02:02 Nice.
**Chris Lightfoot-Wild** 02:06 Hello.
**Pawel Filipczak** 02:08 Hey.
**Bob Strecansky** 02:09 blue.
Well, hello.
We have a new face!
**MG Marylia Gutierrez** 02:17 Hello!
**Bob Strecansky** 02:18 Good morning.
**Pawel Filipczak** 02:19 Boom.
**MG Marylia Gutierrez** 02:29 Yeah, I'm here mainly to ask a question.
**Bob Strecansky** 02:33 Oh, well, we usually wait a couple minutes to start the SIG meeting, so, but the floor is yours if you want to start chatting while we're waiting for people.
**MG Marylia Gutierrez** 02:43 Yeah, so I've been working on the Clarity config, like, part of the group that has been creating, and yeah, I've been working, like, on the JavaScript, we have the Java, so right now we are just doing an update on, like.
current state for all languages, just to see how things are going. And I see the PHP has marked, like, on the… basically the compliance matrix, all of them fully compliant.
But at the same time, the issue that is, like, tracking what everybody is doing is showing that PHP is actually following the 0.4 schema from the configuration file.
But… and I was just looking for, like, is any, like, documentation that, like, how… if users want to start using, is it ready to use? And I saw just, like, this is how you start, but I could not find if it is really compliant with the latest release candidate, or…
Just, like, if people want to start using, it's good to go, or not?
Because, yeah, we're also planning to do, like, a blog post on updates on all of them, and I just want to also include PHP, but I don't know what to put.
**Bob Strecansky** 03:52 I'm sorry, which part of the spec were you hearing about? I couldn't really hear what you said.
**MG Marylia Gutierrez** 03:57 The declarative config.
**Bob Strecansky** 04:00 declarative config. I think it's still a work in progress, but people are more than, I think we're trying to keep up with this spec, but people are more than… we're more than happy to have people try it out and give us feedback, that's for sure.
**MG Marylia Gutierrez** 04:13 Okay. Do you know what… if… what parts are missing? Just because, like, the… yeah, the compliance, it, like, it got updated recently to show everything is compliant.
**Bob Strecansky** 04:25 I don't, I know Brett knows that, so if you could do me a favor, can you open an issue, and then we'll follow up internally and get back to you?
**MG Marylia Gutierrez** 04:34 No problem.
**Chris Lightfoot-Wild** 04:59 Maybe waiting around for Brett, Bob, or is he potentially not coming today?
**Bob Strecansky** 05:04 I was just giving a couple more minutes, but I think we… I'm assuming we have Quorum here. Does anybody else expect anybody else to come?
Alright, well, then let's, let's rip.
**Chris Lightfoot-Wild** 05:31 You know, Attendee, hello?
**Bob Strecansky** 05:35 Another new face
Alright, let's walk through the, open pull requests really quickly.
Alright, looks like it would depend upon thing. Chris, it looks like you got a SQLite 3 for test and contrib that depend on it?
Port requests that you have open.
**Chris Lightfoot-Wild** 06:03 Yeah, there's a one-liner, so hopefully, yeah.
**Bob Strecansky** 06:05 Okay. There's some dependency.
Okay, I think we can probably approve the… approve and merge this, so that's good. Thank you.
**Chris Lightfoot-Wild** 06:19 I guess the only bit, maybe for a future discussion, if Brett's around as well, but there's…
we've mentioned something called, like, Three Musketeers or something like that, like, development practice in our repo, that, like, the same code should be runnable in, like, local and the pipelines and stuff, but…
The images that… You know, make, test, use, aren't run in the pipeline.
So, obviously, it's all green in the pipeline, and then it comes to local test, and it blows up.
Maybe. Well… Hope for discussion, maybe, in future.
**Bob Strecansky** 06:51 Yeah, that's definitely an interesting topic about.
Alright, couple Dependabots.
Do you have any of context on this implement migration to component provider? Chris, looks like you started discussing this with them.
**Chris Lightfoot-Wild** 07:09 Yeah, I wasn't sure where that… I think they picked up on a comment on a separate issue, but then…
They were targeting at the V1 branch, and I've not heard a response back yet, so…
**Bob Strecansky** 07:21 Okay.
Keep our eyes on that one.
Let's see if I can tell us your color here is…
Those are just… Github Action Plops.
Why don't messing in here… Nothing with PHP prioritize backlog…
road test to KB2. I know Brett has discussed coming up with a plan for…
SDKV2, but I don't know that we have one quite yet.
Anybody have any thoughts on that? Chris, I think we were talking… we have talked about this previously.
**Chris Lightfoot-Wild** 08:08 Yeah, I wasn't aware there was any other blockers or things that should be done first, but obviously Brett's done most of the work there, so he was,
It would be good to sort of move toward using it, though.
**Bob Strecansky** 08:23 Yeah, I think you're right. I think we have to come up with a…
there's a plan of how to implement V2 more broadly.
**Chris Lightfoot-Wild** 08:30 I was obviously using SPI a bit more, and we're in a halfway house with V1, which is a bit confusing for people.
**Bob Strecansky** 08:38 Totally.
**Sergey** 08:41 But yeah, I think, I think…
May I please go ahead, Bob?
**Bob Strecansky** 08:45 Oh, I was just saying, yeah, I think we need to come up with an action plan for releasing V2, and communicating that it's a breaking change, and etc, etc.
**Sergey** 08:55 So, by releasing, we also will make V2 the main.
It'll become the…
**Bob Strecansky** 09:01 Yeah, I think… I think that's what we have to figure out, Sergey, I think.
we have had, you know, the V2 branch available for a little while. I don't know how many people have tested it, because it's difficult to test that, but I'm sure, like, we… eventually V2 will become main, and I think we have to determine
a process for that. I don't think that we… we obviously have not come across doing a major version release for the SDK yet. And I know Brett… I know Brett had thoughts about this, but I don't think he's really documented them anywhere. So, I think that we can…
Been come up with a plan and, figure it out, but…
It says I have to be today.
**Sergey** 09:41 Sounds good.
**Bob Strecansky** 09:44 Alright, we're up to 21 million installs of our API, that's very exciting.
And I think that's… let's take a look at the open issues…
Looks like we haven't had one opened in a while. That's a good thing, I think.
Alright, anybody have other agenda topics? Welcome, Samuel!
**Sergey** 10:13 Right.
**Samuel Arogbonlo** 10:17 Hi, thank you. I… I haven't part of…
Using hotel in my company. Anyways, for introduction, I'm Samuel.
I work with P2P staking, as a senior SRE engineer, so… We're moving away from…
VM… VM agent, vector, blah blah blah into OpenTelemetry.
So, I've been having some back and forth with the new changes, yeah, so I thought…
it would be good for me to be a part of these meetings, and maybe I might also have an opportunity to contribute to the building.
Excellent.
**Bob Strecansky** 10:56 You're welcome.
**Samuel Arogbonlo** 10:57 Thank you.
**Bob Strecansky** 10:59 Does anyone else have agenda topics that they'd like to cover today?
**MG Marylia Gutierrez** 11:05 Well, since I'm here, I can bring two other things related to things that aren't working, just in case it is useful for you all.
So yeah, I work in a lot of different stakes, so, like, I'm part of, like, the JavaScript contributor experience, database semantics, so for the database semantic, like, has been unstable since beginning of the year.
We have been… I've been kind of going also around, and just making sure people know how to implement, if they have any questions on the…
The migration, because we want to make sure that people have, like, at least a period of 6 months that is sending the old metrics and the new metrics, and then you can create a new version just with the new metrics.
So, also, if anyone has any questions, feel free to reach out to me. I'm always happy to…
Basically, answer questions in case nobody has any now?
And the other one is part of the contributor experience. We do have a survey that is every time a person that merges a PR with a new member who haven't contributed before, we put, basically, a survey just saying, like, hey, let us know how was your contribution.
And then I review those, and then I share back with the SIC.
And I noticed, like, the… so this repo doesn't have that. We do have that for about, like, 5 or 6 other repos. Is any interest that I add to this one? Because then I can add to this repo as well.
**Bob Strecansky** 12:36 Yeah, you can… feel free to… we have 3 rep… we have 3 repos similar to a lot of the others. We have the base repo, the contrib repo, and the instrumentation repo, so any or all of those will be…
We are very happy to have that.
**MG Marylia Gutierrez** 12:51 Cool, yeah, I can add to, all of them, the three of them, and then, basically, I wait to have a…
certain amount of responses, then I go back to the second share, just because I don't want to share, like, every single one, because it removed the…
Basically, the incognito part of it, but yeah, you might see me from time to time just coming here to share it.
**Bob Strecansky** 13:16 Wonderful, that sounds like a really great way to garner some feedback from new contributors.
**Chris Lightfoot-Wild** 13:24 Hmm.
The second point you made there, sorry, sounds like one of the things we've spoken about in the past, about not being entirely certain
How we transition between different versions of the semantics conventions.
You know, when things have been renamed, etc.
Yeah, I'm not sure if we went in the right direction or not with that, but if you've got insight into that, maybe that's one for me.
**MG Marylia Gutierrez** 13:52 So, basically, what you have to do, there is a environment variable that is,
what is the name? It's basically opt-in semantic measure, I can get the name here and share with you. So, basically, you have this for the HTTP and the database. Currently, those are the two…
Person does not set up this environment variable, you continue sending just the old metrics.
If they send, like, database dupe, then you send both, and if you send database, it's just the new one. So the idea is for you to have this flag.
let people know that this exists, like, through release notes, pretty much, and then at least let it be, like, this way for 6 months, at least, and then you can remove this flag, and remove the old metrics, and just send the new ones.
**Sergey** 14:47 Do you mean conventions?
**Chris Lightfoot-Wild** 14:49 Total.
**MG Marylia Gutierrez** 14:52 You might repeat it again?
**Sergey** 14:55 Chris, please go ahead.
another info.
**Chris Lightfoot-Wild** 14:58 I was gonna say, that sounds a bit more graceful than perhaps what we've done, because in the past, I feel like we've just bumped up the schema version in…
Any of the instrumentation packages and reflected the newer… I think…
**Bob Strecansky** 15:13 if I understand correctly, this is a relatively… New, right, Marlia.
**MG Marylia Gutierrez** 15:18 Yeah, so we have been doing this because we marked those two as stable. I think for the others, when it's, like, experimental and they keep changing between versions, I think people didn't care that much, but now that it's like, oh, it was…
we had, like, some big changes on it. A lot of, like, the main names have changed on the database one, so this is why we want to make sure that people have that… that chance.
**Chris Lightfoot-Wild** 15:45 So once we've decided we've also got stable
We're using the same… emitting the stable, keys.
We'd have to implement that as well, I guess, too.
Kind of, they can coexist for a while.
**MG Marylia Gutierrez** 16:03 Yes, correct.
**Chris Lightfoot-Wild** 16:04 Okay.
**Sergey** 16:06 While you described the way it works, you mentioned a couple of times metrics. Did you mean conventions, or actually metrics?
**MG Marylia Gutierrez** 16:15 Because, yeah, the convention has both, like, first span and metrics, so a couple… don't name the name changes on both of the things. We have, like…
If you haven't implemented, because there were, like, a few new metrics, if you haven't implemented those at all, you don't need the flag for them, you just add them.
But if you had it with, like, a different name, that is when you would need the flag.
**Sergey** 16:39 Okay, and you still use the same version of the conventions when you emit the data, regardless of the flag, or the flag affects also the version that you include in the data that you send?
The question is, on the side that receives the data, can it understand what conventions are being used just by seeing the versions that are attached to the piece of data?
**MG Marylia Gutierrez** 17:04 I'm trying to think if we send the actual version of this schema. I don't think we actually send the version.
**Sergey** 17:11 Because, if you think about it, like, if necessary, this is for the people to transition, right? But it will include also the backend.
So… so you… the way you described it, that it will only work if the backend will completely switch.
from old to new, just in one go, right? So, the backend itself will not be able to understand if the data is being sent, like, it will not work with the mix.
While some things still send old data, and other things send new data.
It will not be able to distinguish.
**MG Marylia Gutierrez** 17:41 Well, there would be, like, for example, if the person is adding the flag, they know that changes are coming, so this is why they can, like, for example, on their dashboards or backend that they use, say, like, okay, accept those two names for this dashboard. So this is why it's the transition period, that they can receive both and adjust their own, like, things to accept both names.
And then, at some point, the old one is gonna stop sending. But they will have control over that, because
It is the version of the instrumentation that they are using, so they know if gut drops or not, for example.
**Sergey** 18:20 It's just the problem will be that if they themselves have, like, a huge fleet of agents, and they transition them gradually, then…
It will be harder for them to understand, like, to distinguish just to use this.
all those dashboards for old data, and new dashboards for new data, it'll be harder, if I decide correctly.
Because the same version of the conventions will be marked in both cases.
**MG Marylia Gutierrez** 18:43 Well, the idea is that they would change their existing dashboard to accept both.
Right, so they would not have, like, a… yes, they would not have, like, a completely new dashboard. It's just, like, a transition, like, now also accept this name.
**Sergey** 18:59 So… so we never use the same name with different, meaning attached to it, so we always change names, so this way they can just adapt and have dashboards that can just use both names? Is that what you mean?
**MG Marylia Gutierrez** 19:12 Yeah.
**Sergey** 19:13 Okay.
I see. Thank you.
**Bob Strecansky** 19:28 Appreciate you, Marile. Thank you for joining today and giving us this insight.
Did anyone else have a…
**Samuel Arogbonlo** 19:43 Yeah, so I just wanted to ask, I mean, this is my first time joining a meeting like this,
Is this, like, an open conversation for any… anything entirely in the OpenTelemetry stock?
**Bob Strecansky** 19:58 Yeah, this… this meeting is specifically for the OpenTelemetry SIG… the OpenTelemetry PHP SIG group, so if you have questions about OpenTelemetry PHP, or you want to talk about
a pull request that you're working on, or if you want to talk about roadmap, or if you want to… you know, anything that pertains to the OpenTelemetry PHP subject interest group is fair game to discuss here.
**Samuel Arogbonlo** 20:21 Okay, cool, cool, cool. So, I… I just wanted to throw in again on…
Just a little part of what I mentioned before, of what I'm trying to build, and…
I realized that my gateway collectors in my stack, so I've got a full stack, gateway Collector, event collector, agent, target allocator, and my gateway seemed to consume lots of memory, right?
I even tried to, like, set up a soft limit.
Just to ensure that I don't lose data, but that's for a garbage collector now. But I realized that when it gets to the soft limit after a while, it begins to drop data.
And of course, that would mean that I miss out on metrics, and I miss out on logs. So, two questions, right? First of all.
Is it normal for the gateway collector to consume lots of memory?
because it does a lot of things, right? Processing, enriching the data, doing the multi-tenant separation, because in our setup, we've got multiple teams, and…
we have to find a way to drop data per teams, depending on the label and node selector and all of that. So, first question, like I said, is, is it normal to have very high memory usage? Or, let me say very, but high memory usage when it comes to gauge collectors?
And… If that is not normal, what are the things we have to put in place to, like.
avoid all of that. And…
Is OpenTelemetry very sensitive to issues with the backend? Issues with the backend, here I mean, low-key and VMetrix, because in our case, we ship the logs to low-key and ship the metrics to VMetrix, and then everybody gets to do it from Graphana.
So, I have been toiling with making changes, you know, and trying to spread traffic
through the four collectors, because I use 4 replica sets now. But…
it gets to 5GB, and then I hit the soft limit, because, I mean, it's crazy. Why do I have to run a collector that runs all the way to 6GB, you know? So, yeah.
I don't know if that makes sense.
**Bob Strecansky** 22:36 It does. So, yeah, the…
the collector is a different subject interest group. I can find out when they meet if you'd like to go there, but, the collector has a lot of really great configurable attributes to ensure that,
you don't drop… you don't drop metrics and logs and traces and spans. Some of the most important… some of the most important things you can do are making sure that you're sampling traces and metrics and logs, if that's something that you're willing to do, or allocating more resources for the collectors to ensure that you can
do that. The collector also has some really great metrics that are exposed that you can use to determine whether or not you're right-sized, or so on and so forth. This isn't the right place to give you, like, really good recommendations for the collector. All of our collector usage is surface level, right? Like, I've used it in my day job to be able to
send… just, like, have a place to send traces, but, yeah, the collector sign would be the right place, or the, OpenTelemetry Collector, Slack channel would be a really great place to ask questions there, too. They're very helpful.
**Chris Lightfoot-Wild** 23:42 I was gonna… one thing to add to that as well, when you said about the sensitivity of… the sort of default PHP, setup is fairly sensitive, because it's synchronous.
Although I know the Elastic guys here have got the async.
exporting mechanisms for their special transport, but if, like, your collectors are having problems, then the SDK will sort of retry
pushing… You know, exporting data out to it, which is blocking on the PHP side, by default.
So… That has an impact on the PHP side.
**Samuel Arogbonlo** 24:24 Hmm.
**Sergey** 24:26 Hey, if I understand correctly, the possible mitigation for that is to place a chain of collectors, right? One is close to the application.
And somehow you can ensure that it will be always available.
And then it will reach out to… I guess you called it gate collector? There's some kind of mode of gate, right, a collector has.
And you kind of, like, can,
stream data there, so essentially to use two hops instead of just one.
**Chris Lightfoot-Wild** 24:54 Nope.
**Sergey** 24:56 This is where you have to isolate your application from…
Any issues that your collectors will have.
Because you don't want to affect your production.
Just because your monitoring infrastructure is… It's not right.
**Bob Strecansky** 25:08 The OpenTelemetry collector, by default, is relatively light. I think it uses about 50 megabytes of…
memory at idle. I remember reading that not too long ago, and I know that that's… this is a common pattern, like Sergey was saying, like, as a sidecar to your application, rather than as, like, another application that you're sipping across streams, so that way you can sort of…
collect data locally, and then aggregate it with, via a bigger collector. Again, the, collector… the collector side channel is definitely the best place to learn more information about this, but, just giving you some, like, baseline information that we know.
**Samuel Arogbonlo** 25:46 Perfect, first, first, first, thank you. Will the recording of this meeting be available to the public?
**Bob Strecansky** 25:52 Yeah, it should.
**Samuel Arogbonlo** 25:54 Okay, please, I would want to go over it again. Thank you.
**Bob Strecansky** 25:58 No problem.
**Sergey** 26:00 Thank you, I'm trying.
**Bob Strecansky** 26:01 Yeah, thanks for joining.
**Samuel Arogbonlo** 26:04 Sorry, sorry, just one more thing. Is there a chance that I could be a consistent contributor on… because, I mean, OpenTelemetry is pretty new.
I would want to be part of the process with contributing, writing code, and all that.
**Bob Strecansky** 26:19 Sure, we would love to have you write code. Some of the best ways to get started, if you go to the OpenTelemetry PHP,
GitHub repo!
you can see in our issue… in our issues, we have, lots of ones that are, say, help wanted, or good first issue, or something along those lines. So those would be really great things for you to get your feet wet, start learning the codebase, ramp up your contributions, and then, from there.
You can definitely become a consistent contributor. That'll also help you to learn some of the, like.
ins and outs of the codebase. And if you have Questions while you're…
reviewing these, or you're not sure where to start, or if you need assistance, our open… our hotel PHP channel and the CNCF Slack is a great place to be able to
Discuss these issues asynchronously, and get help to understand what you need to do, and so on and so forth, so…
That's how you… that's how you become a contributor. We would love to have your contributions.
**Samuel Arogbonlo** 27:23 Okay, okay, thank you, thank you, thank you, thank you.
**Chris Lightfoot-Wild** 27:25 Let's joining the Slack channel?
**MG Marylia Gutierrez** 27:29 Hell.
**Samuel Arogbonlo** 27:29 Yeah, I'm on the selection a lot, actually.
**MG Marylia Gutierrez** 27:31 Yeah, and each repo, if you look at, like, the main page, all of them have a tab for contributing. Usually, that is the one that has, like, if you have any dependency when you need to run things locally, and…
things like that. Yeah. Yeah, it's gonna show, like, also on the README, like, you don't even need to click here. It's kind of like, yeah, it has a new tab, like, we added there. So yeah, this is also dependency you might want, if you want to just understand concepts in general, not specific to PHP.
We have a new channel that is OpenTelemetry New Contributors, then we have a few maintainers just checking that channel in case people are, like, a little lost on where to go. That is also a resource for you.
**Bob Strecansky** 28:15 I'm posting a link to… I'm posting a link to that in the,
Zoom chat now, so we have it.
Yep.
**Samuel Arogbonlo** 28:45 Okay, okay, okay, awesome.
Thank you.
**Bob Strecansky** 28:47 Spectacular.
Alright.
Meeting adjourned. We'll see you all on the internet.
**Chris Lightfoot-Wild** 28:59 Chill. Chill it.
