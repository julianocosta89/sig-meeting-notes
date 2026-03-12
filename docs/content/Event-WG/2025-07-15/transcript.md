SIG: Event WG
Date: 2025-07-15
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:08 Robert T.
**Robert Pająk** 00:11 No trust.
I still have an interesting topic.
**Trask Stalnaker** 00:31 Yes, yes, I was looking forward to discussing this with you.
So yeah, so I'm very interested in this trace based log record sampling.
So I wanted to start kind of working on that and seeing where that intersects with your work also.
And what I wanted to do was kind of talk through how we see that being configured.
So let's say, for example, with the log record processor.
cause, that's currently right in your it would be a log record processor that does this.
And so batch log record processor.
How do we do that? How do we add, can we even add.
**Robert Pająk** 02:13 Like speed processors.
Yes, so you can. You can add not. This is log log records right here.
**Trask Stalnaker** 02:21 Yeah.
**Robert Pająk** 02:21 So you can add custom processors by name, you can register it using the configuration. SDK, there is something called register, a component provider. And so here, like my proposal. And I want to work on this. Maybe next week. I'm not sure if I'll able to prototype it and test it out from next week is just to have a custom processor which basically is wrapping another one. So there will be something like, you know, trace based, you know, double dots. I don't remember the name in English and then inside it will have processor and the name of the batch, for example, batch processor, and you will be basically to be just, you know, Indented once yeah exactly processors and then you'll have then you have this dash or dash, for instance.
my processor, or it will be trace trace based. For instance, yeah, double dots. I, how is school design.
**Trask Stalnaker** 03:32 Full end.
**Robert Pająk** 03:33 Colon.
Okay, yeah. Colon, then new line.
some configuration. One of these will be processor, probably of wrapping or whatever like a field right processor column, and then you'll have batch, and inside you'll have you know, the Batch processor.
**Trask Stalnaker** 03:53 Oh, yes, yes, you're like for I understand. That's.
**Robert Pająk** 04:00 Yes.
**Trask Stalnaker** 04:02 Batch, and then everything.
**Robert Pająk** 04:08 Exactly.
**Liudmila Molkova** 04:21 Is it something that declarative config supports already.
**Robert Pająk** 04:25 It's short.
In my opinion, I want to test it out. I want to. First.st Simply, this is something which is.
in my opinion, compliant with specification that it should work.
and I just want to kind of make it work in the go configuration. SDK, it's something better to go, at least, but I think it's implemented in Java already.
**Trask Stalnaker** 04:48 I will try it out. But yes, I understand what you're saying, and I think.
**Robert Pająk** 04:53 For is.
I think, that it may be also. Maybe it will be easier if it will be not only one processor, but multiple processors.
But it's kind of specific how you want to implement this trace based. You know, processor.
if you want to accept a list of processors that you can put a simple batch, etcetera, or, if you want to have it one, we could also.
**Trask Stalnaker** 05:18 Some ideas.
**Robert Pająk** 05:19 To have something like a composite processor which basically can use as one. But in multiple places. So yeah.
this is this is not. I don't think it's a critical thing to decide right now.
**Liudmila Molkova** 05:36 Would we use the similar syntax for severity based? So there will be the top level severity, based process, or whatever level, but probably top level.
**Robert Pająk** 05:49 There was already. This was already requested by the collector guys I created as an issue.
or it, I think.
No, I have not written sure. Because, yeah.
**Trask Stalnaker** 06:06 If you wanted to combine them, you would just can continue the nested party.
**Robert Pająk** 06:15 If yep, exactly.
**Liudmila Molkova** 06:25 That it would essentially match the code that you would write otherwise.
**Trask Stalnaker** 06:35 Right.
And so what we're doing here sort of is formalizing this chaining concept and encouraging training of things for clarity which I like. I like. I like the chaining.
**Robert Pająk** 07:00 Thing is that this is something which collector wants and play.
And basically, the collector just wants to dock put our configuration. They're already doing it.
**Liudmila Molkova** 07:13 Like you would configure a collector in the same way as you would configure SDK.
**Trask Stalnaker** 07:27 All right.
I'm gonna try this out in Java this week.
Unwell.
Keep you post. I'll I'll send you a draft Pr. Or something.
or maybe it already. Well, yes, yes, cause what I think my goal would be if this works out from a configuration perspective is to like, bless.
you know these names as standard log record processors that are included in the Sdks.
Initially, it can just be contrib. Maybe I'll send a contrib. Pr.
**Robert Pająk** 08:22 I think initially, you can. Even they can be like experimental. And you can even refer to the supplemental guidelines there. I think there are. I think both of them are defined there. But maybe I'm wrong.
There is some prototypes for both of them.
**Trask Stalnaker** 08:37 Hmm spec.
**Robert Pająk** 08:39 Yeah, but they are just supplemental.
**Trask Stalnaker** 08:41 Implement, some.
**Robert Pająk** 08:41 Supplemental Guidelines.
**Liudmila Molkova** 08:43 That's right.
**Robert Pająk** 08:44 Need to. Yes, I think we could pro work towards promoting them. So they are kind of built in.
But at least we have some pure, pure work.
**Trask Stalnaker** 08:53 Yeah, maybe I'll do that. Maybe I'll I'll just do it in the SDK. Java SDK repo itself, not trying to merge it, but just as a prototype, and then we can make a spec pr, and point to that, and follow the process cool.
Alright. That makes me happy.
**Liudmila Molkova** 09:20 Yay!
**Trask Stalnaker** 09:21 Anything else to chat about on that topic, or we can move on to the next big topic.
Lydmila, you want to. You want the honors of. I think you're the only one of us who has official permission to merge in this repo.
**Liudmila Molkova** 09:48 Oh, my gosh! I went through several of this moments, merging some very long standing Prs, but this probably is the top one.
**Trask Stalnaker** 09:59 She was pretty, epic.
**Liudmila Molkova** 10:03 Yeah.
**Trask Stalnaker** 10:04 Let's see, I will go ahead and resolve outstanding comments.
Alright merch! When ready.
**Liudmila Molkova** 10:14 Yay, merch when ready. Yay.
**Trask Stalnaker** 10:25 Alright! Come on, go, merge queue! Don't fail us now.
**Liudmila Molkova** 10:32 Okay.
So I think, where is this in?
I thought that we have 2 ways to go ahead. The 1st one is we can keep polishing stuff around exceptions. We have another epic attempt that is not controversial, but full of tiny little cuts and tiny little discussions, and it might take a few months before we.
I don't know. Remove the scope from it or get it in in some shape, anyway.
The other pass we can take. We can start implementing the taps that that's been already merged.
**Trask Stalnaker** 11:22 This one any other? Are there any others that need still need to be merged? I mean, implemented.
**Liudmila Molkova** 11:32 Exceptions, errors and exceptions.
**Trask Stalnaker** 11:37 There's an exception. Oh, the one that we haven't merged yet!
**Liudmila Molkova** 11:41 We? Yeah, and it will. It's it's got closed because it was stale. But yeah, I'll reopen it.
**Robert Pająk** 11:47 I think we can work concurrently on both topics.
Regarding this complex attributes I thought about creating issues.
or of to just to capture all of the parts of the specification that we will want to change, because I imagine I do not want to have a 1 big Pr similar to the, for example, this measurement processor, which will be taking for ages.
I'm just thinking about making a lot of sub issues for each part.
So we will not just scope creep Dprs. And if people ask, even, you know, for other information, for example, what about that? We just be prepared for that? And just say, here's the sub issue for it. Here's the sub issue for it. Just to, because I'm concerned about the scope about need picking, you know, even vocabulary or the stuff. And I think we'll move faster if we just scope out for little sections, even even, you know. Let's have one Pr to update this section, other Pr for this section, etcetera.
**Liudmila Molkova** 12:55 Yeah, wonder, maybe we can have a draft Pr like this just for us that does everything. And then it can.
**Robert Pająk** 13:02 We are doing this, we are doing similar things, you know. They'll go very often. We're meeting a very long Pr, we're making a draft Pr, which is our expect, how we think it will look like like for your art. And then we are often, and we can use that to create the sub issues. Even so, yeah, make sense.
**Liudmila Molkova** 13:24 And this would include the span event, deprecation, and.
**Robert Pająk** 13:31 Complex.
**Liudmila Molkova** 13:31 Attributes everything about events and blogs.
**Robert Pająk** 13:38 Okay.
**Trask Stalnaker** 13:39 I think that's I mean I would treat that as a separate topic from complex attribute.
**Liudmila Molkova** 13:50 I'm thinking more of a what does the Sig needs to do? We are actually pretty close in terms of autops, right? And the vision.
**Trask Stalnaker** 14:04 Yeah.
so I I agree, these are, we want to.
**Robert Pająk** 14:12 No, I I think nothing books us for having this in the draft, and creates creating some issues. If it's get, you know we it's not.
We do not need to necessarily, you know, solve all of the sub issues.
There will there go one by one, and we can always adapt right if there will be needed. But I think even in this draft we can also try to kind of have some thoughts how we want to deprecate the span events, and and we want to work it into specification. Is it what you have in mind.
**Liudmila Molkova** 14:47 Yeah, I'm thinking that we have the 1st start up the event vision that outlines what we are going to do before stabilization.
And a lot of this autops, or either they contribute to that vision.
And if we can start implementing the vision, a bunch of things about, let's say, complex attributes.
**Robert Pająk** 15:17 Are not in scope of the Sig to actually go and.
**Liudmila Molkova** 15:25 Fully implement, right?
So it needs to be implemented. I'm definitely on hook for it.
But it's not part of the Sig deliverables.
Holy.
And I would
**Trask Stalnaker** 15:43 When we say implement, I guess maybe I'm are we talking implement the spec, or I mean sorry.
**Liudmila Molkova** 15:50 Bye.
**Trask Stalnaker** 15:51 Implement it in a language, or write the spec.
Yeah, the real spec for it.
**Liudmila Molkova** 15:58 Right there we go spec first.st
**Trask Stalnaker** 16:00 Okay, got it? Yes, yes, that's what I meant to, just making sure we were using it the same.
**Liudmila Molkova** 16:06 Yeah, and just a way for us to stay focused. I would consider, this group to try implementing the event vision or tap.
And once we do it, we actually completed the the scope of the seek plus. There will be time for stabilization.
**Trask Stalnaker** 16:34 Yeah.
Let's go.
**Liudmila Molkova** 16:38 Let's go. Okay.
I might have time next week to to make a stab on the vision, and the spec draft that we will use for the project planning essentially.
If anybody wants to try earlier, go for it. But yeah, I I will. I can try next week.
**Trask Stalnaker** 17:13 Yeah, that sounds great. And I, I like that idea.
getting the ball rolling on that part.
And then if we find that we have bandwidth. We can start talking about that.
**Robert Pająk** 17:33 We might figure out this implement complex attributes. It won't be an autop, right? We want just a draft. Pr, or am I mistaken?
Yeah, draft people.
**Liudmila Molkova** 17:44 I mean, draft Pr is the 1st step of in the implementation. Right? This is what.
**Robert Pająk** 17:48 Yes.
**Liudmila Molkova** 17:48 Find out what we actually need to implement.
**Robert Pająk** 17:52 Draft. Yeah, implemented? Yeah.
**Trask Stalnaker** 17:55 Yeah, yeah, yeah.
**Robert Pająk** 17:58 Yes. Yeah.
**Trask Stalnaker** 18:00 Yeah, more clear. There.
**Robert Pająk** 18:04 For others that won't be watching us.
**Trask Stalnaker** 18:08 Yes, our big audience.
**Liudmila Molkova** 18:15 Hi, mom.
we might find out that we need to.
Proceed with errors and exceptions at that.
At some point.
**Trask Stalnaker** 18:31 Yeah, it is kind of it's got some overlap for sure. With this.
**Liudmila Molkova** 18:41 Yeah.
So let's let me what I can do this week. I can.
We'll look at it and maybe cut everything that's not.
That's not a dependency.
**Trask Stalnaker** 18:59 Hey, look! I approved it, and Robert blocked it.
**Robert Pająk** 19:05 I'm not sure what. Why, I blocked.
**Trask Stalnaker** 19:12 Yeah, yeah.
**Robert Pająk** 19:13 That's me!
**Trask Stalnaker** 19:14 It's a different Robert.
That's.
**Robert Pająk** 19:17 No, I think I blocked it, but I think I blocked it because I was not able to dismiss my approval, or something like that.
**Trask Stalnaker** 19:26 I'm just do you think, yeah, yeah. Why don't? If you.
if you have the time to resurrect it? I can go back through like after you resurrect it, I can go back through and see if I still I can issue a reapproval.
We got a lot of comments. A lot of people were okay.
**Robert Pająk** 20:02 If I remember correctly, some of the things in the Otep were very not controversial, and I think there could be even addressed before, and I think that even we discussed some of it like last month in auto. Go seek. And we were even thinking about. I was thinking about even making a cementing convention Prs and specification Prs. But they just had no time to to work on this, but it is one of my probably top. On the 1st place on my to-do list.
**Liudmila Molkova** 20:34 Nice. So I think that if I remember correctly, the there are 2 controversial parts. The 1st part is it's hard to.
We don't do enough explanation on for languages that don't have exceptions like go and rust.
**Robert Pająk** 21:00 Yeah, we can work on that.
**Liudmila Molkova** 21:01 Yes.
**Robert Pająk** 21:01 Super in parallel.
Yep.
**Liudmila Molkova** 21:06 Yeah. And the other part is, there are a lot of choices I make there on the severity, and it will take years to agree on. So maybe we can somehow extract the severity, guidance.
**Robert Pająk** 21:26 Yep.
**Liudmila Molkova** 21:30 Okay.
So I think what whatever we depend on is the span events, everything that mentions bad events.
and the moment we remove spend events, we have a question of severity.
We can say it's sunset.
**Trask Stalnaker** 22:24 So this would be not logged exceptions, but caught like exceptions that are stamped onto spans as the exception escapes the scope.
**Liudmila Molkova** 22:39 Right.
And there were a bunch of questions on this.
I need to remember.
**Robert Pająk** 22:53 There. There is also one thing which, in my opinion, will be good to be addressed. I didn't see that in this autop I think there they may be a difference how the instrumentation or SDK should handle an exception which is handled by the end user from an exception which is not handled at all?
Or do you disagree Trask, or in Ludomiwa?
Or it should.
**Trask Stalnaker** 23:24 I still.
**Robert Pająk** 23:25 And.
**Trask Stalnaker** 23:26 I still like the general If an exception escapes a local route.
**Robert Pająk** 23:38 Span.
**Trask Stalnaker** 23:39 Then that is recorded, and that is an error.
But if it escapes a non local route span.
then it's more like a debug level because either the user will handle it and log it.
or it will escape all the way out.
**Liudmila Molkova** 24:12 If we can agree that severity is slightly dynamic.
that would be in in enough. As a 1st step, we maybe can postpone discussions on what does the unescaped severities depending on whatever.
**Trask Stalnaker** 24:41 Yeah, I mean, I.
The important part of this, I think, is going to be controversial.
**Liudmila Molkova** 24:54 Which one.
**Trask Stalnaker** 24:56 Just some of the some of the key things in here about recording exceptions.
I just think it's a trick like we have a lot of prior art in different sdks and different instrumentations are doing things differently.
And so any choice that we make is going to contravene some of the existing instrumentations.
But I think it's very important.
**Robert Pająk** 25:33 For example, in Java, if there is an exception with which it's not handled before a span is finished, do you somehow capture it and log it.
**Trask Stalnaker** 25:48 No only if it escapes the span.
**Robert Pająk** 25:52 Yes, that's exactly so. If it accepts the span, so if it accepts, exchange the end right? So.
**Trask Stalnaker** 25:59 Yeah.
**Robert Pająk** 26:00 It's not captures. Then you're yeah. So this is a behavior which I seen in many sdks. And I think we should specify this kind of behavior that this is something that basically the SDK should do and how it should be handled, because this is a totally different. I see it as a total like this is different thing for the you know, SDK, maintainers, etc. And I think we can.
Yeah, it's a different. It doesn't require user end user, you know, reaction to do anything on it, or instrumentation library or anything.
**Trask Stalnaker** 26:32 Oh, no, no! The the Java SDK doesn't do that on its own.
**Robert Pająk** 26:37 Okay.
**Trask Stalnaker** 26:39 But the Java instrumentation, all the Java instrumentation that we write we do try catch rethrow, try to test.
**Robert Pająk** 26:50 So you have, you have to do it everywhere. Okay.
**Trask Stalnaker** 26:52 Yeah.
**Robert Pająk** 26:53 Okay.
we don't have to do it and go we we just can see that that there was an unlet exception before this span has ended.
Is it possible to do it in in Java? And would you like to have it or not?
**Trask Stalnaker** 27:18 I do. How think it is possible in Java? I don't think it's possible to do that in the SDK.
It doesn't really bother me where it's done.
as long as the guidance. As long as we have guidance for the sort of end result.
Even if it's on instrumenters.
but I I even though I the job instrumentation, does it? I don't. In our distro the Azure Monitor Distro.
We suppress those internal, the exceptions stamped on internal spans just because they're so noisy and costly, and so we only.
**Robert Pająk** 28:09 I see.
**Trask Stalnaker** 28:10 Report the ones that bubble all the way up to the local root span.
And so that's kind of where I'm I like the idea of saying, record those internal spam exceptions as debug level.
But that's that's a big change from the existing Java instrumentation and a lot of other instrumentations out there, so not sure if that will fly or not.
**Liudmila Molkova** 28:51 In a lot of cases.
So okay, so there, I think there are 2 parts. The 1st part is what applies to existing cop and telemetry instrumentations.
and if it used to be recorded as a span event, what do we do now?
This is where the probably we will get the most feedback. Around this part there is the other part which is even more controversial, and maybe I should remove it like, forget about span events. Who cares like. There are tons of existing log records, libraries, right how they should set severity.
And maybe I can extract this piece and keep it for the future, because it's it's it's too vague, too big, and it does not help us solve the immediate needs.
**Trask Stalnaker** 29:58 I didn't follow. So you mean, like, how like a log for Jay, I think they're using.
**Robert Pająk** 30:05 I think it's how the end users should mark severity right to Miwa.
**Liudmila Molkova** 30:10 Users.
Yeah, and users, yes, but also like, let's say, our libraries. Azure is the case. We write tons of logs, for example, connection is dropped. There isn't. The span happens on some very high level somewhere.
Not the same instrumentation.
**Trask Stalnaker** 30:28 Yeah, no, no, yeah, that's a good thought to remove. What's that?
And I forget.
**Liudmila Molkova** 30:39 I'm not sure if there's a section. But I think I'm mixing.
**Trask Stalnaker** 30:44 Yeah. Here.
**Liudmila Molkova** 30:45 Those 2 goals, yeah.
**Trask Stalnaker** 30:47 Okay, yeah, yeah, makes sense.
**Liudmila Molkova** 30:51 So maybe if we can focus on the span events and open telemetry instrumentations, we can make it more the adjustable.
Okay.
so maybe we'll do this for this week I'm I will try to focus on remembering what happened here. There is a similar Pr and semantic conventions with some feedback.
I'll try to reduce the scope of this auto, and I'll try to bring some parts of it to the next spec meeting.
To collect some initial thoughts and feedback.
and from there we will decide how to proceed further.
**Trask Stalnaker** 31:50 Cool. Yeah, I think that it's a good topic to start seeding into the spec meeting. And it feels like we based on today's meeting going short.
that we have some bandwidth there.
Yeah, I'll watch for it or ping me when you make a update, and I'll I'll review it before the spec meeting. Then.
**Liudmila Molkova** 32:19 Wonderful.
**Trask Stalnaker** 32:30 All right. Speaking of meetings going short.
**Robert Pająk** 32:37 Congratulations and thanks a lot or other work.
**Trask Stalnaker** 32:41 Yeah.
**Liudmila Molkova** 32:44 Oh, now time to actually work on this.
**Trask Stalnaker** 32:50 Yeah.
**Robert Pająk** 32:50 But I would say it's half of the success.
**Trask Stalnaker** 32:53 Oh! More.
**Robert Pająk** 32:53 Some agreement. Yeah.
**Trask Stalnaker** 32:54 Much more. Yes, except for the the the limit, the attribute limit thing that's still gonna be.
**Robert Pająk** 33:05 Yes.
**Trask Stalnaker** 33:06 Hard.
**Robert Pająk** 33:07 There will be a lot of opinions how to count this stuff.
**Trask Stalnaker** 33:13 Cool.
**Liudmila Molkova** 33:14 For sure.
**Robert Pająk** 33:16 Okay.
**Trask Stalnaker** 33:17 Thank you.
**Liudmila Molkova** 33:18 Thank you all.
**Trask Stalnaker** 33:19 Bye.
