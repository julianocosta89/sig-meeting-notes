SIG: Python SIG
Date: 2026-08-20
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 01:40 Hello.
**Tammy Baylis** 01:45 Hey Riccardo, how you doing?
**Riccardo Magliocchetti** 01:58 Hey, Tammy. How are you doing?
**Tammy Baylis** 02:03 I'm okay, thanks. I got, got quite sick a couple weeks ago. Something was going around where I live, but there's, A lot of sore throat and coughing, and I'm… Mostly better, yeah. How was… how was your time off?
**Riccardo Magliocchetti** 02:22 The time off was great. The comeback to work was traumatic, though.
**Tammy Baylis** 02:30 Yeah, welcome back!
**Riccardo Magliocchetti** 02:33 Thank you.
Week.
Two weeks away from the computer, it is.
He's a thing.
**Tammy Baylis** 02:44 Yeah, it, it changes you biochemically, I think.
**Riccardo Magliocchetti** 03:30 Welcome, everyone, to this week's Python Code. We're waiting a few more minutes for more people to join.
And in the meantime, please add yourself as an attendee to the notes.
And also, if you have any topics you want to discuss… Also, admin, thank you.
Still not topics… Could be a short one, just the edging, maybe?
Okay, wait a topic.
I think it's you, Lukas, about the Oracle Deep Instrumentation.
Yes.
Good.
Okay, welcome again.
I guess we can start. I don't say it would be a bit late.
So, Tammy do you want to do the… Triage, please?
**Tammy Baylis** 05:58 Yeah, I'll go ahead and do that.
sharing… window… Ryan, okay.
Hmm… So… Right, this board, default has some good sorting now, and I really like the updated labels that start popping up, which is nice.
We'll start… we'll stop at around 9-10, we do have some topics.
Hmm, PR55.
Drop the protobuf dependency… I missed the last couple. I don't know if there are any talks about, pure Python protobuf, but, lots of good context here from Diego.
Right, and I think for a moment earlier this week, just everything was failing.
There's no… Issue… There's a lot of good info here.
Stock of PRs.
Is Diego here right now?
No.
Header says it's a draft, but it's not a draft anymore.
I think it'd be good…
**Diego Hurtado** 07:49 Oh yeah, that's fine. Sorry.
**Tammy Baylis** 07:51 Oh, hello! Hi, Diego.
**Diego Hurtado** 07:54 Is this ready?
**Tammy Baylis** 07:55 for review?
**Diego Hurtado** 07:57 No, because it's… Oh, CI is failing, right, on that PR. I was just working on that this morning.
I gotta fix the CI, but once it's, It is, it'll be ready for review. This is the topic that we have been discussing.
The last, few weeks about, removing the protobuf dependency.
I'm doing this in 4 PRs, one by one, first removing it from the OpenTelemetry Proto component, then from the… the common component for exporters, and then from the exporters themselves.
**Tammy Baylis** 08:37 Okay.
**Diego Hurtado** 08:37 Yeah, in fact, Yeah, you can make it a… mark it as draft, for the time being, until I fix the… the CI, and then I'll… I'll mark it as ready for review when… What is this?
**Tammy Baylis** 08:54 Awesome.
Exciting.
Thank you.
**Diego Hurtado** 08:57 students.
Alright.
**Tammy Baylis** 09:03 Remove packaging as a runtime dependency.
Oh, haha.
**Diego Hurtado** 09:08 Oh, yeah.
Yeah. Same idea. I'm trying to remove, dependencies, I have not yet had, a chance to… investigate the ideas people had on this PR, on how to make, Essentially, vendoring, more convenient.
So, yeah, I'll do that, and I'll let you know. I'll let you know when it's… In fact, you can make… mark it as draft as well, because it still needs, me too.
Just to get that, thank you.
**Tammy Baylis** 09:46 Thank you.
Feature to add opt-in attributes. Cluster name, vHost.
To the PICA instrumenter.
Neither is in the SEMConv yet, but there is… Oh, they didn't create an issue, nice, thank you.
There's no PR for the SEMConv yet.
So I'm wondering… I'm wondering if there should be a PR for the SIMConv issue first.
Before we start review of this one.
**Riccardo Magliocchetti** 10:49 I guess there's, like, another comment.
**Tammy Baylis** 10:53 Okay.
**Riccardo Magliocchetti** 10:53 London. Lipia.
**Tammy Baylis** 10:56 Thank you, Riccardo.
One more minute, fix SQL alchemy, safely handle garbage collected, dark… I think I've seen this one.
Is this for the flaky test? Yes.
Pie, pie!
As usual.
And so, if I remember correctly, they were trying to change the source code.
Okay, well, I will say it's ready for review, there's a linked issue.
Yeah, I think… Can take a look.
Oh, one more. Just do one more.
Django Add Code Attributes disband.
Right, I commented on this one… So the issue… that is trying to be fixed was created 4 years ago. It's an older issue.
It happened way before we started, stabilizing the logging API and making the logging instrument more reliable.
And… Yeah, I've kept… I've kept it as no status, because I wanted to gauge current interest, because, of course, whenever new code's introduced, it has to be taken care of, and I'm wondering if… if what the logging instrumenter writes as its attributes that do, adhere to the SEM conv, I'm wondering if that's sufficient, instead of having to add more features to… the Django instrumenter, so that'll stay as no status for now.
Okay, that's enough.
Triage for today… Stop sharing, and back to you, Riccardo, for… the minutes.
**Riccardo Magliocchetti** 13:21 Thank you, Tammy.
Okay, first topic from today is Lukas Oracle DB instrumentation.
**Lukas Hering** 13:33 Yeah, Just for, just for some context, so I created this package, kind of, for my own personal stuff. I ended up using it at my employer.
For Oracle DB. I was kind of surprised it wasn't in Contrib already.
And then, Pablo ended up reaching out that, he also is looking to use this.
So, I just wanted to discuss if we're open to moving this into… Contribute.
I kind of… I probably shouldn't have… I probably should have used another name for this, because I'm probably gonna have to yank the version so that the… the beta versions resolve correctly. But, I should be able to… I can coordinate with either Leighton or whoever has access to the PyPi account to get this sorted out.
I will say this is, like, it's just a trivial wrapper around the DB API, basically. But some other folks at Oracle that I chatted with, that they're actually looking to contribute and expand this to support stuff like, server side tracing on the Oracle DB, so I thought… so we kind of said, okay, we can probably try moving this to contribute. Yeah, Riccardo?
**Riccardo Magliocchetti** 14:58 Well, since you work at Oracle.
**Lukas Hering** 15:01 Yeah.
**Riccardo Magliocchetti** 15:01 Has it been discussed to add net instrumentation to the client?
**Lukas Hering** 15:07 I actually… so the… The team that brought it up to me… I… I actually didn't bring that up.
I'm not sure what kind of what they're, so I, so they, they did mention that, so, so Oracle, the newest version of the client has, like, callback support, so you don't need a monkey patch anymore.
I think they still want to have it as a separate package, so, I mean… We could discuss with just having, like, this live, or… Are you thinking more, like, we want this to be… Maybe owned by… Oracle, like, maintained by them, I could discuss that as well.
**Riccardo Magliocchetti** 16:04 What? No, no, this is, like, this is the question you have to… to ask, but, like, I think this… Maybe popular enough that it would be handy to have it.
and contribute.
Bye.
**Lukas Hering** 16:17 Yeah, that's what my thought was, also for just general backwards compatibility for existing clients, but…
**Riccardo Magliocchetti** 16:29 Diego?
**Diego Hurtado** 16:31 Right, well… I mean, if your intention is to move it into Contrib, My particular opinion is that it's fine, as long as, There's a maintainer, which, in this case, obviously, could be you.
Have you considered to… add, native support for OpenTelemetry.
Oracle, instead?
**Lukas Hering** 17:01 Yeah, that's what Riccardo was saying.
**Diego Hurtado** 17:04 Oh, okay, oh yeah.
**Lukas Hering** 17:05 I can explore that a little further, Yeah.
I'm not… I'm, like, I mean.
where I am in at Oracle is I, like, I'm not really, I don't really touch the databases side of things side of the world, so I'm a little disconnected there, but, Yeah.
**Riccardo Magliocchetti** 17:29 Yeah, I guess it's a completely different team, so yeah. Or just, like, more a curiosity one time.
One request, of course.
**Lukas Hering** 17:38 I guess, yeah, I mean, just temporarily, at least, like, if you look in the code, it's, like, literally one file, or, I mean, it's… it's… it's one file that… is, like… You know, basically just… Using the DB API, so…
**Leighton** 18:02 Yeah, Lukas, I'm totally, totally okay with adding this to contribute. I think, if you can start off another workstream to kind of just maybe plant the seed for, native support, and like, if you need any help with that, like, that would be the ideal, but could be a separate workstream.
And just from the contributing guidance, yeah, if we… if we have you as a maintainer of it, as well as you as a component owner.
I think it covers all the, the, I guess, the thresholds of, allowing us to be in Contrib, so… Just a small suggestion, if… I guess because a lot of us aren't… familiar with Oracle that much. If you can kind of, like, port the simplest version of it, or, like, whatever you have, and then we can release it, and then your colleagues can start contributing, that would be the ideal… Order of operations, does that make sense?
**Lukas Hering** 19:10 Yeah, yeah, that's, that, yeah, that was my original plan.
**Leighton** 19:17 Cool. Yeah, yeah, we can get this through for you as soon as possible.
**Lukas Hering** 19:22 Yeah, I guess a quick question for Riccardo, since… since you've done the Elastic instrumentation, do you have the API as a hard dependency in Elastic, or do you have a separate package?
that… Is injected, you know, via callbacks or something.
**Riccardo Magliocchetti** 19:41 I haven't done that, but it's a self-dependency, like, it's… if the… the pay package is importable. I don't remember, like, they check for importer of something.
And if it's, available, but it's, like, a concrete, Alberta implementer, otherwise it's just an op for the…
**Lukas Hering** 20:05 Yeah, because I think the only… the only concern with adding native instrumentation would just be the fact that they… that package has… I believe it has zero dependencies, and they probably want to keep it that way.
At least, like, of… Allow it to be used with zero dependencies.
**Riccardo Magliocchetti** 20:25 Yeah, but… Again, like, as Leighton said, I think it's… I guess it will take a while to discuss this inside.
Like, with another team doing that, so… We can… Lukas is pretty small, and also hopefully, like.
a popular one, we can manage it in contrab, I guess. No position for me.
Thank you.
And… next topic is from Diego.
**Leighton** 20:58 Well, I think, Tammy has her hand up, Isabelle, the previous.
**Riccardo Magliocchetti** 21:01 Oh.
**Tammy Baylis** 21:02 Oh, yeah, thanks, Lane, sorry. Yeah, Lukas, quick question, thank you for this.
Probably for the future, but were you thinking of implementing, SQL commenting and context propagation into Oracle with this setup?
**Lukas Hering** 21:19 So, I mean, actually, one of the benefits of keeping it in Contrib is… I believe the DB API does that, right? The SQL commenting,
**Tammy Baylis** 21:28 Yes.
**Lukas Hering** 21:29 Yeah, so it's… if we… if we do that, I mean, it still doesn't need to live in Contrib, but currently it just uses the DB API.
**Tammy Baylis** 21:38 Nice.
**Lukas Hering** 21:39 I believe… Yeah, the… the folks that I've talked to that are closer to the instrumentation side, it actually sounds like there's another path for doing… trace propagation, That doesn't involve SQL commenting.
And I think Yeah, so that would be potentially, like, a supplemental contribution,
**Tammy Baylis** 22:09 Thanks, that's awesome. I… and I also support this. Thank you very much.
**Riccardo Magliocchetti** 22:20 Okay, thanks. Sorry, I missed your end, Tammy.
Okay, Diego, your next one.
**Diego Hurtado** 22:33 Right, okay.
Yeah, this is, A topic that happened in the OpenTelemetry packaging, channel in Slack, so… pretty much what's going on here is that, Several of our instrumentations have, a hard pin, on… OpenTelemetry instrumentation, you can read that there, Right below where it says we have two instrumentations.
In my comment?
So… In that scenario, right, we have an instrumentation.
instrumentation X and Instrumentation Y, both of them have a hard dependency on OpenTelemetry instrumentation. And everything is fine, because every time we… releases mutations in lockstep.
we also increased the hard dependency on Alberto 11.3 instrumentation, so that means the, If someone wants to use a new component of OpenTelemetry, they can.
Because the… All these limitations always point to the latest, version of OpenTelemetry instrumentation. Now, when the Elasticsearch instrumentation, stopped being released.
then the Elasticsearch instrumentation got, I mean, the last release of Elastic instrumentation is now pointing to a specific, harping or ventilometer instrumentation. So, now, what I… And this causes a problem, because if someone, has… is using the OpenTelemetry, Elasticsearch instrumentation, for whatever reason, I understand that, Elasticsearch now supports native instrumentation, and I don't want to… I don't want to focus this discussion on the Elasticsearch instrumentation specifically, because this is something that can happen anytime any instrumentation stops being released, right? So let's focus on the general aspect, let's not focus on the Elasticsearch instrumentation itself. So… Now, the… what I'm suggesting to avoid this problem from happening is, to… change this hard dependency we have for OpenTelemetry instrumentation.
to, one that is, described there a few lines below, that says, that uses this, I don't know, I think tilde is the right word, tilde equals… Yeah, right there, thank you. So that, every instrumentation can work, with every… stable release of telemetry instrumentation. In fact, I think this is a principle we should apply everywhere. Every… No… no open telemetry.
Python component, whether it's SDK, API, exporter, whatever.
Should, in my opinion, depend on a hard version of, other OpenTelemetry component, they should always use this tilde equals constrained itself.
So… That's what I wanted to discuss with you, applying this approach, There are a couple of more things that are also related to this topic. One of them is that, in order to fix this particular problem with the Elasticsearch instrumentation, it'll be to make one final release of the OpenTelemetry Elasticsearch instrumentation that just, Changes this constraint from a harping to a… Tilde equals, constraint.
And, also to make, a stable release of OpenTelemetry instrumentation. That is also related, I don't know if you want to discuss that now. But yeah, I wanted to hear your thoughts.
About, this.
What do you think?
**Leighton** 27:15 Oh, sorry, Riccardo, go ahead.
**Riccardo Magliocchetti** 27:18 Happy to grow, it's great.
**Leighton** 27:21 Yeah, Diego, I thought… I think this topic has been brought up many times already, and it's always, I think… contingent on just bringing the OpenTelem Transportation packages and semantic conventions to stability, like, I think… The general consensus was we're all okay with this, as long as those are… satisfied, so… this is, at least from what I remember. I believe this topic was brought up, like, quite a few times, so…
**Diego Hurtado** 28:00 Yeah.
Riccardo?
**Riccardo Magliocchetti** 28:06 Sorry, I was writing in notes.
Kildura, repeat, please, the first require… like, the request for a last… Elastic search esto meseso package.
Why?
**Diego Hurtado** 28:22 Make a final release of that package, and
**Riccardo Magliocchetti** 28:26 Oh, we did relax it? Okay.
**Diego Hurtado** 28:29 Exactly, yeah. Guys, I need to step out just for a second, because the delivery guy is at my door, but I'll be right back in, like, 30 seconds, okay?
**Riccardo Magliocchetti** 28:37 True.
**Leighton** 28:47 But yeah, at least for the relaxing, the… Dependency… For each instrumentation. Yeah, I think… I think this was, this was talked about before, just… Never got the push of, Getting the stable releases over, so…
**Riccardo Magliocchetti** 29:10 Yeah, like we discussed about bumping, OpenTab instrumentation.
in the context of, cutting 1.6 instrumentation rash.
Versions with a stable semantic dimension?
**Leighton** 29:30 Right.
**Diego Hurtado** 29:30 book.
Sorry.
I'm back.
**Leighton** 29:37 Yeah, perhaps.
Oh, yeah, so Digo, we were just talking about, so the greater effort is to bring the instrumentations to 1.0, Or to stable, and that is, I think, is a much bigger, kind of, piece of work That involves getting instrumentation.
As well as semantic conventions to 1.0. But, like, perhaps we could just do it piecewise and, like.
you know.
Iteratively do these things.
**Diego Hurtado** 30:10 Oh…
**Leighton** 30:10 Try to tackle the dependency.
First.
**Diego Hurtado** 30:16 Okay, wait, we do not need… To solve this problem, we do not need to make instrumentations.
stable.
Instrumentations in the 3 year of dependencies.
**Leighton** 30:31 Right, I'm not saying… I'm saying we were discussing that, but I'm saying to address your issue, it's like, perhaps it's only a subset of that bigger problem, right? Which is just to make the OpenTelemetry instrumentation stable.
**Diego Hurtado** 30:48 Opentelemetry Instrumentation package, yes, okay.
Sorry, I thought you meant making every instrumentation stable. Yeah, the OpenTelements instrumentation package, I think we can make it stable just based on the fact that it has been there for so long.
**Leighton** 31:09 Yeah, I think, I think, we would just have to… I think, I don't know if it's a tracking issue for it. There's a tracking issue for the greater, like, the bigger, instrumentation stability? But yeah, if we want to, like, carve this work out, to… kind of tackle the low-hanging fruit of, dependency conflicts. It would just be, like, what we did for… regular stability, kind of just, like, scrutinize the API surface, you know, do, like, a… kind of a bug bash kind of thing, you know, the typical 1.x kind of… process, so…
**Diego Hurtado** 31:49 Right. You also mentioned the semantic conventions package needs to be stable?
**Leighton** 31:56 No, no, no, that's part of the bigger work item of making instrumentation stable in general. Okay. Saying this is just a subset of that. Yeah, so we don't have to talk about semantic conventions, so…
**Diego Hurtado** 32:09 Yeah, right, so… Yeah, sorry, Riccardo, go ahead.
**Riccardo Magliocchetti** 32:14 Yeah, like, I have… two things I want to say. The first one is that When we discussed bumping to 1. Open-type instrumentation.
We also have a discussion about What… What the helpers that are inside of a tablet instrumentation should be able to output.
If only stable, instrumentation… a fully stable, somatic convention or not.
And so, like, I think later you were on the side that if you cut 1.0, The OpenTime Distribution 1.0 should only have helpers to… Send the stable semantic telemetry.
And so if we do that… We'll have, like, we cannot bump.
the dependency to 1.
Or to… for every instrumentation.
And this is one issue.
About the…
**Diego Hurtado** 33:30 Yeah, also, I think, yeah… There are also other issues. I don't know if, Lukas, there's something else you want to discuss?
You mean you… you should timebox this or something?
**Riccardo Magliocchetti** 33:48 I figured…
**Diego Hurtado** 33:49 Hi, Lucas.
**Riccardo Magliocchetti** 33:49 topic is also from you, Diego.
**Diego Hurtado** 33:52 Oh, no, it's just that I see Lukas has, like, a… Sound like a clock?
Emoji? I don't know if…
**Leighton** 33:58 I'm assuming that… Something like that.
**Diego Hurtado** 34:01 licenses.
Okay.
Sorry, sorry to interrupt.
**Riccardo Magliocchetti** 34:12 So yeah, like, was just… So, like, So, like, what Diego wants, and the packaging, SIG, and also the operator people, and the Lambda people, I guess.
Is it, like, we want to have, like, more relaxed dependencies.
Yes. And… And to the first question.
I don't agree with that, because that will be, like.
But we are going to maintain a distribution of open telemetry, but… Is not what the… OpenTelemetry, Python people.
is developing. If you're going to, like, cherry-pick out packages and stuff like that, I'm not sure I… I'm in favor of doing that.
And also, like, my opinion on the matter is that Damn… What the downstream, users, again, the operator, SIG, the packaging SIG, and also the Lambda layer, the people bidding the Lambda layers.
are doing… are, like, delegating the bump of new Python distribution of the… new open terminal distribution to depend Abbott or renovate.
And I don't think that's enough.
Because you're like, okay, you see that it breaks.
But it breaks when, we dropped the packages.
But also, you don't get new added packages.
I really think that… you know, being able to only handle new Python releases by Dependabot, I don't think it should be, like… there are, like, I don't think it's the right tool.
And I don't think, like… What downstream users should do.
Like, you can start with dependable, okay, but someone or something should look at the changelog.
And I know this is…
**Diego Hurtado** 36:38 Right, okay, so… No… I am just, asking for… These, instrumentations to… use, a more relaxed constraint. In theory, this should work, because, okay, let's, let's say that OpenTelemetry instrumentation is… is 1.0… Right now, okay? So, in the future, as… we… only the… the minor version and the patch version… and the… sorry, the minor number and the patch number are going to increase, right? So it's always going to be stable, and all the instrumentations can depend on any version that starts with one, which should work. Now, what people do to update their versions downstream That we cannot control.
Should they do it like that or not? It's gonna work forever for them or not?
maybe or may not. The… But I don't think those are… Those two topics are related.
I mean, the… us relaxing this version, constraint.
and people using Depend Abbott or Renovate, or something else. I think those are… quite independent.
**Riccardo Magliocchetti** 38:15 Yeah, like, this is more like a discussion.
included in the thread, I was lucky.
You're linked.
**Diego Hurtado** 38:26 Sure, I just, would like to understand, if, if you're objecting the… Change of constraint.
to… from… Equals equals to tilde equals.
**Riccardo Magliocchetti** 38:43 Break it.
I'm… I don't like the requests.
And, kind of post the request of cutting, apache release for, Package we dropped.
Being it, Elasticsearch or not, like, the fact that they work for Elastic, I guess, it's put me in the… like, I have a bias, of course, but this is more… to me, it's more like a general… Issue?
But… So, for a specific project.
For a specific package. At the moment, I oppose, because we are losing lockstep.
We are testing a lockstep.
And to me, like, doing this specific… Releases for a single package could open a kind of wall.
And for the second question, yeah, like, it's… One day or the… or another, we should… for the movies.
like… Without the requirement of having the very same version of instrumentation, and… When traveling to instrumentation, of course.
**Diego Hurtado** 40:01 Go to go to the,
**Riccardo Magliocchetti** 40:02 I'm doing that.
But we are not still there.
**Diego Hurtado** 40:07 Yeah, how about we continue this discussion in the OpenTelemetry Python in a thread between you and me, so that I can understand better?
What do you mean?
**Riccardo Magliocchetti** 40:19 Okay, Adam?
**Diego Hurtado** 40:20 We will flame.
**Aaron Abbott (Google LLC)** 40:21 Yeah, yeah, no, that sounds good. I… I was just gonna say, I'm also… it would be nice, maybe, if we brought it to an issue. I don't know if there's already an issue in the repo, but it's just hard to follow on all the Slack threads, and the… the proposal isn't super clear to me, also.
**Diego Hurtado** 40:38 Okay, yeah, I'll create an issue, in fact, I'll create an issue in a draft PR, because what I want can be expressed with code changes, so that I… You can see exactly what I mean.
I'll do that, and I'll attack you both.
**Riccardo Magliocchetti** 41:00 Thank you.
**Diego Hurtado** 41:03 Alright, thank you.
**Riccardo Magliocchetti** 41:05 Well, next topic is also from you.
**Diego Hurtado** 41:10 Let's see what that is… Right, okay.
Thank you, yes, so there is a project, sorry, I don't think I linked it here in the PR, but there is a… project… It's a new repo… well, I don't know if it's new. It's a repo, the Semantic Conventions Conformance repo.
maybe you have already heard about it.
It basically… it's a… a set of… definitions.
for tests… That, are executed on instrumentations. So… the… and the tests themselves. So, what this repo does is that it pretty much says, okay, A HTTP instrumentations, should produce this telemetry.
For them to be compliant with semantic conventions, right?
Which is great. Now… the, Trask, created a PR here to add tests for the Python Flask request instrumentations.
I don't know if… I think it's a draft BR still?
Zoom…
**Tammy Baylis** 42:41 Oh, Diego, I added a link to the meeting notes. It's PR41.
**Diego Hurtado** 42:47 Yeah, 41, exactly. Yeah, thank you, excellent. Oh, it's already merged. Great.
So… the The idea is to… The idea with my PRs is to move… Put these test cases in… the… You know, or… own… repo, so that if our instrumentations are not compliant with semantic conventions, they fail.
Or CI, so… We can fix them. In fact, I would like to do this with every instrumentation that Where that is… that applies.
So, I wanted to introduce this idea to you.
about, putting these tests in our repos. By the way, this doesn't mean I object this project, both things can coexist.
I just want the failure.
to happen in our CI as well, so that we realize quickly that any of our cementations is not compliant with semantic conventions.
**Riccardo Magliocchetti** 44:03 Lukas?
**Lukas Hering** 44:04 Hey, yeah, completely agree, I think we should have these in the intro repo, but, so what exactly… I know we added, like, Weaver checks somewhere… Was that… is that in the main repo, or is that in… I'm not sure… is it in Contrib? I'm just asking, like, so what's the difference? Is this just, like, kind of… helper scaffolding around Weaver, the… the semantic conventions.
Validation repo?
**Diego Hurtado** 44:32 Yeah, this, semantic conventions Conformance repo uses Weaver. And so I think, a way to understand this is that the semantic conventions provides definitions for the tests.
That the instrumentations have to run.
So that it provides a result against which… The telemetry produced by the instrumentation can be checked against.
**Lukas Hering** 45:02 Gotcha. Yeah, I do think that… or… yeah, I might be wrong, but I think, like, the tests for these should live in… Wherever the instrumentation library is, so it can be fixed there.
**Diego Hurtado** 45:14 Yeah, I agree.
**Lukas Hering** 45:14 Another kind of just off-topic comment, or, something we could try is, like, go on GitHub, find some Flask projects.
Instrument it and run it through.
But that wouldn't require, like, really any effort, and, I feel like that's where we're most likely gonna catch some maybe some semantic convention bugs is in, like, somewhat realistic applications.
But, yeah, that's just… that could be further down the line, but… So…
**Diego Hurtado** 45:52 Yeah, right, that… that's also a… feature enhancement. Someone else has any idea, before I start working?
I think realistic out here.
**Aaron Abbott (Google LLC)** 46:05 I think Carlos was before me.
**Carlos Alberto Cortez** 46:08 Yeah, I wanted to ask, like, so, did you have a chance to talk to Trask about this? I'm not opposing that we are doing the thing two times.
But I'm wondering what's his vision and perspective on this one.
**Diego Hurtado** 46:24 Yeah, during the last, specification maintainers call. I discussed this briefly with Trask. I informed him.
that I wanted to do this, I think, they are, I think he's okay with that, in fact, I think, this, actually… Works in favor of their goal.
The general goal here is to… make the OpenTelemetry instrumentations, compliant with semantic conventions, because that's a big problem that the entire OpenTelemetry project hash, right? Yeah. So…
**Carlos Alberto Cortez** 47:07 Yeah, I think that they're probably misunderstood. I'm just wondering about this status. Okay, because I was at the maintainer's call, but it was not really discussed up deep. Anyway, I can follow up on that. I'm mostly curious about… always the chance that work may be lost, like, you know, duplicating cycles and doing the same. As long as things start, I think that could be the… just imagine that suddenly he has some intern working on these, and then they have to port what they did there to Python, stuff like that, you know?
**Diego Hurtado** 47:38 Yeah, I think, actually, Trask is working with Lumila on this, and he's already aware that Lumila is actually, if I understood correctly, doing the same thing that I'm proposing for the JNAi instrumentations.
So… so yeah, I think that they're pretty much in sync with this idea as well.
**Carlos Alberto Cortez** 48:02 Although JNAi, as far as I saw, it's in the main repo. At least, I saw a few PRs there with JAI stuff at that semantic compatience Conformance repo. It's not… or not yet, at least, in the actual JNAi repos themselves.
**Diego Hurtado** 48:18 Okay. Yeah, because, something Trask mentioned to me during that call was that, there was already, like, a harness implemented by Cummila that could be reused for, what I'm trying to do here.
So… So yeah, I…
**Carlos Alberto Cortez** 48:38 Yeah, the…
**Diego Hurtado** 48:38 Kind of a business.
Appreciate that.
**Carlos Alberto Cortez** 48:40 Yeah, correct, because I think that, yeah, that was exactly the thing. If there's something that they already have in mind, so we don't have to write that from scratch. Lyrmila, by the way, is, told me that she's, not working this week, she's in a conference, so yeah, we can see her next week, probably, yeah. Okay, yeah, let's pull up online. Thank you.
**Diego Hurtado** 48:59 Yeah, I do have a pending task to check that, harness that… Track my… transformation.
I mean, these PRs I opened before being aware of that.
That's why they are still rough.
**Carlos Alberto Cortez** 49:13 Okay, got it. Okay, yeah, that, that, yeah, that puts more, color into the conversation. Thank you.
**Riccardo Magliocchetti** 49:23 Pardon?
**Aaron Abbott (Google LLC)** 49:25 Yep, I'm actually adding a link right here, but we do run it in CI in Python Gen AI, but there's, like, way fewer packages overall, so… Get a better link.
So it's not… a huge concern. So I wanted to call out two things. Well, I mean, first of all, I think it's a great idea.
yeah, like, it seems great to have a good understanding if we follow the semantic conventions or not.
there's this issue here, I added long GitHub Actions times.
So, I wanted to call out, I think.
adding more CI jobs is probably not… it's probably not a good time for it until we kind of fix this. It seems like Python might be… consuming a lot of the quota for GitHub workflows across the org.
So I think we should probably fix the CI before we work on anything like this, and once we, like, kind of batch the jobs a little bit more, if that's the fix, I'm concerned that the CI will get pretty long.
So I think we should just pay attention to this, because… from what I've seen, the setting up Weaver and everything, especially if you're doing, like, database instrumentation, it's kind of like the Docker tests we have, they can take a while to run.
They could take a while to start up, and they can be flaky.
Yeah, and then the other thing… Sorry.
**Diego Hurtado** 50:45 No, no, no, go ahead, please.
**Aaron Abbott (Google LLC)** 50:47 No, no, please go ahead with that one, and I'll say my second thing after.
**Diego Hurtado** 50:51 Yeah, I was just wondering, that quota that you mentioned is for the entire OpenTelemetry project?
**Aaron Abbott (Google LLC)** 50:58 Yeah, seems to be.
**Diego Hurtado** 51:02 Okay. Yeah, that's bad. Yeah, okay.
Maybe there's some optimization we still can do, but there's no guarantee that that's the case.
So… I mean, that… in fact, actually, not being able to expand our CI, it's… it's like a hard… blocker, almost for this project, right? I mean, we cannot… Add more stuff there until we fix that.
**Aaron Abbott (Google LLC)** 51:36 Yeah, and I think maybe we chatted about it last week, and another option was to run like, yeah, like, Lukas said here, I just copied what you said, Lukas, but run it only in the merge queue, and not on every PR upload, or run it, just a subset of the checks, or nightly, or whatever, so… There's… there's some things we can do, but, yeah.
Yeah, and then the other thing I was gonna say was, I feel like it's pretty early days for this conformance thing, and there seems to be a lot of churn.
So I agree with Carlos, like, let's check with Trask, and for the sake of, avoiding churn, maybe we could wait till things stabilize a little bit.
**Diego Hurtado** 52:19 Right.
But do you mean that, do you… do you expect those semantic convention conformance tests to change, because the semantic conventions themselves?
Are still unstable, so…
**Aaron Abbott (Google LLC)** 52:35 No, no, I'm just talking about the runner and, like, the scenario harness.
**Diego Hurtado** 52:41 Okay, yeah, yeah, on the, yeah, yeah, the infrastructure we'll… we will use to run this test. Okay, yeah, I get what I mean.
**Aaron Abbott (Google LLC)** 52:49 But overall, yeah, definitely supportive. That's all I had.
**Diego Hurtado** 52:54 Alright, thank you.
**Riccardo Magliocchetti** 53:00 Yeah, like, I was going to add that, when Ulzimila contributed, with a wrap that we have in Cortez duties.
I also played with… with this idea.
Months ago.
And, working something similar, like, a synth provision of this.
Without the harness, without the scenario, just plain PyTest.
And so, like… Regarding also the… this… the doubt that Carlos, had. Also, I think that Aaron said before that… Our use will be different, like, We care more about… the quality of the export, and more event, the big picture of… What everyone is a sporty or not.
That is what, I guess, the conformance test is doing.
And so, like, while we… we can use stuff, I'm not sure.
But we need to lose, like… sharing the application will be great, but I'm not sure we… We need to reuse also the… the YAML stuff for the… like, all the stuff that Abbott strapped, The code from the… from the runner.
like, we have everything in Python.
But…
**Diego Hurtado** 54:46 So, you mean that we… we may not need to reuse that harness? That's… that's what I mean?
**Riccardo Magliocchetti** 54:54 Yeah, like, I'm not sure how much value it has.
For us, like, it makes a lot of sense when you have, like, 7 languages, and you want to… To, you know, write the same thing.
But for us, I don't know, like…
**Diego Hurtado** 55:13 Okay, I'll take a look at that, and sorry, I'll… I'll bring back more information regarding how the harness is and stuff.
**Riccardo Magliocchetti** 55:25 Thank you.
Okay, I think this was the last topic.
Anywhere else?
Okay.
Awesome. So… I don't think…
**Aaron Abbott (Google LLC)** 55:51 I guess that's it.
**Riccardo Magliocchetti** 55:52 Okay.
Thank you.
**Aaron Abbott (Google LLC)** 55:55 Alright, see y'all next week.
**Diego Hurtado** 55:56 Thank you.
**Tammy Baylis** 55:57 So…
**Hector Hernandez** 55:58 Thank you.
