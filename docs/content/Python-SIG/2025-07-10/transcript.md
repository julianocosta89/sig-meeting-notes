SIG: Python SIG
Date: 2025-07-10
Duration: 67 minutes
============================================================

## Zoom Recording Transcript

Riccardo Magliocchetti 00:05:19 Hello!
Ezzio Moreira 00:05:26 Hello, sir!
Aaron Abbott 00:07:42 Hello, everyone! How's it going.
Dylan Russell 00:07:47 Hello!
Riccardo Magliocchetti 00:07:58 So welcome everyone to this week. Patency call.
We're waiting a few more minutes.
In the meantime, Peter yourself
to the meeting notes as an attendee. And also, if you have any last minute last minute topic, please feel free to add them.
Okay, I think we can start.
The 1st topic is from Jeremy.
jeremyvoss 00:10:09 Alright just got in was having some issues with team the zoom. So this works I'll share my screen. I think that'll make things easier.
Would that be all right?
Riccardo Magliocchetti 00:10:23 Yep.
jeremyvoss 00:10:29 Possible to share just a Oh, yeah, there we go.
like to share just edge. Oh, here we go. That's how they do it.
Okay, can we be able to see my screen.
Riccardo Magliocchetti 00:10:44 Yes.
jeremyvoss 00:10:47 Okay, alright cool.
all right. Everyone to to work on this for a while. But I just haven't had time.
Basically. I do have. I do have this issue that that breaks us down in in much more detail. That's also linked in the in the signals. But essentially, this is sort of been a simmering issue for some time, and we've kind of been like sort of patching and hack instead of solving it from the ground up the core issue is that
we, when we have each instrumentation, has a list of dependencies that that it requires to be present
before it before instrumentation actually begins.
so the most basic case is like the flask instrumentation wants flask to be there, and might have like a constraint on what version of Flask and the vast majority of instrumentations only have a single dependency that they want. So the that scenario is very simple.
The problem is, we have 2 edge cases. We have a handful of maybe only like 2 or so instrumentations that require what I would call an and scenario, meaning they have more than one library that they and they require both of them, or all 3 of them, to be present. For instrumentation.
that's off top my head. There's like Cassandra and and another one, and then there's a few that are sort of the reverse that they want. There are sort of
that. There are more than one scenario that they
want to instrument, and so they want to be able to sort of treat their dependency list as an or so like, for instance, Fastapi, there's fastapi and fast Api slim, which is basically just a different version of fastapi
and instead of having a different instrumentation for that ideally, we want Fastapi to detect either of those scenarios rather than both of them together, when deciding whether they should instrument. Same thing goes for Kafka Python, Kafka, python. Ng, same thing goes for Psychopg 2, and Psychopg 2. Binary.
So those are what I would call 4 scenarios where you you don't need all of the instrumentations to be present. But you you want one or the other.
and essentially for ages. We've treated that actual dependency list that's unlike the project, Toml, and such as. And so the and scenario has always been fine for for manual and auto for doing the dependency check before or after the implementation is loaded. Everything works.
The worst scenario is what's been tricky. And basically, this has led to a bunch of issues in the past, a bunch of multiple breaking changes. There was one where
fast Api push pushed a break, or the fast Api instrumentation had a breaking change. That essentially made it. Just not work, because no one is. Gonna have fast Api and fast Api slim together.
and then, more recently, there have been a few changes that have sort of overwritten some parts of instrumentations that aren't quite designed to do what they do now.
to to make this work for those or scenarios, but have have broken other scenarios in the process. So that's my! That's my kind of long summary but essentially, I have this Pr out now to just sort of fix this issue from the ground up by just like, instead of have having, like some hack.
just adding another field that is treated as, or this would cover cover all scenarios. So instead of just having.
let's say, like instruments, kafka, python, Kafka, python, ng, or fast VPN fast Api slim, which
breaks in some scenarios or just instead of ignoring that second package that we want to instrument. There's now another field that says instruments and then instruments any.
It was originally instruments, either, but people would give the feedback that any would be clear
for even more complicated scenarios. You can have instruments and instruments. Any. This would basically be, let's say, there's like a scenario where you want, you know. Fast Api, and fast Api slim, but in or fast. Api Slim. Excuse me, but in either scenarios you want some like common utility package, or whatever you could do something like this? So this would mean, basically this, this this
instrumentation can instrument foo or bar. But in either scenario we want both of these here.
There's no instrumentation that I've found that would want something like this. Everything seems to be either be an and scenario, or an or scenario
but this is this. Would this would cover all the current use cases? And it would solve this problem from the ground up, because I've changed the actual logic for dependency checks to check both of these.
So that's that's that. There's not so much documentation on this. So for my quote unquote documentation update, I've just. I've updated. I think it's I think it's the instrumentation. Readme. We don't have. We don't have much talks about dependency conflicts in our public like public documentation.
or rather, or like website documentation, just like, read me and stuff.
Everything is passing. Everything is working well. But this is a change that is like designed to both solve some breaking scenarios, and also sort of.
and also solve some some scenarios that there have been sort of hacks for. So I really want, like a like, a good amount of approval on this to make sure it really works for everyone, especially people that have, like vested interest in interest in fast Api, Psycho, pg. 2. And Kafka.
So yeah, that's pretty much it I just want like a lot of a lot of eyes on this since it's I wanna make sure it works for everyone. And then the one thing that has been blocking me is I created another Pr to show how this could be utilized so the previous Pr, it like sets up that feature. But this would be an example of like how it would actually be
used like this. Pr, actually has the changes to those project tunnels. And
it's just sort of inexplicably failing the the rough test.
Which is a bit a bit of a newer part of that that'll pass.
There we go.
The other one is is transient, but this one consistently fails.
It just says that
it just has this. It doesn't really give you much details, and I know rough is a bit newer. We didn't have that this like when I started out so I was wondering if anyone knows what would cause this if rough could be broken or if there's something that I need to do when I update the project tunnels. I've already used the generation scripts to make those changes. So it's not that.
yeah, that's it. Just love love some approvals and and feedback on this pr, and then I need a bit of help figuring out what's going on with this rough check.
Yeah, thank you.
Riccardo Magliocchetti 00:18:51 Thank you, Jeremy, any comments or questions.
Alright, cool.
jeremyvoss 00:19:08 No one seen- no one seen that that rough issue before.
Riccardo Magliocchetti 00:19:13 Okay, thank you. Okay.
Well, I'll try to take a look next week hopefully, ask you.
Thank you.
jeremyvoss 00:19:23 I'll stop sharing.
Riccardo Magliocchetti 00:19:34 Okay, okay.
Next topic is from me, yeah, just a quick update. I'll try to cut
a new release tomorrow. I think it's due.
And if you miss something or something, we should really get in the next release.
Please say something now.
because I release. I think it in my tomorrow morning. So it's night for most of you in the
American time zones.
And yeah, I just just a couple of notes there on Wispia from
Dylan on updating Bottle Core using log directory instead of events. Api.
And I think we can match this already, since the instrumentation is released with the others and is not like released
on its own, like other Gen. AI stuff.
Or do you want to wait.
Dylan Russell 00:20:49 For.
Yeah, I wasn't sure how this works exactly cause this Pr needs
the event name to be in the log record field.
and that is still in the unreleased changes in the hotel. Python. Repo.
So it'll yeah. This change will basically require that users have
whatever. The next version of Hotel Python is.
Riccardo Magliocchetti 00:21:32 Okay. But I think that like, you need those I don't remember.
Oh, because, like, I'm pretty sure like this depends
somehow on the always on the latest
release video, I remember wrongly, and we'll double check.
But okay, yeah.
yeah, I'll try.
Dylan Russell 00:22:06 Look.
Yeah, I'm not sure exactly how it works, but.
Riccardo Magliocchetti 00:22:11 Yeah, because, like, which should be fine, because it will always be using the
the release done at the same time. So it will have the
like. This documentation we already use the next open 1050 python release. I guess so. It should be fine
also, like green, because it's using testing, I guess. The main on.
Dylan Russell 00:22:39 Oh, the Korea possible?
Right?
Yeah.
Riccardo Magliocchetti 00:22:47 And yes, speaking of changes in logs, we have another Pr from actor.
But again, I think we have to find a way to not break compatibility.
Yeah, I don't think like this. We get in the next release. So if you have a
time, please take a look and review.
and also like, if you have any idea to, to, not to break compatibility would be great. Yeah.
Hector Hernandez 00:23:26 Yeah, I tried as much as possible. I'm not sure how not break. In this case. This is like a big change. So yeah, any feedback is
will be great. Thanks.
Riccardo Magliocchetti 00:23:40 Oh, thank you for the Pr.
Aaron Abbott 00:23:42 Yeah.
I think I think we have a lot of breaking changes we need to do for logs. So there's like a
the SDK log record. I don't know if anybody
got around to that yet, but the
it it doesn't really need to have. We don't need a separate Api and SDK log record.
I think it should be in like our backlog. There's a project planning board and a bunch of stuff was raised by the from the Tc review. There's also, like the export format
it pretty much
it. It conflates like this SDK log record with the export format, and it doesn't really look like the one that we built for metrics. So
there's that.
yeah, I I don't know. I guess I guess we could keep doing this and try to make everything compatible, or we could
try to stage the real stage, the breaking changes together to reduce the kind of disruption to users. What do you think.
jeremyvoss 00:24:44 Think like one thing that would be beneficial. This this would, this would apply for some breaking changes. Not all. I'm not sure about this one
is.
Even even if we're just not, we might not necessarily have, like a formal sort of dep, like a deprecation process, for, like breaking chains and stuff. But if we are like removing certain items, even if even if we just
like, add like a deprecated message
to the old sick, to the old object, or or yeah to the old object. For like one release, that would be really helpful. But if we are like changing a form. If we are changing like a format, for instance, then it doesn't really solve that because it's not. It's not that something is missing. It's that something changes
so I don't know if that applies to this, but that'd be helpful.
Aaron Abbott 00:25:37 Yeah, I mean, I think we are kind of doing that. But if we, if we have 3 consecutive releases that deprecate things, and then people are like, I just fixed these deprecation warnings.
They might get a little bit annoyed. But
jeremyvoss 00:25:53 Another thing some were proposed was, if we had some like
top level. Do do we mention anywhere? I I guess we do have a section in the change log that says breaking changes right?
I think we do.
Aaron Abbott 00:26:09 Maybe we're thinking of another repository.
No, I mean.
jeremyvoss 00:26:12 So yeah, some way to like at the top level just signal. There's something to look at.
Aaron Abbott 00:26:22 Yeah, I mean, I'm not sure if people read the change log, I think.
Sure, yeah. Like having having the
The the deprecation is nice. And then moving to the thing. I just I guess I'm just saying it'd be really nice if
people didn't have to do multiple rounds of
cleanups in their code, or or also like.
if our ecosystem at least could be consistent. So
unfortunately, we're gonna have contribute instrumentations that that create warnings right
like. I think that Pr. That that Dylan mentioned right.
Dylan Russell 00:27:05 That.
we didn't submit the change to put like the deprecated stuff on events yet. But if we had, yeah.
yeah, I think we can update all the instrumentations
before we do that at the deprecation warning.
Aaron Abbott 00:27:28 Yeah.
Dylan Russell 00:27:28 Oh, yeah, maybe that's not possible in all these cases.
Aaron Abbott 00:27:38 Yeah.
So I don't know any other thoughts on that like.
Dylan Russell 00:27:47 I like the idea of just doing it all at once, like getting all the breaking changes together. And
I mean, yeah, I like the idea of a deprecation warning for like a release or 2. But
then just just making the change.
I don't know. Yeah.
Aaron Abbott 00:28:12 Okay, so so, Ricardo, for this release, do we have any?
Did we add any deprecation warnings for this release related to logs.
Riccardo Magliocchetti 00:28:20 Yeah, we have. There are names, a lot of logger names.
Aaron Abbott 00:28:25 Great.
Riccardo Magliocchetti 00:28:26 But we like. We only have deprecation warnings. We don't have removals yet, so.
Aaron Abbott 00:28:34 Okay? And as just kind of like a barometer. If people use the next release
and assuming they're just using, like Otlp exporter and contribute instrumentations. They don't have any manual usage of this stuff. Are they? Gonna see
any warnings? Would they see that deprecation warning, or would it be a silent.
Just everything's fixed at once.
Riccardo Magliocchetti 00:29:00 Oh, I don't know.
Aaron Abbott 00:29:05 Cause. I think there were some exports right? So like
Riccardo Magliocchetti 00:29:09 Like if they're if they're using the interfaces.
Aaron Abbott 00:29:12 Or they're using like I think one of the Renames was probably the log processor.
Do we rename the Batch processor, or that was already called log record batch, logger processor, right.
Hector Hernandez 00:29:26 Yeah, we'll rename that one.
Aaron Abbott 00:29:29 Okay, so yeah, like, the user will have to take action.
Sorry they won't have to take action, but they'll see a warning if they don't
do this change just from this release. And then, if we have more next release, I guess it's it's fine. It is what it is. I don't wanna
necessarily block.
But yeah, I I guess I'm just trying to say it would be great if we could
reduce the number of times that people have to deal with the deprecations.
Dylan Russell 00:30:01 Yeah, that makes sense to me.
Riccardo Magliocchetti 00:30:05 Yeah, like. But the problem is that like we hadn't not, you know.
like not everyone is working on this thing at the same time. So
the changes will come once once it works. So yeah.
Aaron Abbott 00:30:23 So so sorry were we trying to merge this one for the current for the release tomorrow.
Riccardo Magliocchetti 00:30:29 Oh, yeah, if thought but I would. I pressed merge this morning. But I probably yeah, something failed. Yeah.
Aaron Abbott 00:30:41 Okay. Okay.
Riccardo Magliocchetti 00:30:45 So I don't know. So maybe like we can skip and do
all the log records, the the names at the same time. Yeah, I pressed.
Yeah, but free.
Aaron Abbott 00:30:58 Yeah, like we could set up a we could set up like a
milestone or something for the next release, with all the bugs for for all the breaking changes we want to do, add, add all the deprecations and
the following release, and then do the actual breaking change in either a
1, 1 or 2 more releases after that. But
does that seem reasonable? Is this one urgent? Hector.
Hector Hernandez 00:31:25 No, not really. I'm just trying to push the stability for logs here. But yeah.
Aaron Abbott 00:31:29 Magic.
Okay, so what do folks think of that? I mean, I I don't have a super strong opinion, but I just want to minimize the annoyance to users.
Dylan Russell 00:31:44 Think, that makes sense.
jeremyvoss 00:31:46 And I think we might be able to do it.
Dylan Russell 00:31:53 Yeah, I'll probably have a little bit of time to work on some of this stuff, too. So I can
yeah, work on a couple of the changes that were mentioned.
Aaron Abbott 00:32:05 Okay.
Riccardo Magliocchetti 00:32:06 Okay.
So maybe, like, we can revise
after we merge everything we have open after the next release.
and we'll see like what is missing
and what we'll be breaking. So yeah, yeah.
Aaron Abbott 00:32:26 Yeah. So we should make like a I don't know if people like these milestones. We could also just use a label, but we could add all the bugs
that will have breaking changes to logs. I mean, obviously, we can't read the future and know everything, but we could add those to either give them a new label or give them a milestone, and then plan that for the next, not not the release tomorrow, but the following one.
Riccardo Magliocchetti 00:32:49 Yeah, makes sense. Let me add it to the notes.
Okay, thank you. Any other comment.
Otherwise we move to the next topic from Ezium.
are you there? Yeah.
Ezzio Moreira 00:33:45 Yeah, I think that have a comment.
I think that you in Kandu, can you?
Yeah, I work in this pr, should they create the you spend attributes, and
we need to decide what value returning in in this function
1.21 or 1.23 I don't know
our version. I return this function.
Riccardo Magliocchetti 00:34:42 I don't think I have an answer
so like maybe like for Vspr, I just stick with the same schema version, and then.
probably like we should revise. Like.
because I don't think our schema version matches the actual semantic convention exported. So yeah.
But yeah, like, for sure, like, I'm pretty sure, like the the
the stuff we were adding are probably are being added added later than 1 21.
So but yeah, so as I just had to like minimize the changes of the
of the schema version we export. And then, probably, like once we have
now, we double check what we're actively supporting, we should probably stick with your version
that matches the reality. Yeah.
does it make sense to you?
Ezzio Moreira 00:35:59 Nope.
Riccardo Magliocchetti 00:36:01 Okay.
Ezzio Moreira 00:36:05 Thank you.
Riccardo Magliocchetti 00:36:06 Thank you.
Okay.
And then next topic from Aaron.
Oh, yeah. I saw.
Aaron Abbott 00:36:21 Yeah. Can you hear me?
Riccardo Magliocchetti 00:36:25 Yep.
Aaron Abbott 00:36:26 Okay, good. Good so I saw that I think, Ricardo, you added this to the topics last time, or somebody did. Did did we discuss this more or no, and.
Riccardo Magliocchetti 00:36:37 Yeah, I think by the media did go through the the notes, he added, that's so.
Yeah. But.
Aaron Abbott 00:36:47 Oh, oh, I see. Yeah, Media added some to the previous.
Riccardo Magliocchetti 00:36:51 Yes.
Aaron Abbott 00:36:53 Okay, I mean, I would. I would like to kind of
get more feedback from the group. Like we could even do.
Riccardo Magliocchetti 00:37:03 There you go!
Aaron Abbott 00:37:04 Kind of a capacity plan where people just like we did this in the Jen Aisig, where people tallied, you get 10 or 100 points. And then people
would write what you're planning to focus on, like, where you'd allocate the points so we could see what's
what's actually important to people in the next 12 months.
Yeah, I think biggest achievements. I would agree with
with the stuff that Nmedio added.
but yeah, maybe maybe other people have more achievements. They want to point out.
Yeah, for for me. I wanted to bring up the configuration. SDK,
for example. So it'd be cool to know if other people support that. So may maybe for next time I'll set up a
I can kind of copy the capacity plan spreadsheet we did.
and we could do that as a little exercise, maybe time box for like 10 min or something. But
yeah. And then the last one was this, sub projects that the Gctc can help with.
Video, you add some stuff forgotten it.
Anything more automations?
Yeah.
Riccardo Magliocchetti 00:38:19 Yeah, the issue is about having more permissions on the token used by open telemetry. Bot right?
But at the moment we have, I think a couple of Prs just reducing the permissions. So something like that so.
Aaron Abbott 00:38:34 Okay, yeah, for me, I don't think we have any any big blockers with Gctc, like.
if we, as we keep going with kind of some of this Gen. AI work. I think that's the biggest, the biggest area. So there's like
complex attributes.
It was something that we're discussing there.
I I feel like it, would I? I try to attend the the Spec Sig meetings, but
it could be pretty hard to know all the small things that were added.
So
that's that's 1 thing I would like things to be a little better in is knowing what spec changes are actually important and need to be implemented.
You know, for example, if if the spec matrix gets updated, it'd be nice if
we were made aware of that kind of stuff with an issue in our repo.
But yeah, okay, let's do the the capacity plan thing. Next time
I'll put a note in the doc and I'll I'll set that up.
Riccardo Magliocchetti 00:39:35 Thank you.
Thank you. Adam.
Aaron Abbott 00:39:39 Yeah.
Riccardo Magliocchetti 00:39:44 Okay, then, last topic we have for today is Sergey.
General installation. SDK.
Sergey Sergeev 00:39:54 Yes, sorry. I had some issues with my connection, but finally could join.
So is it, my topic being discussed now?
Riccardo Magliocchetti 00:40:06 Yes, subscribe sure.
Sergey Sergeev 00:40:09 Yes. So Aaron probably knows about this idea from Lm special interest group, where we quickly
briefly discuss this idea. But in general there are some number of Gen. AI. Or Lm. Instrumentations.
for example, instrumentation for Openai instrumentation for Google, Vertex, and etc. And each of them emits some telemetry.
and I believe, as a community now
thinks about 2 types of telemetry where events.
all logs coming from Gen. A. Calls may be optional.
and the idea was to create. Basically, this boilerplate
Common Library as part of the python contrib. So the instrumentations can be simplified.
and some of that boilerplate code can be moved to that general instrumentation. SDK,
and first, st I wanted to get some feedback because I I couldn't find any examples of
this in the current python can tape. So what the community thinks about it.
Aaron Abbott 00:41:55 Yeah, I mean, I think I I've made it clear in the other Sig, too. But I'm in favor of this.
we have this kind of thing for for, like Http and for sequel, and it's been pretty helpful to have kind of some shared code
obstruct away a little bit of the boilerplate.
Sergey Sergeev 00:42:11 Yeah, you can.
I can. I can show briefly, just the rough idea of what it may look like. So I think this group maybe
way better thinking in terms of code. So
Aaron Abbott 00:42:30 Oh, awesome. Yeah.
Sergey Sergeev 00:42:32 Yeah. So in general this is
the home of general instrumentation in the python country.
Can you see my screen?
Aaron Abbott 00:42:44 Yep. Yep.
Sergey Sergeev 00:42:46 And can you is the type.
Okay? Or do I need to make it bigger.
Aaron Abbott 00:42:52 That's good for me. Yeah.
Sergey Sergeev 00:42:54 Okay. So we have the instrumentations here. 3 of them are already implemented, and one of them is instrumentation, and chain is still being worked. So it's part of trace, whoop, donation. So we are moving this instrumentation from tracewoop
repositories into open Celematte. But we need to change some
telemetry which it emits. And we need to support. Now 3 different types of telemetry and
right? So basically, instrumentation is simple. It uses land chain callbacks where you get
where where you can plug your callback handler
and on different events in the framework.
you can emit basically some different.
So to simplify it a little bit. So I just tried to do this poc with Gen. AI SDK,
was it shared to library?
And I think I am in a wrong branch.
Something else is going on.
But yeah, let me quickly find the proper one.
because it's not the the right branch.
Sorry for that unprepared.
Aaron Abbott 00:44:30 That's okay.
Sergey Sergeev 00:44:31 Oh, we have to share the link to Poc. And
oh! And Pablo mentioned that there is some. There are some helpers for Sd.
For SQL. And Http.
Pablo Collins 00:45:20 Aaron just said that there were, and do we.
Aaron Abbott 00:45:25 Yes.
Pablo Collins 00:45:26 Do we already have this for SQL. And Http.
Aaron Abbott 00:45:29 I think what Ricardo said is what I was thinking. So we have, like a dB. Api. We have like a whiskey, which are at least composable things that people can reuse. I think it's not. It's not one to one, because at least there's like a existing
standard in Python already for those. But
there's also there's a little bit of Htp stuff. I think we have.
for example, we have some shared libraries for preventing Http instrumentation from recursing
just really basic stuff. But I I think we've found it pretty useful. Is that what you meant, Ricardo?
Riccardo Magliocchetti 00:46:07 Yeah, like, I was thinking more on the
and the effort started by Layton for
for the same curve. But yeah, probably like whiskey and stuff like that.
Sergey Sergeev 00:46:24 Okay, second, try. So basically, the SDK, how it simplifies development. So for different types of telemetry
or Jenny, a
interactions, we might be interested. We can provide some helper methods like Start Om, which accepts different
attributes which are not yet connected to telemetry. So basically, your instrumentation library can report something like start. Om, and it can import model prompts, or even keywords dictionary.
And in general we can 1st
internalized word as an object representing some of those interactions. Again, it's not the telemetry yet.
and it helps. It can help to build different experts. So here, for example, just as a sample.
I,
introduced an expert service produce span metics and events. So it basically turns that internal structure into the telemetry needed. But user can configure, for example, to emit just span and metic, and instead of
emitting request and response from our model as an event, it can put those on
span attribute. So for some backends, it's preferred methods.
And so and as well, we can maintain backward compatibility with trace, whoop by waiting them to implement that trace whoop, exporter
so they can, using Ucode and have some time to migrate to semantic convention expert here.
and additional additionally, we can do something like instrumentation sites, runtime evaluations for Om request responses.
This is just an idea how you can integrate something like external callback handlers. And again, you
they can use gen AI SDK types
such as that element location structure. Instead of just trying to parse SDK,
trying to understand which Sd trying to parse telemetry
directly trying to understand. Is it
like span metric and event forever, or the telemetry, or is it just span and metric? And I need to look up
that, he viewed on span hopefully. It provided some high level idea.
Let me know. I I think it makes more sense for Aaron or anybody taking Jenny a special interest group.
Aaron Abbott 00:49:55 Yeah, definitely.
I think I think this is great, even just like the most basic stuff of having shared data types between the instrumentations
not having to reinvent the wheel. So if you prepackage this kind of stuff you can get.
have have some more shared instrumentation code that that does the actual emitting like you showed
So I I was wondering if, for, like the initial Pr.
do you think it's okay to scope scope it down like, for example, Skip. Could we do the Evals in in a later Pr.
Sergey Sergeev 00:50:29 Yeah, yeah, definitely, this is poc, so I'm trying to validate the whole idea end to end
for initial. Pr, I think it will be just
basic Api to report Lm invocation, because this is fully defined in semantic convention and same
to provide basically just one type for
Lm. And vacation, and one exporter which will or converter, probably exporter, is a little bit just.
will be too ambiguous because we have
telemetry exporter. We will need to figure out name, but it will be just the one to turn to telemetry.
as, for example, Openai instrumentation does. So Openai can be the 1st target for
to showcase how to use this SDK from an instrumentation library.
Aaron Abbott 00:51:41 Yeah, I think this is great. Oh, Ricardo, get your hand up.
Riccardo Magliocchetti 00:51:44 Yeah, you have a couple of questions.
And the 1st one is so like.
like kind of related to the Poc. But so do we have news about the trace loop donations, because I
yeah, me follow the.
Sergey Sergeev 00:52:01 Yeah, we we are in talks with them. And specifically, I'm I'm from Cisco. Sorry I didn't have my name, and we are working with them to do that. What we discovered trying to
to to move.
Basically. Sorry. Can you hear me?
Riccardo Magliocchetti 00:52:25 Yes.
Sergey Sergeev 00:52:27 So what we discovered trying to move just link, chain instrumentation. So 1st of all, trace, whoop, internally, use a word of proprietary named attributes like tracewoop dot. I don't know
token usage, or something like that. So for
attributes not yet defined in semantic conventions.
they use proprietary attributes. So we needed to rename them or to drop them because we don't have yet semantic conventions defined for it.
And second,
basically, when we do it when we convert everything to semantic convention, because we miss some of the attributes definition in semantic convention.
we basically have to to reduce the telemetry we
produce for now. And this is the problem. So for trace whoop, it doesn't make sense if we produce less data than they need. So and this SDK. May be an option to
to add them to produce the telemetry in the format they need until semantic conventions is catching up with defining them properly.
Riccardo Magliocchetti 00:53:59 Okay, makes sense. Thanks. So like, the idea is that they they use this code.
And maybe, like, you'll have some hooks there, and we'll just use these hooks to like, enrich what we can export. Okay, yeah.
Sergey Sergeev 00:54:14 So Api will be richer
then it's consumable for semantic convention telemetry yet. So we can pass every all the data we we basically get from the instrumentation
callback. So instrumentation callback gets all the data so we can pass it to start Llm. So attributes we already defined in semantic conventions can be named, everything else can be passed as dictionary.
and we can have them all
in the course where we can have basically the dictionary for those undefined yet
and trace, whoop can implement an exporter, or we will implement a backward, compatible exporter which will use all the data in python to produce, trace hoop telemetry.
So we we can really let them switch to this library instead of maintaining their own copy.
And in semantic convention in Lm Semantic convention group. We can work to bridge that gap.
to define all the attributes not yet defined.
Riccardo Magliocchetti 00:55:39 Okay. Thank you.
Sergey Sergeev 00:55:41 And this is a kind of bright idea. I don't know if it turn into some maintainability hell as we go, but we can prototype it, using specifically a land chain instrumentation. It's quite a big instrumentation and defines a lot of type types. I think if we can make one chain, one graph instrumentation
transition to using that SDK, we will cover most of the cases.
Riccardo Magliocchetti 00:56:17 Thanks. Yeah, I would also just like to also try to convert the Openai
instrumentation currently have, because it's, you know, the style is very different from.
Sergey Sergeev 00:56:30 Yeah, that's cool
is just 2 types which should be covered even with this Poc, because it's just oh, I'm on vacation and 2 in vacation. So right now, I don't think it provides
much more. What do you think?
yeah. What do you think, Karen?
Do we need
something?
It's basically chat completion.
We do need to figure out how to support Sync and Async here
I didn't even look into. I think, in the vacation support.
Maybe maybe it's not different at all.
Riccardo Magliocchetti 00:57:23 Yeah, it's just like some duplicated code with a sync. Yeah, I told you, select.
Sorry. Go ahead. Sorry.
Aaron Abbott 00:57:34 I was. Gonna say, I had to step away for a second. I have some
some kind of code that might be good inspiration in the vertex in the vertex package
in this repo.
Yeah, that one I think if you go into, I'm trying to wish.
So one of them is events.
There's just a bunch of data classes there which is not super interesting. It looks like you kind of already have that. But
this is based on the current semantic conventions. But it's it's just like a hook point that somebody would call to do the stuff. So you pretty much have that figured out.
If you go into the maybe it's patch.py
and if you yeah.
So these both call this with instrumentation helper.
If you see that on 1, 65.
Sergey Sergeev 00:58:36 Yeah.
Aaron Abbott 00:58:39 So this, I think this is a kind of nice approach that lets you do sync. And Async.
because you have just one function with the context manager and the outer function would be sync or async, and then within the yield block.
The the person who calls it can await
the inner response. If that makes sense. So maybe just take a look at that one, let's do it on the call. But
I did think about this problem a bit.
Sergey Sergeev 00:59:09 Okay?
Yeah. I'll
pull up with just the branch. Get a rough idea it's not yet even working end to end.
Maybe maybe next week it will be more polished. So somebody once we done the Poc end to end. We can break down that pull request to smaller skeleton, probably with just 2 invocation support
and basically to to review it.
Yeah, please let me know. And Pablo is from splunk as well. So, and he's
old Timer in this group. So
again. It will be probably somebody else from my team showing up on the next call.
or maybe Pablo can represent us.
Riccardo Magliocchetti 01:00:24 Okay. Thank you.
Aaron Abbott 01:00:27 Cool looking forward to it. This is really things will be pretty helpful.
Sergey Sergeev 01:00:32 Yeah. And some things which I realized may be redundant. So ideally, the types should be just brought above
schemas for telemetry. So if
if it gets developed that far, we can optimize it by introducing the proper expertise, maybe, and turning all the the
types interpret above.
But I think initially, it will be more dynamic just to support
specifically Gen. AI domain which is evolving very quickly.
Aaron Abbott 01:01:21 Okay, okay, sounds good.
yeah. My only other feedback would be. I think I think I mentioned this before, but it would be great, if you can opt this new subdirectory into the into the typing.
it makes it much easier for like review and maintenance, and I think
for a Core library. It would be good.
Sergey Sergeev 01:01:47 Yeah, I'm I'm still an Iranian python. After
like 7 years of Java, go and break. So
yeah, we'll appreciate this community help. But hopefully. Pablo will keep me honest
even before I reach out to this group.
I'm also learning Python Sergey. So
python, 3 after python 2.
Pablo Collins 01:02:14 Yeah, exactly.
Sergey Sergeev 01:02:23 Okay.
Thank you.
Riccardo Magliocchetti 01:02:26 Okay, thanks again.
So this was the last topic for today
we have a couple more minutes. If anyone has something else to add.
Otherwise see you next week, and thanks everyone.
Pablo Collins 01:02:47 Thanks. Bye-bye.
Ezzio Moreira 01:02:48 Cheers.
Riccardo Magliocchetti 01:02:49 Bye.
Aaron Abbott 01:02:49 Later.
