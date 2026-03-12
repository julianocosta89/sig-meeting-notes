SIG: PHP SIG
Date: 2025-09-03
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Bob Strecansky** 01:49 Hey, Brad.
Yeah, I can't hear you.
**Brett McBride** 02:04 How about now? Can you hear me?
**Bob Strecansky** 02:06 I can hear you now.
2025 is the year of Linux on the desktop, I think.
**Brett McBride** 02:12 This year, for sure.
**Bob Strecansky** 02:18 How you doing?
**Brett McBride** 02:20 Yeah, not too bad. Just crawled out of my deathbed. I've been sick all week.
**Bob Strecansky** 02:26 Oh, no, what are you doing? Why don't you go get some rest?
**Brett McBride** 02:29 Oh, no.
**Bob Strecansky** 02:29 Or you need… you need human interaction.
**Brett McBride** 02:32 Yeah, yeah, a bit of that. No, I spent quite a few days just… Now I'm just a bit better now.
**Bob Strecansky** 02:40 Good.
Singapore.
**Brett McBride** 02:45 Hello, I go. Hello, Sergei.
**Ago Allikmaa** 02:48 Tape.
**Bob Strecansky** 02:54 Yeah, there's definitely a lot of stuff going around, isn't there?
**Brett McBride** 02:59 Yeah, I thought I'd made it. I thought I'd made it through winter.
**Bob Strecansky** 03:03 I was… you know, I didn't even, like, I didn't even consider that is your winter.
**Brett McBride** 03:07 Yeah, yeah.
**Sergey** 03:20 I guess.
**Bob Strecansky** 03:22 Hello!
**Brett McBride** 03:24 Hello, Sergei.
**Sergey** 03:29 So… Do you have a sprinter?
In Australia?
So it's Springfield now?
**Brett McBride** 03:35 Sorry, I missed that.
**Sergey** 03:37 Do we have a spring? Do we have a spring season?
**Brett McBride** 03:40 Spring… yes, yes, we do. It's, yes, it's spring today, or yesterday, or… So, things should be getting better.
**Sergey** 03:52 Is that… is this, an issue for you guys, like, to always, Correct, like, if you… if you… if you have mentions in literature, people refer to spring, you always need to correct what months they mean and stuff like that.
Well, it's not necessarily, like, spring is just spring, right? It doesn't matter what month it is.
**Brett McBride** 04:10 Well, I mean, different hemisphere, we're different, to… to… to the Northern Hemisphere, but also Australia has, I think unusual seasons anyway, we go by calendar month.
Instead of around, probably, the equinox, which I think most other countries do, yeah, just…
**Bob Strecansky** 04:35 I feel like Brett's my, like… I feel like you're my Australia liaison. It's like, all the questions that I'm too afraid to ask somebody else, I can just ask Brett about Australia.
**Brett McBride** 04:45 Yeah, I'll give a, confident, if not correct, answer.
**Ago Allikmaa** 04:51 Yeah, even around here, people actually colloquially go by calendar month, and then there's always someone who corrects. Now, it's technically not… customed yet.
**Brett McBride** 05:03 Yeah, yeah, yeah, I do that too.
**Bob Strecansky** 05:07 Being confident is three-quarters of the battle, Brett, and as one of my friends says, there's no such thing as true stories or false stories, only good stories are bad stories.
Okie dokie, shall we? I think we have… we have Quorum now.
**Brett McBride** 05:25 Let's do it.
**Bob Strecansky** 05:25 Let's… Let's do it.
Right.
Open new pull requests… Wow, Brett, you really timed that well for this one, huh?
**Brett McBride** 05:48 Yeah, I thought I'd give you something to talk about.
**Bob Strecansky** 05:51 Okay, well, we can talk about, we'll put that on the agenda, as well as my feature adding additional tests. That's a fun and exciting one that we can talk about in a couple minutes.
I think those are the only open issues in the regular repo?
Couple contribut things, but nothing.
New… nothing new enough. I know that, this one has a lot of discussion, but… I haven't looked at it.
**Brett McBride** 06:19 That's right, I'm all over that one, and I think it's close, I think it's close to it.
**Bob Strecansky** 06:22 I assume.
I see that you're all over that one. Thank you for that. That looks like it must have been a lot of work.
**Sergey** 06:29 Does Spec have a concept of a session? There is a concept of a session in… Hu I thought that maybe something like that coming from mobile, I thought maybe mobile have, Oh, space.
**Brett McBride** 06:41 No, that's a good point. Look, there could be a concept of session in spec, but I don't think it would align.
**Sergey** 06:48 So they don't mean… so by session, they don't mean something here, like sequence of requests that… Signify some kind of workflow.
**Brett McBride** 06:56 No, no, that's simply auto-instrumentation to create spans when a session is started, ended, interacted with, in PHP.
**Sergey** 07:10 I'll read that, thank you very much.
**Bob Strecansky** 07:12 I'll have to read through that later, because it sounds pretty important.
Well, in the prioritized backlog… Chris, you got one that's pending review. Are we stuck here?
**Chris Lightfoot-Wild** 07:27 Yeah, sorry, I'm not, I'm not a little bit.
It is. That's true.
**Brett McBride** 07:34 Wasn't it? That was.
**Chris Lightfoot-Wild** 07:35 Someone said there was still a problem with it, and I said, I don't…
**Brett McBride** 07:39 Mmm.
**Chris Lightfoot-Wild** 07:40 double-check what they said, because I don't… I didn't understand it worked that way, but…
**Brett McBride** 07:46 Because things don't automatically move Around in this board, just because we closed the issue, or whatever, so it could just be…
**Chris Lightfoot-Wild** 07:55 Yeah, I need to find some time to test what they suggested, but my understanding of it is that, obviously, the new feature doesn't… use the environment like that. It populates them at runtime, so… But, you know, someone's reported it, so I'll have to see if I can reproduce.
So…
**Bob Strecansky** 08:13 interesting.
**Chris Lightfoot-Wild** 08:14 Unless you want to move it out of the way, but otherwise, yeah, I'll try and action it at some point.
**Bob Strecansky** 08:18 toward this… Yeah, this board is merely a placeholder for work, it's not… it's not all-telling.
And that's, that's about it for that.
Road to SDK V2, we only have the metrics temporality one, that's alright, leave that as is.
Ugh.
So close!
We're almost there, to 20 million. Congratulations, everyone.
And then… okay, so I think those are all of our main… checkpoints. Brett, do you want to talk about SEMFCOM 137.0 first, or do you want me to Chess first.
**Brett McBride** 08:57 Yeah, I only need a couple of seconds, it's… It's almost a no-op, there's nothing of interest to us in that one. I just generated it, because it was released.
But also there's, So that I can tag a new version, because there was one… Same cold thing that was added in a pull request last week.
**Bob Strecansky** 09:21 Okay.
**Brett McBride** 09:22 which was, I think, Deployment Environment Name, we hadn't… we weren't generating, so… So once this is launched, I'll just be able to tag a new version.
**Bob Strecansky** 09:33 Got it, okay. This… yeah, this looks very, very straightforward to me. Do you want me to approve it so you can merge it?
**Brett McBride** 09:39 Yeah, please.
**Bob Strecansky** 09:40 Alright, on it.
Cool. That's easy enough.
I'm gonna click the merge button, too, while I'm here?
Alright.
Cool. Easy enough.
And the, Last but not least, I wanted to chat about my augmented test suite investigation. So, with using Cursor all day, every day at work, I have learned how to use it a little bit better.
I asked it to help us generate a more complete test suite coverage, and it actually came up with a bunch of really good recommendations. So I started working on a PR to get through this, and then… it had a difficult time working through SOM, and FAN, and Stan, and PHPsalm, and PHP CS Fixer, and this, so… I still have work to do on this, just wanted to let you know that this was something That I was looking through and considering in case anybody else had not done it yet. I don't expect to have any time to work on it before my vacation, so I'll probably have to pick it back up after vacation, but if anybody is curious about this, I thought I'd mention it.
**Sergey** 10:56 AI is not smart enough, you cannot just tell it, fix it, so that CS or PHP fixer will pass it.
**Bob Strecansky** 11:02 It is… it is smart enough, I have not yet.
It… it was sort of… I think I need to be… we need to be… I need to be a little bit more intelligent about the prompts that I'm giving it, and I also probably want to create some cursor rules for this, because I think it was writing stuff that was conflicting upon one another with some of these tools, like cell and phpStand and PHPCS Fixer, so I'm most likely… will give, like, add a couple more input parameters, like, it needs to pass all of these things. However, that obviously takes a long time to run locally, so I'll probably have to do that and let the agent Knock it around for a while, but… Yeah, haven't gotten… haven't gotten fully there yet, but we're well on our way.
**Brett McBride** 11:45 So the cursor run locally?
**Bob Strecansky** 11:50 Jen?
**Brett McBride** 11:50 Does Cursor run, like, a local AI agent, or LLM?
**Bob Strecansky** 11:55 Yep.
Yeah, it's just a cursor's a wrapper around VS Code that allows you to interact with some of the AI tools. I may… I may try and come up with a CLI answer to this, too, so I can put it in a screen and let it do its thing, but I have not yet gotten that far.
**Sergey** 12:14 So… What do you think about maintaining that? Is that, like, human-readable and understandable, what each test tries to achieve? Like, how is this gonna be, like, let's say in the future, if it fails.
How is it gonna be to understand why it failed and how it should be fixed?
**Bob Strecansky** 12:30 Well, that's a great question, Sergey. My answer is, I think the test suite, the test suite entries that it added, they feel, at least at face value, they feel pretty human-readable and pretty human-actionable. I think it's just kind of augmenting what we have now.
And I'm probably going to do a second pass on this, because I want to prompt it to make sure that it doesn't change any core functionality of the library, and just changes the test suite.
And I think that is relatively easily validatable and consumable. That will just… that onus will be on me to make sure that I understand the test suite that AI runs, so that in the future, if something were to go wrong with that, I can do it. I think it's a pretty good learning experience for a lot… to get a big swath of the codebase understood, too.
So, I'm not expecting anybody else to maintain those cursor… like, the cursor-defined test roles. I'm not even positive that we'll add them. It was more of a thought experiment on whether it was possible.
**Sergey** 13:28 Hi, you want to keep them completely separate for the time being? Like, even if you merge them? Like, keep them as a separate group?
**Bob Strecansky** 13:35 I mean… I mean, I'll probably keep them… I'm gonna keep them in my PR until I merge them.
when I merged them in, I'm wondering if… I had considered maybe, like, a PHP annotation saying that this was generated by AI, so that if we get to a point where it really feels stuck, we could probably do something. I'm hesitant to do that, because if we write a test.
It's testing on the functionality of the library, and if something else changes, there's no point in adding that test if… There's no point in having that test if you feel like you can just remove it at any point, only because it was written by AI. I'm not a huge… AI proponent. I just think it's… I think that this is a really interesting way to determine where our test suite coverage is lacking, and hopefully try and fix some of it. But I'm not, like… I'm definitely not married to merging this, and I'm definitely not married to anything, I'm just wanting to give people feedback on what I was attempting.
**Chris Lightfoot-Wild** 14:27 So would you be dropping out changes that are in source, did you say?
So, that's ill when the tests.
**Bob Strecansky** 14:34 No, I want to explicitly ensure that we're not changing the core functionality of the library, that we're only changing the test functionality.
**Chris Lightfoot-Wild** 14:41 Yeah, just because it looks like…
**Sergey** 14:43 That all the tests pass.
**Bob Strecansky** 14:45 Yes.
**Chris Lightfoot-Wild** 14:46 Well, it looks like it breaks stuff, though.
in… Right. Yeah, right now.
**Bob Strecansky** 14:51 Right now, right now it does, because I have not yet finished this PR. That's why it's.
**Chris Lightfoot-Wild** 14:55 Yes, are you intending for it not to touch it at all, and only test them, sorry?
**Bob Strecansky** 15:02 Yes, yeah, I'm intending for it to only test current functionality that's built into the library… into OpenTelemetry PHP API and SDKs, not change OpenTelemetry PHP APIs and SDKs.
**Brett McBride** 15:14 So, improve our test coverage.
**Bob Strecansky** 15:17 Improving.
**Chris Lightfoot-Wild** 15:18 Okay, rather than it, like, changes the code, and then… Makes the tests work with the code it's just changed, and, like, ends up with garbage.
**Bob Strecansky** 15:26 Yes, I do not want to do that. I explicitly do not want to do that. I have seen that, but… Internally, like, at my company, I've seen it by too many people, and externally, I've also seen it by people, so… My intention is to improve code coverage here, nothing more.
**Sergey** 15:42 Was that your explicit query to AI to improve code coverage? This purpose?
**Bob Strecansky** 15:47 That was my initial query, yes, and then I had to do many subsequent queries to try and get it to fix all of the other things, but… I… I just figured I would put this up as a draft to show my thought experiment, rather than keeping it in the dark until I said, here's a huge PR with 450,000 changes, please approve so I can merge it.
**Chris Lightfoot-Wild** 16:10 You look at all kinds of other techniques that try to kind of, like, find security holes in API and stuff like that?
**Sergey** 16:16 They essentially try to jitter all the inputs, send all kinds of invalid inputs. I guess it's a different purpose of those tests. I don't know if they will also achieve better code coverage, since they usually…
**Bob Strecansky** 16:29 Beautiful.
**Sergey** 16:29 It forced the code to enter all the check-ins, right? The checks that you have.
**Bob Strecansky** 16:34 Are you… You're talking… are you talking about adding, like, code… like, code fuzzing, or test… Yeah, yeah, exactly.
**Sergey** 16:41 If I zoom.
**Bob Strecansky** 16:41 That is explicitly outside of what I'm trying to accomplish here. I agree that that would be a pretty good goal. I think that we have, like.
that might help us to uncover some things that our library doesn't have. I don't think that our library has enough maintainers to have fuzzy code testing, or maybe that's a perfect example of where it would be helpful, but I know that takes a lot of extra compute, so…
**Sergey** 17:03 Why do you think it introduced as a big effort? Like, you need to always, you know, it requires ongoing effort, one initial effort?
**Bob Strecansky** 17:10 I think that… yeah, I think fuzz… like, from… I… we don't use it at work, so I don't really have a cool, like.
Fortune 500 practical application for it, but I do know that it's often used to find, like, what you were talking about, security vulnerabilities and performance degradation and stuff, but I… I do know that it takes a non-zero effort to maintain a fuzzy test suite, and I… I know I don't… I'm not interested in maintaining that at this moment, not necessarily poo-pooing it for the future, but that's not at the top of my priority list now.
**Sergey** 17:39 Hmm, excellent. Thank you.
**Chris Lightfoot-Wild** 18:02 Well, if that was… I did have something to ask, if you've wrapped up on that bit, if there was nothing else.
**Bob Strecansky** 18:08 Go ahead, yeah, I've completed.
**Chris Lightfoot-Wild** 18:11 Sorry, I didn't add it to the agenda, but if we've got some time… Yeah.
There's just been a couple of issues raised, about, like, Laravel's instrumentation, and then, sort of, the termination thing happening outside of… the currently instrumented Request handler.
Obviously, it kind of creates these… isolated spuns with different, Different trace IDs?
Obviously, in my head, it'd be good if it was all under the same you know, Laravel instrumentation was, like, the entry point, and then it could disable or enable it kind of at will. I'd seen the configurator.
But I wasn't sure, Like, usages of the configurator, and you can specify, like, a name, and it looks to be able to then disable This is where my understanding's a bit fuzzy, but, like, does it disable pre-existing tracers?
So they can kind of toggle them on and off on demand, or is that… am I thinking of this wrong? Because in this particular example, like.
There's an environment flag to try and disable console tracing in the instrumentation correctly.
I just… You know, it's quite simple, it just doesn't run the hook for one given function.
But then, some other things, like, have event watchers where, Redis, for example, is a thing that is hooked.
So then, during a console worker, it does check if anything's in Redis, and then that starts its own, like.
Trace, and that, you know, happens quite a lot.
So, I might not have explained it very well, but, like, as a simple entry point, can you flip the lights on and off, I guess, to the instrumentation for it to be no off and back? Is that what the configurator is for, or I'm totally missing the point?
**Brett McBride** 20:08 Yeah, I… I… yes.
Yes, you can. You can… you can turn, traces off, or instruments off by… By their name, or by attributes.
Yes.
Yes, that's the idea of that configurator. We've got a few things called configurator, but I'm pretty sure I know which one you're talking about.
And… yes.
That's what it does.
**Chris Lightfoot-Wild** 20:37 But I guess my thought then was to try and… have that entry point, and then decide whether or not the instrumentation as a whole, everything under the, you know, the namespace LiveL stuff should be on or off.
But yeah, that…
**Brett McBride** 20:52 Yeah, you can do that, because it has wildcards as well. So you could do larval.star, or larval.database.star, or…
**Chris Lightfoot-Wild** 21:01 And that affects already… previously created traces.
**Brett McBride** 21:05 Yeah, why do you decide to…
**Chris Lightfoot-Wild** 21:08 do that on occasion.
**Brett McBride** 21:09 Oh, I said.
**Chris Lightfoot-Wild** 21:09 apply for nutrition.
**Brett McBride** 21:11 I think it's only… I think it's only at, creation time.
**Chris Lightfoot-Wild** 21:15 Because I probably don't need to switch in the newer branch, in the SPI-based one, where you're given the new, sort of, context, and there's a tracer provider instead of directly a tracer.
Probably need to lean toward.
making the traces every time I need one, rather than… it just persists one, because then you can't toggle it on or off, undo the disabled check, or whatever, you know, needs be.
I just didn't know if that was, like, less performant or desirable.
**Brett McBride** 21:45 Yeah, so you're kind of talking about… Turning things off.
in… in flight.
**Chris Lightfoot-Wild** 21:51 Yeah.
**Brett McBride** 21:53 Yeah, I'm… I mean, I think you can, but I don't think that was the… I don't think that was the design goal for it. I think it was just to… Sort of configure it.
something on it, like, this thing's too noisy, I just want to turn it off from here on. Not, I only want one of these, and then I want to turn it off, and then I want to turn it back on again, you know, within a single request. It's… it's supposed to be a more coarse You know, apply to everything once, and now… you know, forever.
My, my understanding of, of, of, of that feature.
**Chris Lightfoot-Wild** 22:33 Okay.
**Sergey** 22:33 Boom.
**Chris Lightfoot-Wild** 22:34 Let's play around with you.
**Sergey** 22:35 trying to solve? You're saying that you can… you have a situation where you capture pieces of spans, the database spends, outside the larval request, so you don't have kind of, like, root requests as missing?
**Chris Lightfoot-Wild** 22:47 Yeah, I think it was on, if you're running, like, an artisan command for a queue worker or something, and you don't want to trace that bit, and you want, ideally, like, the job to… Be the start and end of the trace.
But then, it processes the job, finishes a trace, and then independently checks Redis.
Which is part of another hook, but that starts its own fresh trace.
And you end up with, like, weird-looking spans that are, sort of.
Isolated and all over the place when…
**Sergey** 23:18 Is there any way to connect them using… Using the tracing, that distributed tracing, like, past the… trace ID and connect those things, into one trace.
**Chris Lightfoot-Wild** 23:28 One of the things where it's a long-running process, and you just start a trace at the very start, and I have all these things that are just sort of building up in memory and not going anywhere. And someone had raised I guess, like, a bug, when they were using Laravel Octane, I think, for… You know, long-running, sort of, request processing, and it was just filling up Very large traces.
Do you remember?
**Sergey** 23:51 Well, you will still send all the spans, there is no such thing. Maybe I misunderstanding what you're saying. There is no such thing as trace, it's a virtual thing, right? It's composed out of spans that have the same trace ID.
there's… you know how to trace in memory. Do you mean, like, you will accumulate all the spawns that belong to a particular trace and not send them?
**Chris Lightfoot-Wild** 24:10 I guess it was… Yeah, I wasn't sure what point that trace is supposed to end on up for very long-running things, but it seemed like it was kind of doing the wrong thing currently.
But, yeah, I guess I need to…
**Sergey** 24:24 kind of like a mechanism to end that race, right? Technically, like, it's, you kind of, like, move this complexity to the back end, to the presentation layer, like, they need to decide… they technically… not at any point can know for sure if trace ended, right? They find all the spans that belong to the trace and they present them, but it's possible that you will, if you rerun that query in 5 minutes, the trace will be bigger.
Might be bigger.
Right?
**Chris Lightfoot-Wild** 24:51 Might contain additional things that only discovered lately.
**Sergey** 24:55 Like, what you say, like, if there was some dormant background job that just woke up and added something to the trace. Now, obviously, there can be discussions, like, philosophically, should it belong to the same trace? If it's just a background job that was spawned from the trace? It all becomes, then, what is the usability kind of, like, use case, right?
How you prefer for users to see it.
how you connect. Maybe it's better to present it as a link to respond instead of trace ID, like, it becomes, I don't know, if you are then capable to present it in a convenient way.
But, yeah, so… Regarding that, I'm not sure if… for sure understand what is the use case. You're saying after the response was sent to the user, there is still something running after that, and it kind of, like, doesn't pass trace ID, so it becomes its own trace, kind of like orphan spun, not belonging to anything?
**Chris Lightfoot-Wild** 25:49 I think that's what I'd seen, and whereas perhaps my understanding was more you'd want to instrument the user… user land part of it, like, you know, not the framework doing a check for a cache key or something, but… the user's job, or the use… the request that the user code is specifically processing. And if there's a cash check in that, then fine, I'd add that in, but not outside of the… that scope.
And it currently… there's a flag that kind of tries to disable some stuff, but… Doesn't really work.
Yeah, so I guess maybe I need to play around.
**Brett McBride** 26:23 A long-running process that's generating work, and you don't want to trace the things that this long-running process is doing, but when it does.
Find a piece of work, that's a… that's a user request, and you want that.
**Chris Lightfoot-Wild** 26:37 Yeah, one like that. That unit of work to be instrumented. Yeah, yeah. Everything else outside of that, not to be. But currently, you've, like, it's instrumented the Redis calls, and then that's it. It's just for the entire lifetime.
Deciding to…
**Brett McBride** 26:49 Trying to throw something in the spam.
Yeah, look, you might… you might be right, then, about Configurator being the… the… the… the way to… to tackle that.
Because as I'm thinking more about it, it's… It's like a multi-layered… you know, find the first matching rule. So, you probably have to look at the tests.
For that configurator to see what it can do.
Because I think it's predominantly a Niveay Thing, which means it's probably very good once you can understand.
**Chris Lightfoot-Wild** 27:25 Yeah, my brain's far too small to understand correctly.
**Brett McBride** 27:28 That's true.
**Chris Lightfoot-Wild** 27:29 It's a problem, isn't it? Yes.
**Sergey** 27:31 it be cleaner to introduce just an API, some kind of, like, pause-resume functionality, then you can just pause, and that means, That's it, it doesn't produce any spawns. Because, okay, if I understand your use case, Chris, you're saying you have some custom entry point that you want to define in your application, and you want to be able to say, okay, this is the start of my entry point, whatever happens, you know, on the thread.
I will generate a trace for it, spawns, and then at some point, I will go… I identify the end of this entry point, and that's it. I don't want… I want to pause the generation of the spawns, and until I start the entry point, new entry point again, I want everything to be ignored, not… Not to be considered of interest… of any interest, right?
**Chris Lightfoot-Wild** 28:13 Yeah, that's… that's about, yeah.
**Sergey** 28:16 Yeah, so it sounds like, maybe just introducing simple API, it might be implemented with this configurator thing behind the scenes, but… Maybe just say, okay, pause resume, and that will achieve this purpose that That might be also useful for any future… future use cases where people just want to do it. Like, I remember the classic agent that we had, I used it, for example, for For testing, We had this component testing, where agent was run on a real application, and kind of, like, communicated with backend, but I didn't want to record any kind of, like, initial setup of this environment.
for the actual code that I wanted to be monitored. So I was able to say, okay, pause, and then when I know that actual code that I want to monitor starts to run, then I will resume.
The… the work of the, you know, the tracing itself.
Yeah, so… So it might be a useful API, just… Just to introduce it directly.
**Chris Lightfoot-Wild** 29:16 Great.
Yeah, maybe I…
**Sergey** 29:18 Even if you implement it behind the scenes using the configurators. But then if you can make it more flexible, it sounds like it would be a shame to limit it to Laravel, like, because it sounds like, general case, people would just want to disable completely, right? Not just Laravel, right? You yourself said that you also don't want to capture any other databases, like database, even if they come from PDO, right? Not necessarily from Laravel code.
**Chris Lightfoot-Wild** 29:43 Yeah, yeah, potentially. I mean, I guess… I probably needed to get my head around it first, and then before I could even say, this is the pain point I had, or this works, and it's good for that pause-resume extraction, abstraction, sorry.
M.
So maybe I can just look into that configurator, if that sounds roughly like I might be on…
**Brett McBride** 30:03 Yeah, it sort of sounds like you want to, A disabled configurator for the general long-running thing, and then when you go to kick off a User request, or a traceable request, or whatever, you know, set you… Turn everything back on.
**Chris Lightfoot-Wild** 30:21 buckle in.
**Brett McBride** 30:22 And then you're in the context of, like, that's now the active configuration.
For that trace.
Until that ends, and then revert back to your… Disabled one.
**Chris Lightfoot-Wild** 30:33 It sounds the problem with these solutions is, even if you discuss it now, you're already aware that it's a hack.
**Sergey** 30:40 And obviously, it will backfire, because, like Brett, you said, that everybody assumes that these configurators are only set once at the beginning, right? No, whoever maintains them in the future will assume that this is the case, and it was… and it's not fitted to be switched on and off repeatedly during the lifetime of request, right? And then it can be broken, this use case can be easily broken by just doing something with this configuration, the response, or whatever, and then changing… changing them during the request will not have any effect if the response is already cached from the start. So, I'm just saying, it's better to implement something with explicit intent.
Than trying to ride on something that is maybe fitting for now, but can be easily… Be broken, because it's, by itself, is not… it's not the way it's supposed to work, right?
But, you know, the question is, I agree with you, it's better to investigate, is this fits the, you know, to get something working for now, and then maybe… you know, make… packaging it in a better way, or are you basing it on something that is working, and make… and you are sure that it fits your use case. That I agree with you, it's better to start with something.
**Chris Lightfoot-Wild** 31:49 Yeah, so I could do that as, like, an investigator, and then maybe a proof of concept, and then obviously you can… if you think it looks better as a separate, distinct feature, and… There's kind of a use case there for it.
Discuss it.
**Sergey** 32:00 I would definitely use it, like, because for now, I think we have to jump through some hoops in order not to record this setup phase of the application. I don't even remember how to do it.
I guess we just ignore those spuns somehow, yeah.
**Chris Lightfoot-Wild** 32:18 Cool, well, thanks for that. It's useful.
**Bob Strecansky** 32:23 Alright, I have a hard stop at 8.30, and that's now. Does anybody have anything else they want to talk about?
Alright, cool. We'll catch y'all on the internet.
**Chris Lightfoot-Wild** 32:32 It is all.
**Bob Strecansky** 32:34 Nope.
