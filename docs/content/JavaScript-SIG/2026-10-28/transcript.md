SIG: JavaScript SIG
Date: 2026-10-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trent Mick** 01:30 Nope.
**Jared Freeze (Palo Alto Networks)** 01:32 Dang.
**Trent Mick** 01:33 Smaller today.
Guessing.
Everyone's still hungover from release parties?
**Jared Freeze (Palo Alto Networks)** 01:48 What kind of party?
**Trent Mick** 01:50 Release parties, trade it over.
Mine.
**Jared Freeze (Palo Alto Networks)** 01:52 -Oh.
**Jackson Weber** 01:58 Yeah, I'm… The party's still going over here, I just took an hour to join the SIG.
**Trent Mick** 02:04 Nice, thanks, you had to go get a private room, because…
**Jared Freeze (Palo Alto Networks)** 02:13 Are you in Washington, Jackson?
**Jackson Weber** 02:15 Yeah, I'm, in the Seattle area.
**Jared Freeze (Palo Alto Networks)** 02:19 I actually just got pinged by… a web dev from ClickHouse that wants to use the browser SDK.
Today.
Which is funny.
Like, they're like, we updated to 3 yesterday.
We want browser now.
I'm advising him not to do that.
**Jackson Weber** 02:40 Must have been a good, 3.0 release, huh?
**Jared Freeze (Palo Alto Networks)** 02:43 Yeah, well, they… he wants to release a browser SDK.
**Trent Mick** 02:49 You guys still haven't done that 3.0 yet, have you, or is that issue done?
**Jared Freeze (Palo Alto Networks)** 02:52 No, no, I found some bugs in the instrumentation base I want to clean up first.
**Trent Mick** 02:58 In your… the new one, yep.
**Jared Freeze (Palo Alto Networks)** 02:59 Yeah, and also, I have no idea. I'll ask you later, privately, but I have no idea if instrumentation from Node, like, pulling in that module is okay alongside our own.
Because if you try to… I think it should be fine, right? Because it's…
**Trent Mick** 03:16 Browser? Fine, to have the… just the instrumentation package?
**Jared Freeze (Palo Alto Networks)** 03:21 If somebody made instrumentation for 2.0, JS.
if they pull it in alongside our SDK, will it just sort of do the right thing with the globals?
I think the answer is yes.
But I wanted to test it, because I am having trouble wrapping my brain around.
**Trent Mick** 03:41 There shouldn't be any globals that it's doing.
Oh, do you mean, sorry, when, like, the logger provider?
**Jared Freeze (Palo Alto Networks)** 03:49 Yeah, yeah, yeah.
**Trent Mick** 03:51 Yeah, no, I think it's probably… Fine… I can't think if things would break, and there's a lot less going on on the… Browser implementation side.
**Jared Freeze (Palo Alto Networks)** 04:02 Yes, that is true.
**Trent Mick** 04:05 if you get… there is some bug that, like, hasn't even been documented, but for people that are going through the hoops to get ESM instrumentation going on the node side, if there are two separate versions of import in the middle installed, then… You can get issues, but that's only if you're going A little bit off the current reservation, because it does have a… global in its package thing that it's using to… You can… you can tell it ahead of time which… modules to try to instrument, which not? But anyway, browser side doesn't know that.
Yeah, Matt, I assume this is the… Config provider… Let me share.
Okay, so… Right.
I guess we can get started. I'm not gonna have a whole lot, I didn't prepare.
Agenda items for myself. Mark can't make it today.
So I'm driving.
Just take a look at my notes, see if I had other things that I wanted to do. Oh, yeah.
So… Give me a sec, Badsen.
Thanks, Sarah.
Nice. Okay, we're getting some things to talk about then.
Alright, let me get started. I'm not sure if Matt's here, no, he's not. Okay, so… This is… Thing for declarative configs. So the instrumentation section of a declarative config file allows passing instrumentation, mostly schema-free, there's an instrumentation slash development.general section, which is… has… does have schema from declarative config.
Or… some general things that can be independent of the particular instrumentation, so, like, there's .http, dot, and some… schema-defined config for, like, which headers to capture, that kind of thing. But then there's also a instrumentation.js, instrumentation.java, which are kind of freeform open things that the individual language SDKs can use to… configure their instrument, or do whatever they want.
Matt had… this one's been sitting around for a while, and we've been discussing that. I need to come back to it. I basically dropped the ball, because declarative Config went on the back burner while 3.0 happened, and I need to get back to this one. But this will define a new… element of the API, eventually, called a config provider, long logger provider, those kind of things. And some implication, potentially, on the ordering and what SDK does for starter… starting up and dealing with config, and for instrumentations, and so there's some interesting things there, and that you now, even more so than before with, like, a meter provider and stuff, you want the SDK to set up and register its global providers before the instrumentations start doing their thing.
And I'm intentionally vague there on what doing their thing is. This is probably not construction time, it's sometime after, but we don't have well-defined Well-defined.
states that instrumentations go through, which Jared's trying to deal with on the browser side with the new instrumentation base a little bit. Anyway, Yeah, so Matt fairly threw that on, because I need to get back on that.
Anyone stop me at any point if you have… Particular things to add.
Brilliant.
**Marylia Gutierrez** 08:47 Yeah, just… Yeah, just a reminder, today was the last day for voting for GC Elections.
I know there are a few people that were having issues to log in. We are able now to also identify a bunch that could be affected, and I'm messaging all of them. I know, like, some people on this call got affected, but yeah, hopefully, if anyone still has any issues, yeah, you feel free to ping me.
Yeah, basically the… if you ever… voted on a prior election, and your username has upper and lower case, you were not able to log in with GitHub, pretty much. You have to use Gmail, so I have to make a change for that.
So yeah, just a reminder. And the next one, also another reminder that this is the last week for nominations for the Community Awards, that you can nominate up to 5 people.
So yeah, we are doing this to the end of this week.
**Trent Mick** 09:47 Cool.
Thank you.
And then… so next, the PR, we're behind on SEMCOM for at least, well, one… one release behind.
And then also for thing… people who are… So I'd appreciate a review on that. Once I get that in, then I can do a SEMConf release.
I'm hope… I'm guessing 145 will come out soon, because it's been 2 months since next release, and… martin, working on browser-side stuff, has a federated SEMCOM repo for client-side.
SEMCOM, which is waiting for the 145 thing, so I'll try to get that out as well. There's also, like, a minor change. With our change to TS down, the… module.exports that you get when you require a module no longer has the same ordering of keys that were in the original TypeScript file, which actually broke my generation script for the changelog here, but is not exactly something that affects anyone else.
Unless you're crazy.
Yeah, Jared, I'll let you know, you gave me the appropriate response, which is a one-word response to basically, I'm not touching this thing.
I fixed the script, it's fine.
David, wanna take it away?
**David Luna Bistuer** 11:07 Yeah, there's not… not an issue or something, but just something that came up today, and… kind of have… want to know the opinion, so I can kind of wrap them around. So, lastly, we're working with sessions right now. I'm kind of trying to wrap around my head and all that stuff, and one of the things that maybe… necessary, or some vendor, or some people might want to have is, like, to propagate the session.
From the front end to the back end. So, in front end, you have sessions, you generate the session ID, then you, of course.
you add, attributes with the sessions ID, but maybe you want to propagate that, so time stream services are capable of just get the session ID as well, and actually then decorate these, logs and spans with that.
So… Kind of thinking about out loud on how could be the best, or the optimal way to do it, so through package, maybe, and then… and… And I know that there are some, semantic conventions for sessions, so should we do… should we use the same semantic conventions for that?
So, I don't know, just… Has anyone think about it, Sometime.
for,
**Trent Mick** 12:23 This is perhaps in the browser side, you get more…
**David Luna Bistuer** 12:26 Yeah.
**Trent Mick** 12:27 with…
**David Luna Bistuer** 12:27 But I think it affects both sides, so you as a consumer, as a receiver of the propagation, of the context.
How do you want to consume that?
As a downstream service, so… In Node.js, I'm instrumenting my service, my Node.js services, and I get some requests, that request comes from some context, and then… that context, it might be the session, or something that it's… it's not custom from the, you know, it's not from… it's something that is not custom, but it's something that it relates to OpenTelemary, like, sessions, but it's a front-end thing.
So it's kind of a broader line, it's not completely custom, it's not completely from the user that is using baggage with its own names and values.
But it's not… Yeah.
It's a big…
**Trent Mick** 13:22 More official than baggage, you're saying? You'd like it to be?
**David Luna Bistuer** 13:27 I don't know. Then…
**Trent Mick** 13:28 Then the next level up is TraceState, I think, right?
you know, OT… colon, sess.
For some short thing for session, I don't know, maybe. But I don't have… I don't have solid feel there at all.
I have not heard of anyone suggesting a trace date variable other than the thing needed for.
Sampling.
**David Luna Bistuer** 13:52 You bet.
**Trent Mick** 13:54 But yeah, maybe.
Because, you know, it'll be a quick implementation path if we're talking about updating the spec to what's allowable to add to Tracy.
Yeah.
Interesting.
Jared, you got…
**David Luna Bistuer** 14:16 Let's go for food.
**Jared Freeze (Palo Alto Networks)** 14:20 I mean, we have a pretty complicated session manager. I don't know exactly how that might apply here.
But… I, I'm… One of the problems we have on browser, and I may be completely off base here, is… The limitation on what headers you can read?
So, I've been lobbying the W3C to… exposed more, because the trace parent is not… Part of it, but they have something called server timing.
Which is, like, you get a little bit of information about the document generation, like, how long it took and stuff. They give you a little range.
that's super useful, but there's way more useful information than how long a page took to generate on the backend. And so, exposing more headers would be really useful. One of the bigger problems with the web is that, you know, most people are moving to dynamic files and cached HTML. So the… Advice to update a meta tag is not really available.
effectively, to most people. So, if you're passing around things, you know, and you're trying to get it from node to browser, you're pretty limited in the real world, even though that is, you know, the advice. Because most people are not generating HTML for every user on the fly any longer, with single-page apps.
So again, I may be off base, but, like, if you do want to pass session, like, back and forth, or trace parent, or whatever, it's a little more difficult than it should be.
So, we have, you know, in my day job, we have session management that's fairly complicated. I don't know if that applies here.
At least for browser, it might. But we have semantic conventions around that as well. Like, quite a… quite a few. Because we make a distinction between a person opening multiple tabs and a person being in a tab, not only being in that tab, but when the page is visible.
like, they all get IDs all the way through, and they're all considered part of a session, so… If you want to talk about that later, we can. I'm not sure if that applies here, but…
**Trent Mick** 16:25 Okay.
Is there a connection between front-end and back-end, but not with sessions? Is it just, like, a session… and contain so many trace IDs, and that's the… that's the only connection you have, or…
**Jared Freeze (Palo Alto Networks)** 16:40 I think right now… I mean, we're actually in the middle of that sort of integration because of the way our company just got restructured, so we do actually have backend.
Agents sending… IDs, but we haven't actually locked it down yet. Like I said, the… we're using the trace parent recommendation, the W3C meta tag.
But for all the reasons I just stated, it's not the thing people want to use. So, we're still trying to figure that out. I think, at this point, what happens is it's a small call to a config server.
That then fetches it.
Because people are comfortable with that, so it's like a new endpoint that's like, get me a session.
And then come back with it, sort of thing.
**Trent Mick** 17:25 Interesting.
**Jared Freeze (Palo Alto Networks)** 17:26 Yeah, it's not…
**Trent Mick** 17:27 That thing, too, to say, like, what's my current session for this?
**Jared Freeze (Palo Alto Networks)** 17:31 Yeah, we also send data at that point, right? Because it has cookies on it.
So, there's… quite a few things going on. Now, not everybody's gonna want that, obviously, but, it is something that works for us, where you can, you know, and those… and the back end as well is taking in quite a lot about Location, and some other things, so… Okay, thanks.
**Trent Mick** 17:55 Thanks.
David, anything else you wanted to add, or…
**David Luna Bistuer** 18:01 No, no, the sun.
Okay. Yeah, okay, continue tomorrow with the Rosaic.
**Trent Mick** 18:07 Sure.
Okay, this is… sorry, I was pulling off a few to-dos that I have. So, when we did the… the any value… Addition to recently, relatively recently.
Which started off in logs and has now moved to API spec, so this is for the, like, extended types for attribute values. It's all defined around any value.
There's this… languages added way back when, is that when Okay, so originally, attributes could just be… these primitive types, or homogeneous arrays of those primitive types, and those are the simple types of attributes could be. And then.
Later on, extended or complex types were added, and that added all these guys.
So, basically almost anything, but there are… there are certain limits, there's not actually anything. And then, any val… or an empty value, support for an empty value is added, if it makes sense in the language, for example. It doesn't in Erlang, I'm not an Erlang guy, so I don't understand why, but for example, you can… you can set a nun in Python.
And then I think whoever was writing the spec just said, well, here are the empty values for JavaScript and TypeScript, I'll just put undefined in there. However, when we added it, we explicitly have excluded undefined in our implementation of it, so I wanted to go back to the spec and make sure that that gets updated. The reason we have excluded that If you didn't know it, so that you could build up an object where you have conditional… so, like, attribute foo of my attributes object is the value of this environment variable if it's defined, or if it's not, then… Leave it undefined, and then it gets… removed from the… from the object, which is a pretty common idiom in JavaScript code, so we didn't want to break that usage pattern and have a whole bunch of undefined, attributes, which… there's no… in OTLP, there's no distinction between null and undefined, so those undefineds would end up getting… looking like nulls, and it ends up just being kind of messy. Anyway.
So that's an FYI.
It's a follow-up.
Okay… So here's my… Contribution for the Guinness Book of World Records on title length.
There's a bug in… a long-standing bug in our… hotel and our tracing side things, and that for… we've been using these NVARs forever, for 3 years, but the spec actually has these NVARs for the exact same thing, so I wanted to change out. I was thinking we've had them for long enough that we should probably phase them out. Does anyone know of any Bright that we have, and how long of a phase-out period we should do for these things? I was gonna add support for both.
And then after a little time, add a deprecation warning.
Because just adding deprecation warnings right away is a pain in the ass for users.
Of some SDK, if they're using, kind of thing. But I'm not even sure if I'm being too… too conservative on this. So, like, say for a release.
We just document that it's deprecated, and 99% of people won't see those docs.
Then… We had a warning, and then we dropped them after some point. Anyway, if anyone has some opinion, please… comment on that issue, or let me know now.
**Jared Freeze (Palo Alto Networks)** 21:23 I know I'm not actually part of this SIG, but what we usually do is the TypeScript. The TypeScript hint, I think, is actually pretty useful for people. Very few people actually.
**Trent Mick** 21:34 How do you… how do you do that, though? This is just about a function… That internally… let me go find… So… What's the file name?
**Jared Freeze (Palo Alto Networks)** 21:51 You said this is an environment variable.
**Trent Mick** 21:54 Yeah.
Where's the create expand limits here? So, this… this NVAR is wrong.
And this should change to either try to use what the correct MVAR name is, or if that's not defined, then fall back to this one. There's no… there's no place to put the TypeScript deprecation thing that people would see in their ID.
Right?
Because it's about whether they set the envar in their, like.en file, or wherever they set environment variables.
**Jared Freeze (Palo Alto Networks)** 22:27 I think the only way that would work… yeah, yeah, it's… the answer…
**Trent Mick** 22:30 You have a totally different… yeah.
**Jared Freeze (Palo Alto Networks)** 22:33 The answer is no. The only way you could do this is if you had an enum that they were importing and then using it in code, but that's not what's happening here. People are outside the code.
**Trent Mick** 22:42 And the enums in JavaScript are a disaster, so…
**Jared Freeze (Palo Alto Networks)** 22:46 Well, constant sent, but if… if somebody was… happened to… to impact…
**Trent Mick** 22:50 I understand, in the future.
**Jared Freeze (Palo Alto Networks)** 22:51 try to build an ENV file out of it, but otherwise, no.
**Trent Mick** 22:56 Yep.
Alright.
Okay, I'll do a little bit of triage. I'm not going to be going through old PRs, but Please add other topics if anyone has anything.
And I have not looked at any of these, I'm thinking, oh, my feet's not my forte, so if other people have… Any insight on these, please let me know.
Mostly triaging is about adding the… Varity, right? Is this just born, but it works?
I'll take a look after this.
Try to figure out what the appropriate response is.
Trib… I think I'll… Okay.
So someone had some warning where… Type ORM.
Here… was… Using its own version of… OpenTelemetry instrumentation.
Which… was the… 3.0 version of OpenTelemony instrumentation, expecting the logs API to be on the API package.
But it wasn't. Anyway, they couldn't repro. I asked them to show me what their… what their layout of versions was.
Anyway, okay, slide.
Message them, I'll follow up.
Again, we may close it if we can't get a repro.
for that. I think someone had been on… Slack and hotel… Yeah, an OTel.js dev.
Where's chat?
At that link, if people care, with something similar, but…
**Jared Freeze (Palo Alto Networks)** 25:40 Can you scroll all the way to the right in the code block?
I wanted to see that last path.
So that's the new path, yeah, yeah, okay.
**Trent Mick** 25:50 Yeah, yeah, they're using a newer one, yeah.
**Jared Freeze (Palo Alto Networks)** 25:52 Got it.
**Trent Mick** 25:53 It is a 3.0.
I was wondering if this is a mix of 2.x generation and 3. I think you can get… But… It… it shouldn't be allowed, because the… Because they got the… That could only happen if… the 2.X generation of Typeworm had a… dependency range that allowed a 3.X version of.
instrumentation.
Which I don't think is the case when I go to…
**Jared Freeze (Palo Alto Networks)** 26:38 Yeah, I'll speak out of turn and say this is suspiciously, like.
Depending on which package manager you use.
It sort of will pick and choose, like, if something's already in the folder.
**Trent Mick** 26:51 David.
**Jared Freeze (Palo Alto Networks)** 26:52 preferential.
**Trent Mick** 26:52 or something, I don't know.
**Jared Freeze (Palo Alto Networks)** 26:54 Yeah.
Like, if you don't do an isolated install, I recommend most people do that now.
At least in NPM, you can do, install strategy isolated.
Which is going to be the newest… default, I think.
I think 12 may already do this, but it basically makes sure that, you know, it doesn't hunt up through directories trying to find libraries. It doesn't do a best effort. It's like, I'll use whatever you tell me to use.
**Trent Mick** 27:25 that install time, or… it has to be install time if it's a packaging manager, as opposed to Node.js changing how it, at live time, resolves a load, but…
**Jared Freeze (Palo Alto Networks)** 27:36 Yes, this doesn't have anything to do with the loader. It has to do with what's in the file. Actually, if you scroll to the top, go ahead and change your version.
to, latest.
**Trent Mick** 27:47 Legacy on Island there.
**Jared Freeze (Palo Alto Networks)** 27:49 Yep.
**Trent Mick** 27:57 Anyone strategy discussed here?
Linked.
During dev.
I have not looked hard, but I've never found, like, careful… Language descriptions of what those mean.
**Jared Freeze (Palo Alto Networks)** 28:33 Yes, I like this one.
**Trent Mick** 28:34 sense of what they're…
**Jared Freeze (Palo Alto Networks)** 28:36 I've tested them in reality, and linked in Knip is how I found that.
We were missing dependencies, and… And some of the packages.
**Trent Mick** 28:48 So, sorry, say again, what's your recommendation? Or what's your understanding things are gonna change, too?
**Jared Freeze (Palo Alto Networks)** 28:52 I would try it with linked. I think linked, I saw, maybe it was a blog post or something, but linked is supposed to be the newest version. Also, it's what the newest package managers do, because of this issue where… You know, if you have, especially monorepos, you'll have, like, dev dependencies.
Like, in OtelJS is actually a great example, where all the dev dependencies got hoisted to the top, and you rely on the fact that NPM will go ahead and look. Like, if it doesn't find what it needs, it'll just keep going up folders until it finds a node module it needs.
**Trent Mick** 29:22 Node will, at runtime, will keep going up.
**Jared Freeze (Palo Alto Networks)** 29:26 Yes, but not in the.
**Trent Mick** 29:27 Campex.
**Jared Freeze (Palo Alto Networks)** 29:28 But the bundlers have their own resolvers as well.
**Trent Mick** 29:32 Okay.
**Jared Freeze (Palo Alto Networks)** 29:32 So, I actually, I don't know, might be a little confused about the difference between the two, but basically, this will not… When you install, it won't be… like, the package won't be satisfied if the package is not present in the thing that's declared.
**Trent Mick** 29:55 Just gonna see if we have… Yeah, no, we don't have a preference in our NPMRC files.
specified.
Do you, in your repos, do you set some install strategy, or do you avoid NPM?
**Jared Freeze (Palo Alto Networks)** 30:09 No, we use, we use MPM. I tried to get people to use other things, they said no.
But we use LinkedIn.
Just for this reason.
**Trent Mick** 30:18 Do you set it in NPMRC, or in the… You do.
Do you have that in the browser?
**Jared Freeze (Palo Alto Networks)** 30:25 No.
I don't think so.
**Trent Mick** 30:30 Bruh… Yeah, engine strict, I don't even know what that is. Okay.
**Jared Freeze (Palo Alto Networks)** 30:37 I like that.
**Trent Mick** 30:37 That is true.
**Jared Freeze (Palo Alto Networks)** 30:38 No.
**Trent Mick** 30:38 Yeah, nevermind.
**Jared Freeze (Palo Alto Networks)** 30:40 That, is what, engines… like, engines now represents that.
Where it's… you can say, on… fail, you know, warn or error, or whatever. This does error for… versions of Node before the engine's key.
**Trent Mick** 30:58 Which we probably couldn't use in Contrib, because we often get… like… One instrumentation only works with later ones, but other instrumentations are still using the sports version, yeah.
Okay.
Great.
So yeah, just those two that I'll follow up on.
Just a brief look at some recent issues.
NPRs.
One minute ago, Jesus, can't keep up.
There are… if we had a thing on exporter, like a thing so I could subfilter, there are so many issues coming in on the exporters now.
But… I feel bad for… so at some point, we did want… last week, we said at some point, we'll discuss what the new focus topics are going to be. I'm proposing we don't do that until Mark's back, because… He's a big part of doing these things, but… If y'all are interested, prepare your arguments for what things we should focus on.
The reason I brought up that thing about exporters is that reworking, stabilizing the exporters It's probably a likely one.
And then… pick your poison from here. I'll likely be trying to… Finish off some of the work I was doing on declarative config.
But I am… keen to think about the stabilizing instrumentation side things. A data point recently in the OTEL packaging SIG They got surprised by… the support for older versions of Node being dropped in a minor version of Auto Instrumentations Node, and that's because we're in the 0.X region, and I guess I empathize or sympathize a little bit in that it's not that clear to a lot of people.
who are just used to 1.X and beyond versions of SEMVR, where they expect any breaking changes to be in a major.
This… difference in SEM for… when you're in 0.x land is a little bit, surprising for some people, and it's also a total pain in the ass to deal with.
In terms of ranges and support and stuff like that. So, to get… auto-instrumentation's node out of 1.x.
the way we're doing it right now, at least, unless we kind of say, hey, we're 1.x, but it's not really stable yet, would be to, stabilize… Instrumentations, because that's basically what that thing is about, so… anyway.
Stuff to think about for upcoming work.
Okay.
I think that's it.
Unless anyone else has something else they want. Hey, Matt, I saw you showed up. Yes, I'm probably gonna get my… About your issue on the config provider. I'm gonna probably get my, thing that was working on the declarative config path, issue 6999. I've been working on that one so long, I know that it's the only issue that I know the issue number on.
In today, and then I'll be looking at your config provider thing pretty soon.
So I realize I have to get back on that.
**Matt Wear** 34:15 Cool, thank you.
**Trent Mick** 34:18 And then, okay, I'll give you guys time back then.
We'll see you next week.
See y'all.
**Jackson Weber** 34:26 Have a good one, y'all. Bye.
