SIG: Java SIG
Date: 2026-03-05
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/1yExftIsUwGg6_rBxgYO8xjciMHcLo-7mbU_ixssOMYYNQTaGMICCOxzCC3xWiE.OpzYocYSWtIU_e2y
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 04:41 Hey, Steve.
**Steve Rao** 04:42 Yeah, hi, just to see you again.
**Trask Stalnaker** 04:45 Long time no see, yes.
**Steve Rao** 04:48 Yeah, I have an issue to discard today.
Yeah,
We have finished the development of our new distro, and we start to provide the service for our users in February.
**Trask Stalnaker** 05:07 And, thanks.
**Steve Rao** 05:08 Yeah, in this process, and yeah, the issue I provided is the problem we found from our user site recently.
**Trask Stalnaker** 05:17 Great, great.
Let's see…
Or a framework… Native Instrumentations.
Right.
Okay…
**Steve Rao** 05:51 Yeah, you can see the OK, interceptor in the stack trace.
Yeah, I found, in some implementation in our Java instrumentation.
we used the extension point from the framework, and yeah, in this process, we thought TriCast to avoid some…
ESAP, reception.
And, yeah, sometimes if we, make some mistakes in the…
Observability, logic, and it will influence the user's request.
**Trask Stalnaker** 06:39 Oh, I… I understand, I understand what you're saying is the… the extension point…
Right, right, for the distro extension points.
Okay.
Yeah, I would just, I mean, if you… probably the easiest thing to do is to just send a PR so that we can kind of…
Talk through specifics.
**Steve Rao** 07:12 Okay.
Okay.
**Trask Stalnaker** 07:15 Because, we can look at, what, Instrumenter 309?
**Steve Rao** 07:22 And it is the, solution is to add,
Track has to the start and end in… in… Instructor method.
**Trask Stalnaker** 07:43 So, it's not quite lining up, probably because it's a different version. Do you know which…
**Steve Rao** 07:52 Let's see, SDK span end, spanned end, okay, so it's…
**Trask Stalnaker** 07:58 And, okay, so it's one of these…
Oh, I see, and it's calling span processor.
So it's your spam processor that's throwing the exception? Yeah.
**Steve Rao** 08:10 Yeah.
**Trask Stalnaker** 08:13 I see.
So That's a good question, whether… I mean… Because you could argue… For example…
The… what are we calling here? Multispan processor…
I mean, potentially… Could try a catch around, you know, each one of these.
**Steve Rao** 08:47 Yeah, yes, yeah, this is also a solution.
**Trask Stalnaker** 08:56 For this particular case, I don't know if we'd want to try catch around this…
**Steve Rao** 09:05 Yeah, if we track as, here, yeah, it's also another solution, and, it can,
But it will cause a problem. In a normal case, there are two track ads.
Yeah, because in our, instrument, instrumentation, we, we will add track ads by, by the body.
**Trask Stalnaker** 09:36 You know, add… Oh, by Bite Buddy?
**Steve Rao** 09:39 Yeah.
**Trask Stalnaker** 09:41 Where do you add the try-catch?
**Steve Rao** 09:44 If we add the track has in the, start and end method in, instrumental.
It will cause your double trackheads.
for normal Because, better body will add, track ads automatically.
**Trask Stalnaker** 10:10 Yeah… I'm not sure about… adding, adding try-catch… here…
I mean, honestly, in general, I like to know that, you know, we've broken something.
And this… I would, like… I'm not sure about…
Oh, we'd need a good plan on where we wanted to put tri-catches.
I guess… I mean, in theory, you could do try-catch.
**Steve Rao** 10:57 Here, yeah.
**Trask Stalnaker** 10:58 And… And you could fall back to parent, returning parent context.
**Steve Rao** 11:10 In our, current, temporary solution is add the track as in, the start method shown in the, screen.
But, yeah, maybe we… I can use the…
**Trask Stalnaker** 11:28 Problem because users are implementing bad spam processors.
I mean, cause you could also…
you know, your spam processor, you could add try-catch in your spam processor.
**Steve Rao** 11:43 Hmm.
Yeah, okay, I can compel the different solution later, and choose the better one, and we can also discard in the PR, if necessary.
**Trask Stalnaker** 12:04 Yeah, maybe… I mean, I think it would help to have, kind of, concrete proposals, maybe a
You could lay out a… Couple different options.
Because it would be… a pretty… it's… quite different…
Let's see, so when this bubbles up, let… yeah, that's a… let's see, where does this bubble up to?
Oh, yes.
So, actually… Hi, this is much…
Because… Putting it here…
is similar to in Byte Buddy, where we suppress throwable.
**Steve Rao** 13:10 Hmm.
**Trask Stalnaker** 13:10 everywhere.
We do that because that is sort of the intersection of where the user code calls our code.
When we inject the bike code there.
And so, the equivalent Where we're injecting…
Classes, like this, into the chain.
Is the user code
Right, is… this is the user code here, and we've just wired in our tracing interceptor.
So… I think I would put it… In the tracing interceptor.
**Steve Rao** 13:57 Okay, but, if we do it like this, maybe we need to add trackers in Avi in this chapter.
**Trask Stalnaker** 14:09 Yeah.
**Steve Rao** 14:12 Okay, you, you think this is necessary?
**Trask Stalnaker** 14:15 I don't think it's unreasonable.
We can… We can do a little bit better, wow.
I don't know, it's… That's just my first, I can ask…
I want to put it on the agenda for tomorrow, I can see what Lori thinks.
**Steve Rao** 14:39 Okay, good.
**Trask Stalnaker** 14:43 Just… We're just gonna change this to…
Oh, it's Thursday, but we're gonna change it to General and say… Trask for Steve.
**Steve Rao** 14:57 Okay.
**Trask Stalnaker** 15:00 Try catch to…
Yeah, because otherwise, like, right, the… you could put it in…
Instrumenter, but that's not gonna cap… that's not gonna stop any bugs in this code.
**Steve Rao** 15:37 Yeah.
**Trask Stalnaker** 15:39 So the only way to really… I mean…
buffer ourselves from the user, is to put it… Here.
**Steve Rao** 15:51 Yeah, it's an easy way, easy solution to stop all prevalence.
**Trask Stalnaker** 15:56 Yeah, and it aligns with the Byte Buddy.
Approach that we already do.
**Steve Rao** 16:01 Yeah.
**Trask Stalnaker** 16:03 But yeah, I'll run up by Lori tomorrow.
**Steve Rao** 16:06 Thank you.
**Trask Stalnaker** 16:08 Yeah.
Glad to hear you all are…
rolling out and starting to get feedback. That's good.
**Steve Rao** 16:17 Thank you.
**Trask Stalnaker** 16:21 Cool. Was there anything else you wanted to chat about?
**Steve Rao** 16:25 Yeah, Husink, do you have any, thing to, Discord.
**Huxing Zhang** 16:36 Yeah, hi, Trask.
Long time to see. Okay. I haven't been a few days, participating in this meeting because,
there's quite a lot of stuff to handle, except for Java, we have a lot of things to…
To, to, too, so…
I haven't been participating in this meeting for a while, but I heard from Steve that you mentioned that you want to bring in a coding review agent into this repo.
So, I…
**Trask Stalnaker** 17:12 Yeah.
I can… Sure, sure. I have just… I have a PR here, This guy here.
And I've… I've generated…
a bunch of PRs, module by module, for it, using it, just to kind of evaluate it.
But you can see…
most… I mean, the… most of it is these knowledge-based articles that I pass
That I guided Copilot, to write for me.
But basically document… it's basically documenting a lot of, sort of, the unwritten rules of our repository.
And then directing the coding agent to use those.
**Huxing Zhang** 18:14 Okay, I see. So it's not, not about,
code review, not only about code review, but you have bringing all the knowledge that an agent could
Implement a feature based on that knowledge.
**Trask Stalnaker** 18:33 Yeah, yeah.
So right now, I'm focused on using it as, to do code reviews, and I want to hook it in the knowledge articles to either the standard co-pilot review, or… yeah, probably that.
But then also, yeah, definitely this should be… and I might not have hooked it up
Oh, I think I did…
at least if you're using Copilot, and I don't know how to do it for others, but I did tell Copilot…
about these knowledge articles. I don't know… I haven't…
Really tested to see if it… uses them.
well.
**Huxing Zhang** 19:30 Yeah, okay. Have you been, using this, to… for the code review already? Or you're going to do that?
**Trask Stalnaker** 19:42 Yeah, locally, I've… what I've been doing for a while now is…
I'll just, for reviewing the PR as… for a first
for the first couple passes I make through PRs.
I will, load the PR locally, and I'll ask Copilot to review it for me, and inline certain comments, I think. Did I…
have, I don't think I commuted that…
But, kind of like this, where… insert inline comments directly into source files.
So I'll… I'll get Copilot's feedback on… a PR…
And I'll use that to then… then I'll look at the inline comments and decide if it makes sense or not, and then I'll post
things that I think make sense to the PR.
And so what I'm trying to do now is kind of automate that.
first… pass… and then, obviously, you know, there has to be human, detailed review, still.
But at least, potentially, we can optimize the sort of… initial…
PR, conversation and getting feedback to PR authors.
**Huxing Zhang** 21:16 Oh, okay, I see. So that you are reviewing the, codes, no coding in your, your no-code desktop, and then you.
manually post that comment, feedback that you think that is valuable, so, to, to the PR on the website.
Yeah, okay. That's what I've been doing for…
**Trask Stalnaker** 21:40 Maybe the last month or so.
**Huxing Zhang** 21:44 Oh, okay. So, yeah, yeah, we actually, we've been doing things for a couple, couple of while, for, for a while. We are already automating, like, things like this, and,
basically, we use the, like, GitHub, OpenAPI or MCP tools. They can fetch the,
Code, internally, and
doing the code review, and then post it back to the, to the, PRs, on the website, so that you can, yeah, you can, you can see the,
coding review.
comments by the agent directly in your PR, in our internal repo, so we have been doing that for a while, and that's…
I think that's a good attempt for our first round of the review, and they will…
The review agent will go through some principles that we have summarized internally, and which we are thinking, in our knowledge base, we think that these, principal rules that they should follow, or…
the things that they may be… pay attention to, something. And we found that the model can give very…
follow this instruction very well, if we're using, like, models like, Serapik.
Models, they, they are doing very well, and they can…
pinpoint some, like, rule violations. If we have, like, 10 or 20 rules, that… we will pinpoint that this behavior, this line of code, well, violates the rules, maybe, which, which rule, and it will give the…
a very good, good, result. I think we… we are… we think that it's very valuable for our developing cycle, very well. And then, this is… AI can do the first round of review, and then we'll do manual review for the second round.
And this is what we have been practicing for a while.
I think this might be, worth,
Doing this, then in this, ubuntu Metro Airport.
can try this approach as well. I'm hoping.
hopefully can, yeah, help with this. If you have any questions, yeah, maybe we can discuss.
**Trask Stalnaker** 24:24 Awesome. Yeah, so we had… in the Java Contrib repo,
I did turn on Copilot, automated co-pilot reviews.
So, like… Like, this was actually… I sent a PR today that it actually gave me a good
Caught a good, problem in it.
But I've kind of… it's been a li-
The results have been a little mixed.
Not… Some have been…
Good comments, some have been less good comments.
But I haven't focused on…
Like, having a knowledge base for this repo, it's just…
We have a style guide, and we kind of let…
So I think that's part of the problem.
Yum.
the instrumentation… I've been really hesitant to turn it on in the instrumentation repo, just because it's high, volume until I had a little bit more confidence.
but yeah, I would love,
If you've got any, either kind of… Specific…
Things that have worked or not worked, or if there's anything you can share, like the instructions that you gave it.
Yeah, I'd love to, you know, just ping me on Slack, send it over, because…
this is kind of…
My project right now, trying to get something like that going here in the instrumentation repo.
**Huxing Zhang** 26:09 Okay.
So, in general, if you're using Copilot to review, so it will give you general comments, because he doesn't have the domestic knowledge. So, actually, in GitHub, there is a custom review guidelines, like.
you put a special name, I think it's called GitHub Compiliter.
distraction or something like that. If you put, things in that, yeah. And then there will… you can put, yeah, specific projects, specific, things, rules there.
And it will automatically grab… grip it and, giving you feedback based on the, that,
Not marked on file, yeah.
**Trask Stalnaker** 27:00 Now, are you using the built-in Copilot, because… review, because I don't know, I couldn't figure out what model
the co-pilot Review uses, and… Certainly, I get a lot better review,
code review when I run locally with one of the, you know, the, top models.
**Huxing Zhang** 27:28 Yeah, we're not using…
the GitHub co-pilot, we… we… we develop our, an agent that can call… actually, can call cursor.
you can use Cursor's CLI to choose a specific model that you want, and you're doing a review. The review is happening
inside the cursor agent. The cursor agent actually, pick up some… first, you'll fetch the code from the GitHub repo, and then
Neither will to review And locally, NSN send the comments back to the… no platform.
That's what our process.
**Trask Stalnaker** 28:18 What model are you using?
**Huxing Zhang** 28:21 We're using Anthropic.
**Trask Stalnaker** 28:24 the model, yeah, wasting, let's…
**Huxing Zhang** 28:28 Behaved the best.
I'll pass, I'll pass 4.6.
**Trask Stalnaker** 28:32 Oh, nice. Okay.
Cool, yeah,
I think that's a good choice, and that's what I'm nervous about. I'm not sure if, the…
built-in GitHub co-pilot review.
Will be as good, because you can't Pick your model.
And… Whereas when I run it, locally.
Yeah, I can, like, when I run the code review agent locally, I can run with Opus, or Sonnet, or Codex, whatever I want.
Actually, what I was doing for these
when I kinda, was generating
the current batch of PRs. I actually had it run once with, Sonnet and once with Codex, because they both kind of picked up different things.
**Huxing Zhang** 29:31 Okay.
**Trask Stalnaker** 29:32 I would be interested to… yeah, I think, actually, that's probably worth having it run with Opus also, because
But yeah, they tended to pick up. I did kind of a side-by-side comparison of just…
I don't think I used Opus, I think I just compared Sonnet and, Codex, and they both…
Found things that the other didn't.
**Huxing Zhang** 29:56 Okay, that's good.
**Trask Stalnaker** 29:57 Kind of regularly.
Yeah, so I might do something kind of like what you're…
What you all are doing of… running…
the Copilot CLI, similar to the… the… Cursor, CLI.
to run the code review agent, basically, so that I can pick the model, but I could potentially do that as a GitHub.
Github Action.
So that it could be sort of automated, and I don't have to run it locally.
**Huxing Zhang** 30:35 Right.
**Trask Stalnaker** 30:38 Nice. Yeah, good to… good to hear you're having, that was… good to hear you're having success with that.
I totally agree, it's like, it's kind of amazing, like, the finds, because it's very complementary to the things that even, like, I'll notice, like, it'll catch some things that I…
wouldn't catch. So… It's very useful.
**Huxing Zhang** 31:04 Yeah, yeah.
And, I… actually, I would like to ask another question So…
So, Trask, do you… will you plan to attend the Cook County EU this year?
Because I'm going this year, and .
**Trask Stalnaker** 31:24 Oh… No, I'll miss you.
No, I'm not… I won't be there.
**Huxing Zhang** 31:30 -Oh.
You're not going there.
**Trask Stalnaker** 31:33 Yeah…
**Huxing Zhang** 31:35 Oh, I thought you, you, you, you would, would be there, and, maybe we could meet there, I think. So, do you, do you know any maintainers, well.
And we'll join, we'll be… attend the… who can't you guys hear that?
**Trask Stalnaker** 31:52 Yeah, I think a lot of people are, from the Java side, I… I suspect that…
Jack?
We'll be there… Let's see, there's a… there's a… here, let me…
give you a thread, there's a Slack thread in the Hotel Maintainer's channel.
Where people are… Thing.
If they're gonna be there.
I don't see Jack commenting yet.
So, not sure… Also, Jason Plum from the JavaSig usually goes…
But there'll be a bunch of people from other… SIGs, also.
And they'll have the, the OpenTelemetry… booth.
**Huxing Zhang** 33:04 Yeah, I'm interested in connecting with you in the EU, so please ping me, any information if you know that, anyone would be there, and maybe we can chat about,
Hotel, anything.
There.
**Trask Stalnaker** 33:23 Okay.
Yeah, yeah, sorry I missed you this year.
**Huxing Zhang** 33:27 Yeah, I'm glad to meet you, yeah. Yeah.
**Trask Stalnaker** 33:31 Yeah.
Hopefully in the future, future KubeCon.
**Huxing Zhang** 33:39 Okay.
**Trask Stalnaker** 33:40 Alright.
**Huxing Zhang** 33:42 Good to see y'all.
**Steve Rao** 33:43 Yeah. Bye.
**Trask Stalnaker** 33:45 Take care.
**Huxing Zhang** 33:46 Bye-bye.
