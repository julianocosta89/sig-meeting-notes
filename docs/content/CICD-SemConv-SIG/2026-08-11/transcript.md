SIG: CI/CD SemConv SIG
Date: 2026-08-11
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Alan Clucas (Pipekit Inc)** 00:23 Hello?
**Adriel Perkins** 00:24 Dang, good day.
How are you?
**Alan Clucas (Pipekit Inc)** 00:29 I'm alright, how are you?
**Adriel Perkins** 00:31 Doing okay, thank you.
Happy to finally be able to join again, even though, like, I'm still… Technically not here.
Because I'm driving.
**Alan Clucas (Pipekit Inc)** 00:54 I've missed quite a few, so…
**Adriel Perkins** 00:58 No worries.
Is it just us so far?
**Alan Clucas (Pipekit Inc)** 02:01 Yeah.
**Adriel Perkins** 02:07 Be a sparse crowd now today.
**Alan Clucas (Pipekit Inc)** 02:18 So… No apologies in the channel, but I'm useless at doing them as well, so…
**Adriel Perkins** 02:24 Man.
So, do you and, did you already do your talk, or is your talk up and coming with, Robert?
**Alan Clucas (Pipekit Inc)** 02:33 That talks in October.
Okay.
We've also submitted it to… Well, we also submitted it to KubeCon… Salt Lake, and that was rejected, but it's also in for Observability Day.
On the co-located.
**Adriel Perkins** 02:52 Okay, sweet.
**Alan Clucas (Pipekit Inc)** 02:53 for Salt Lake, so… and we haven't heard back from that. The date for that's a bit further off.
Excellent.
Comment.
Yeah, so… might be doing it. I think there was a third submission. I think, Robert submitted it For me. He's, he's relieving this one.
Nice.
Yeah.
And, as of about 2 hours ago, I've released the version of Argo workflows with tracing in it, so…
**Adriel Perkins** 03:25 Nice!
**Alan Clucas (Pipekit Inc)** 03:26 GA, so… Connection.
**Adriel Perkins** 03:28 Congrats! Woo-woo!
**Alan Clucas (Pipekit Inc)** 03:30 At last. It's not got any of the SemCom stuff in it, but that's… that was a future problem.
It's a now problem.
**Adriel Perkins** 03:41 So now is the future.
**Alan Clucas (Pipekit Inc)** 03:42 Yeah, it doesn't conform to SemCon at all, but I'll give that a go in secret, because my employer doesn't really care.
They should do, but it's hard to explain to them.
**Adriel Perkins** 03:56 Yep, no, Hunter's… Hunter… I get that, for sure.
**Alan Clucas (Pipekit Inc)** 04:01 I will attempt to do it, and then actually be able to give feedback on… What works and what doesn't work for.
Virago.
**Adriel Perkins** 04:10 It's funny, because, like, I think… I feel like… Like, almost every company's like, we want better observability, but, like, Few are willing to… a few, like… Understand and are willing to put the effort into getting there.
**Alan Clucas (Pipekit Inc)** 04:30 Yeah, they all like it when it works, but… Sort of don't… just sort of muddle through when it doesn't… So… Yeah, but we… one of the things I'm trying to push for is And admittedly, it's not… it shouldn't be top priority at the moment, is that one of the things we can sell As I… company… we're a… we're not an open core thing, but that's sort of the closest to our model. You know, we've got… our workflows exist, and we build a enterprise UI and stuff on top of it. And one of the things we can do is, and we already do it for metrics, is, you know, integrate that all into a single pane of glass.
Because the metrics you care about are very well defined for a workflow.
And then do the same thing for tracing, and, you know, be able to click around between all the different views of your workflow, including going into the traces for it. So, it all makes sort of sense, but… And is… is a big selling point versus building all the different bits separately for… especially for our core businesses, which are, like, data process… or data analytics-type companies, where the expertise is… I've written a Python program once.
**Adriel Perkins** 05:49 Yup.
**Alan Clucas (Pipekit Inc)** 05:52 So, yeah.
**Adriel Perkins** 05:53 Cool.
**Alan Clucas (Pipekit Inc)** 05:55 That's where I'm trying to get us to, and then… Obviously, it helps with it.
conformant.
**Adriel Perkins** 06:01 Yeah, absolutely.
I'm curious, though, how it'll play out with the, Usage of pipeline versus workflow term.
Yeah.
It'll be interesting.
Let's go!
That makes two, right? So that's Jenkins… well, technically four.
GitLab, GitHub, Jenkins… Argo workflows.
**Alan Clucas (Pipekit Inc)** 06:36 Yeah, well, Argo's not conformant yet, so that's… it does tracing, but all the traces were invented before.
this SemConv even existed, because I wrote them, like, a year and a half ago, and then it was minimum effort to get it.
In and released, and then get people shouting at me about what works and what doesn't work.
But yeah.
**Adriel Perkins** 07:01 That's always the fun part.
Boom.
Well, I don't have anything, and I guess no one else is gonna be able to make it today.
We've got…
**Alan Clucas (Pipekit Inc)** 07:15 Somebody else has arrived, just called C.
**Adriel Perkins** 07:19 Oh, okay. Cool.
Hello.
**Alan Clucas (Pipekit Inc)** 07:25 Hello.
**Adriel Perkins** 07:35 Cool, well, welcome.
Did you have anything today that you want to discuss, Alan?
**Alan Clucas (Pipekit Inc)** 07:41 No, no, I… mostly just showing my face to make sure I… Remember who you guys are.
**Adriel Perkins** 07:48 Great.
**Alan Clucas (Pipekit Inc)** 07:49 Yeah, and listening. So, no, nothing to bring up.
**Adriel Perkins** 07:55 I'm gone. Yeah, me neither. I'm still kind of, like, trying to… Get back into the swing of things, so… Ho- hoping to… Get the, start working on the infrastructure.
fixes, so that we can start adding instrumentation into those shared workflows within OTEL.
So we can see the ENV propagator work within GitHub, and then…
**Alan Clucas (Pipekit Inc)** 08:23 That'd be cool.
**Adriel Perkins** 08:24 the… The Tekton folks have directed me to open up a TEF.
First, Right. So we'll be opening up a temp, a TEF for… conformance. I don't… this is, I guess that's the way I'd phrase it, but,
**Alan Clucas (Pipekit Inc)** 08:47 Do they already have any traces omitted?
**Adriel Perkins** 08:50 They do, yeah.
**Alan Clucas (Pipekit Inc)** 08:51 For the actual workflows.
**Adriel Perkins** 08:53 Yeah. In the same way, though.
**Alan Clucas (Pipekit Inc)** 08:55 Yeah, and…
**Adriel Perkins** 08:57 When I… So, like, we use, I use it on a side project, and… I wanted to see, in part, like, the tracing. Also, there were just some tenancy things that, like… I liked… From there, so, like, it worked a little bit easier for the tenancy things that I was trying to do.
And so on.
I tried that, but the traces were really hard for me to, like, sort through.
So, like, it was hard for me to understand, like, what trace set of spans was attached to my… specific brand.
And, like, because they're very much… they feel very much like just the controller doing the things, not necessarily, like, the information about the learn itself.
And so,
**Alan Clucas (Pipekit Inc)** 09:55 When I was, like…
**Adriel Perkins** 09:57 Sorting through those spaces, I just was struggling a little bit, in part because, like, I am used to the CICD semantics, so, like.
I think my head probably was like, hmm, like, I should be able to see a pipeline here. Oh, I can't see a pipeline here. What… what do I search for?
So, I don't know, I'm gonna open up a tab. But I've got to really, like, deeply analyze those traces further, because it's, like, really hard to figure out, like, where it would even go.
Okay.
**Alan Clucas (Pipekit Inc)** 10:27 So… All right, I should probably have an explore of this, because that's interesting information, and see what they've done, and how I could learn from it.
**Adriel Perkins** 10:38 Yeah.
I mean, I'm definitely happy the traces are there, and, you know, they have information.
just this specific… method of which I use pipeline traces was really difficult for me to shift mentally, so… Maybe next week… well, I don't know if it'll be next week, because I'm supposed to be out of, like, out of town next week on vacation.
Finally.
I like to hope it's a real vacation.
you know.
**Alan Clucas (Pipekit Inc)** 11:10 Nice.
**Adriel Perkins** 11:11 But, assuming that I am.
Which, yeah, I leave that day, so I probably won't be here, but… I am, since I am taking vacation, it means that I get to chill and, like, not work on work, but instead of work on things I want to do.
wildlife chill, so… Probably.
See if I can't write something down.
For that. Okay.
But I have a… I have a system up and running with, like, real pipelines running, so, like, it'll… I can share the traces.
Okay.
**Alan Clucas (Pipekit Inc)** 11:51 Yeah, yeah.
I'm… I'm gonna investigate, because, yeah, it's definitely interesting.
And… Well, I'll share it. I don't know anything in particular.
**Adriel Perkins** 12:03 Yeah, cool.
Alright, well, that's all I had. Anything else from anyone?
Alright, well, y'all have a good rest of your day. We'll see you out there in the main channel.
**Alan Clucas (Pipekit Inc)** 12:20 Alright.
Bye.
