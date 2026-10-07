SIG: Ruby SIG
Date: 2026-10-06
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Matthew Wear (Dash0)** 00:43 Oh.
Was that you were slightly muffled? I'm guessing it was a hello.
**Kayla Reopelle (New Relic, Inc.)** 00:52 It was a hello. Can you hear me better now?
**Matthew Wear (Dash0)** 00:55 Yeah, yep.
**Kayla Reopelle (New Relic, Inc.)** 00:55 Okay, great.
Give.
One more minute before we get started? I know Hannah and Rob aren't joining us today. I'm not sure if anyone else can make it.
Here are the meeting notes, if anyone wants to add anything to the agenda.
Okay, it's 3 after. We can get started.
Did anyone attend the SpecSIC this morning?
Matt, I see your name.
**Matthew Wear (Dash0)** 02:14 It was the weirdest SPEC SIG ever. Oh, really? Anything to say, so we all just left immediately.
**Kayla Reopelle (New Relic, Inc.)** 02:22 Fantastic.
Yeah. Okay.
Well.
What conference is happening this week? I saw, like, a post of cupcakes somewhere.
**Matthew Wear (Dash0)** 02:33 I have no idea.
**Kayla Reopelle (New Relic, Inc.)** 02:35 All right.
Well, that makes that easy.
Okay, so then, yeah, on Core, I thought we could look at the metrics and logs.
milestone progress, It's really exciting. We have PRs for almost every issue.
And, I'm hoping to review more of those this week, especially now that we have The, logs and metrics, internal… Provider shift, finished.
So that's exciting.
Before we move on there, I guess, is anyone here today interested in having us prioritize any of these issues in particular?
I can go to the PR page, too. I guess that might be more… relevant.
Okay, I'll take that as a no.
continuing to jump around a little bit. I did… rerun the prompt to get some more, like, an updated look at logs and metrics. It turns out there are possibly some issues missing for logs. The prompt took longer than I thought, so it only finished right before the meeting.
But, in metrics, we've made some good progress so far.
And there may be some other issues that either need to Change or be adjusted in some way.
I'm not gonna go through it all here, but, Yeah, if you're interested.
I think probably waiting until a little after the meeting, I'll open the PR officially when I feel more confident about the prompt output.
This is just… Here for kind of my own accountability.
For the logs milestone… We have one of the issues done, issue or PR open for another one.
I think that… since we have so many pull requests open for metrics, I'd probably just lean on trying to finish… That one up first, and then, if there's interest in time, moving into logs.
What does everyone think about that?
**Matthew Wear (Dash0)** 05:12 Sounds good.
**Kayla Reopelle (New Relic, Inc.)** 05:17 All right. That note.
There's also, Thompson… James Thompson opened a pull request a long time ago to add the CodeQL runs to the CI, like we do for Contrib, to the core repo.
And the settings were changed, by an admin, so we're all clear to do this now. Before I merged the PR, I just wanted to see if anyone had any concerns about running CodeQL on all of our PRs for The core repo going forward.
**Matthew Wear (Dash0)** 06:05 Not here.
**Kayla Reopelle (New Relic, Inc.)** 06:12 Okay.
Great.
Go ahead and merge that, and then.
There's also… I'll make the change to admin so that it's required.
And we kind of already talked about that.
Okay, anything else in CORE before… Move on.
Alright, we had the first version of OpenAI, OpenAI Instrumentation Gem released yesterday, which is very exciting. I know we've been working on that one for a while.
There's two other gems to release today.
They're just minor… bumps, though, and I was wondering, that release that went out yesterday didn't add OpenAI instrumentation to all.
Logger is already there, so this, you know, logs, metrics, patch is already available.
in that.
I'm wondering if, we have any… If we're… if we're comfortable with adding OpenAI to all.
**Matthew Wear (Dash0)** 07:35 I think that should be fine.
**Kayla Reopelle (New Relic, Inc.)** 07:43 Okay, great. Then I will take care of that one after we do the other two releases.
Okay, I don't know what this one is… Oh, yeah, this is a bigger change to CI that I wanted to hear people's thoughts about.
it's… it's a decently sized PR, so I think we can just more, like, call it out today and try to look at it if you have time.
It would change the way that we are assigning groupie versions in our CIs, so that they're defined I think in one place.
Yeah, I still need to think through it more. It's using… Me's, as The tool to help this change.
But, that is a bit of a shift from what we've been doing, and it would be quite different from what we're doing in CORE, too, so… I think there's a few other PRs that are maybe… Related to this one, at least one dependency PR.
So I'd say take a look at it if you haven't.
Before we move on, though, does anyone have any immediate thoughts about it that they would want to share?
Okay.
And.
Let's see, auto instrumentation. Siobhan, I wanted to check in with you to see how the operator work is going, and if you need anything from us there.
**Xuan Cao** 09:48 So the image is ours. I just need to wait for them to merge the test image PR first.
**Kayla Reopelle (New Relic, Inc.)** 09:58 Okay.
**Xuan Cao** 09:58 And then I'll update those that Mega up here to I've ever seen.
In the operator, so that's… that would be, like… Just two steps.
Well, yeah.
**Kayla Reopelle (New Relic, Inc.)** 10:15 Nice! Okay, that sounds good.
Thanks.
Okay, my next question is, I'm wondering, now that we've merged, this is just the issue with the, Instrumentation only, metrics and logs.
work, what are our next steps? I know we have this legacy global provider shim removal, Wondering… Matt, if you have any sense of how long you want the dual… Pattern to exist, or when we should think about removing the shim.
**Matthew Wear (Dash0)** 11:00 So… I guess I have two thoughts there. One is we could… We could just leave it until 1.0.
That would be… The… the longest we would leave it, or.
If we wanted to remove it earlier, we could just have, like, I don't know, like a few releases out, so that… The majority of people will probably have.
If they've upgraded, they've upgraded both, because really the only way you get in trouble here is if you upgrade the API without the SDK. I think that's how it works.
So, So I think, in general.
like, I don't think people are gonna hit this problem, and I feel like if we had, you know, a handful of releases out, we could consider removing this.
Earlier, if we wanted, but… Yeah, those are the 2 options. I don't really have strong feelings either way.
**Kayla Reopelle (New Relic, Inc.)** 12:02 Okay, sounds good.
I kind of like the idea of leaving it till 1.0, but we could see how long that is, and if it ends up, you know, being a few… minor releases, then we could just pull it out anyway. So… Maybe we'll check back in.
In a few weeks, and see what we think.
**Matthew Wear (Dash0)** 12:25 Yeah, I think that sounds good. And then I think 2413, we're probably close up at this point. I feel like all the work that we were tracking there is is done, and we do have that separate issue for removing the shim.
**Kayla Reopelle (New Relic, Inc.)** 12:40 Nice. Yeah, I was wondering that too, so… Alright, let's go ahead and close it.
Great. Okay, so then the other thing is that now that we can add these metrics to.
our instrumentation. Wanted to make sure we were all on the same page about how we wanted to do that.
There had been some talk in the past about… Only emitting metrics that have… Stable conventions, and if we have different conventions for our metrics and for our traces? Does that cause a problem?
HTTP, at a minimum, could at least be a guinea pig if we do care about the conventions, because there is a way to add things to only the stable implementations.
But… or the staple conventions. But, yeah, I guess I'm just curious overall about What people think about metrics and semantic conventions versions in our instrumentation.
**Matthew Wear (Dash0)** 13:47 I would say we're definitely free and clear to emit anything that conforms to semantic conventions.
**Kayla Reopelle (New Relic, Inc.)** 13:56 Even if it isn't the semantic convention that matches the rest of the library.
**Matthew Wear (Dash0)** 14:05 Are you saying there's kind of, like… Dumb.
The metrics would be… Oh.
would adhere, but maybe, like, the attributes would not, or something.
**Kayla Reopelle (New Relic, Inc.)** 14:16 Yeah, yeah, like, the trace attributes and the metric attributes might be different. Like, like in, you know, database instrumentation, for example, we have… I think Trilogy is maybe the only one with the SEMCOM stability opt-in environment variable.
But if we wanted to add something to, like, PG instrumentation.
we probably don't want to put in work to emit a metric that aligns with that older version.
Of the conventions, so… yeah, I guess, is it okay if the attributes have a mismatch, and we just go ahead and omit the latest metrics?
**Matthew Wear (Dash0)** 14:58 Yeah, I wouldn't… I wouldn't emit metrics on old semantic conventions. I think that doesn't make sense, and I'm guessing… Like… If if we actually go through those instrumentations and Emit the right, attributes on metrics. It's probably not like a huge leap to.
**Kayla Reopelle (New Relic, Inc.)** 15:25 Yeah.
**Matthew Wear (Dash0)** 15:26 to, update it for traces, too. Not that they have to be combined, but maybe they can kind of, like.
follow each other, and then we can get the opt-in flags, I guess, for, For stable, shortly after.
**Kayla Reopelle (New Relic, Inc.)** 15:43 I mean, I think, Hannah has PRs for most of the database instrumentations ready.
And was just opening them one at a time to… Kind of allow reviews to move along more quickly.
So, that would kind of leave, I guess, GRPC. I don't think we've done any work there on conventions.
Nice, this feels like a good paradigm to me, with thinking about conventions and… how outdated we might be in some of the libraries.
Okay, that answers the next question, and then… The last one is kind of just, like, what do we want to do with the PRs that were previously open to add metrics to instrumentation? I mean, we have some, like, this is a super old one that I opened a long time ago.
I'm kind of inclined to just close them all and start over. I think most of them do something related to, like, adding their own meter, or, you know, some of them also have updates to the base instrumentation gem as part of them.
But it is… it is work that people put in at some point, so… Before, you know, just closing them, I wanted to bring this to the group.
**Matthew Wear (Dash0)** 17:13 I guess it depends on how far off some of these things are.
**Kayla Reopelle (New Relic, Inc.)** 17:18 Mmm.
**Matthew Wear (Dash0)** 17:19 Oh.
Yeah, like, I guess some of those were, like, Sidekick and Redis, like, do we really… do we have… Do we have reliable conventions for those, or are those things that we're…
**Kayla Reopelle (New Relic, Inc.)** 17:38 Yeah.
**Matthew Wear (Dash0)** 17:39 Well, Kind of inventing…
**Kayla Reopelle (New Relic, Inc.)** 17:51 Yeah, I think making sure that whatever… We're adding Has a Reliable Convention would be a good… First up.
**Matthew Wear (Dash0)** 18:05 Yeah, that seems like a good first step to me. I actually emit things that are defined by semantic conventions, and then… things that are not metrics that are not defined by semantic conventions. I don't. I don't know what to do on that yet. I haven't thought that far ahead.
And we can. We can do some research and see what at least what other SIGs are doing there.
**Kayla Reopelle (New Relic, Inc.)** 18:30 Mhmm. That sounds good.
Because we do also have our Ruby namespace now, too, in semantic conventions, so… If it is something that truly doesn't… have a place in another language, we can define those.
But it should still be defined, I think, before we add it to instrumentation.
**Matthew Wear (Dash0)** 18:51 Yeah, and if it turns out that, it's pretty easy to add our own, you know, for things that are not.
That are not based.
or yeah, that do not have, you know, spec level semantic conventions. Then I think we can definitely use those existing Prs as as inspiration, or take what we can from them. My guess is… I saw a couple of those were from Zach. My guess is he's not going to come back and finish those up.
**Kayla Reopelle (New Relic, Inc.)** 19:22 Yeah, yeah.
**Matthew Wear (Dash0)** 19:23 But we could probably take.
Take what we can from those, and give whatever credit we can to.
initial work, and move those forward, if that's useful. But I'm sure… I guess what I'm trying to say is I feel like probably whatever he did was probably valuable, one way or another, if we…
**Kayla Reopelle (New Relic, Inc.)** 19:41 do.
**Matthew Wear (Dash0)** 19:42 up with metrics in that space.
We can close them, but we should not forget about them, I guess.
**Kayla Reopelle (New Relic, Inc.)** 19:48 Yes, okay, that sounds good.
Okay, so maybe… I wonder what the best way is to preserve them. I mean, they'll exist in… pull requests. I don't know if we really need an issue to track.
adding metrics to instrumentation? I guess we could, if we… if we want to look at it, and just be a little more precise about adding them to different libraries.
**Matthew Wear (Dash0)** 20:15 I feel like it's a good idea. I feel like I fear opening an issue for such a thing just because.
**Kayla Reopelle (New Relic, Inc.)** 20:19 that's.
**Matthew Wear (Dash0)** 20:20 I end up getting a bunch of, Robot PRs trying to add.
**Kayla Reopelle (New Relic, Inc.)** 20:24 Lena.
**Matthew Wear (Dash0)** 20:24 We'll have to answer questions sooner than we want to.
That's my only… It's my only concern.
**Kayla Reopelle (New Relic, Inc.)** 20:33 Okay.
**Matthew Wear (Dash0)** 20:33 A year ago, this would not have been a problem.
**Kayla Reopelle (New Relic, Inc.)** 20:36 Yes.
Yeah, I agree. Well, we have it tracked here, so maybe this is our secret tracker for now, or, you know, internal tracker, maybe, rather than using the word secret.
And when we feel more confident about the way we want these things to look. We could create corresponding issues.
**Matthew Wear (Dash0)** 20:58 Yeah, that sounds good to me.
**Kayla Reopelle (New Relic, Inc.)** 21:00 Okay, great.
Wonderful. That kind of satisfies my questions on this topic, but does anyone else have… Questions or thoughts?
On it.
All right, great.
I mean, that's kind of our agenda for today.
We do have other pull requests open, but, I feel like… If we have another 40 minutes for OTEL, time might be better spent reviewing the pull requests than just chatting about them here.
Does anyone else have anything they want to discuss today?
**Matthew Wear (Dash0)** 21:55 Nothing to discuss. I was just gonna say that I did, open a PR for.
Declarative config for logger provider.
Just to have, like, another… just to have another signal, and… It looked easier than metrics, but…
**Kayla Reopelle (New Relic, Inc.)** 22:16 Great.
**Matthew Wear (Dash0)** 22:17 And, yeah, I think I'm trying to make it so that the, to use the config gem, you don't need to depend on the logs SDK. It's kind of like, if logs SDK is present, it will configure it, but it's…
**Kayla Reopelle (New Relic, Inc.)** 22:30 not.
**Matthew Wear (Dash0)** 22:31 a hard dependency of config. It's like a soft dependency. So No rush on this, but if anybody wants to take a look at it at some point in time, then that might kind of… Oh.
if we like what we do for logs, then I think it will kind of set the stage for metrics.
**Kayla Reopelle (New Relic, Inc.)** 22:51 Nice. Yeah, that sounds good to me.
Thank you for opening that.
**Matthew Wear (Dash0)** 22:55 problem.
And yeah, I think… We did have a question way back when, about, like… How does the declarative config get picked up? You know, is it zero code?
Oh.
And… From what I can tell, I think Java is actually zero code, but everybody else, there is at least one line of code, basically.
We need to.
Oh.
run the, config dot, I forget, install?
And.
And that one line, or small number of lines, is… is acceptable. That's how JavaScript works anyways, and pretty much everything other than Java.
So I don't think that declarative config is meant to be zero code.
Boom.
**Kayla Reopelle (New Relic, Inc.)** 24:00 That's good to know.
**Matthew Wear (Dash0)** 24:02 and Feel free to correct me on that, though, if anybody finds otherwise.
Because, yeah, like, the… The one thing… One thing I'm… yeah, I'm just thinking, like, in the future, I know we've kind of had talks about.
Wanting to be able to.
Set up, like, custom, you know.
custom resource detectors or custom processors, whatever, using declarative config, like right now, we're kind of only allowing the things that ship in.
In our repositories, because they're the only things that we know about.
And, you know, we basically are mapping, like, config options to… to Ruby classes, more or less. And.
Eventually, we want to be able to, to extend that, for, for third-party components, and… you know, all that requires some level of, like, registration. I think you basically will need a registry somewhere behind the scenes that maps, you know, config options to Ruby classes, dynamically.
And that just all gets like hard when Like, in the zero code case, if it's kind of like our auto instrumentation, where we will load everything first, it's like, we won't really give Other code an opportunity to, like, insert itself in the registry before we try to set it up, and it just becomes, like, a huge… Chicken and egg disaster.
But if you know, if declarative config ends up being, you know.
You execute this line of code, then… Oh.
Then everything just needs to be registered before that line of code executes, and that's a little bit easier to deal with, I think.
**Kayla Reopelle (New Relic, Inc.)** 26:01 Yeah.
**Matthew Wear (Dash0)** 26:04 Yeah, that's just tangent. Don't let me… Waste our free time that you were about to give us back.
**Kayla Reopelle (New Relic, Inc.)** 26:10 That's.
**Matthew Wear (Dash0)** 26:11 excited.
**Kayla Reopelle (New Relic, Inc.)** 26:12 Oh, it's good. It's it's good to keep in mind. because that's that's an important project for us to keep.
tracking, too. Thanks for looking into that more.
**Matthew Wear (Dash0)** 26:21 No problem.
**Kayla Reopelle (New Relic, Inc.)** 26:25 Alright, great. Well, with that, then, we'll release… release the time, release the half hour to everyone.
So, yeah, have a great week, and I'll see y'all next week.
**Matthew Wear (Dash0)** 26:38 Thanks.
