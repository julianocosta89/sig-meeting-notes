SIG: JavaScript SIG
Date: 2026-01-21
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:37 Hello?
**Trent Mick** 00:58 Okay, I realize someone just copied. Nevermind.
Someone just copied this.
I am.
dating.
**Marc Pichler (Dynatrace)** 01:18 Yeah, I think it had the wrong date on it.
**Trent Mick** 01:22 And then, so I assumed it was just last one that started anyway, yeah.
**Marc Pichler (Dynatrace)** 01:25 Yeah, I just updated it before joining the court.
**Trent Mick** 01:30 I was doing it at the same time as you, I think.
Might be a quiet call.
Sorry, Andre, you probably added your name already, I just had removed it.
I'll just wait one more minute.
Alright, I guess we can get going.
Okay, welcome to Amateur Hour. I'm running the show today, so he's gonna… be pretty sad.
Okay, David? Is David even around yet? Okay, I gotta go talk with David then.
Wah, wah.
**Marc Pichler (Dynatrace)** 03:40 I guess I could, also say a few things about this.
**Trent Mick** 03:44 Sure.
**Marc Pichler (Dynatrace)** 03:46 So… I have started looking into that already. The question is where to place the SDK logs,
And for config stuff.
we…
So, basically, the plan is to remove the mvar config from SDK logs, and just have it be handled by the Node SDK in the new configuration package.
And… we… are… Looking into which options we have to move it there.
Currently, it's running automatically when you instantiate the logup provider, which also means that it's included when you run it in the browser, which, there it's just a no-ob and that code, essentially.
So we have, kind of, 3 options. I opened the draft PR to split
I think it might be linked down below here, to split that environment variable configuration into a separate function.
So it's not running automatically when you instantiate the processor or the provider, but, you have to pass it in through the constructor, the results of the function.
And we're… Now trying to figure out where to place it, if we should.
put it in…
the SDK logs package and keep it there, for now, so that people have a backwards compatible way of doing things.
then there's the option to just do it in Node SDK and not expose it directly to end users, so they would just have to rely on the internal logic for now.
Or we do it in, we move it to SDK logs.
And,
expose the function from there, so people, SDK node, I mean, sorry, we move it to SDK node and expose it from there, so people can still use the logs SDK, but just use the configuration for the logger provider and the batch spam processor.
From Node SDK directly, and we also use it internally.
Hmm… These are the three options that I see. I'm not sure which one we want to take.
Right now, I feel like I'm preferring…
**Trent Mick** 06:23 It's the first one that I listed in the doc, which is to just…
**Marc Pichler (Dynatrace)** 06:27 place it in Node SDK and not give people a way to… Do it with a function.
Because that minimizes API surface.
I'd be interested to hear what you are thinking.
**Trent Mick** 06:44 You said the first one you listed where? Here? These ones, or…
**Marc Pichler (Dynatrace)** 06:47 No, it's in the, in the doc.
In the SIG meeting doc.
**Trent Mick** 06:53 Duh, sorry, okay.
**Marc Pichler (Dynatrace)** 06:55 Yeah, so it's placed in Node SDK.
do not expose it to end users, they must migrate to Node SDK if they want to keep using NVAR configuration.
It is… The most breaking change of the three.
But it seems to be the finer,
Thing that we would probably keep the longest, so they just have to migrate once and be done with it instead of migrating twice, possibly.
**Marylia Gutierrez** 07:30 My thought here was, like.
Exactly what it's like, what is the end goal? Like, how will you see, like, in one, two years? Especially, like, with declarity config, like, this is not gonna exist the way it is right now, because it's not, like, a function to get from the environment. It's just read from the file.
What is… Like, the changes that would make that possible in the future.
Like, from those options, is that any of the three that would align with what we want? Like, in a year or two or something?
**Marc Pichler (Dynatrace)** 08:04 Yeah, I think, all of the three work with declarative config, because they are just optional code that we can deprecate later.
the one that probably is the safest is the first one that I listed here, because people don't get ahold of it directly, right? So you can internally switch to the configuration package and config provider.
without… Users noticing.
So, this is also the reason why I feel like I prefer that one.
Because it's… Very breaking now, but less breaking, or not at all breaking later.
**Marylia Gutierrez** 08:55 Is it better to go to do the braking from, like, the…
Like, the major version, the 3.0, or, like, do the breaking… No. What is it?
**Marc Pichler (Dynatrace)** 09:03 So, SDK logs is not stable yet.
Okay, yeah, we can. Do it before we stabilize it, so that we don't have to bump major versions later.
**Marylia Gutierrez** 09:12 Okay, yeah, got it.
**Marc Pichler (Dynatrace)** 09:14 Yeah, and also, I feel like all of these are kind of needed to avoid,
making our lives difficult later with declarative config, because if something is not configured there in the declarative config, it might get read from enfars later on.
So you might not be able to disable it. This is why the idea is to remove it.
**Trent Mick** 09:44 So, in… in building the…
So, perspective from a vendor here. So, Elastic, we have an SDK that is a distro of
the OTel node SDK, effectively.
And we found in some cases that it would be nice if SDK Node was a bit of an SDK builder, so it did expose some things on, like, how to do this part, how to do this part.
For the cases where…
our SDK doesn't need to customize anything. As much as possible, we try to make our SDK be the same as Upstream, but we do some things that Upstream doesn't support yet, so, like.
We have a central configuration service that's built with an op-amp client, which we can upstream later, but the op… like, the config is essentially Elastic-specific. Anyway, for the parts where we don't need to be different from upstream, it'd be nice
Sometimes, if… how to parse the environment stuff was an accessible function in some library in Node.
But that said, I can understand why you don't want to go expose more API service… surface and SDK node, unless, you know, there's a clear user of that, as opposed to just throwing out functions that people might or might not use as a pain for maintenance later on, so…
Yeah, I don't have a problem with number one. I guess the only… or option one. I guess the only potential complaint is you're gonna get someone who is just using the
SDK logs and not using SDK node, but I guess we can wait and see if that happens, and then…
They can either reproduce the logic in their own side, or they can,
ask for it to be exposed in SDK node, right? Is that what you're thinking?
**Marc Pichler (Dynatrace)** 11:35 Yeah, I guess we would, people could ask if…
We can expose it, but then we would also wait for a bit and see how many people actually need that.
Because we have had that in the past, where one person was asking for it, and it wouldn't make sense to just expose it for one,
one user, but if there's, I don't know, 10 people that ask for it, then that's an indicator for us to say,
There's probably something there that we need to look at and expose it, and… Yeah.
**Trent Mick** 12:13 Okay, chat.
Yeah, when that first person comes in, it gets to be a hard decision to say, no, we don't expose how to parse the functions, but I guess we can wait for that.
Or at least I find it hard to see them. Okay, cool. I'm fine with option 1.
**Marc Pichler (Dynatrace)** 12:31 Alright, I will change my PR then to, do option one.
**Trent Mick** 12:36 What is your PR doing right now?
**Marc Pichler (Dynatrace)** 12:38 It does option… To.
**Trent Mick** 12:43 to all the changes to SDK logs, didn't we?
**Marc Pichler (Dynatrace)** 12:45 Yeah, I kept it all there.
**Trent Mick** 12:46 Rowan.
Yeah. But I just need to move to tests, and .
**Marc Pichler (Dynatrace)** 12:52 the code.
**Trent Mick** 12:52 That sucks.
**Marc Pichler (Dynatrace)** 12:53 fairly self-contained.
**Trent Mick** 12:56 Yep.
What's the… so, I mean, all these equivalents for tracing already exist in SDK node.
What's the situation for metrics right now?
**Marc Pichler (Dynatrace)** 13:06 Metrics never had it to begin with.
We made a conscious decision not to add it there, for… .
**Trent Mick** 13:15 into SDK Metrics, but SDK node does have the config for metrics, I imagine, right?
**Marc Pichler (Dynatrace)** 13:20 Yeah, exactly, yeah.
**Trent Mick** 13:22 And those are… similarly, they're option 1, they're not exposed to the user, is that right? Like, you have to use the Node SDK class to get that config built up? Okay.
**Marc Pichler (Dynatrace)** 13:32 Yeah, exactly.
**Trent Mick** 13:33 Okay, that's cool, so this makes logs the same as metrics then, basically.
**Marc Pichler (Dynatrace)** 13:37 Hmm. And there's, actually not…
A lot of environment variables that we need to look at here.
So you can see the code, it's not too many, and right now, if you use SDK logs, you don't get exporters configured automatically.
So you're basically left in a half…
configured state anyway, if you use environment wherever, so moving it to Node SDK, I think, makes the most sense.
**Trent Mick** 14:07 Okay.
Okay.
We… so… slightly off-topic, but related, we still have… we have the same situation for exporters right now, right? In that the exporter
Modules are looking at the environment themselves instead of that being given to them.
**Marc Pichler (Dynatrace)** 14:23 Yes, but the configuration code I,
in the refactors last year, or I don't know how long ago that was now, I split the config code from the business logic,
Because it was kind of all over the place, so it should be easier to remove that, in the future, or introduce,
separate, a separate factory function that just creates an exporter without the configured.
MVR-configured stuff.
**Trent Mick** 14:59 Okay, good.
**Marc Pichler (Dynatrace)** 15:00 Yep.
**Trent Mick** 15:02 And I mentioned earlier, that's what the…
declarative config stuff is probably already using, and for exporters, yeah. Okay. Cool.
Okay, I think we're good. I don't know.
Moving on, unless someone shouts.
David?
**David Luna Bistuer** 15:24 You're muted. There you go, yeah.
Basically, a small change that may,
keeping on the topic of turning the, the CI.
This is a small change, but actually, it's leveraging something that we did in the past, which is, we have a script for each package that needs the services to be run in Docker.
So now it's not necessary to start all the services at once.
just to test one package. So, the idea here is that… is that we… we get rid of the… the service dissection.
now the Docker Compose file comes… it's a source of truth of, for our services.
And then we, just run the… just the services that we need for each package. So, for example, if Postgres and MySQL have changes in APR,
We will start only these two services and test on that. The result is that we are speeding up a little bit the CI, because we don't need to wait for more services to be started that are going to be… are not going to be used.
Okay.
So, yeah.
**Trent Mick** 16:33 And that works because…
This runs test services start script in the affected packages, and those ones are already set up. This is iRedis, for example, already set up to specify the services they care about.
Is that right? Yeah.
**David Luna Bistuer** 16:51 Yeah, sounds great to me.
**Trent Mick** 16:53 It's also nice that we no longer need to maintain this to be in parity with the Docker Compose file that we have.
**David Luna Bistuer** 17:01 Yeah.
So, yeah, what you can do locally,
With MBM scripts, you're also the CIO for BDS.
So, that's… that's a good part. So, just less maintenance and…
And, yeah, I think it was about…
I think we get some minutes in HCI, so… and it's run.
**Trent Mick** 17:26 Oh, saved from it? Did you look at the times?
**David Luna Bistuer** 17:30 Yeah, I can, I can make a comparison here.
**Trent Mick** 17:34 If you have a before and after to show, it's helpful motivation to see that it does take that. But yeah, that's the time for service. Oh, yeah, I guess…
Because we would have always been, kind of, the… taking the time for the slowest service to start up, or all of them start.
**David Luna Bistuer** 17:50 Coming up.
**Trent Mick** 17:50 I guess they're… they're fighting for resources, so…
**David Luna Bistuer** 17:53 Okay, that's very well. Yeah, the last round was for a few days ago. The last… I think, usually, starting all services is around 7 minutes, 8 minutes.
it varies a little bit, but then if you're just, you know, changing one packet, and just starting on single service, or maybe no services at all, because, for example, there are instrumentations, like on Undichi.
That doesn't need any services to run.
That, to some reason, doesn't have to wait to… for all service to be started. So, yeah, best case scenario, it's zero.
In others, it could be just, you can… I think I tried Postgres, I think it was around 1 minute just to start that specific service, so yeah.
**Trent Mick** 18:31 Instead of 7 or 8.
**David Luna Bistuer** 18:32 I guess.
**Trent Mick** 18:32 Okay, cool.
**David Luna Bistuer** 18:35 I'll add some information about the times.
**Trent Mick** 18:39 Yes, I'll…
**David Luna Bistuer** 18:40 look forward.
**Trent Mick** 18:41 I'll review that later. Yeah, sounds good. Cool.
Okay.
If no other comments on that?
Andre.
**Andrei Borza (Sentry)** 18:58 Hey, not much to say about this, basically just this, was fixed with 2.4.
But it's still breaking in.
with Cell Edge.
I pinged the creator directly, but maybe I can just file this as an issue. I just thought maybe I could bring it up here if Jared is here, but…
It seems not to be here.
**Marc Pichler (Dynatrace)** 19:24 Is it actually released already?
**Andrei Borza (Sentry)** 19:27 I… I think this was part of 2.
Or…
**Trent Mick** 19:32 Which package is this? This is resources.
**Andrei Borza (Sentry)** 19:34 resources here.
If this hasn't been released yet, then… never mind.
**Marc Pichler (Dynatrace)** 19:48 That's…
**Trent Mick** 19:49 I don't think it's been released.
Yeah.
**Andrei Borza (Sentry)** 19:52 Oh, okay, okay, my bad then.
**Trent Mick** 19:55 Okay, that's… that's great, because I was really hoping that the global this.whatever would… that pattern of just… Yeah. Because it used to be before it was just doing process.rgv.
And whatever the static analysis, or whatever the mechanism that Vercel is using to warn about that, I was hoping that just doing global this, that would be fine. Right. Yeah.
Okay, so I guess we need to wait on that a little bit to see.
**Andrei Borza (Sentry)** 20:21 Yeah, I'll delete this, I guess. Thanks.
**Marc Pichler (Dynatrace)** 20:26 Alright, I can, I would try to get a release out, tomorrow.
I just triggered the release PR.
**Trent Mick** 20:36 Right. Okay.
Nice. Easy one. Okay.
Carlos is not here today, I guess.
You can put this up.
Just reading this.
Oh, right, that was a discussion about…
What was the issue that we had here? This guy.
Jackson's here on his phone.
Okay, sorry about that.
No, that's totally fine.
**Jackson-iPhone15** 21:31 Yeah, sorry, I had to open her back up to, unmute, but I'm here.
**Trent Mick** 21:44 Yeah, so Carlos is maybe asking if we have opinions on… the discussion here, I guess?
**Marc Pichler (Dynatrace)** 22:04 But, wasn't,
It seems the assumption here is that we do fail fast, but
if I recall correctly, that's not what we do, right? We…
Get to a certain space where we encounter something that's not valid, and we keep The first few.
But we dropped the rest, is that right?
**Jackson-iPhone15** 22:43 Yeah, that's correct.
**Marc Pichler (Dynatrace)** 22:51 So it would be interesting to see what.
**Trent Mick** 22:54 We're also totally fine with spaces.
Currently.
Our docs…
Yeah, anyway, sorry, I dropped this big turd, because there's a bunch of weird side things that aren't even necessarily related to the…
Whether one should follow, The baggage spec.
unencoded… oh, so I'm… sorry, I might have been wrong. Was that…
this supporting space, was that just because that was added in this PR?
I don't remember.
**Jackson-iPhone15** 23:36 Oh, did you try it with the PR code itself? If so, then yes, it does support space.
**Trent Mick** 23:41 I can't remember, or if we already currently supported it.
**Jackson-iPhone15** 23:48 I would be surprised if spaces worked, only because I'm aware that the, current implementation should only accept, baggage octet.
So, I believe unencoded spaces should not work.
But, certainly with a PR, they will.
**Trent Mick** 24:07 Right, okay, with the pier. Okay. The,
One of the weird things is that the…
Comment for that function says if value contains whitespace, equals, or…
quote characters, and that's, again, not touching on the backslash and semicolon that are also excluded by baggage stuff, but that's one thing. Then it says it must always be quoted. The implication being, if you quote it, then the quotes will get removed, and it'll allow those characters to go through, but that's not at all what the implementation does. It just ignores the double quotes and puts it through, literally.
Now, wait a second, that was two quotes that went down to one.
I think it just doesn't do anything with the middle, it just drops outer quotes.
Just strips one note or quote inside, if it exists. Anyway.
Okay.
Most of this stuff is educate stuff, so I guess following whatever comes out of this discussion is gonna be fine with me.
I guess it's… It's on me if I want to go comment about other things, because…
One thing that's weird is, if spaces… if we're meant to fail hard on spaces,
For resource attributes, that's fine, but we explicitly do not fail hard on spaces for
the export or OTLP headers NFAR, which is…
Similar in that it's key-value pairs, but we… Want a space in there.
Even though I'm not even sure if that's against spec, because Python, for a while, was not allowing a space in there. You had to use the percent encoding to get a space in there, but…
Basically, all the other…
Languages allowed a space, and because it was fairly common for adding an authentication key that has, like, bearer space and then the actual token.
And an authorization key, so…
I don't know, it's… I find the whole thing spec-wise kind of weird, but this is exactly the right place to go talk about it, so…
I'll go take a look and read and follow up on this if I feel necessary. I don't… Jackson, are you guys, like, blocked on this, or…
**Jackson-iPhone15** 26:20 No, no, we have a solution on our side for now, but we were just pushing this upstream just to have clarity. Our biggest concern is just the discrepancy between SDKs.
**Trent Mick** 26:33 Okay, cool. So, it sounds like, spec-wise, this'll get sorted out here.
And… Yeah, I don't know if…
if a decision comes out here, and then JavaScript changes to following that spec, does that solve the problem for you, or you're still going to have that discrepancy between all the others, right?
**Jackson-iPhone15** 26:53 Yeah, until implementation gets done on the other SDKs to align with the spec, we'd still have the discrepancy. For now, we won't break on our side so long as baggage octet strings are still accepted, which I don't expect any reason for that to ever change, so…
Yeah, in any case, We'll, we'll, follow the conversation on the upstream, spec update, and…
Except whatever decision gets made there. In that case, I can then discuss with folks working on the other SDKs to get everyone in line. It's okay if it takes, some time. I understand these kinds of large spec cross SDK changes are gonna be a bit expansive, time-wise.
**Trent Mick** 27:37 Yep, okay. Okay, great. Thank you.
So, yeah.
to do on that. Okay, cool.
So, as ever, if anyone has more topics, you can add them later, but we'll start looking at…
Triage.
And if anyone's actually looked at us already, please jump in.
**Marc Pichler (Dynatrace)** 28:06 Yeah, I, had a quick look at this, I…
didn't really look into the code itself, I just had a look at the thing here, and I think that's the sort of functionality that we want to remove in the future anyway.
The… doesn't fix the bug, though. It's just something to keep in mind, that…
People probably shouldn't be using this, and we might want to mark these things as deprecated for 3.0.
these are these, utility functions, that are in, SDK TraceWeb, that are used for instrumentation, and that are causing this anti-pattern of, depending on the SDK for.
instrumentation.
**Trent Mick** 28:55 The only instrumentation using it is the user interaction one, or is…
**Marc Pichler (Dynatrace)** 29:00 I think there's just one, yeah, in the.
**Trent Mick** 29:05 Oh, and there's also a web… there's now a… in the browser repo, there's also a web utils that has…
get Element XPath exported as well.
And I don't know who's using that, though.
Oh, the use… the instrumentation user Action… Oh, God.
Okay, the browser repo has an instrumentation user action.
The contribib rep repo has an instrumentation user interaction.
They don't both use Git Element XPath. They… Do both use… a different utility called…
Get elements CSS selector. Okay, sorry, I'll stop talking. I don't have opinions, but… mark your…
Thought would be to deprecate this, and we shouldn't have a web…
**Marc Pichler (Dynatrace)** 30:06 Yeah, exactly. I think we shouldn't have, instrumentation utilities exported from, the SDK package itself.
Because, like, the whole idea between the API and the SDK split is that you don't have to depend on the SDK for instrumentation.
But if we export the utils from the SDK package, that's… That's just the same,
outcome, which is that you depend on the SDK, and then… .
**Trent Mick** 30:40 So…
Skate packages…
Dang… Aggie.
**Marc Pichler (Dynatrace)** 31:24 But looking at the,
Actual thing that they are asking for, it seems to be a rather easy fix.
**Trent Mick** 31:35 So we might just…
**Marc Pichler (Dynatrace)** 31:38 We might just fix this, and
while doing that, also mark stuff is deprecated.
Might even be a good first issue.
**Trent Mick** 32:01 Okay.
How about that?
So, fix it here, presumably look at… an issue.
on Webbytails to do the same?
And then… Mark it deprecated.
Perhaps… Same for… are there other utilities exported by…
**Marc Pichler (Dynatrace)** 32:27 Yes.
**Trent Mick** 32:28 Okay.
Backditched. And then… Get instrumentation.
Sorry.
In stream annotation, user inter… Action 2 inline this. Let's see.
Bottom.
cheering on it.
And then you thought maybe that's a reasonable…
**Marc Pichler (Dynatrace)** 33:14 Oh, sorry.
**Trent Mick** 33:15 first issue?
**Marc Pichler (Dynatrace)** 33:16 I think so, yeah.
**Trent Mick** 33:19 So you're up for grabs, too.
**Marc Pichler (Dynatrace)** 33:22 And it would be… probably a P2Bug.
**Trent Mick** 33:27 Okay.
X.
And that takes it off this list, does it? Yep. Okay.
Contrib.
**Marc Pichler (Dynatrace)** 33:47 Yeah, this is just not released yet.
**Trent Mick** 33:54 What's not released yet?
**Marc Pichler (Dynatrace)** 33:55 So, 0.54.
It is not the version that would have that dependency, version here.
So it's on main, but it's not… Yeah, I gotcha.
Yeah.
**Trent Mick** 34:13 Yeah.
**Marc Pichler (Dynatrace)** 34:15 Also, not a bug, but a feature.
**Trent Mick** 34:21 Was that the…
Was that this one?
**Marc Pichler (Dynatrace)** 34:27 Yes.
**Trent Mick** 34:28 Adding, oh, 16?
**Marc Pichler (Dynatrace)** 34:30 Okay.
**Trent Mick** 34:31 So… Do we keep this open, or just close it, same?
Oh, that is listed right here.
**Marc Pichler (Dynatrace)** 34:38 Yeah, you can… you can assign this to me, and I will just close it once I do the release.
**Trent Mick** 34:57 It's not really a bug, right?
**Marc Pichler (Dynatrace)** 34:59 Yeah.
**Trent Mick** 35:02 Thank you.
Boy.
**Marc Pichler (Dynatrace)** 35:13 Yeah, I think that's, related to the recent change in the exporters.
Where, somebody… started working on, doing the retry properly.
So, essentially, in the past, what we did was, if it was, like, a connection refused error, that,
Returns pretty much instantly.
We wouldn't retry, and now we do, which is the spec-compliant way of doing things.
But the… Nope, sorry. The downside of that is that… We will…
Probably block on shutdown, for longer than is necessary, because the default thing is, if you start it up, it tries to export to local host, if you don't have a collector running there.
Retry a bunch of times until it hits the timeout, and then return.
So, on shutdown, it tries to do one final export, and…
Then that doesn't, complete in time.
We likely have to abort the retries.
**Trent Mick** 36:38 Is there a way to communicate that?
**Marc Pichler (Dynatrace)** 36:42 I suppose force flush would be…
I don't record what the spec says about Forest Flush, but…
it comes to mind as the thing that I never really knew what it is for, but I wouldn't be surprised if that is actually what it's for.
You can assign this to me as word, then I will have a look. I did review the PR on the retry, so this is on me.
Anyway…
**Trent Mick** 37:17 Okay, so…
**Marc Pichler (Dynatrace)** 37:23 I can also, write up the comment.
**Trent Mick** 37:26 Okay.
I'll just add that. And you want to take it?
You don't have to take everything, but okay.
**Marc Pichler (Dynatrace)** 37:36 Yes, I just have a lot of context on that one, so it makes sense for me to look into that.
**Trent Mick** 37:41 Yeah. If force flush works, that'd be great. I know in our… the pre-OTEL agent that I was working on, we had a thing where the equivalent of the exporter would be told to
reduce all of its timeouts when we were in shutdown mode, so we try to do this last flush, but we give much shorter timeouts for everything, so that we can end pretty quickly, yeah. And certainly no retries at that point.
Okay, thanks.
Didn't we discuss this last week as well?
**Marc Pichler (Dynatrace)** 38:14 Yeah, I was meaning to look into this, but I don't really have a… Lambda test setup ready.
**Trent Mick** 38:23 Yeah, me neither.
So… Nest?
specs have been… Okay, I guess we're still waiting for…
**Marc Pichler (Dynatrace)** 38:43 Yeah, I think we have a needs author response label or something.
**Trent Mick** 38:53 Okay, so we'll just leave that one there.
I… yeah, I had questions, I didn't know…
what… because they're talking lambda to lambda, right? So I don't know what that trigger is for the second lambda in that pipeline.
Which I think I'd want if I was trying to debug this.
Okay.
Next.
This is… Not from the same person.
We also kind of discussed this last week, right?
I don't know why I'm ticked.
I always love to see catches 3 layers deep.
Oof.
I might be able to look at this, but not soon. Too much stuff stacked up.
I don't know if Jared had…
Okay, he still has it in draft, though.
Okay, I'll make a note to try to look into this, but…
It might be a while for me.
Okay… You know, go make that note.
Okay.
Right. Bulltriage.
If anyone… no one has anything else?
Do we see which one has more?
**Marc Pichler (Dynatrace)** 42:02 I think Cora has more right now.
**Trent Mick** 42:05 Yep, good timing.
Do we, like, we always run into the same, like, top 5.
Do we skip down a bit here, or…
**Marc Pichler (Dynatrace)** 42:14 Yeah, I guess we could skip a few.
**Trent Mick** 42:20 And I don't feel up-to-date on any of these.
**Marc Pichler (Dynatrace)** 42:23 I… I guess I would have a question, maybe, about the top one here, the, concert gear.
Depthing… SpanX border… yeah, this one.
So, essentially, what's happening is that on some runtime, I don't record exactly which one it was.
**Trent Mick** 42:51 Plotfluid.
**Marc Pichler (Dynatrace)** 42:52 Consultant.
**Trent Mick** 42:53 Dirt doesn't exist.
**Marc Pichler (Dynatrace)** 42:55 It does exist, but it doesn't do anything. So they don't get… any,
any results, and that causes them to, like, go on a wild goose chase on why their SDK isn't working.
But it is actually working, it's just not giving any output.
And there's…
Unfortunately, then, also no way to detect, like, to do feature detection if Console exists, because it is actually there.
So…
**Trent Mick** 43:32 What is this?
Was it Cloudflare? No, it wasn't. Did they say that thing?
**Marc Pichler (Dynatrace)** 43:38 Because it seems… Seems to be Cloudflare workers.
**Trent Mick** 43:54 No op.
Sorry, I just lost the back. We put it there, but it's the no-op?
Thanks, guys.
How do you… yeah, how do you tell, then?
**Marc Pichler (Dynatrace)** 44:08 In my opinion, we… I'm not sure what to do here, so…
In my opinion, this is something that they should just implement, because it's… not…
Too crazy of a thing to use.
And it's… Pretty much there in every other runtime and works.
Or at least anyone… any runtime that I touched before had it.
**Trent Mick** 44:39 So, if we want to go old school, we could get… Back in the day before…
when you're supporting versions of Node before util.inspect existed, You would get a…
a polyfill, basically, for util.inspect and put that in a thing, so… like, Bunyan has that for supporting, like, node 0.8 or something like this, it's going way back.
So, like, we could use console.log because we know that there are some used things out there where it doesn't work, a lot of our workers maybe being the only one who identified.
I don't know if this qualifies as a tail wagging the dog or not. It is kind of lame that our…
The console exporters don't work in a certain environment where things otherwise run.
Because it is meant to be just, like, as baseline of a debugging
Output as you can get, right?
**Marc Pichler (Dynatrace)** 45:37 Yeah.
**Trent Mick** 45:39 So…
**Marc Pichler (Dynatrace)** 45:40 I think what we settled on in this PR is to do, like, a chase and Stringify or something, or…
**Trent Mick** 45:49 Is that degrading, basically, the output for anyone?
**Marc Pichler (Dynatrace)** 45:52 Yeah, it would degrade the output, like, you wouldn't get the fancy colors, and, in the, dev tours, you wouldn't see this thing where you can, like, expand stuff.
It would be just one, like, large string that's being logged.
**Trent Mick** 46:15 I mean, I guess he could go the other route and do the output format that's, like,
the collector has, which is kind of a text-based format that has no relation at all to JSON-ish.
And he was looking for configuration, right?
**Marc Pichler (Dynatrace)** 46:36 Yeah, the initial idea was to do configuration, but… It seems to me.
**Trent Mick** 46:40 that just kind of went off track. It's not about whether an attribute to console dir, right? Because that isn't the issue. You need to change to not use console dir at all.
**Marc Pichler (Dynatrace)** 46:49 Yeah, exactly.
it kind of went off track, because I think somebody commented on it, and then they tried to solve that problem, but then it didn't solve another problem anymore, and it just got way out of hand.
**Trent Mick** 47:10 Okay. I don't know, also, kind of…
**Marc Pichler (Dynatrace)** 47:12 Got off track with this one, and…
**Trent Mick** 47:32 Just kinda died.
**Marc Pichler (Dynatrace)** 47:33 Yep.
the initial… I think the initial goal that they had was to support the…
GenAI Semconf, which has deeply nested attributes.
**Trent Mick** 47:59 Yep.
**Marc Pichler (Dynatrace)** 48:01 Which doesn't show up this way.
So they wanted to make it configurable, but that seems to be… Kind of…
Not a great way to go about it as well, because then, like, you're using…
I don't know, auto-instrumentations node or something like that, to set the console exporter to just see stuff.
But you can't configure that, so you need to, like, do the SDK setup manually.
**Trent Mick** 48:28 Encode, because it gets spheral pain, yeah.
Would… do you know if the spec allows us to add additional…
values to the exporters config, so where you can choose OTLP or… console.
**Marc Pichler (Dynatrace)** 48:46 Oh, no.
**Trent Mick** 48:47 Oh, it's GK Environment Service, so… I'm so… to these guys.
Not really.
That's the old deprecated console one.
And that's… I'm not sure if it's something that we'd include in our instrumentations node. Like, we could have a contribib package that had, like, beefed-up debug
Ones.
**Marc Pichler (Dynatrace)** 49:11 Hmm.
**Trent Mick** 49:11 And people could use that, but if it's not, like, in the default configurable… Stuff that's not as useful.
Okay.
**Marc Pichler (Dynatrace)** 49:35 We can't feature… we can't tell if we're running in cloud.
**Trent Mick** 49:39 Sorry, workers, Kim.
**Marc Pichler (Dynatrace)** 49:41 We… might be. I haven't checked that.
Bing.
I guess one way to, like, move that ahead would also be to undo all of this, try to make it work with Cloudflare workers, because that's a separate issue anyway.
And try to tackle that another time, and then just make GenAI semconf work, but.
**Trent Mick** 50:15 Oh, is that the whole issue? Because our default depth 3 isn't sufficient?
**Marc Pichler (Dynatrace)** 50:18 Right, yeah. That was, I think, what they came up with to begin with, and then there was some…
Like, the hook.
**Trent Mick** 50:27 Oh, I see, so it is two things. Yeah, it is two things.
Because one, this fixes love for our workers, but two, it also makes the depth infinite, basically, right? The other fix here for them is to just go infinity.
Which… I mean, should that be fine? Why did we limit it to 3?
Probably just to be defensive.
**Marc Pichler (Dynatrace)** 50:50 I guess to be defensive, and, like, with the previous types, there wasn't really anything that you could get beyond 3.
Yeah. Since you had the attributes, and then you had a key and a value, and that was it.
And now you have, the whole thing nested, so… 3 doesn't cover it anymore.
**Trent Mick** 51:12 Okay, so I, like…
I would think break it up into two issues. One, I would be fine raising that 3 to…
I mean, there are two options there. You can just go infinity, this is a debugging-only thing, it should be fine.
No one should be creating spans with that much… attributes with that much depth anyway.
Or you could put it at some, like, ridiculous, but still somewhat of a guard 100 level, or even 10 that's gonna solve the problem.
And then have a separate issue for the club for a workers thing. We could let that one just sit.
Kind of thing, so… Okay.
Dang.
**Marc Pichler (Dynatrace)** 51:56 Or we could… we could also just call that a won't fix and comment on the actual issue on the Cloudflare workers thing.
And people opened.
I remember seeing that, and it had a lot of thumbs up there as well.
**Trent Mick** 52:16 That was, this one.
**Marc Pichler (Dynatrace)** 52:20 Just two? Only two.
**Trent Mick** 52:25 What was this thing asking for?
Yeah, I guess could add more color, but…
**Marc Pichler (Dynatrace)** 52:42 Because this is… it's not just an us problem, right? Everybody who uses console D is somewhere…
It's gonna be…
**Trent Mick** 52:49 Just gets surprised that things aren't working at all.
Yep.
Like, even if they just change the output to print, like, console, they're not implemented.
then you'd at least have a sniff.
But… Okay.
match.
Okay.
I'm… Not sure how helpful or not helpful that is, but that's my comment.
Okay, working down from there.
Jamie as a stand, that's in draft.
Really?
I don't even know about the module loaded.
Sorry, it's NJS loading back, it's… Dang.
I'm not totally following. I don't see the actual warnings that are kicked out here, but…
David, you looked at this a long time ago.
**David Luna Bistuer** 55:42 Yeah, I'm trying to remember what was your… So…
Yes.
Yeah.
No.
**Trent Mick** 56:25 Okay, I don't know. I would need to sit down and play with it a little bit. He does have a repro rank.
**David Luna Bistuer** 56:31 Yeah, so I need to go again.
That food, please.
So, yeah.
**Trent Mick** 56:43 Okay.
I am playing in that area right now, so maybe I could… Take a look at it.
**David Luna Bistuer** 56:51 Marina! Mama Vina!
**Trent Mick** 56:54 Promises, but I'll… I'll try to take a look at that again.
When I'm in there.
And anyone have anything added? Nope. Okay, one more, maybe?
Renovate…
Did you, like, did we just want to close these, Mark?
Did you renovate… the guy that wanted to change or renovate config? I don't know.
**Marc Pichler (Dynatrace)** 57:24 Yes.
**Trent Mick** 57:25 You're kind of the master of our config.
**Marc Pichler (Dynatrace)** 57:27 Aye… forgot to follow up on that one, that was before the holidays, then.
**Trent Mick** 57:34 Yeah.
**Marc Pichler (Dynatrace)** 57:36 Or have another look at this. I started, ignoring a few of our packages here, because they don't need updating, and then…
I'll also go in and try to figure out which… Things we actually want here.
**Trent Mick** 58:09 Okay, I don't know. Or is that in Contrib that you're ignoring, so…
**Marc Pichler (Dynatrace)** 58:14 Yeah, there's… there's multiple PRs for Renovate here.
**Trent Mick** 58:22 Okay.
Okay, anyway.
I guess you're kind of the master. I'm okay, I was just saying, thanks.
Okay.
Hit a Marillia one. It's been sitting around for a little while.
**Marylia Gutierrez** 59:03 Yeah, this one might…
change… I might have to, like, re… Rebase after the changes on the other, so yeah, don't…
Don't look at that one right now. I can put back and draft this so I don't confuse people.
**Trent Mick** 59:16 Okay, that's fine.
By the way. Oops.
I think I'll just call it. We're at the end of the hour.
So that's what we got.
And… If no one has anything else, thank you. We'll see you next week.
**Marc Pichler (Dynatrace)** 59:43 Thank you.
**David Luna Bistuer** 59:45 tournaments.
**Trent Mick** 59:45 Well, later.
**Andrei Borza (Sentry)** 59:47 Thank you. Bye.
