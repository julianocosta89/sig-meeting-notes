SIG: Semantic Convention SIG
Date: 2026-03-02
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/VnnNuYDp_4I0xx3h3NR2g6jrgW8R8ZFCQhs2gR75vZvB9c_mfGsZQS4ZMOIMAYNG.FJJgQtREprVy4ocT
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:00:44 This is newer!
Trask Stalnaker 00:00:46 Let's see…
Liudmila Molkova 00:00:55 It's… it's, it's just, I don't know, an avatar.
Trask Stalnaker 00:01:06 I started chatting with it here, see if it respects any… Any commands.
Liudmila Molkova 00:01:14 Oh, in private?
Trask Stalnaker 00:01:16 Yeah.
Oh, I missed the… I see they sent a message to the general channel.
before I joined.
Liudmila Molkova 00:01:29 Oh, right. And I, I told it, you don't see it?
Trask Stalnaker 00:01:34 I see your response, but I can't see its initial… Post.
Liudmila Molkova 00:01:41 It's saying, waiting for the Zoom host permission to begin taking notes and recording.
Trask Stalnaker 00:01:49 Yeah, that is interesting.
Wow.
Liudmila Molkova 00:01:56 I think it just pretends.
It's why I recorded over the weekend.
Not sure whose turn it is to derive the call, I can do it. Give me just one second.
Trask Stalnaker 00:02:20 We should write our names on the, in the meeting notes, who drove each one, so that we can actually remember.
Josh Suereth 00:02:38 I don't know if I've done it in a while, if you want me to take a turn.
Liudmila Molkova 00:02:42 I'm almost ready, yeah.
Josh Suereth 00:02:46 I just feel bad, I think it's literally been, like, a month and a half or two months since I…
Liudmila Molkova 00:02:50 Yeah, then go for it. I wouldn't mind.
Josh Suereth 00:02:53 Okay.
Alright.
Let me make sure I can share.
Yeah, let me copy…
This is the right one, right?
Just 20 seconds, yeah.
We have a bunch of notes. Oh, I have notes.
Okay.
Let me copy-paste these, then.
And folks, feel free to add your topics.
We'll do a little bit of triage, since we need to make progress. Alright,
C… To find messaging exception events, Ready to be merged.
Awesome.
Alright, switch to Markdownlint CLI 2. Let's take a look at this one.
I think… Did I move this there?
Oh, great.
Okay, so this one is,
using Markdown Lint CLI2 action. If you haven't used that instead of Markdown Blint, it has a GitHub action. We started using that in our makefile, I believe? Or no, this one moves us to it.
I've been using Markdown Lint CLI 2 now. I like it. I think it's a little bit better of a design.
I think we started moving other parts of, OpenTelemetry to Markdown Lin CLI 2, if I recall correctly.
Trask Stalnaker 00:04:39 I don't remember.
Josh Suereth 00:04:41 What was that, Trusk?
Trask Stalnaker 00:04:43 I don't remember, sorry.
Josh Suereth 00:04:45 Okay.
I think what this does, though, is, yeah, package lock changes because we start using the CLI 2, and then, there's a config for the CLI 2, for, like.
ignoring front matter, and what to pay attention to. And then I think the only contentious part, and I believe this changed, was now there's recommendations in VS Code to use this, and the git ignore has changed, right? So,
Yeah, using the GitHub action, I think, is slightly better than using run make markdown lint, just from a caching reason.
Yeah. I think… I think this one's pretty good to go, if anyone wants to take a look at it.
I can quick approve this, because my concern was addressed.
And we'll head back.
Oh, was I not sharing?
I was not sharing anything I was looking at, was I?
I am sorry.
I haven't done this in a month yet. Here.
This switches to use Markdown Lint 2, it uses GitHub Action, and, the big change.
Is basically,
It starts to fill out VS Code Extensions JSON with recommendations, so that you actually get linting errors in your VS Code, which is quite nice.
So that's actually a big… I think this is huge, personally, because I'm terrible at actually making those changes myself without having an AI do it for me now.
The other thing, was… Yeah, we use,
Yeah, the GitHub action check. So, the make file actually changes to actually have a local NPX run of Markdown CLI 2. And like I said, I started doing this locally myself, and I… I like Markdownlint 2 better.
It seems to be a little bit faster and less, frustrating.
Okay, cool.
Let's, let's move back to the next one.
The needs more approval, GenAI exception event for client operations.
I think this one…
This one is approved from… by the SIG, or… yeah, Ludmella, you represent the SIG, right?
Liudmila Molkova 00:07:11 Yep.
Josh Suereth 00:07:12 Okay.
And this is related to the exception shifts that are happening, right?
Liudmila Molkova 00:07:18 Right, it's less gen AI and more a general, exception, so we are looking for another
Approver here.
Josh Suereth 00:07:28 Cool.
Alright.
Let's go on to the next one. We normally do… do we normally do need some more approval, or do we start with blocked? I'm just remembering that.
maybe I'll just highlight these for people to review, and then we'll move on to blocked.
Okay.
Defined reasoning tokens attribute, that one also needs more approval.
I'm not gonna open all of these,
JSON schema definition for GenAI tool definitions.
Another one that needs… so lots of Gen AI stuff. Define fast exception event, this is related to the exception changes, right? That's similar to that GenAI one.
Okay.
Yep. Cool. Add V8JSResource.activemetrics and VAJSResource.type attributes.
This one's more interestinged.
Liudmila Molkova 00:08:26 Oh, I think we should move it to the co-donors. We have existing conventions. They were contributed by Marillia, and when something comes up.
We asked Marilla… oh, she approved, and somebody, Christopher approved.
Josh Suereth 00:08:43 Yeah, so I think this appropriately moved over after that, so then we just have to review this now that code owners have commented.
Cool.
Alright.
Then these two that have the little symbol, does that mean they're currently in the process of being merged, or that they are…
Yeah, they're queued for merge. Alright, so those just need to move to ready to be merged, so that we don't, whatever.
Trask Stalnaker 00:09:09 You know what? It's weird, if you open, one of them.
is… I had marked it ready to be merged, and then, so if you scroll down.
Let's see if this is one of them. Yeah, look at that. I put it in ready to be merged, and then GitHub Project Automation Bot moved it from ready to be merged to needs more approvals.
Liudmila Molkova 00:09:31 It happens because there is an automation that says when it's approved, it's ready… it's moved into needs more approval.
And it's not possible to configure it conditionally, and so if it's already…
Cool. We can just turn it off? I don't know.
Josh Suereth 00:09:50 We could… we could also update it so it, like, adding it to the merge queue means it's ready to be merged. Like, we don't… the reason we had ready to be merged, I think, is because we didn't have a merge queue. What if we just get rid of ready to be merged and use the merge queue now?
Like, once you think that…
Trask Stalnaker 00:10:06 I think the way…
Josh Suereth 00:10:08 Oh.
Trask Stalnaker 00:10:09 I think the way that, at least I've used that, has been, like, hey, this is ready to be merged, last chance to look at it, we'll probably merge it in the SUMCOMS meeting.
Josh Suereth 00:10:23 Oh, okay, gotcha, gotcha. Okay.
Liudmila Molkova 00:10:25 Yeah, given how many needs more approvals we have, it's also a signal, I don't know, if I do my morning triage and I see a bunch of things there, and they are not something to raise discussion, I just merge them.
And approvers on their own cannot merge.
Josh Suereth 00:10:41 Gotcha.
Okay.
Liudmila Molkova 00:10:45 Now, Chris, Krista, if you wanted to say something, I saw you.
Christophe Kamphaus 00:10:47 Yeah, I just wanted to say exactly that, that approvers cannot merge it.
Josh Suereth 00:10:54 So approvers move it to ready to be merged. That makes sense. Cool.
Alright.
Got it.
Let's go back to… okay, so we have these two, which I'm gonna slide… I'm gonna slide them over and see what happens.
We'll see if they slide back during the meeting. Alright, stabilized deployment environment is blocked. I believe this one was, around moving it to a new, is that correct?
Trask Stalnaker 00:11:22 Yeah.
And there's a PR up for that now.
Josh Suereth 00:11:26 Yeah, so I think we decided… I wasn't sure if they were going to hijack this PR and change it to be the… moving to a Noom.
Add the new values… Is it a separate PR?
I think they just changed this…
Trask Stalnaker 00:11:43 No, they didn't. No, there's a new… There's a new PR, yeah.
Josh Suereth 00:11:47 There's also a new PR, cool.
Maybe we should just reference that on this PR so we don't get confused.
Okay, cool. Switch Front Matter to Markdown. Let's just see if, this has had… I know that, Patrice was working with James on this.
It's been removed from the front matter property in this reordered. Let me know if there's anything else.
Inspector Coleman.
Discussed it separately.
Okay.
Yeah, this one's still in progress, it looks like.
So we'll leave that one there.
switch TOC generation to Dock TOC?
Okay.
This is another one we'll have to look at, what is this blocked by?
Oh, I should click further down.
as clean as we can. We probably don't want to wait a few more weeks. Let's assume that…
In the meantime, to streamline this PR, we can resort to simple Perl, search or place for post-processing.
Oh, by the way, great job on the improvements you contributed DocToC.
It looks like this is blocking our website.
Christophe Kamphaus 00:13:35 I think he put a workaround in place, so I don't think there's anything blocking here.
Josh Suereth 00:13:41 anymore.
Alright.
I still… I still would prefer to let, Patrice get back and tell us if this is gonna work for the, front end.
It might be a good idea to start getting folks to review this in the meantime, though.
This is another one that switches from using our make tools to using
No, it still uses our main tools.
Yeah.
Liudmila Molkova 00:14:13 So I think there is nothing to review if…
This is changed, and Patrice is asking James to change.
the markers, and if… If there is no strong reason to change markers.
Not sure why would we do this.
Josh Suereth 00:14:33 Yeah, what is this postscript thing doing? Do we know?
Liudmila Molkova 00:14:39 It's Burl, you know it's Josh.
Josh Suereth 00:14:42 I, yeah, why is it in Perl? And that, that, that, maybe I'll make a comment on that, of, like, can we please limit the number…
Trask Stalnaker 00:14:50 of languages.
Josh Suereth 00:14:51 remember how to use. What?
Christophe Kamphaus 00:14:53 It's the workaround that's in place until, DocTok.
Supports custom pre and post tags.
Josh Suereth 00:15:03 Okay.
Trask Stalnaker 00:15:05 Python, please.
Josh Suereth 00:15:09 You what? Python, please?
Trask Stalnaker 00:15:11 Python.
Josh Suereth 00:15:12 I'm fine with Bash, too, honestly, but I… yeah, just… or not… not, like, yet another language.
Ugh.
Just to be clarified.
Trask Stalnaker 00:15:29 Or Bash, yeah, I would fully support shell if it's simple.
Josh Suereth 00:15:33 Bash for something.
Where we can limit the number of technologies needed.
to generate…
Mark down.
Okay.
Cool.
I'll make that as a comment. Alright. I think that is all the blocked ones.
Do we go through a waiting co-owner's approval or end triage, or do we move on to the topics?
Liudmila Molkova 00:16:08 I sometimes go through entreeged, but we can move to the topics.
Josh Suereth 00:16:13 Yeah, I think… I think we have a bunch. This is one I really, really, really want to talk about, but…
I will add that to the topic for later. Alright.
Cool, let's, let's move on.
Oh, we have the Issue Triage Board. I'll… we'll get to that later.
Ludmila, why don't we start talking about, event naming and severity for exceptions?
Liudmila Molkova 00:16:36 Yes, I wanted to share,
The part that we've been working on, in LogSig?
And we're trying to clarify
how to create exception events. Trust created a bunch of them for the, like, the actual pieces, HTTP, RPC, messaging databases, boss? Gen AI! And this summarizes the guidance that, be behind them.
There are two pieces, oh, three pieces. The first one…
when you report… like, this is the guidance for instrumentations, primarily. So, like, you're instrumenting, let's say, an operation.
And it's an open telemetry instrumentation. How do you record exception? So this is the replacement for the record exception span event.
So the first thing we're asking, it should be an event, it should not be just a log record.
So, if you're a user application, you can do anything, but… or if you're a log bridge, you just pass through what you've got. If you're writing OpenTelemetry exception event, it should be an event.
Second, it follows the… some pattern, which is, like, the operation that's failing, like HTTP client request.
It would be the spend type, if there is a spend.
And it should start with the separation name, and followed by exception.
So, in theory, somebody can use ends with exception.
As a way to filter on the exception events.
We are asking conventions to document this thing.
So if you're writing instrumentation, you have a convention, you should have convention for span, metric, and
Exception event.
Then there is a guidance on how to set severity.
What we are saying.
And I used to have OTAP on this, but it's actually… I'm not sure, like, we decided that it's not the OTAP, it's more of a guidance and semantic conventions.
So I have guidance when to set which severity.
it came from .ap, and it says if it's FATO, sorry, if it's the…
Application ending situation, panic, out of memory. Invalid configuration, it's fatal.
If it's something, that… Severe?
Like, it… you return an error response, you're in a server.
like, the root level instrumentation. It's the server, consumer instrumentation, and you…
detecting an error, it should be It should have error severity.
It only applies to, essentially, server and consumer spends. Like, in the places where you would create server and consumer spends.
Or in similar places where you know it affects your remote caller.
If it's something internal to the application, you assume your exception will be caught or handled in some way.
It doesn't mean it will be, but you expect it.
So if you're in the client-producer situation, you would report it as warning.
There is no info.
then… debug. It's… it's like exceptions that are…
alleged, but not important. So, for example, my caller remote caller.
Started the request and then canceled it. I get an exception on my server.
It's not an error situation for me, it's a totally valid case. I haven't… it had nothing to do with this. It's a debug. And there is everything else that's essentially trace. For example, I don't know, in Python, it's common in FastAPI and other places to return exception instead of error code.
Those exceptions are effectively recorded at trace, because they don't convey any… any special information beyond just error code.
Any questions so far?
Okay, then the last, is that we did not come up with a guidance on
When to add extra attributes, but we are saying that
It could… there could be an opt-in option that just adds
span attributes. If you have a span, you can enable setting demo exception event, so it's… it becomes useful without a span.
So, to summarize, it replaces record exception.
Span event, and it's important for instrumentations to start sunsetting the
Span events that are in the process of deprecation.
Trask Stalnaker 00:22:25 And for some context on, I've been sending
PRs for these specific exceptions as I, am working on, and we have a…
an environment variable in SEMCOM now to opt-in to emitting these things as events instead of spam events.
And I've been implementing that in Java, and hoping that with the, the 3.0, Java 3.0 major version bump in the first half of this year, that we will make that cut over.
Josh Suereth 00:23:21 I have one concern about this here.
But I don't know if this affects any other language but Scala.
So, there's a trick that Scala uses, with lambdas, and it has a return statement, and the return statement could be nested inside of a lambda in an expression.
And so what it will do in that case is it'll throw what's called a non-local return exception, which has the value of the return statement in it.
in the lambda. And then whenever it has a call to a lambda that has one of these returns in it, it will, because you… to have a return, you have to be in the same lexical block of code, it will put a try-catch around it, and if it catches that specific exception, it will return the return value.
And if you're in the middle, and you get one of these values, you have to propagate it, but you shouldn't log it. You shouldn't even trace it, really.
Because it's actually an expected part of the flow.
Liudmila Molkova 00:24:19 I think, or, if recorded.
Should not record this artificial exception, or if recorded, should set the severity to trace.
Trask Stalnaker 00:24:31 I think we agree that those should not be recorded.
Maybe we just need to make it that…
clearer that that's the ideal. But in general, you would have trace off. Although, yes, even if trace was on, yeah, you wouldn't even want those.
Josh Suereth 00:24:51 Yeah, you could, if you want, you could, like, put a… put a comment about that non-local return shenanigan thing.
I just remember running into a lot… that a lot in the past with, like, generic try-catches.
Liudmila Molkova 00:25:04 Can you leave a comment, and I'll make sure to… Yeah. Let's think about it.
Josh Suereth 00:25:11 Okay.
The other thing I wanted to ask, though, is,
You're saying if you don't know.
if your exception is actually fatal, it's always warn. So any kind of library would always use warn.
Liudmila Molkova 00:25:27 any kind of client library would always use WARN for the things that are
So, it's rowing to the collar.
Any web framework Server framework would log error.
Josh Suereth 00:25:47 Yeah, so… But the… does the server framework know that the error is not caught?
Look, isn't that true on both sides?
Trask Stalnaker 00:25:59 Well, Jetty, for example, if you're… like, Jetty server is generally the topmost, the first thing that is handling, so…
If it gets an error all the way up there, it knows there's nothing, sort of, for it to propagate.
Beyond, so it would mark it as an error.
If you're thinking of, like, spring, that…
wouldn't be considered a server framework, because that sits underneath Jetty in that case.
Josh Suereth 00:26:31 You know, I'm thinking about something which manages Jetty. So, like, if I'm… like, let's say I start up Jetty.
And I have a thing that wraps Jetty, so Jetty throws an exception.
I will… actually reboot Jetty.
Right? What should the behavior be?
My concern is just, I, like, following this guidance. I'm trying to make sure that I understand
When to do air and when to do warning.
Liudmila Molkova 00:27:00 So if you're… you know what kind of instrumentation you are. If you emit a server span, or a consumer span, or you would have.
Josh Suereth 00:27:10 So you're saying anyone who is returning a server consumer span can use error. Anyone who doesn't should… .
Liudmila Molkova 00:27:18 Yeah.
Josh Suereth 00:27:19 Should use warning.
Liudmila Molkova 00:27:21 Yeah, and if you're, cautious enough, you would see that there is no internal here, because we have no idea what internal spans should do.
Josh Suereth 00:27:32 Yeah.
Liudmila Molkova 00:27:35 But who…
Josh Suereth 00:27:36 for internal, honestly. Like, because internal, I can actually see you going this direction for internal. Absolutely, yes. The only reason it's not there is because we have a…
Liudmila Molkova 00:27:48 background jobs, for which we don't have semantic conventions.
And we decided that once we decide what to do with, like, if we had internal spans in semantic conventions that needed this, or if we had a guidance for background jobs, we would probably feel better being
Specific for internal.
Trask Stalnaker 00:28:12 Java instrumentation currently emits background jobs as internal span.
Liudmila Molkova 00:28:17 Oh, maybe I should replace it with messaging consumer, yes.
Josh Suereth 00:28:23 This example.
Trask Stalnaker 00:28:24 I think we need… that… that seems…
Josh Suereth 00:28:27 Well, we should open.
Trask Stalnaker 00:28:28 Yeah, I would love clarity on that before the major version bump, so that we can align.
Josh Suereth 00:28:39 Yeah, just… just, like, what… what… what is a background job, and how should it be modeled, and
We decided that we wanted to have producer, consumer, and client-server, where one is synchronous and one is asynchronous.
So I kinda get that.
background job, to me, doesn't feel like internal. It feels like maybe its own thing. I don't know if we need, like, a new top-level span kind for that.
Trask Stalnaker 00:29:11 Please, no.
Josh Suereth 00:29:13 Okay.
Alright.
Trask Stalnaker 00:29:18 I can buy into consumer.
Josh Suereth 00:29:20 What?
Trask Stalnaker 00:29:21 I can buy into consumer…
Josh Suereth 00:29:23 I… that's kind of how I'm feeling about… I think you saw my arguments there before. Okay. Alright, I'm getting distracted. Cool. This was a good discussion, though. Thanks for… thanks for pushing this forward. I think, again, getting these kinds of, like, how to write conventions, I think is super critical.
Going forward for us.
Okay.
Any other comments on that?
Alright, next up is stabilizingotel.event.name.
This is Trask.
Trask Stalnaker 00:30:10 Yeah, we're not seeing your screen, though.
Josh Suereth 00:30:13 Oh.
Trask Stalnaker 00:30:13 In the meeting notes.
Josh Suereth 00:30:15 Oh, I'm… the link isn't working. Oh. Oh, you have two links. This is a bad link.
Trask Stalnaker 00:30:21 Oh, God. Fantastic.
Josh Suereth 00:30:24 Alright, cool, I got, I got the link.
Trask Stalnaker 00:30:31 So, yeah, so…
We've talked about this in the past, I think we've got our necessary three prototypes now.
So…
We would like to… my motivation here is, from the Java side, we would like to start automatically
Emitting, When somebody is using a logging bridge, and they…
add hotel event name. We would like to automatically
Turn that into event name.
Cool. And it's pretty important for,
Being able to emit events via… Language logging libraries.
Josh Suereth 00:31:29 Yeah.
Anyone have any concerns with that?
Trask Stalnaker 00:31:41 The naming aligns nicely with the hotel. stuff that we have done for,
internal fields, like span fields, to emit them to, like, Zipkin and Jaeger.
Josh Suereth 00:32:03 Yeah, I was gonna pull those up, I think they're right below this.
We have hotel scope name, we have…
That's the library attributes. Anyway, I was gonna show it off, but it looks gross, sorry.
Yeah, cool.
Anything else to say there? Anyone have concerns, questions?
Alright, let's move on to this one. This is a more fun discussion.
Trask Stalnaker 00:32:31 Yeah, so why don't you go to the issue…
and scroll to the bottom, I…
posted the diagrams that we discussed last Thursday.
to try to explain what I was not explaining well in that meeting.
Josh Suereth 00:33:02 So, I have one question here, and I know that you're gonna hate me for this.
I hope not.
We talked about having the server-related things in the service namespace and having client underneath it, specifically so that if you make a change to the service namespace, it's the same set of ownership of all of those attributes.
So that client actually should be nested in the server namespace, so that the owner of the service namespace, when they make a change to name.
They would also make similar changes to, service client name and service server name.
I know that we don't have that true for, like, client… Client and server today.
with, like, HTTPSNConf.
Which means client and server, I think, technically are owned by HTTPSEMCOM, right?
Trask Stalnaker 00:33:55 But… Tangentially.
I mean, it's not a strict owner… nobody strictly owns the client namespace or server namespace.
Liudmila Molkova 00:34:08 It is the core part.
Josh Suereth 00:34:10 What?
Liudmila Molkova 00:34:10 It's at the core part, it can never be removed from central semantic conventions.
Josh Suereth 00:34:16 I know, I'm just saying, but who's the code owners for it?
Liudmila Molkova 00:34:20 everybody, all the SAMConf approvers, and the HTTP, I think.
Josh Suereth 00:34:26 Okay, which effectively means to maintain… well, I guess my question is, if I make a change to client service name.
in a way that's incompatible with service name, can I do that without getting approval from the service people? Yes.
Today.
Trask Stalnaker 00:34:39 We want to add the service people to the client.service.
Josh Suereth 00:34:44 That just means they're added for, like, possible review. That doesn't actually block it without their approval. You know what I mean? Like, this is the… my concern has nothing to do with the name itself, it has to do with ownership.
Like, it would be totally possible, because of the way that client and server are listed today, that you could get your two green checkmarks, and no one from service would know that you're making a change.
Trask Stalnaker 00:35:08 That can happen already today.
I mean, we can… you get, you only need one… so in… in the service namespace?
Josh Suereth 00:35:18 Yeah.
Trask Stalnaker 00:35:19 if, I'm just gonna… Say, Carlos is, is a, Gen AI approver.
If he approves that PR, that's one.
If I approve that PR, that's 2, and I can merge it. Nobody in service…
Josh Suereth 00:35:37 It ignores coding this?
Trask Stalnaker 00:35:40 No, but I'm a… I'm a code owner.
Right.
Josh Suereth 00:35:45 But you're a general maintainer. I'm fine if general… like, I'm hoping that general maintainers have enough savvy to, like, not allow that to necessarily happen, but it's…
Trask Stalnaker 00:35:54 General maintainers have to hit… general maintainers have to hit merge on everything, so…
Josh Suereth 00:35:58 Okay.
So that's a thing for us to maintain, then. It's more, okay, we can add them to the list of people who get notified of changes, that's fine. But that is my concern, is actually around ownership of these namespaces and making sure that things…
Are updated similarly.
Trask Stalnaker 00:36:18 So the way that I was seeing… viewing this is kind of like the embedded stuff that we've talked about before.
And, you know, it would make a lot of sense in our tooling to understand these embedded pieces, and that could somehow tie to ownership.
Or…
Liudmila Molkova 00:36:40 And not allow you to introduce something that.
Trask Stalnaker 00:36:43 with conflict.
Liudmila Molkova 00:36:44 As the… yeah.
Josh Suereth 00:36:45 Yeah, embedding would actually fix this, yeah, agreed. Okay.
Alright, anyway…
Trask Stalnaker 00:36:51 That said, I have zero… I don't really have a preference on client.service versus service.client. If you have a preference from a naming perspective, I just don't think it…
I would prefer not to…
make a decision on that based on this ownership concept, because I'm not really sure that that quite fits it here.
Josh Suereth 00:37:15 I… I do think… I think there's…
Trask Stalnaker 00:37:16 Better… I think there's better solutions for that.
Josh Suereth 00:37:19 Okay, if there's better solutions, there's better solutions, but I do think we have chosen namespaces specifically around ownership. Like, that's… that is a thing we have done across this ecosystem.
Right? Where, like, different conventions kind of get a namespace in which they live and own. And that's how we're doing directories, that's how we're doing code ownership, so, like, maybe that's a broader question for us to answer. I don't want to get distracted on… let's talk about specific details.
Trask Stalnaker 00:37:44 Client address, like, it also makes a lot of sense for client address to be co-located with client service name. You can make that argument as well, because typically, like, in Java, the way that we calculate, the way that we allow users to
configure, we let them make maps from client.address to… or rather, server.address to server.service name.
So I could make the argument that there's co-location on that side as well.
Josh Suereth 00:38:15 8.
That one…
You're not… so the thing that fills out the client address and the thing that fills out the service name are different, though. You're actually using one to fill out the other. So I'm gonna make a counter-argument to you there.
You don't want the code that looks up the client IP address to have to also fill out service name. That's an optional thing that happens later, and you need some kind of a lookup or external system.
So, I would argue that, like, the system that does the service name annotations uses a system that has client address.
Not vice versa.
Right.
So there actually need to be independent in some fashion.
Liudmila Molkova 00:39:01 It's actually a common story that some attributes are derived from others, and it's sometimes useful to capture it.
formally, like the… I don't know, we have some user agent stuff that's…
under the same namespace, but it's the post-processing that Synthetics, I think, updates
sets the flag based on the content. It's unrelated to your, your, your, your here.
Josh Suereth 00:39:28 Yeah, we're getting distracted. Sorry, I'm just mentioning my overall concerns. I think this proposal, in terms of, like, the shape, is exactly what I think we wanted to do to solve this problem, right?
Liudmila Molkova 00:39:44 I… Really hate the names, like, server, service name.
Trask Stalnaker 00:39:49 I know.
Liudmila Molkova 00:39:49 Super ugly. I spent maybe 15 minutes with my AI.
trying to figure out a better name, and the only thing we came with is Kohler and Kali, but I hate it even more.
So, I'm okay with this name, but, like, it's the best that they can come up with, but…
Still sucks.
Trask Stalnaker 00:40:14 Maybe we need to, go server.application.name.
Make an alien… go ahead, move, start.
Josh Suereth 00:40:24 I was there already, Chess. Yeah.
I'm with ya.
It's too late to change service to be application, though.
Trask Stalnaker 00:40:37 alias it?
Josh Suereth 00:40:42 You're saying, like, anywhere where someone expects service.name, we would say application.name is exactly the same thing?
Liudmila Molkova 00:40:53 To make things even worse, app would mean client app, and application.
Josh Suereth 00:40:59 Yes.
Trask Stalnaker 00:41:03 It's all horrible.
Yeah, I feel that pain.
Josh Suereth 00:41:10 this does solve the issue we needed to solve of, like, we have consistency now between the… between them, right? So, like, here, this makes sense. Here, this makes sense if I'm in the middle.
so, we're down to just…
than naming Bike Shed, right? So I'm not gonna waste more meeting time on naming Bike Shed, let's do that offline. Yeah.
Trask Stalnaker 00:41:33 If anyone has concerns with the shape or, like, why we're trying to do this, you know, please take a look.
Josh Suereth 00:41:39 But yeah, I, like, this consistency of service name is always, from the client, and if I'm in the middle, the service name is the same on this side as it would be… sorry, the server service name is the same here as it would be here. I like that consistency.
We can argue about what the names need to be later.
But the shape of it, I think, is right.
Trask Stalnaker 00:42:04 But let's argue about the name on this PR before we merge this PR, because we've already renamed it once.
Josh Suereth 00:42:13 Yep.
Okay, so let's, let's get that bike shed finalized. So, AI… I don't mind.
The bike shed.
on naming… Service versus application.
Again.
Trask Stalnaker 00:42:28 Versus something… I'm also trying to decide if service. If we did service.server name… Is that any better?
Michele Mancioppi 00:42:41 Oh, look, I came in at the right time.
Trask Stalnaker 00:42:44 Michelle! Yeah, oh, you missed. You, you…
Michele Mancioppi 00:42:49 service.pierre three times, and I appear in a cloud of sulfur.
Josh Suereth 00:42:55 We, we were looking at this, and we like what this does, but we hate the name.
Michele Mancioppi 00:43:03 I don't think anybody on Earth without a giga brain is going to get it.
Trask Stalnaker 00:43:09 Server.service.name? Yeah… that's… that's not good.
Michele Mancioppi 00:43:20 Is that, the point is, for it to make sense, it needs to be counterintuitive.
So you're there, like, I have… I'm on a server span, and I see something on client, and I'm like.
Why?
For things like server.address.
That makes sense, because thinking of the other side at the technological level is something that people have in their heads. But to do this at the logical level is something not even for me clicked. Like, I had to read it 3 times.
I… I was typing a comment saying not Rasky got the paper wrong, and I'm like, no, he didn't.
Josh Suereth 00:43:55 I would argue the same thing's true of Pierre, then.
Ms. Shelley?
Michele Mancioppi 00:44:00 No, Pierre, because, no, no, Pierre has built in the notions that it's the other side.
Josh Suereth 00:44:05 Yeah, but logically, I'm… have one side talking to another. Client-server's a completely logical thing.
Michele Mancioppi 00:44:11 Yeah, but…
the evalu… when you do peer, it's contest-independent. Like, whenever Spain you are, it's always the other side.
Evaluating client.service.name reminds me… requires me to keep in the head that, oh yeah, this is a server, therefore the other side is a client.
And this is what it means.
And this thing here requires a gigabrain. I don't have it.
Josh Suereth 00:44:35 I think that the problem is actually just the name service.
Like, if I want to know what are the clients my service has, looking for service.client.names would make sense. I get a list of all my client names. I just grab all the possible attributes. Here's all the clients of my service.
You know?
If I want to know who my service is talking to.
I should be able to find that as well, but anyway. I think the main confusion here is we called the stupid thing service instead of, like, application or something more general, and now we're getting to networking, where a service is a real thing in Kubernetes.
And when we talk about services, we're really kind of talking about deployments, or sets of deployments, right? We're not talking about services.
That, I think, is the problem.
Michele Mancioppi 00:45:25 Yeah, but it's not a solvable one 7 years in.
Josh Suereth 00:45:29 Yeah.
Well, you didn't hear the bike shedding, where we were like, what if we just call it application here, and we just tell people service and application are the same in some way?
Michele Mancioppi 00:45:41 Oh, that is the worst of all worlds. Yeah.
Josh Suereth 00:45:44 So what I'm gonna keep doing is throw worse ideas at ya, and then we're eventually gonna be like.
Michele Mancioppi 00:45:48 But that's fine.
neil yashinsky 00:45:51 It's well known that on the internet, the best way to get the right answer is to start off by posting the wrong answer.
Trask Stalnaker 00:45:56 I don't know, we've tried, like, 10 wrong answers on this call, and we still haven't gotten to a radio type.
So we haven't gotten close.
Michele Mancioppi 00:46:03 That's smart.
Trask Stalnaker 00:46:04 Right answer.
neil yashinsky 00:46:04 No, we've proposed that… see, that's the problem, is someone needs to come forward and falsely claim the correct answer is this, and then everyone can say why it's not, in my humble opinion.
Rather than just proposing thoughtful things. If the thoughtful is the problem, you don't want to be thoughtful.
Trask Stalnaker 00:46:19 Yeah.
neil yashinsky 00:46:20 You want to be… you want to be thoughtless, and then it's easier to reverse engineer the thoughtfulness on the thoughtlessness, so to speak. Intellectual straw person at a…
That's usually where I add the most value, is, you know, the thoughtless input that reverse engineer provides the right answer.
Michele Mancioppi 00:46:43 You effectively want to recognize the… somebody is wrong on the internet. That doesn't work.
Josh Suereth 00:46:53 The, that may be, generally… Understood and, confusing.
Let's… this doesn't work.
Trask Stalnaker 00:47:03 No.
On PRs, it does if your branch is on the upstream.
Josh Suereth 00:47:11 Ugh, okay.
Well, I'm gonna do something on a hidden tab here, give me a sec.
Liudmila Molkova 00:47:18 I am being there. I have done that. Please do it, but I don't believe the outcome.
Michele Mancioppi 00:47:24 the worst LLM.
Josh Suereth 00:47:26 Yeah.
Liudmila Molkova 00:47:28 So maybe Josh has access to some internal Google supermodel, AJI.
Josh Suereth 00:47:33 I cannot show you anything, so…
neil yashinsky 00:47:36 We know nothing!
Josh Suereth 00:47:40 Names for,
attributes in… Confusing, or at least understood by industry. Alright, I'll just do that in the background.
Yeah, the reason I think that there's a decent… one thing I've liked about LLMs is, because they're mass marketed off, like, docs and learning from people, is when they spit out something.
Usually, it's what a normal person could reasonably assume exists, or, like, a piece of verbiage which is the most commonly used in the industry, that it'll chunk out. So when it disagrees with you, you have to ask, like, do I need to diverge here?
Sometimes, yes. Actually, a lot of times, in my case, there's, like, reasons that we're doing something interesting. But a lot of times, it's like, no, actually, it hallucinated an API that I should just make a real API, because that would be useful for my users. Or, the name that it chose, I'm not using that name, and that would be a name that everyone would immediately recognize and understand.
And the third reason to do it is, when all this agent code people are writing, I don't want to confuse them further.
Right? And so it's, like, making sure that all of that agent stuff that gets written is better.
Alright, cool.
Michele Mancioppi 00:49:04 While the LLM spits out the answer?
Do we have 2 minutes?
to, there is that long thread in the, semantic conventions.
channel, I'm going to copy and put it in the chat.
Where there is something that, I probably need some closure more than anything else.
And it is the fact that in the open-to-entry specification.
It says that you cannot put a status message if the status code is not error.
And for the life of me, I don't understand why it is like that.
Trask Stalnaker 00:49:47 That's a spec part question.
Michele Mancioppi 00:49:49 Yeah, yeah, I understand the practicality of it, I just don't understand why the spec is like this.
We literally wouldn't need a status code error if it's implied by message.
Liudmila Molkova 00:50:07 actually, there is… and I'm going to rephrase this problem. If…
Let's say HTTP request was intentionally canceled.
We have no means today to record it on the span that it was success, but canceled.
Michele Mancioppi 00:50:25 We would do something like, I don't know, htp.intentional.cancellation equal true, or something abhorrent like that, right?
Well, in reality, that wants to be on the status of the status master of the span. Sounds pretty obvious.
The point is that we can either mark the span as an error and tell you why in reality it's not an error, which everybody's going to love.
Error, it's canceled. They say, no, no, it's canceled, but it's a good cancel.
Oh, that's terrible.
Liudmila Molkova 00:50:59 I think it should be… it cannot be just dispense status, because we would want to express it on metrics as well.
And let's say we can do this for RPC because consolation is part of RPC status codes, but not for HTTP. If it's success, it's not an error type.
But it's very important information to know.
Michele Mancioppi 00:51:21 Hmm.
Liudmila Molkova 00:51:24 So the only way we can do it today, without abuse, like, without breaking changes, we can abuse HTTP status code and say that, I don't know, minus 1 is cancellation, or 0.
Michele Mancioppi 00:51:35 Oh, no, if you put something that is non-numeric in status code, you're gonna have an angry mob of…
Observability developers coming at you and say, what do you mean it's no longer an Intel?
Liudmila Molkova 00:51:45 I mean, minus 1 is still an int, or 0 is still an int.
That's abuse. That's, that's backward combined.
Michele Mancioppi 00:51:53 But there's already a distressing amount of instrumentation that we put status code zero, literally right there, if they don't know any better.
Liudmila Molkova 00:52:04 Now, we can say that, that it's probably more important to know
It's still important to note that the request was canceled.
And 0 does not represent it well.
Michele Mancioppi 00:52:19 Would we make a special attribute with, htp.
Response.cancellation.reason.
Trask Stalnaker 00:52:30 Well, we have a… I mean, we need a canceled, semantic convention.
More generally, looking for the issue,
That we have. I'll put it in chat.
If you've seen this, just a convention for canceled spans.
we have this in Java, it would be nice to be able to mark things, not only HTTP and RPC, but internal, like, reactive,
async reactive stuff as canvas.
Michele Mancioppi 00:53:07 So, you mean to have a top-level cancellation namespace?
Trask Stalnaker 00:53:15 Could be useful. That's what this…
Michele Mancioppi 00:53:18 Interesting.
Liudmila Molkova 00:53:20 some…
I see two options. Either we do it specifically for cancellations, or the more scary pause, but it makes me more excited, is
Operation can… Operation status equals canceled.
But it… it doesn't work well with the rest of the ecosystem. We need to think it through.
Michele Mancioppi 00:53:44 I can tell you that the word operation has crept into Dash Zero very early on.
To provide a higher level representation of what this panel wanted to be.
We did not regret it.
We're even annotating operation types, so it's HTTP, database, or something.
There will be value on that.
But however, the moment that you start having a status for the span and one for the operation.
people no longer follow it. And something that we did in the studio was…
Operation metadata is set only on what is effectively an entry span.
Entry span are the spans where the trace context comes from hydration, so you know that the parent is not generated by the same SDK.
a great thing.
since we don't have the entry SDK, entry bit implemented anywhere, you know, the SDK is maddening, but it's a great feature. Having a status for the operation is different than the status of the span.
Haven'.
Trask Stalnaker 00:54:47 So, McKelly, not sure how you thought this topic was going to fit into two minutes, but.
Michele Mancioppi 00:54:54 Why do you think that they thought about that?
Trask Stalnaker 00:54:58 You asked for 2 minutes, if we.
Michele Mancioppi 00:54:59 Yeah, I know, they lied.
But I thought, I thought the idea would be, like, it turns out, like, no, or next time, or there's an obvious thing that I missed.
Because that isn't, so… Then I'll bring it up next time.
Josh Suereth 00:55:19 So, just feedback from the LLM, it actually recommends your current recommendation trask, because then it says it gets less confused with the existing client.address and server.address. And so, it said that it's better to align there than other. But again, this is like, you know.
take it with a grain of salt. It also… I notice, like, at least ours is really self-affirming, so if you want it to disagree with you.
Trask Stalnaker 00:55:48 Yeah.
Josh Suereth 00:55:49 really have to prompt it, which is what I'm…
Trask Stalnaker 00:55:51 an open…
Josh Suereth 00:55:52 I'm still, I'm, like, challenging it and saying, really? Like, what if we're stupid, kind of a thing, going for that. But, yeah, it, it, like, it went through, and it did give all the options we already talked about. Pier, source and destination, what else did we, we had talked about previously?
Oh, that's.
Liudmila Molkova 00:56:11 Kelly.
Josh Suereth 00:56:12 downstream. That one, I think, is the worst.
Nobody.
Liudmila Molkova 00:56:16 He knows which one is which.
Josh Suereth 00:56:18 Yeah, yeah, exactly.
Michele Mancioppi 00:56:20 I can tell you there was a source and destination, we had it at Instana.
Nobody got it.
Liudmila Molkova 00:56:26 We actually have them in some conf, I know ACS has them, but we don't use it at all. And it would be very confusing now to start using them for client and server.
Josh Suereth 00:56:36 Oh yeah, from and to was the other one.
Liudmila Molkova 00:56:41 Oh, I like it!
Josh Suereth 00:56:43 I mean, if you want that, yeah, it would be, like, service.com.name and service.2.name.
But it said that that was less good because it doesn't align with server… er, sorry, server and client of today, and how that doesn't match, like, the span types and all that. I'm like, okay, cool.
I think it over-indexed on reading our docs, though.
But, we can continue.
Trask Stalnaker 00:57:12 I wanted to hear your thoughts on log type.
Before we… Yeah, I actually typed up my thoughts on LogType, I think. Oh, great, alright.
Josh Suereth 00:57:20 So, yeah, yeah, I was… that's the other thing I was doing during the discussion.
Oh, and there's even a comment on it.
My main concern with the idea of log type is we define… so if you…
Trask Stalnaker 00:57:36 Oh, and Hillmar's here, and Hillmar's here.
Josh Suereth 00:57:38 God bless you.
Trask Stalnaker 00:57:38 Hey.
Josh Suereth 00:57:39 Great! Let's have, let's have a brief discussion. We only have 3 minutes, but my main concern is actually log type,
I think that this is a really, really good thing for us to figure out no-tel. But this is… would be a attribute on the log itself that says, hey, this is not a log, and you have to have compliance and forensics and things, and you… you… you should not let it get lost or changed and all that kind of stuff.
My main concern is actually around, end-to-end…
usage in OpenTelemetry. For context, what we've done internally for logs is we actually throw a resource attribute that's basically throwaway to make sure that audit logs are bundled and reported in their own batches, separately from the rest of logs, so that we can actually have a clear channel through things, like in the collector, right? You could actually have a processing pipeline for audit logs that has a different set of batching and resiliency
requirements than regular logs.
To make sure that you aren't dropping them. But my concern is that with this Semcov, if we don't actually prototype out what this looks like, and we do it at this low a layer.
The features that we actually need to build around audit logging and having higher granularity delivery, we might not ever be able to actually do.
Right? Especially if audit logs and regular logs are still blended together in one big bundle, and the collector would have to actually go parse the stupid frickin' thing to figure out what to do under… underneath it.
Go ahead, Michelle.
Michele Mancioppi 00:59:12 Is there a reason why this is not a log event name?
Why do we need an event name, which in reality is an event type? And now we put a log type as well.
Liudmila Molkova 00:59:27 Because there could be more… a lot of different, specific events with different structure that are all audit logs.
Michele Mancioppi 00:59:36 Yeah, but in reality, it's,
So, for example, if I understand correctly, this PR is from SAP.
And, the SAP, has been building,
login service for audit log purposes, trying to get synchronous semantics since before I left.
the,
fine. We could tag the log as, okay, this is a log… audit log, but in reality, it said, like, this is an SAP audit log, and then you build a pipeline around it, so I do not see…
an orthogonal thing, where I'm having a type audit.
With a bunch of events that in reality could be something that are not audit logs.
So the event name is gonna be sap.hanna.audit something.
And then you have a number of event names that are audit logs.
Liudmila Molkova 01:00:36 It's like a sub-namespace.
Michele Mancioppi 01:00:41 We're excited.
Josh Suereth 01:00:41 I still don't know how you work with that generally. It means someone has to have a list of all the audit log types. Hilmar, we're out of time, but is there anything you want to say before we, I think this… there's a lot of discussion, but Hilmar, I want to give you a minute or two to say…
Hilmar 01:00:55 Thanks, thanks. So, the main thing I'm not quite sure about introducing or using an event name would be how I can have multiple different audit log events with different required mandatory attributes under
the same name. I mean, this doesn't work, right? I would need to define.
Michele Mancioppi 01:01:18 Multiple.
Hilmar 01:01:19 once. So if I then have multiple different events, then I would, I don't know, do
some extra processing by each and every event name, and then I would need to have, I don't know, different filters and all those, and I would need to keep track of those different names. And that's my current problem. I would need something to actually group
A large set of different events.
And this could be audit logs, but this could also be things like, I don't know, something which should generate an alarm.
Right? I will have, I don't know, XYZ exception should trigger an alarm, and if user FUBAR logs in, I would raise an alarm. Totally different events, but
something which then can be grouped together. How would I do this in OTEL?
If there's a solution, I'm happy to use that one, but currently I… I don't know how I can group
Different events, with different event names together.
Josh Suereth 01:02:24 Yeah, right now, the only way… I think we all have to drop, but the only way to do grouping, which is what I was suggesting, is we group by resource, we group by instrumentation scope.
Right? Those are the… those are the only two groupings, like, in the protocol that OpenTelemetry naturally has right now. So, if you… if you were to group, you would have to do so with an instrumentation scope convention, or with something in resource. Both are not really ideal here.
Like I said, internally, we're using resource, and we actually… you'll have, like, a log from the same resource, but we'll actually add an attribute to the one to make sure it's bashed and sent in kind of, like, a separate channel and separate… separately droppable section.
So… so that's… that… that's a possibility today, but it's not great. I do need to drop for my next meeting, so I don't want to, like.
Sorry, I think we're gonna have to call it here. Michelle, if you want to remain on and say what you need to say, I have to drop, but the TLDR is… let's just… let's keep discussing, and let's kind of discuss on that thread. I think that the PR as…
written now is unlikely to get adopted. I think we want to look at this more holistically, like, about your problem. So let's figure out… Yeah, let's figure out, like, an end-to-end working example of how this would work, and then let's figure out what the conventions from that need to be.
Hilmar 01:03:44 Okay, cool, great. Would love to continue there.
Josh Suereth 01:03:47 Yep.
Hilmar 01:03:47 Nice, have a nice day.
Josh Suereth 01:03:49 You too, thanks.
