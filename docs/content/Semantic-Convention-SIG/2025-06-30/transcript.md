SIG: Semantic Convention SIG
Date: 2025-06-30
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:51 Hello!
Trask Stalnaker 00:02:00 Oh.
Whoa! That's not me!
Alright, shall we? I think Josh is going to be late.
Liudmila Molkova 00:03:42 Let's get started. Do you wanna drive? I I can try whatever you like.
Trask Stalnaker 00:03:48 I can drive today.
Alright let's start with our triage board.
and so we want to start over here.
Looks like oh, no!
All right.
Liudmila Molkova 00:04:54 Maybe we can hit March when ready, so when
sure resolves, or you would rather wait.
Trask Stalnaker 00:05:01 I think it gets merged when ready gets cancelled. If you push another commit.
Liudmila Molkova 00:05:08 I see.
Trask Stalnaker 00:05:13 We can try it
alright needs more approvals we got
Jen AI is this? Let's see.
Liudmila Molkova 00:05:42 I think there are some comments that need to be resolved.
Trask Stalnaker 00:05:50 Gotcha
clarify count maybe we can talk about this.
Liudmila Molkova 00:06:04 Yeah, I'll add it to the agenda.
Trask Stalnaker 00:06:07 Okay, I'll jump the link there.
Create entities, registry.
So we've got approvals.
I'm gonna mark it ready to merge.
Once.
Basically, comments are addressed.
gen, AI, gen, AI.
Sam's Pr, alright. We are making progress here.
Cool.
clean up of docs.
Okay? Needs more approvals.
This one went. Okay, span ended.
So we've got 2 reviews from the helpful we've got some and resolved.
It was active. Okay, so let's wait for that one to calm down.
Oh, man, this was a massive
yes, I think you've got
approvals now. We should probably merge before.
cause it's just gonna keep gathering conflicts.
Liudmila Molkova 00:08:37 Yeah. So I'm thinking, sorry, I added to the agenda. I want to talk about your question. I think it's a great point.
Trask Stalnaker 00:08:44 Okay, cool.
Oh, yes, and this will be interesting. So
we can't. Is, are you thinking that basically
one of us will request the co-pilot review manually, each on each Pr.
Liudmila Molkova 00:09:09 I'm thinking we should start by manually requesting it, if it produces anything meaning consistently, where should try
enabling good by default.
Trask Stalnaker 00:09:28 Oh, Ken, I didn't know you could enable it by default.
Liudmila Molkova 00:09:31 Yeah, you can.
Trask Stalnaker 00:09:33 Okay, great, great. Okay. Yes, I agree with, let's see.
if it produces if it's useful.
Also. We have a
ticket open with the Cncf. We've had it open for a few months about getting
maintainers co-pilot licenses.
and so cause right now like you can click. You can request a review. I can request review because via Microsoft is paying for our co-pilot licenses.
But not everyone has that
Liudmila Molkova 00:10:24 I didn't know that. Good to know.
Trask Stalnaker 00:10:27 Yeah,
so I did just ping them on Friday. That Cncf ticket to try to get some more movement on that. It seemed like they were in discussion with Github to let us
to do that. So I'm I'm optimistic. Part of the problem is that we have a hundred 20 maintainers across open telemetry.
So they kind of initially.
That was a lot. But I'm still optimistic.
Alright, and so we'll probably hit our time box.
Anything in these. Okay? I saw this one
is blocked on. Now on this. So that'll be great.
if we? Yeah, we'll talk about that later. If we do get this in, I could use this
to. I'm gonna make planning to make the release today.
if we get it in, I can test it out in the release. Otherwise we'll just test it out next month. It doesn't really matter.
Liudmila Molkova 00:11:57 Oh, wonderful! I'll I'll try to get it in today.
Trask Stalnaker 00:12:06 Oh, this one was just why is this blocked?
Add docs for context, info propagate. Oh, this was the original.
Okay, so, Sam, this is kind of superseded by Sam's Pr. I think to talk. Okay.
Liudmila Molkova 00:12:40 I actually chatted with Tammy and Lynn on this.
They are quite interested in this effort we talked about
how to make it less problematic surcy call commenter.
We talked about, maybe yeah.
having a special implementation of propagator that users would provide SQL commenter, propagator.
And then it's also an opt-in mechanism.
And maybe in some cases we can be smart enough and propagate something if we know it's not the prepared statement.
But essentially, I think, we what I realized, we made this Pr somewhat contentious.
and people were thought there is no way to make progress.
But I think that there are ways.
Trask Stalnaker 00:13:44 Okay, cool.
Okay, cool. Let's move on.
General topics. Yes. June. Release the last day of June.
Planning to hit the release mechanism today? Any.
So if we do get those
automation Prs, and that's great. Oh, so do you.
Yeah. So why don't we add
Liudmila Molkova 00:14:39 Milestone.
Trask Stalnaker 00:14:40 Matters.
Liudmila Molkova 00:14:41 Hmm.
Trask Stalnaker 00:14:42 Yeah, that's a good idea.
So what do we got here? 1, 35.
And so let's this one would be
nice to get in is this required to get in weeper.
Liudmila Molkova 00:15:17 Oh.
this is necessary because this is this updates weaver version. And without new weaver version, the schema next generation doesn't work.
Trask Stalnaker 00:15:30 Okay.
But I mean, if if we didn't get a either this or the schema next generation in is that okay for the release. Okay, so we'll we'll try. But if it doesn't work only because I'm I'm on vacation tomorrow through the rest of the week.
So today's my last day to make the release. Otherwise, I mean, I know you could make it later this week.
although it won't be June release anymore.
Liudmila Molkova 00:15:58 Yeah, let's try today. If it doesn't happen, it doesn't happen. That's fine.
Trask Stalnaker 00:16:02 Cool.
Let's see does. Is this gonna work is approved.
Did work.
But I guess anything that we had.
Yeah. So anyone on the call have anything specific they want? In this release.
Alright. So that's all. We will
see if we get those in today and make the release.
James Thompson 00:16:58 Perhaps you could look at a couple of my small prs that already have one approval or so
right? Because a couple of them are editorial ones. A couple of them are just extending enums.
Right? So they're not adding attributes. It's just editorial ones.
Trask Stalnaker 00:17:19 Okay, could you drop could you drop links to those in the meeting notes here?
James Thompson 00:17:26 Yep.
Trask Stalnaker 00:17:27 Cool.
Nice to meet you, James.
James Thompson 00:17:36 Yep.
Trask Stalnaker 00:17:40 Alright. So let's go on, Lamila.
Liudmila Molkova 00:17:47 Yeah, I wanted to chat about. Oh, and Josh joined. Nice. Josh.
I. We had an interesting discussion on whether
changing the value type of the metric is breaking, or a knot so.
Josh Suereth 00:18:07 Let's do hint to double by specification. It's not breaking.
I don't know if I showed you the specification. But yeah, we we tried to specify. So it doesn't matter in practice. That's a different question. Does it actually break endpoints? Because they probably don't pay attention to that spec
if you want I can find, like in the spec. It legitimately says that changing from int to double should not affect
like your consumption of a metric.
that's why we never specified it in some comp to begin with. What? What's the the general thought right now in the group, though, before I just jump in with what the specs is.
Trask Stalnaker 00:18:56 Yeah, so I don't know if you cut this. The kind of the context here of the discussion is basically CPU count in a couple of places is marked as an Int.
But potentially future proofing, or in the future it might
want to be a double for accommodate milli cores
but it seems like, since it's not a breaking change to switch to it from int to double
that maybe it doesn't really matter, and we would just leave them as int.
For now, since that's what they are today and
in the future, if you know.
5 years from now, if the Java introduces a milli core aware CPU count, then we can switch it.
Liudmila Molkova 00:20:04 I think there is a similar problem on that net where the the value is taken from a variable that's int
changing the value type or introducing new Api. It's probably a major version bump for java.net.
and even though the semantic conventions might not change the any real application, would expect some breaking changes for a major version of the Runtime. Right?
So it will be okay. Even if it was breaking.
Josh Suereth 00:20:44 Yeah, I think
my point was that the by protocol, it's not breaking. I'm checking the Api quick, because I think
like what you're saying is the Api you create where you create a counter with an int, or create a counter with a double.
Would that be breaking right? And I think it might.
Oh, sorry!
Getting attacked by cat.
Go ahead.
Braydon Kains 00:21:14 I understand why it's not breaking as as protocol. But
considering semantic conventions are also defining what back ends would expect, and back ends. For example, the one that we're most concerned with cloud monitoring does care about like the interpretation of the metric as an inter a double. And so does that mean that like, it's not breaking at a protocol level. But we're breaking the expectation by changing.
No. So cloud monitoring we do use whether it's inch double in some of our stuff, but we're moving to double everywhere.
Okay. I didn't.
Josh Suereth 00:21:49 Yeah, like, like. And again, that's for Prometheus. Compatibility. Right? Like, Prometheus, is double everywhere effectively.
So we, we're also doing the same thing. But that's
yeah. Anyway. Like like to to your direct point. Yes, like some of our internal systems, allow types from an open telemetry standpoint, and the protocol of open telemetry. We have said the the type shouldn't matter. It's an efficiency reason to get the point across. If you have a system that is doubles only great. If you have a system that does support types, and you'd like to leverage them, you can. But if it changes from an into a double that should not break your system.
Braydon Kains 00:22:29 Okay? So it's so if it if it basically we should, we should tell backends
consuming the semantic conventions not to care about the value type.
Josh Suereth 00:22:42 Yeah. And in the Api specification
the value type is actually not listed
as a like required field. It's actually not even listed kind of as a field, even.
Braydon Kains 00:22:56 It's allowed.
Josh Suereth 00:22:58 But it's not listed in our Api specification.
I remember we had a lot of talks about that, like 2 or 3 years ago.
Trask Stalnaker 00:23:05 But we're promoting that here now to a very visible part of the semantic conventions.
Braydon Kains 00:23:15 Brush him.
Josh Suereth 00:23:16 Yeah, I was. I was personally not a big fan of adding this on weaver myself. But that's that's for other reasons, like like
we. There's reasons folks want it. I get it. And I think part of it is about Cogen. Cogen is harder without it. But I also think even when you have int and double, there are languages where like, even if I use int, I have to generate more than one type of int, because is it uint? Is it regular? Int, is it? U, 32, you know. Like, what size of int do I need to support? I think we languages that have typed primitives
are somewhat problematic for us. Right? So
yeah, I I understand why we want this. I understand. What we're trying to do here. It's just we're going against the specification.
We're going against the protocol.
And we're putting on like requirements that actually aren't there today. So if we want to do this, and like force it out all the way upstream. I would recommend we change the spec in some way
for that, but that would be a breaking change.
Go ahead, Lydmilla.
Liudmila Molkova 00:24:24 I'm thinking 2 things first, st maybe we should call it differently. Maybe we should call it value type Api hint or something
to say. It's.
Trask Stalnaker 00:24:35 Yeah.
Liudmila Molkova 00:24:35 Requirement.
Trask Stalnaker 00:24:37 Don't we have, weren't we? Considering like a code? Gen.
Liudmila Molkova 00:24:44 Oh, yeah, no.
Have annotations. We we can.
We can have them.
We actually don't even need viewer changes to implement annotations.
But this.
Trask Stalnaker 00:25:04 Not render, not render it in the in the markdown, but just have it as a
code, gen annotation, basically for code generators.
Liudmila Molkova 00:25:15 EE, okay, okay, it makes sense.
The thing that we were motivated by is when
some we wanted to validate this. So if somebody reports a wrong type
for the metric value, then we would flag it. But it sounds like we shouldn't alright.
Braydon Kains 00:25:48 Like a metric can be interpreted as either. You can like, take it as inter as double, so like there wouldn't. Is there even a version of like it's reported incorrectly like, I guess the report incorrectly would be like
the As as double is not right or something. I'm trying to think about like how you'd actually validate that from a like a protocol standpoint.
Liudmila Molkova 00:26:16 So you let's say somebody reports a histogram in seconds, but it reports it says, int ridiculous. But
this one of the mistakes you can make, and then we don't.
Braydon Kains 00:26:31 In it seconds sorry, and then never mind, doesn't matter.
Liudmila Molkova 00:26:37 Oh, the granularity! It's the granularity problem, right?
And you would check that. It's reported or or cpus is an exalt example. Right?
Somebody does not report the fractional part of CPU.
That's that's a problem. We would rather flag it.
But anyway, it sounds like we don't have a consensus that this should be in and that shape.
and we probably want it to be less.
not not the requirement actually right. It's not the violation, we should not flag this violation, we should not.
and force the type.
Josh Suereth 00:27:31 Yeah, I think, based on comments in Weaver, where I made the same comments about breaking it is, it should only be a warning if like, the Int. Doesn't match the int in the policy that weaver provides for that reason.
Cause. I again, I, if we want to start making these changes.
we. We need to kind of update more pieces of the spec to denote that I'm going to find the links to send everybody for where we call out that value can change
yeah.
Anyway.
Liudmila Molkova 00:28:05 Okay, let's let's bring it back to the viewer discussion. The other point I wanted to make is.
that it sounds like for cpus. It's better to have a blanket statement that cpus are double
wherever we measure cpus, it's double, but it's a hint.
So it's not a it's not a requirement.
Braydon Kains 00:28:29 Yeah, when I was reviewing this, the system changes. I I sort of like assumed that like it should
report an int.
If like, I know it will only be int, but otherwise be double like there's there was a few weird ones where on Linux it's only ever going to be like a whole number, but because the way we do it on windows is different. Just call it a double, and then like, call it a day. It's like whatever like, you could kind of just apply that logic to every single thing
if if you really wanted to. So like
that kind of kind of shrugs.
I'm okay with all the CPU counts being fractional, even though in in our namespace they'll never be. There will never be fractional cpus, as far as I know
still doesn't really change anything to make it a double for us.
Trask Stalnaker 00:29:31 And it kind of makes sense to me as a it's a hint to instrumenters, but
depending on the Api that you're instrumenting.
if you are. If your Api is giving you doubles or
int, then it makes sense to just pass that type on.
Braydon Kains 00:29:53 Yeah, to to my knowledge, every CPU count metric like the Apis that I'm familiar with for getting all of these on both platforms are are.
our integer like whole number
but on like container orchestration platforms you'll you'll get Miller cores and stuff. And it sounds like Jbm. Is gonna start doing that, too.
Trask Stalnaker 00:30:13 Oh, I don't know if Jvm. Will or not. I'm just making that up.
Braydon Kains 00:30:17 Okay. I see.
Trask Stalnaker 00:30:18 They're doing some container aware stuff already.
Braydon Kains 00:30:26 I think, actually go like, just put something out about being container aware in that way, too. So it wouldn't surprise me to see other languages start to do that.
Trask Stalnaker 00:30:42 All right.
So we moved these to
out of.
So then we can't. Is this one still blocked on this until kind of it cycles back through weaver.
Liudmila Molkova 00:31:03 Yeah.
Trask Stalnaker 00:31:04 Okay, I want to let me multi select and.
Josh Suereth 00:31:12 I. I copied the specification
wording and the link to where it is in the in the discussion.
So you can see.
Braydon Kains 00:31:25 White text on white background.
Josh Suereth 00:31:27 No, no, it it's it. Look in the meeting notes, I mean.
and paste it in zoom. It kept all of the
all of my background colors, and I couldn't figure out how to turn that off. So I just put it in the Google Doc.
Braydon Kains 00:31:43 By the way, Josh, I might have a mic cable loose, or something.
Josh Suereth 00:31:47 Oh, am I Fuzzy? Okay, let me take a look.
Braydon Kains 00:31:49 Back, now.
Trask Stalnaker 00:31:54 Alright! I'll let.
Josh Suereth 00:31:56 Is this better?
Trask Stalnaker 00:31:58 Yeah.
Braydon Kains 00:31:58 Yeah, seems fixed.
Trask Stalnaker 00:32:02 Let's move on.
Announcement.
Yes.
Liudmila Molkova 00:32:09 Yeah, we've chatted about it a bit during the triage. So I hope to get some of the 1st pass of the review automated.
There is a file that contains the very short versions of our policies.
And
I'd like to try and see how it goes. As we discussed. Somebody who has access to a pilot will need to request it at least initially.
and once we see that it produces something reasonable. We can enable auto review, at least, I hope we can.
So let's see how it goes. Definitely. There is a room for improvement. I don't expect it to be perfect.
considered an experiment.
Trask Stalnaker 00:32:59 And Josh, you missed earlier, but I mentioned that. We do have a ticket open with the Cncf. Trying to their
is, possibly a good likelihood of a path forward for us, getting co-pilot licenses for all the Maintainers.
Josh Suereth 00:33:23 That that sounds awesome. I can't wait to try it.
One of my coworkers made a blog about using it on his project, and I'll share that with everybody. It was really well written and very cool. What you can do now.
Trask Stalnaker 00:33:39 Up, down counter, ning.
Liudmila Molkova 00:33:48 It's been back and forth on this. Is Christis here?
But I think we are most on the same page now.
So we went back and forth with up-down counter, naming what it says. Now use count instead of pluralization, for up, down counters.
and it's raised so many questions and concerns.
The interesting part of the story that we've been actively
preventing people from using pluralization on up-down counters.
So we are now in the state where there are a lot of metrics that
follow some version of this guidance, and few metrics that violated most of them are Kubernetes related.
and more. And now stable.
So I think we
came back to the very short version of this guidance that that we can actually apply. And it's it's a pure taste. I I feel there is no technical reason behind it. It's just the consistency and taste
which is, do not floralize up, down, counter names.
Braydon Kains 00:35:07 I think there is one technical reason which is the the thing we discussed last week, which the with the forced namespace
thing, like kind of a namespace that's also a metric.
I think that would be the main like if if you need to preserve the namespace and don't pluralize it and make a new namespace, or whatever. But
yeah.
Trask Stalnaker 00:35:33 It also it it kind of does. I like it from the namespacing perspective, also that it
creates a namespace for other like. It's a noun, and for other attributes. Underneath this namespace as applicable.
Braydon Kains 00:35:54 Now, are we? We're we're keeping this as being only for up-down counters and not for counters
like counters can be plural. But up down can't.
Trask Stalnaker 00:36:09 Let's get this in for counters today. I forget.
Braydon Kains 00:36:14 I I've interpreted this guidance for all this time as being like, oh, counters are fine to pluralize, and I didn't even think about it until now.
Liudmila Molkova 00:36:23 I made it in a feature. in.net metrics, runtime metrics will pluralize counters and don't pluralize up down counters.
Trask Stalnaker 00:36:35 I mean, I don't think we.
Yeah.
For some reason I thought the up down counters was the trickier one.
But yeah, if you find some examples. Maybe Braden can.
Braydon Kains 00:36:58 Let me think I'll I'll put. I'll post them if I can remember.
Trask Stalnaker 00:37:07 Alright I approved this.
It's nice and concise. Thanks for working through that
generic workflows. Oh, let's see. Hold on! I skipped something.
Definition of server. Address differs.
Liudmila Molkova 00:37:34 Yeah, this is something we should also probably consider for their release. It's a bug
and I I didn't read through it.
Trask Stalnaker 00:37:59 Okay. But this is non stable.
Liudmila Molkova 00:38:03 Right.
Oh, it's it's it's not yeah.
I I guess you can. You can assign it to me. I'll see. If there is anything trivial that can be done. It seems it's just the
the overriding or not overriding something in ref.
Trask Stalnaker 00:38:33 Oh, okay, okay.
Documentation focus. Prs, alright cool. We will take.
I'll take a look at those before the release.
Josh, you're up. Do you want to share.
Josh Suereth 00:38:57 I have to like open everything. Sure.
Right? So entity registry.
Come on.
I'll just show this. So this one now has enough approvals to merge but I just wanted to check and make sure there aren't any last minute concerns what this one does is it creates a
automatically generated entity registry.
And the goal is we're going to start moving things out of the Resource Directory into the entity registry over time. There's an open Pr about this. So, for example.
when in the in the current resource
Directory, when you generate resources, there's a link or sorry when you generate metrics. I should say there'll be an actual link instead of right. Now, when you have an association with an entity of like what resource attributes you expect. It just tells you, and you have to go look it up yourself. Now. There's a physical link. If you click on the link, it will actually go to that.
Trask Stalnaker 00:40:04 That registry, and if I click on it you'll see 404 not found, apparently. Oh, because you gotta open the
file.
Josh Suereth 00:40:11 Have to actually open the file to make it work. Okay, I'll show you that in a second. The registry itself looks like this. It's
every namespace where namespace is based on the names of the entities. So process there's only one
will have the entity listed, and it will tell you what the thing is, and information about the group, and then the set of attributes in it. It also includes information about how to stabilize these things. If you are not up to date with what entities is doing. If we look at service, for example.
service, you can see we have both service
with identifying descriptive attributes. And I think telemetry SDK is the other one that has entities in it.
anyway. So that's that's what the registry is. If you want to see a complicated example, I guess Kate's is the best one. We'll go to that one. We'll review the rich diff.
Kate's has a set of like cluster and container and cron job, and all that underneath it. If you have questions, let me know.
I'll add this as the last bit. Where's the read me that read me like the attribute registry. There's an entity registry
that tells you about all of the different entities that exists, and what you could find on resource attributes to find an open telemetry deprecated works. I didn't. I don't remember updating that that's cool. Anyway, I will update this. If you have any concerns, let me know. The other reason I'm advertising. This is the way this looks and is visualized is I did it, which means it can easily be improved.
So please, if you have any like hate for what it looks like and want to make it better, it is automatically generated. So feel free to update the templates and make it look good.
Right now. My goal is just to make sure we have cross links. You can find everything easily, and there's an index for everything
cool.
That's that one.
Any any thoughts or concerns.
Liudmila Molkova 00:42:24 This looks great.
Josh Suereth 00:42:26 Okay.
Oh.
Trask Stalnaker 00:42:28 Merge it before the release.
Josh Suereth 00:42:32 Or do you care?
I kind of don't want to. Actually, I would like the release to come out and then merge it, because there might be work to update open telemetry, I/O, and so I'd rather.
Trask Stalnaker 00:42:43 Yes.
Josh Suereth 00:42:44 Us cut the release. Then then have, like a month or so to get this out.
Trask Stalnaker 00:42:51 Sounds good.
Josh Suereth 00:42:52 Alright. So I had another one, which is, and I think we just need the notes for this.
I'll add that, by the way
merge after release about, we added the non-normative, how to write conventions
for the entity modeling guide, and what I'm wondering is right. Now, if you look under our general semantic conventions. Sorry under the General Directory. We have how to define semantic conventions in general, for which I would like to add or change defining resources to link to that guide. But my question is.
are we happy with where this is now? I always forget that it's under general like guidance for how to write semantic convention itself.
And so my suggestion is that, and I don't care where. But we put these docs in a place and have them well linked from everywhere, so everyone can find all of them all at the same time. My vote is in non-normative how to write semantic conventions, and I'm happy to like move documents and leave links to them from where they are today.
if people are amenable.
But I wanted to get more how to write semantic convention guides going that T-shaped Api Pr. I had from like 3 months ago. I was finally going to resolve it and move it somewhere, but I wanted to make sure we all agree where it should go.
Go ahead, Brandon.
Okay.
Braydon Kains 00:44:22 It. I don't remember if this is today. But is this how to how to define guide linked from contributing.
Liudmila Molkova 00:44:30 Yes.
Josh Suereth 00:44:30 It is. Yes.
Braydon Kains 00:44:32 Because that's I, the
for, like anecdotal, I have been guiding people to got to contributing mainly when I'm telling people where to go. So as long as stuff is well linked from there, I'm I'm fine, because that's a good like Funnel Point.
Josh Suereth 00:44:47 Yeah, let me be more concrete. So I think when you do how to contribute right, we talk about how to contribute where things belong, and there is a how to define. You say man conventions for guidance.
What I want to do is have under how to contribute, have a link that says there is a series of guides
in this directory.
and then, in addition to just read the initial Guide, because the initial guide is the most important. But I just wanna here's a directory that has additional guides for you to read through. If you're new, that's all. So that that would also get added to the readme
or to the contributing.
Braydon Kains 00:45:29 Should they be like ordered in some way like? Should there be like a 1 to 10 set of documents that you should read? If you want to know how to do this kind of thing.
Josh Suereth 00:45:38 I yes. Was I going to do that? My next set of Prs. Not yet. But if somebody wants to make an order and define that. I think that would be an awesome task to do. And yes, I think it needs to happen. Oh, yeah, there we go.
The culprit.
Yeah, I think that'd be. That'd be wonderful.
I.
Liudmila Molkova 00:45:59 What's up?
Go ahead!
Josh Suereth 00:46:02 I was, gonna say at a minimum, the how to contribute one that's linked here.
that one should be the 1st one.
But there might be some other like contextual things that we decide to put in like concepts. That kind of thing. Yeah, go ahead, Lamila.
Liudmila Molkova 00:46:16 Yeah, I. I also find it difficult that we mix a bunch of different things in the general docs
that are like attributes, specific attributes. And then this Meta guidance. So I'm I would be excited about having a special place for it. I don't think it's non-normative, though we use normative language there every once in a while.
I don't think it's worth separating. So, for example, if you look into the how to define new conventions, the normative guidance. You must use Yaml right, and everything else is non-normative.
Should we split it? Maybe.
Josh Suereth 00:46:58 Yeah, it's different. It's it's weird, though. This is normative language for people writing conventions versus normative language for people using the conventions.
Liudmila Molkova 00:47:08 Bye, bye, right.
Josh Suereth 00:47:10 Yeah, maybe we just make a directory called how to Submit. Maybe we move this out of non-normative
and we move it into a Directory called How to write conventions right under sounds good.
Braydon Kains 00:47:23 Call it tutorial.
It's a bad.
Josh Suereth 00:47:27 It's tutorial that you're putting too much expectations on on what I wrote for the Entity Guide.
I think this would be a tutorial, but the stuff that I wrote I don't know. Yeah, anyway, yeah, tutorial could work, too. I'll put a Pr together that does some of that shaping, and then we can argue about names in the Pr, because I
yeah, whatever folks are comfortable with, I'm good with. I don't really care too much about the names.
Christophe Kamphaus 00:47:53 Maybe getting started.
Josh Suereth 00:47:56 Getting started. Yeah.
Yeah. Getting started, or how to write conventions or guides, even
Trask Stalnaker 00:48:08 Getting started could have 2 different. I like it like getting started with using semantic conventions versus getting started with
authoring. So.
Braydon Kains 00:48:18 At the conventions.
Josh Suereth 00:48:20 Yeah.
Braydon Kains 00:48:26 Cool.
Josh Suereth 00:48:28 I think that's it for my topics. I don't know if you wanted to go through these other bugs documentation focused Prs
Trask, or if that was already covered.
Oh, no!
And it's a generic workflows, is the next one
who added this one.
James Thompson 00:48:49 Hey!
Josh Suereth 00:48:54 Would you like to talk about it?
James Thompson 00:48:55 So what I've tried to do is there's a range of different discussions, requests for describing workflows. Right, be it a Cicd workflow, a transaction processing system, etc. There's a whole heap of different workflows occurring, and there's lots lots of thoughts about having individual definitions.
Alright.
So what I've done is started trying to pose a standardized workflow namespace that can be used across the board to describe these different workflows
right in a generic way, so that
we can easily add the transaction processing system without having to define a whole new scenario, etc.
If you have a look at the files changed
alright. So I've literally taken the Cicd stuff. I've looked at the other spaces to see and try and consolidate down to a common definition of workflows.
Liudmila Molkova 00:50:08 I think I shared it on some previous discussion. I'll try to find it. I think we
this is the over generalization.
If certain area doesn't have something like workflow defined.
It's very difficult to come up with some general thing that would mean something very different, depending on where it's used. And
most importantly, I think we need some real world examples of where and how it will be useful.
James Thompson 00:50:42 Yep, yeah. So like, I've tried to focus on the Kubernetes scenarios.
right? So like a Quan job versus a job. Right?
That's a task. A job is a and that's where describing the implementations comes in.
Josh Suereth 00:51:08 So, I think. Have have you run this by like the Kubernetes folks and the Cicd folks ahead of time?
James Thompson 00:51:14 I'll suggest you to join this meeting to discuss it.
Josh Suereth 00:51:17 Yeah, yeah, okay.
James Thompson 00:51:18 Rather than this one. Yes.
Josh Suereth 00:51:20 Yeah, I want to make sure that we get get their opinion on this because you, you have concrete things. There's there's a few few
high level things to like that Ludmilla is going after is basically like when we add something, we want to make sure that we have instrumentation for it.
James Thompson 00:51:37 Sure.
Josh Suereth 00:51:38 So we want to make sure that this can have instrumentation, maybe has a prototype or demo for it. And so if you're unifying between Cicd and Kate's, we should make sure that we actually have prototypes that do that. The second thing is, we want to make sure that those groups agree.
And I think to Laudmila's point, one thing to address would be the concerns about like, have you lost
context by making this generic to the point where it's actually hard harder to use, like, I think that's kind of what Lidmill is getting at is, does this make it easier to use, or harder to use for workflows are we able to appropriately monitor different workflows.
using the same set of tools? Right? But are we able to go deep enough to actually solve their problems when we run into stuff that's 1 of the bounces every sem Conf group goes through of like how deep to abstract.
I had a a
A Pr for talking about this. We call it a T-shaped Api, where you want a generic thing that covers like 80% of use cases, and then something that can go deep and really understand the details. For if I you know, I'm going to give a non workflow example because I need to like. Look into this a bit more. But let's say for databases. Right? I might generically know this is my slowest query. That's that's part of that 80% that that abstraction we want of like tell me what my slowest queries are.
But the deep use case might be. There's a particular type of index on this database that leads to a cleanup cycle. That's problematic that I need to fix right. And that's the that's the the in-depth T part, or or the the line in the T right of a T-shaped Api, so like
to some extent with this. Pr.
I'll just I'll be. I'll be a little Blunt is. I don't think there's enough in the description.
Because I saw this a little earlier, I believe. Let me come back. My computer decided to stop. Hold on, I don't think there's enough in this to actually motivate the the scope of the change you're making, so I'd love to have more description. Why, like, what use cases you're targeting where you think and why you think joining makes sense, and where you think someone would go to a deeper. Api. I think like that would be awesome to have more of that to kind of justify this right.
James Thompson 00:53:59 Yeah. Yeah. And like, one of the things that came up was, how can can I describe the scenarios? Right?
All right. And like, I focus on the Kubernetes scenarios.
Alright, alright! And it's like, essentially.
I've tried to. If you take the scenario of a cron job versus a job
right? Right. You can now have a clear properties that indicates the type of type of type of task. It is, is it a cron job? Is it a job, etcetera. So you have those different breakdowns. So you can see all my cron jobs are, what's taking my time, etc.
Yeah.
But yeah, like, that's why, it's still especially still in draft. I'm just like I
I'm just trying to balance. How much time do I spend spending writing all the scenarios, all that as well.
Josh Suereth 00:54:48 Yeah, I think the instead of going into the details directly, I would start with the high level rationale and like the your target set of like things you want to solve, like, I want the ability to write a dashboard that works on workflows, and it should work the same on Kubernetes, tasks on fast tasks and on Cicd tasks right? And and here's what I want that dashboard to look like
high level view of that. You don't have to go into super details, just sketch it out. So we understand the motivation behind the Pr. Especially given the scope that you have the amount of things you're touching, right? So like more justification on, why, I think would be super valuable. And yeah, it's this is fine as a draft. And to get feedback. That's what I'm trying to give you is like. Here are the concerns we see. Here's the things to address, so motivation for. Why this is useful. What the abstraction gives us, and why that's valuable. And then
I think Christoph is here. I saw him. I think maybe a few others are on holiday, but just getting feedback from like the Cicd folks from the Kubernetes folks. I don't know if I see anyone from the Kubernetes say off the top of my head here, but getting feedback from them would also be valuable. So, unfortunately, today might not be the best to get all of us, because there's a lot of people are out on holiday, but I don't know. Christoph. Do you have any thoughts here from a CID?
Christophe Kamphaus 00:56:13 I did take a look at the Pr.
One thought I had was what to do about the entities that we already defined, for, Cicd
would say, become workflow entities, or would they stay Cicd entities?
I don't have the answer to that question, but it's something I think we would need to think about here.
Then, also, if it's a generic workflow, Sam can't.
What other workflows would it cover.
for example, when we thought about generalizing that as part of the Ci CD. Sig, before
we thought, there's also other workflow engines like for business workflows.
Would it cover those as well.
James Thompson 00:57:02 That would be my hope. Yes, right? So. And that's why I have like on the basic workflow. It's what platforms running it. Right? So you could have your Ci CD platform. You could have what? Your serverless workflow platform running it so you could have those different workflows.
Christophe Kamphaus 00:57:28 yeah, what else? Yeah, about the discoverability aspect?
I was thinking, how could we make it discoverable so if someone new to samconf, would come and search the docs
to write some semantic, to apply semantic conventions. For Cicd, for example.
would say, then finds the workflows, Thumbcock.
James Thompson 00:57:52 Yeah, so I, that's something I've also been thinking about like.
And I think that's something that ideally we could solve by documentation. Because if I could have my wish for documentation is like, if we take the Cicd scenario.
we go to the the website, we in the Sidebar, we go semantic conventions. We click Cicd right? And then you can see
example implementations of
a metric which is relevant for Ci. CD, it might be defined as a workflow. But you'd see this for a Cicd workflow. This type is set. This is set right. And this is how you know it's a Cicd workflow. For example.
Christophe Kamphaus 00:58:35 Okay, yeah, that's that sounds good.
James Thompson 00:58:38 Alright. And then just like to the Kubernetes scenario, you could have a look at saying, Okay, this is Kubernetes workflow. And the task type is a cron job. For example.
Christophe Kamphaus 00:58:46 -
James Thompson 00:58:47 And that's where the documentation comes in
alright. And I've also put a couple of waver
questions requests in there to be able to describe implementations better as well.
which will also help on this topic as well.
Christophe Kamphaus 00:59:03 Yep.
Then another point is, would there be
at any point in time some overlap between both, for example, a Kubernetes workflow, which is also in Cicd workflow.
James Thompson 00:59:19 So it come down to the way I see it.
You you the workflow, would be managed and orchestrated by a platform. Is it your Cicd platform. That's running it
all right, or is it Kubernetes? Right? You can run a task which triggers another workflow. But then that's the Kubernetes
right? So I think that nested workloads perhaps needs more work. It's something I haven't considered, but
it's something that could be done. Just need to look at it and work it out.
Christophe Kamphaus 00:59:54 I'm thinking here mainly about Tecton, because that implements their Ci CD pipelines on kubernetes.
James Thompson 01:00:03 Yep, right. But is Kubernetes a pop platform that's running it? Or is that just providing?
All right? So I'd say the Cicd. So in that case, Kubernetes
is what's hosting the workers? Would that be correct?
Christophe Kamphaus 01:00:19 It's basically any a pot like any other, and tacked on takes care of
creating the pots and getting the results.
James Thompson 01:00:28 Yeah.
yeah, right? Right, if you can just put the name of that, and I'll have a look. And I'll have a think about how it fits in. Yeah.
Josh Suereth 01:00:35 So. So I updated the the notes with that I might have spelled tact and right wrong. But
one thing I'll say from that. And this is true, for all semantic conventions is, remember that there will be layers, and that we do need to address them, because, as open to lunch. We have to be naive. If we instrument kubernetes for workflow loads and someone else is using kubernetes as a workload thing, it means we will get 2 metrics that look very similar for the same thing. And this is a problem we have today with spans right? Like we might have Http spans and like database spans where the database is communicating over Http.
And and users might be confused if both of those show up and not happy. And so that's the thing we need to sort out these. And I, that's our layers problem.
I give everything a name that I don't know if anyone else shares the name, but that's how I think about it. Anyway, things to solve. I do need to drop. Thank you for presenting this and and hope to continue the discussion.
Christophe Kamphaus 01:01:31 Thank you very much as well.
Trask Stalnaker 01:01:33 I
James Thompson 01:01:34 Bye.
Christophe Kamphaus 01:01:37 You.
