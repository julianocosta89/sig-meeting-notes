SIG: Ruby SIG
Date: 2026-06-02
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 02:39 Hey, everyone!
**Bart de Water** 02:44 Hello, sorry, I'm off camera, I'm still finishing my lunch.
**Kayla Reopelle** 02:48 No problem. I think this has kind of turned into more of an off-camera meeting, so… A-okay.
Let me get the notes up… Okay… Can you guys see my screen?
**Hannah Ramadan** 03:37 Yes.
**Bart de Water** 03:38 Yep.
**Kayla Reopelle** 03:39 Great.
Wonderful.
**Hannah Ramadan** 03:52 Also, hey Bart, it's good to virtually see you.
**Bart de Water** 03:57 Hi, Anna. Likewise.
I promise.
Jeremy off last time, work just got busy.
**Kayla Reopelle** 04:08 Appreciate the reassurance.
Cool. Okay, so at the SPAC SIG this morning, there was a lot happening, I think for our… conversation. The most interesting thing… My internet connection was really bad, and so also, please let me know if I'm cutting in or out at all today, too.
The conversation that I think was the most interesting for this meeting is the self-observability portion.
So there's been an effort for OpenTelemetry to be able to monitor itself.
And we have a bit of that with our… An unspec'd metrics reporter that exists in some of our exporters.
That just basically tells you about drop spans and things like that.
They are working on, like, a more formalized version of this.
some of the discussion today, too, was… You know, questioning, like.
How do we make sure we build something that's compatible with metrics and logs and traces instead of just one of them?
I think this is just the beginning, probably. There were also a lot of concerns about You know, having this kind of thing on by default, or how you can make breaking changes and migrate if you already have Some sort of, you know, unspecked solution, like we do in this SIG.
So, I think, this is something for us to keep an eye on, and if it is a project that anyone is interested in.
I think it would be good to… probably chime in on this PR, even though it was merged.
Or just check in in the specification, slack group to… you know, express your interest, and they can probably connect you with some resources to start implementing this for Ruby, if that's something you'd like to do.
trying to think of if there's anything else, like, this whole middle part, I heard, like, every other sentence, so I'm not very helpful there.
Is there anything on this list that people want to take a look at together while we're here?
**Hannah Ramadan** 06:39 Was the batch… batching project any interesting?
**Kayla Reopelle** 06:45 Yeah, I think I was still having internet issues here, so I did not really hear much of it. But let's take a look.
So it sounds like there is a project.
There might be calendar meetings.
**Hannah Ramadan** 07:11 It just sounded kind of cool.
**Kayla Reopelle** 07:13 Yeah, yeah.
Oh, and it has declarative config implications, so that could be good to keep in mind, too.
Can you guys hear the, like, chime?
From… Okay, great.
So, yeah, so there's, it sounds like… Probably talking about how patching should work with configuration overall. So if that interests you… It does sound like they want more languages to participate. Yeah. So that could be a good opportunity.
Yeah, and one other thing, I don't think that we've ever really had this in Ruby, but, they're working on deprecating OpenCensus, so if that's something that, you know, you're using in… One of your other languages, keep in mind that… they're trying to pull it away, and then also just discussing, like, what it looks like for a hotel to fully stop supporting some sort of component.
In terms of documentation and things like that.
Alright, oh, and I'll put this in the chat… Okay, we don't have anything on the agenda right now. Is there anything that people want to talk about right off the bat?
I do have a few updates.
I guess that I could throw in, too. Schwan, working on the repo setup, there is a repo that exists right now, but it's not something we can commit to yet, and I think it should be ready in another day.
So, we should hopefully be able to merge… to move over the, PR from Contrib this week, and kind of get things going.
Sean, are you saying anything? I see you're unmuted.
**Xuan Cao** 09:42 Oh, no.
Okay. I'm sorry, I was… I was just looking. Oh, sorry, I do have one thing, I haven't put this on this agenda, but it's really not that big deal.
Let me just paste down the link on the… On the agenda.
**Kayla Reopelle** 10:02 Okay.
**Xuan Cao** 10:07 Yeah, so if you can open it,
**Kayla Reopelle** 10:10 Yeah.
**Xuan Cao** 10:16 So this one, it is really small changes, that, attach the endpoint for the… logs and metrics. It's fine. The only thing… is, what I'm concerned is about, the… The, the… how do I say, the mismatch between… The exporters for the meshes, and then logs Compared to…
**Kayla Reopelle** 10:45 Good.
**Xuan Cao** 10:45 trace, but if you could look at a trace, as I think James put it, an entire new function, that's… handle this kind of case. And then… And then somehow, other people find that it's the same issue, but they're using a different approach. So, what I was thinking is, maybe it's a good time to… I don't know, to have, Would it also a common function to the… Open financial comment, or… have, Unifies, HTTP exporter that included all the… all those three different, exporters.
Basically what I'm saying is, having 3… Separate gym.
And, sometimes it creates, How do I say, discrepancies, among the common functions.
I noticed this reason because when I tried to review this PR, essay, why not use this button after, after I… look closely then, I figure out, okay, it's… I didn't look at the right place, but again, it's just created a, I'll say, burden for the maintainer to… when they try to, review the stuff.
So maybe somehow we can, merge some of the common functionalities.
**Kayla Reopelle** 12:22 Yeah, I think that's a good idea. I think originally we were keeping metrics and logs separate from the, like, OpenTelemetry Exporter OTLP gem that we had, just to differentiate differentiate between stable and unstable code, but since we've been, there's been a little more work done lately on the OTLP HTTP and OTLP gRPC gems, we could look into trying to put this there, or… yeah, doing a larger refactor and, putting the shared information into that OTLP common gem and just making that a dependency.
of the gems that we have to reduce the duplication. I agree that it is, you know, too verbose and kind of too repetitive across these, and the drift can make it a lot harder to maintain.
would you be open to… so I guess I have two questions for you. One is, there was a release PR opened to… merge, or to, like, release new versions of the metrics and logs exporter with this fix in it.
Do you still feel comfortable with that release going forward, or do you think… We need to find a way to, like.
circumnavigate it, and that this PR, like, shouldn't have been merged in the first place.
**Xuan Cao** 13:44 Oh, I definitely, think you should go, because for the refactor, it will be, More changes, so yeah, definitely.
**Kayla Reopelle** 13:53 Okay.
**Xuan Cao** 13:54 I'll release that, yeah.
**Kayla Reopelle** 13:56 Sounds good. And then, yeah, and then the second… Question… oh boy, do I still have it in my mind. I think it was… Oh, would you be open to creating an issue that kind of, like, maps out, I guess, your desired next steps for what it would look like to combine the exporters and reduce some of that duplication?
**Xuan Cao** 14:19 Yeah, yeah, I can't open the issue. Yep.
**Kayla Reopelle** 14:22 Okay, great. Thank you.
Right.
Awesome.
Anything else in CORE? I see Bart, I see your message.
About contrib, so we can move over there next, if not.
**Bart de Water** 15:05 Yeah, James already reviewed it and had, like, some great feedback, so I was wondering if there's, A, if anybody had the chance to look at it, because I know everyone's busy, but also B, if there's anything that you want me to do in order to get it into a mergable state.
**Kayla Reopelle** 15:27 Yeah, so I've taken a look at this, and I think at a high level, it looks great. I wanted to do a little more… Of some, like, Deeper digging with comparisons, too, between, like.
the New Relic instrumentation, just because that's what I'm most familiar with, and we recently added support for this, and then also just comparing it with other features more deeply. I think the code itself looks good, and the patterns seem right. I think I just wanted to spend, like, another half an hour with it before approving it.
**Bart de Water** 16:00 Okay.
**Kayla Reopelle** 16:02 Has anyone else taken a look at this?
**Hannah Ramadan** 16:12 I have not, but I would love to.
**Bart de Water** 16:15 Also, one other question while I have y'all is, like, do you prefer me to, like, squash this down before it get merged? Like, for example, the Reels, repo has a preference for that workflow, or you don't really matter? Because originally, I, like, added, like, all the new, sort of, like, instrumentation hooks that the continuation, DSL adds.
But then James sort of, like, rightly pointed out that a lot of them is, like, you know, like, since span events are being moved away from, he's like, that should be logs, and I was like, well.
I'm not gonna be the one introducing, like, logging here in this PR.
**Kayla Reopelle** 16:48 Yeah, yeah.
**Bart de Water** 16:49 So, I just simplified it for the one that I actually did care the most about, is, like, how long does a step take within, like, a perform span?
**Kayla Reopelle** 17:01 Okay, nice. Yeah, I think that's the right call to not add logs, specifically into this one.
For squashing commits, I don't think that that's really… important here, because we will do… I guess you can't really see it anymore, but we squash when we merge, so all of.
**Bart de Water** 17:21 Oh, okay.
**Kayla Reopelle** 17:21 messages will just be in the body of the final commit that'll have the title of your PR as the.
**Bart de Water** 17:27 Okay.
**Kayla Reopelle** 17:29 the main commit, so… Whatever… whatever your preference is there.
Does that… did that answer your questions? Did I miss one?
**Bart de Water** 17:38 Yes, yes, yeah, like, If that's, like, the one thing that would help smooth things over, then I would be happy to, of course.
**Kayla Reopelle** 17:47 Yeah, no, no, I think it's just, taken… taken a little more time with it to compare things for myself. And then, Hannah, you're interested in reviewing it as well?
**Hannah Ramadan** 17:58 Yeah, yeah, I would.
**Kayla Reopelle** 18:00 Okay, awesome, thank you.
Okay, we can also just start opening up the… pages and looking at things, but last call… Before we move into that.
Oh, you know what? I do actually have a question for this group, before we do that.
I am feeling kind of overwhelmed with all the Renovate PRs that are opening up, and I'd like to propose that we change the frequency to be, like, once a month, unless it's a security update.
Is that… Something that other people feel comfortable with, or others… also having issues with the pull request. Okay, I see a thumbs up. Two thumbs up. Love it.
Alright.
**Bart de Water** 19:05 I have no, sort of, like, stake in this, really, as, just a, casual observer.
But, I've, in other open source repos where I am, you know, a maintainer, I've also gotten, like, pretty tired of this, and it's like, 9 times out of 10, it's like, it's a dev dependency. Like, who cares that there's, I don't know, some, you know, Redos vulnerability in there? It's, like, the only person who's gonna get bit by that if I, you know, make a stupid regex myself.
Yeah. But it's screaming critical vulnerability at you, and I'm like, I've got better things to do.
**Kayla Reopelle** 19:37 Yes, yeah, I appreciate that validation. Yes, I just noticed that it is taking away time that I think would be much better spent on other PRs, so… I think this would be an easy way to at least try out a different approach.
Cool, I'll open up a PR to do that.
Sweet. Alright, well, let's just take a look at our poll requests.
We are dealing with some failures related to Markdown link check, This is a… bug that… the folks who maintain this library are aware of, and I think, James Thompson opened a PR in one of the repos to fix it. I haven't taken a look yet.
There's another one in Contrib that's kind of related to the README that I opened a PR to fix.
Looks like we have… Proxy address… for OTLP Exporter.
Eat fun.
CLA review, looks like.
Some folks have already taken a look at it, thank you.
Maybe, since there are… decent chunk of PRs here, Oh, I'm surprised that didn't get merged yet. I thought I merged that.
Is there anything on here right now that people want to take a look at together?
Nice feature request to go along with. Actually, issues to go along with both recent… PRs… Ijin, do you want to talk about this one at all?
**Arjun Rajappa** 22:08 This came out of a PR review comment, which was, I was given by you.
I guess in one of the three PRs which I've raised for OTLP… For the splitting job.
**Kayla Reopelle** 22:28 Nice.
**Arjun Rajappa** 22:33 So, I have removed all the references to the deprecated, or… Use of older version of Exporter, so that we can start using.
I'll be sure that.
**Kayla Reopelle** 22:49 Okay.
Alright, well, there's a bunch of Renovate stuff to look at, let's see… We haven't contrib… Another release… Some docs improvements… Since we're… We're here, you know, is there anything… That catches your eye.
**Bart de Water** 23:53 Maybe related to the one that I was working on, opened by James, to move… active job out of the messaging domain, I saw that one near the top.
I will admit that this is the part of OpenTelemetry that I still find, somewhat bureaucratic and hard to navigate when things are sort of, like, exactly fitting into the right, shape of, yeah, conventions.
**Kayla Reopelle** 24:19 Which number is that, that you… I'm sorry.
**Bart de Water** 24:21 images.
**Kayla Reopelle** 24:22 Seeing it.
**Bart de Water** 24:24 It was by James Thompson, I just saw it scroll by.
**Kayla Reopelle** 24:30 Oh, was it an issue and not a PR?
**Bart de Water** 24:34 There we go. I got there, yeah, that was the one.
**Kayla Reopelle** 24:35 Nice. Okay.
Yeah, this is something I haven't… The messaging conventions are not something I am… very familiar with.
It's a good thing… to contemplate. Looks like there's been some discussion between Arielle and James.
a decent amount of discussion. I'm gonna have done all this. Bart, since you've been using the instrumentation, and then also extending it, what opinion do you have about Keeping the attributes, changing them…
**Bart de Water** 25:17 To be honest, I'm kind of indifferent on whether it's, like, one or the other. In the end, especially if I think of, like, my team, I would like it to be consistent, so that they, you know, can… They can hurt… you know, Somewhat easily navigate, you know, finding certain attributes.
To be honest, I haven't looked that closely yet, into, like, what does messaging even mean in hotel conventions. I was just curious if people might have an opinion here, or, like, maybe could help me enlighten about why things are the way they are.
Because again, like… like I said, for an outsider, sometimes I'm like, yes, conventions, that's great, but then sometimes the conventions seem to be… Very peculiar about some specifics at times.
**Kayla Reopelle** 26:01 Yes.
Yeah, I agree.
Hannah, not to put you on the spot, I know you've been looking a little bit about… I guess to put you on the spot, you've been looking a little bit at messaging conventions this week. Is there any ideas that you have, just from… What you've been looking at, that… Could help puss out here.
**Hannah Ramadan** 26:24 Nothing top of head. I think I need to read what is… what this issue is about.
But I can, I can do that.
**Kayla Reopelle** 26:35 Okay.
**Hannah Ramadan** 26:36 Leave any comments.
**Kayla Reopelle** 26:39 Sounds good.
Yeah, I think this… this is an interesting element of it, and I… Would like to look into the… Issues or pull requests where, James tried to add other messaging systems, and… was turned down.
So.
**Bart de Water** 27:01 Yeah, and then I do see SQS in messaging in SEMConf, and I'm like, well, it has at least the word Q in the name, so it's like, things are starting to get a little.
**Kayla Reopelle** 27:08 work.
**Bart de Water** 27:08 At least for me. Yeah.
**Kayla Reopelle** 27:10 Yep.
Yeah, I would have… Put this in a messaging bucket myself, just at a high level, thinking.
Thinking about those semantic conventions.
categories that I'm familiar with.
at a gut level, I don't know if making, like, a Rails namespace feels… Yeah, I'm not sure if it's dynamic enough, I feel like that might silo… like, Ruby data that's in this category, maybe from… If you have, like, a multi-language system, being able to correlate it with that other data.
But… I'm not an end user day-to-day right now, so, I don't… I don't feel close to those challenges.
**Hannah Ramadan** 28:04 What's the, in alignment with 2361? What's that one?
**Kayla Reopelle** 28:09 I think that's sports PR.
**Hannah Ramadan** 28:11 Oh, okay.
**Bart de Water** 28:12 Yeah, that's right, because specifically the, the step, DSL attributes, they suggested those to be under rails, and I'm like, well, that makes sense, that does seem, like, pretty specific to… What we're doing here.
But then whether, you know, all, like, you know, of active jobs should be under messaging, I'm like, I don't know.
**Kayla Reopelle** 28:36 Yeah… Yeah, and I don't know, is it more complicated than if you're writing queries that some of them start with Rails ActiveJob, and others start with Messaging ActiveJob?
I guess that adds maybe one more wildcard.
**Bart de Water** 28:51 Exactly, and that's the part where I'm like, that feels to me like, you know, we should pick one or the other.
**Kayla Reopelle** 28:57 Yeah, yeah, I think… That's what I'm leaning towards as well, like, we don't usually… Partially my greatest semantic convention.
you know, just thinking about, like, the semconf opt-in environment variable, you would probably have all the conventions the same, and then something to turn on, like the rails.
Attributes, but that would be for all of your attributes at once.
**Bart de Water** 29:24 Yeah, and Ariel did volunteer to, Or at least asked James to, you know, come up with a proposal, so maybe we also just need to wait for that.
**Kayla Reopelle** 29:39 Yeah, okay, that sounds good.
And messaging is also in a little bit of a trickier spot than, like, database or HTTP conventions, because last I looked, they didn't have a clear plan or timeline for moving them to stability, so we won't really have a… firm, like, guideline or recommendation from the semantic conventions maintainers for a while.
**Bart de Water** 30:06 Yeah.
So, then… on that… if that, you know, is going to stay in flux, then for consistency's sake, I would say, like, here on line 26 and 27, should it then be back to messaging.activeJob, because that's at least consistent with the rest?
**Kayla Reopelle** 30:27 That's… that's where I'm leaning, just based on… what I've looked at this morning. I think before… I'd rather not make that call.
right now, I think…
**Bart de Water** 30:39 No, yeah.
**Kayla Reopelle** 30:40 I want to reread, like, James's comments, but I'll add a comment to that effect with my recommendation after I can take another look.
**Bart de Water** 30:49 Alright, well, that I appreciate, and thank you for taking the time.
**Kayla Reopelle** 30:53 Yeah, no problem. Thank you for submitting this. We've… I think we've needed this for a while, and so I was… Pleased to see your PR, and sorry that I couldn't spend more time.
**Bart de Water** 31:02 Yeah, no worries.
like, for context, it's like, I'm sort of, like, investigating what it'll take to migrate off of job iteration, and then it was like, well, like.
**Kayla Reopelle** 31:10 Mmm.
**Bart de Water** 31:11 this will be useful because now, you know, like, one job does not equal, like, one long iteration. You know, they can be multiple.
**Kayla Reopelle** 31:22 Yeah, that makes sense.
Alright, cool. I guess I'll add… A link to the… Conventions issue in our notes, too.
**Hannah Ramadan** 31:40 Thinking just, like, through that one a little bit. ActiveJob, I mean, like, can be used without Rails, right? So… I mean, I don't know how common that is, but would it make sense to… Well… Nevermind, I think the more… I don't know, I'm thinking about it more, I just… it feels like maybe it should remain under the messaging domain, but, Yeah, I'd be curious to… to, like, hear what James thinks more.
Feels like an interesting deviation from everybody else.
**Kayla Reopelle** 32:54 Okay, that was a good chat.
Alright, anything else that people want to talk about today?
Cool, I'll take that as a no. Thank you, everyone, for coming.
And I will see you next week.
**Hannah Ramadan** 33:31 Well, thanks, Kayla.
**Bart de Water** 33:32 Have a good day.
**Xuan Cao** 33:33 Bye.
