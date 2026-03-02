SIG: Profiling WG
Date: 2025-07-10
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/fSgJuD5Ekx0e1Q1B9p6kIYuZ9vp6wCTW__rzuLb6QIzGnXNpcXbh6VVPG6F3P1Zp.JHzRaVsR8jvA2bGG
============================================================

## Zoom Recording Transcript

Joel Höner 00:01:28 All right.
Christos Kalkanis 00:01:46 Hello!
Hey! Joe!
Frederic Branczyk 00:02:48 Hello! Hello!
Ivo Anjo 00:02:52 Hey!
Felix Geisendörfer 00:04:18 Hello.
Martin! You might be giving up some background noise from your mic, maybe mute yourself.
martin stadler 00:04:35 Okay. We'll do. Sorry.
Felix Geisendörfer 00:04:37 Endeavors.
Guess we're 5 min in
where we should get started. Any volunteers, or did I volunteer myself by speaking up as usual?
Yeah, I see the knots. Okay, that's how it's gonna be.
Let me get the document up.
martin stadler 00:05:26 Doomed.
Felix Geisendörfer 00:05:31 Okay, yeah.
if you haven't already at yourself, as on the attendee list as usual. Just do that myself right now. And, Martin, I don't know if you tried to mute yourself already. But I somebody's still giving off. I think it's you still giving up background. Thank you. That worked awesome.
alright. So we have a bunch of agenda items. But if you look at the list and you're like, Oh, there's something we should talk about that's not on this list, please add it now. So by the time we get to the main agenda items we have all the things.
I'm going to start looking by scrolling up in the document through the active action items.
The 1st one is review pr open telemetry, proto number 6, 7, 2.
So let's see where that is.
Dictionary table encoding consistency improvements. I guess it has a bunch of comments.
I guess, Jonathan, it's your Pr. If you want.
Jonathan Halliday (IBM) 00:06:41 2 strands of discussion here. The the easy one is the the second one, which is 1st in chronological order, which is just
changing the text of the comment slightly.
Felix Geisendörfer 00:06:51 Okay.
Jonathan Halliday (IBM) 00:06:51 That's fine. I'll I'll okay that and it makes it less verbose.
The more difficult one that I think we need to discuss is about the semantics of the attributes unit field
which is really not working well at the moment. It's I mentioned this in a a thread on slack.
it. It's different to everything else in the the dictionary, and that causes some
cognitive load for users. Admittedly, I don't think there's going to be many users down at the proto level. This is going to be hopefully a handful of libraries and sdks and and everyone else is going to be using
some form of language Api, and based on those.
So there's there's a limited number of people have to worry about this.
but I think beyond that, it actually isn't expressive enough as it stands. And the issue is that
because the the attribute table where we're storing the actual key values is really the
concatenation, the combination of multiple maps. It's possible for the same key to appear in there multiple times.
And that leads to a problem that if the attribute units field has map semantics.
you have to pick which one of those keys
is going to dominate. So if the keys have different types.
or different units. There's no way to express that.
It's sort of last last ride of wins, or whatever, in terms of putting them into the table.
So my! My latest comment on the the pull request tries to express that
a bit more carefully in proposals we could change attribute units. So instead of being a
a name and unit tuple, it's an index and unit tuple.
because then we can say we're talking about
a particular attribute that exists in the attribute table that index
whatever, and you get the name by going into the attribute table, where the name is already stored. Anyhow.
Felix Geisendörfer 00:08:58 Okay, thank you. Does anybody have immediate thoughts on this? Because I I didn't catch up on the
details yet? And I wasn't able to fully follow, I'll admit, but I would certainly take a closer look after the meeting. Does anybody have immediate?
So it's
Alexi Gufford.
Alexey A 00:09:26 One thought is, what kind of different units for the same attribute like, do we have practical
examples? Or this is just something that we genuinely want to support. Because I was curious.
like, if a particular consumer or visualization tool needs to deal
with like needs to visualize the profile them.
It's just like, if you have a unit. If you have an attribute that have different units, then things become
also complex to deal with in terms.
Jonathan Halliday (IBM) 00:10:01 Yes, I agree with that, and I would. I would hope that at least the standard attributes motel are defined in semantic conventions, such that the name will automatically tell you what the unit is
so like. Network traffic bites, you know it's expressed in bytes, right? But if if some lesser
defined thing comes along and just says network traffic. And you know, 1 1 user thinks that's bytes and another thinks it's megabytes. You've got a problem.
and we don't have control over that. Unfortunately, we we can't define a closed universe of well-defined
attribute names with well-defined semantics. If we could, we wouldn't need this field at all, because the the definition would tell you what the unit was.
Alexey A 00:10:43 Yeah, and bytes versus megabytes is probably an easier case, because you like the the implementation can still get them to the same, the same magnitude, and and then it becomes consistent. It's more complex if it's something completely unrelated. I don't.
Jonathan Halliday (IBM) 00:10:59 Oh, my God!
Alexey A 00:10:59 Some like process attribute named process. And it's
process id in one case and process name in another.
Jonathan Halliday (IBM) 00:11:07 Yeah.
Alexey A 00:11:10 But I I haven't.
I'll take a look at the actual
pull record. But this pool, this pull request, is not new, right so. And you commented there I was just
wondering if there was also like a I need to take a look at the code, because I remember there was like discussions and discussion comments.
I didn't see that there was
like a proposed change in in how we're, you know.
Jonathan Halliday (IBM) 00:11:40 Yeah, just just in the last few minutes I put a comment on that.
Alexey A 00:11:43 Okay.
Jonathan Halliday (IBM) 00:11:44 It has it. It's sorry it's it's not in there as a as a proposed edit of the sort where you can click, merge this.
It's it's in there as a comment.
Because, frankly, I haven't thought it through fully. I I came up with this, you know, 10 min ago, while I was prepping for the meeting.
Christos Kalkanis 00:12:02 Jonathan, should this be attribute index or the attribute table? Because here you're saying, attribute units.
Jonathan Halliday (IBM) 00:12:10 I'm saying that in in the dictionary we have attribute table which is realization of key values. So the elements in the attribute table
tuples of name and value.
And then we also have the attributes unit field.
which is of type attribute unit.
So if we put something into the attribute table as a key value. But we also want to store what the unit is.
We additionally put an attribute units element into the attribute units field.
So essentially what I'm what I'm changing there is for an attribute unit. Previously it was a
a name value trouble. But I'm saying the name can be
overloaded. You can have the same name, but different units.
So you need to be able to express which occurrence of the name you're talking about, and the way you do that is, you
refer to it by its position in the serialized attribute unit table.
Alexey A 00:13:37 Jonathan, do you think we would all agree that at least within a single profile.
like down the levels of hierarchy, like within a single profile. The given attribute name should always have the same unit, or
even that is too rigid.
Jonathan Halliday (IBM) 00:13:58 Well, I mean, on one hand, I can't off the top of my head. Think of a use case where it won't.
But equally.
We don't know what the future use of this specs going to be, and I don't really want to wind a situation where someone comes along in years time and says
this is unfit for purpose. I can't express my use case because the semantics are too limited.
This change, so far as I can tell doesn't make anything bigger or more complex.
It's just swapping 1 1 table reference for another.
So I'm not seeing a downside to doing it.
Florian Lehner 00:14:37 Maybe a crazy idea. But what about dropping the attributes units table on our side.
and trying to bring in a units field in the attribute itself.
Jonathan Halliday (IBM) 00:14:52 Right. So my comment above, there's there's 2 comments in quick succession.
The the second one's the proposed change to the data structure.
But the the longer text comment above it
says, yes, that that's 1 possible way to do it
at the moment. The attribute table field is of type, common key value. So we've we've taken the the key value definition
out of the the common spec that all the other protocols use.
And that's kind of double edged in that
it was causing me some problems in the Java SDK. And might cause problems in other sdks, because some of the code is assuming map semantics for that.
And it doesn't serialize properly. You have to basically write custom serialization code to get it to.
to serialize the way we needed to for exactly this problem. There's there's potentially duplicate keys in there.
Florian Lehner 00:15:50 So it might be that what we want is to ditch use of common key value and define our own type. That is a.
Jonathan Halliday (IBM) 00:15:56 The 3 way tuple of
the 2 fields. The key value already has, plus the the type field. But, as I say in my comment. The
the unit
attribute unit is sparse, right? Only only some of them have that. Some attributes will be strings, for example, and we don't care.
So the encoding is potentially not more efficient that way.
Alexey A 00:16:30 I'm I'm looking at the comment. And one thing that
I'm I'm probably missing something. The comment says. Index for entry attribute index. It says, index into attribute unit table. But the message itself is attribute unit. Is there some kind of recursion here? I just cannot.
Jonathan Halliday (IBM) 00:16:48 Oh, sorry. Yeah. That should say, attribute table.
Okay. Okay.
Alexey A 00:16:58 Okay. And
an attribute table is where we store key like, where this is where we minimize key and values. Right? So
this means this also means that we will have, we will specify, attribute units kind of like more times than necessary, correct.
because the attribute table it has both key and value. So the same key repeats. So, for example, like, if in one profile I have pid like process id attribute, and then it's like 1, 2, 3, 4, 5. Then the attribute table has process. Id. One. Process, id, 2, process 3.
And then for each of those records we would have an entry here, which is like more, which is redundant conceptually, because we will know that, like the unit, is the same in all of those cases.
Jonathan, does it make make sense.
Jonathan Halliday (IBM) 00:18:00 Yes, because there will be cases where you have the same name, but it is.
Alexey A 00:18:07 Right.
Jonathan Halliday (IBM) 00:18:07 The name doesn't determine the to units.
Alexey A 00:18:14 Okay.
Jonathan Halliday (IBM) 00:18:16 There are certain use cases where it's well defined, and you can derive the unit from the name.
But if all of them were like that we wouldn't need
attribute unit at all. We would only need the name, because then we use the name in conjunction with the
the set of rules, and we derive the unit from the the name.
The point of this mechanism is it? It allows for the the cases where the name doesn't define the unit.
So we have to carry that information separately.
Alexey A 00:18:45 I I don't know yet if I like it, but I I understand. No, okay.
Jonathan Halliday (IBM) 00:18:49 Yeah.
Can I ask to
monopolizing quite a lot of time? I think people need to go away and read the comments and wrap their head around it, and we can maybe discuss it on slack.
Felix Geisendörfer 00:19:02 Yeah, I think one thing that could help
one thing that could help people here, including myself, is maybe some historical notes as well, because I don't remember how the attribute unit stuff showed up in in the proto definition. I don't think it was in the people off and I also don't know why we decided we wanted in.
Alexey A 00:19:21 It is from the Prof.
Felix Geisendörfer 00:19:22 It is from people. Oh, I'm sorry I just looked and didn't see it.
Alexey A 00:19:26 Label label. If you look at the label
message in people of proto, it has unit of.
Felix Geisendörfer 00:19:38 Okay, that's where it's from. Got it?
Alexey A 00:19:40 Yes, and it's used for things like bytes. I think bytes is probably the most prominent example, or counts. I think there are also some units that explicitly counts.
Felix Geisendörfer 00:19:57 Gotcha. Thank you so much. This is really important. Pointer. And yeah, that it kind of explains why we're doing it in profiling and not in. Why, it wasn't an open telemetry before. Thanks. Yeah, I would suggest
or maybe the
the more conversation to happen offline on this. And then, once we sort of all had a chance to wrap our heads around it. We can
go deeper on it next time, or maybe already make some progress offline.
So let's go to the next agenda. Item,
write a profiling signal proto consistency check tool. Alexi.
Alexey A 00:20:39 I started to look into this. I have one question, is,
should a tool like this? So 1st I
I plan to use go. If you disagree, let me know. I also looked at the code that we already have, for I think there's a p profile test.
There are 2 links in the
in this action items. And there's also example code in parka
which is, both of those are good basis. One question I have but one of them is using
memory
a representation like there is this in in the collector repo. There is a separate kind of like layer on top of the proto, for in memory representation of the profile.
but Parker code uses the proto directly. So for a tool or library like this for the consistency check.
Should we use the proto, or should we use the collector
Api for the profile data? I again, I don't know the exact motivation for having this additional layer in in the collector. But maybe someone has an opinion.
Felix Geisendörfer 00:21:53 Is the layer on the collectors. P data that you're talking about.
Alexey A 00:21:56 Yes. Dsp, data. Yes.
Felix Geisendörfer 00:21:59 My naive understanding is that P. Data is generated from the proto, so it should be one to one. But
maybe somebody has more details.
Florian Lehner 00:22:10 I think P. Data is not complete yet, so there is support for profiles, but not for the nested messages yet. It's particularly important for
If someone wants to have a filtering process. This is currently not possible, because the nested messages are missing. Yeah, I. I have assigned a task to implement a message sample and then going further down. But the at the moment, it's just on the profile level. As far as I know.
Alexey A 00:22:45 But who is kind of intended audience for the P data interface is this.
for example, does the Ppf collector use be data?
No. So is this just like an inside the collector itself. Okay.
Josh Suereth 00:23:00 Yeah, Pda is supposed to be the stable interface for passing data in the collector. So if you have any component in the collector, that's how you fire it through any of the processors and things. It's meant to be stable independently of the protocol, which is why it doesn't send raw and tries to hide like, what version of the protocol you're using in case we have to support multiple.
Alexey A 00:23:23 Okay for the for this consistency check.
There are just like different ways of how we can have it. One is we could have it as like a standalone command, line tool. And then, if someone serializes
their collection, their their profiling data into a file, they can run this tool and then see like, if all the checks pass
that's 1 thing, and that would be more of kind of like development time thing.
Or do we want to have it as an Api, and then so that the producers of profiles can call it.
And but then it would be kind of like. It would be kind of strange to continuously call it for the consistency check, because usually, if it doesn't pass, it's a bug in your code. I don't know if you want it.
if you want to.
If a particular producer of the data wants to
call it continuously, and every time.
or maybe collector should check the consistency like, Do does collector today do any consistency checks for the data it receives.
and then, maybe like declines it, or something? Is it like for monitoring and logging, is it? Is it like a common thing to do.
Florian Lehner 00:24:33 Not, as far as I can tell.
Alexey A 00:24:36 Okay.
Josh Suereth 00:24:36 It. It's kind of a per receiver decision, too. I think the generic Otlp. One doesn't, doesn't do much. There are things that might get rejected. But it's not the level of validation you're talking about.
Felix Geisendörfer 00:24:49 What
I would propose is for the initial version. Whatever lets you work faster, which might be directly going off. The proto would be useful, because I think our main use case is just making sure we're really aligned on. What's the semantics of our protocol really are? And having working working code to do that would be great. Further down the line. Given also what Josh just said, I could imagine this being a processor in the future. That basically would provide
active validation of the data based on our understanding. But that might just currently be more annoying to implement right away because it's going to be tied to the life cycle of P data. And the collector and upgrades are gonna take more work. So I think while we're iterating quickly, I would say, having it as a standalone tool of the proto would be my guess for what's most effective. And later porting that code as a collector processor would be nice.
Alexey A 00:25:46 Sounds good, do we care which repo it would go to like if I would send. If I'm sending a pull request what repo I would send it to.
Felix Geisendörfer 00:26:01 I. From my point of view it would be fine to be in the proto repo as long as it's type
strictly tied to the proto definitions that would also make it easier, like when we want to make changes to it and the proto at the same time, it's a pull request against a single repo. I don't think that's good. We want to keep it there for long term, but
unless we get pushback from the the rest of the proto Maintainers to have some code in there for validation. I mean, it would strictly be like
tooling level code like it wouldn't be expected to be used by anybody other than people want.
Alexey A 00:26:32 I don't. It.
Josh Suereth 00:26:33 Recommend against putting the proto repo, because you won't be able to move quickly on it.
You like you're going to require. There's a much more limited set of people who can review the proto code than another repository. So if we can either get you a tooling repository where you can do this work, or we have another repository where you can add a tool, and then we can. If you build a container out of that repository, we can use it in the proto repository to validate things. That's fine. That's that's a better structure. We do have a repository called build tools that turned out to be an epic failure that is used by the proto
library. But it was one of these.
basically, if you put too many utility tools in the same code base with no clear ownership. They decay, and it becomes very problematic, right? And so that is something I do not want to have happen to the proto repository again. So if we can find a place to put this, that'd be better if there's a place that the profiling sig already has. Where, like, you want to put this tool.
That's great. Otherwise, let's get you a new repository where you can put this tool. You can iterate quickly. You can have your own set of maintainers from the profiling Sig that can get that thing out the door and review it.
and then we will use a container image you build in Github actions in the profiler like, if you want us to do that in the in the proto repository. Right? But let's not like. Add in pieces in the proto repository that require additional ownership right now, because we we haven't been successful in that in the past, and I don't want you this effort to fail. Does that make sense.
Felix Geisendörfer 00:28:05 Yep.
Josh Suereth 00:28:06 Okay.
Alexey A 00:28:08 There's something cool. Go ahead.
Oh, sorry. Sorry. There's something called open telemetry. Go, build tools.
Would that be.
Josh Suereth 00:28:18 That that's owned by the go ecosystem to do go code to do go code generation.
There's also something called built tools, which I think today is mostly protocol based tooling, but is mostly, in my opinion, is basically abandoned, like very few people try to maintain that. And it's very hard to maintain, because there's no clear ownership of anything.
We have been trying. I can send you an issue on the build tools thing we're trying to extract out components of it. I'm happy to like, if you, if you want to open a community issue repo, to have a repository for this specific tool where you can iterate quickly. I think that would make sense as well. If you want to work with the go build tools, you can, but you will need their approval for everything you do, so that would be the the go sick. I think Tyler might. Tyler Yan might be a good person to talk to for that.
I don't know if you have any other recommendations from the Gc. Morgan, but I would highly recommend your own repo here.
Alexey A 00:29:17 Okay. I'll maybe put it to my personal repo first, st and then we can, and then we can figure out where to where to put the code.
Felix Geisendörfer 00:29:27 Yeah, I think. And I think in parallel, I can raise the community issue for getting a new repo. Josh, just a quick question. There. Is it okay to request, like I don't know. Profiles, util repo, or something that could be generic for future ad hoc. Use cases like this because I don't foresee this to be like a long term project if we make it a processor at some point other than that.
Josh Suereth 00:29:47 We've done. We've done that in the past. I think if you do that, let's give it a clear timeline for how long it's going to be alive. And when we plan to kill it, just because, again, that second part, we have failed to do a lot. So we have a lot of repositories that I think we need to start cleaning up in open telemetry. So if you want it to be temporary, let's put it in a temporary spot where we can literally get rid of the whole thing.
Alexey A 00:30:12 In the another. Another litmus test sort of would be, for, let's say, for the code.
converting open telemetry to people off and back, or other conversions like where that code would would go.
We would need a place for that. And maybe this, maybe this consistency check and those like conversion code. Maybe it could be the same repo, but for that that the answer would be like it would live forever. So I don't, and I don't know if this changes the answer as like if it if it's going to live forever or like long time, we want to find an existing product that could be a fit anyway.
just like converters is another use case that we should think about.
Josh Suereth 00:30:59 Yeah, that makes me think that maybe just giving you a repository for the conversion would make sense.
You could have this as a utility in it, and then you can decide how to evolve as you go. But yeah, if this is a library of conversion, the closest equivalent I can think of is the OP-amp spec, where they have a specification repository, and they have, like a Go library repository for people who want to let in interact with OP. Amp, and then that library gets used in other components of open telemetry.
Alexey A 00:31:34 I don't want to complicate this. But and of course I will. I wonder if, like, if we, when we have conversion. Would we end up having converters in different languages?
Because the consistency check tool, we don't care what language it's about, and it's going to be in go. But if we have like converters, then like, would we have like converters for Java converters for go? Because it then it depends on
who calls it hopefully. No, hopefully.
hopefully go would be enough. And
most of the conversion would happen in the collector code from the ecosystem point of view. But I'm actually not sure. And this is, this is a deep rabbit hole, potentially.
Felix Geisendörfer 00:32:15 Yeah, I I have a proposal here. I think we should really stay focused on conversion in the scope of validation, because we have said publicly. We want people off to be able to round trips through hotel and back intact with our data loss. I think you're also thinking about use cases like, Oh, the go runtime currently produces P. Profs, and we want to eventually convert those to hotel.
But I think the requirements are very different, because that is probably gonna have performance requirements that we don't have for validation. That's probably in the long run gonna make more sense to be upstream, and we can file upstream pro
yeah, issues with the Go project to make get an efficient interface for that. So I would for now stay like in the validation lane. If that makes sense to to limit scope.
Alexey A 00:32:57 Okay. Yeah. Yeah. Sounds, good. Okay.
Felix Geisendörfer 00:33:00 So based on that I would still vote for like a temporary repo. And then that code, I mean, you can write the code nicely if you want to reuse it later, but I think we'll figure out where it should live long term as a separate step, and for now just keep it really focused on validation.
Alexey A 00:33:17 Okay.
Felix Geisendörfer 00:33:19 Cool. Then I I will take an action item to request the community repo, and you can just get started in personal repo, and then we'll move the code over it. I think that should work.
Alexey A 00:33:28 Okay.
Felix Geisendörfer 00:33:30 Just catching up on notes.
Alexey A 00:33:38 Did we submit this tax change.
Felix Geisendörfer 00:33:42 That is an agenda item.
Oh, coming up shortly.
Okay.
yeah, I. It brings us to the next item here that is related to stack changes.
write down all the concern for stack traces performance simplicity. I think I'm probably gonna drop this because I feel like we have alignment on on what we want to do there. I I did promise to review benchmarks from crystals a little bit more, which is later on the list. But I don't know if we really need to have a problem statement for for stack traces at this point. But let me know if somebody disagrees.
Okay, no disagreements means I will just drop it. And if we change our mind we can bring it back.
going to the next one. Yeah. Review benchmarks from Christos. I wanted to do this, but I haven't gotten to it yet. Has anybody else had a chance to review benchmarks? I think there were comments on the Pr.
Alexey A 00:35:12 I remember taking a quick look at it, but I don't remember if
if I had any particular observations.
Christos Kalkanis 00:35:21 There are no newer comments than last time. So I had a big back and forth with Bo.
So Bo had a particular use case in mind that the benchmark he was using he was using CPU events.
But CPU bench does not result in a large number of different stack traces essentially results in all the CPU cores in your system, running exactly the same code, so that generates very few stack traces with a very large number of Timestamps if you're using nanosecond time stamps. So it's not really a good benchmark for the alternate stack trace representation that we're trying to
to establish them.
So yeah, I mean, from my point, like, given that this has dragged on now, for I don't know. Like 4 or 5 weeks, I think. Yeah, we need to make a decision. I think if Alex is confident that
you know we should not go into the double array representation, which is is better if we don't use compression, but with compression
it's it's always worse, are
then I think the sooner we wrap this up the better, because it's the main protocol change that's holding us back right now from
let's say, wrapping up the protocol. And I think this will be also a good time to recap like what protocol changes do we have on the table? So if there's this stack trace representation, then there's the attribute unit that we just discussed today with Jonathan. Maybe that will result in some protocol changes, and then the last one is the default sample type, I think. Which Felix, you have a Pr. Open with the proposed change. I approved it. Lauren approved it
so. Is there anything else other than those 3? I think not. But.
Florian Lehner 00:37:10 I did put has attributes on the table again. We discussed back in December, and it's later on back end today.
Christos Kalkanis 00:37:22 Okay.
Felix Geisendörfer 00:37:27 But yeah, but I think
going to try to to mix catch up on the notes here. So the suite protocol changes our stack, trace representation.
default, sample type, and what were the other? One or 2.
Christos Kalkanis 00:37:38 Attribute units.
Felix Geisendörfer 00:37:42 Yep. Attribute units. Has another one.
Christos Kalkanis 00:37:44 And then, Florian, I raised an issue for today, which is all the has attributes for symbolization. So we we've discussed this in the past.
Florian Lehner 00:37:52 Maybe we can.
Christos Kalkanis 00:37:53 And make a final decision today.
Felix Geisendörfer 00:37:56 Okay, just to move us forward in the agenda, I would say on the benchmarks. I will soon talk about the simple, stack trace representation. I think once that Pr resolves. That also means the benchmarking discussion is resolved. Because I think people, when they refuse this Pr will come back to the benchmarking Re pr, and be like, Okay, do I want to approve this? Yes or no, and then I think it will get scrutinized through the second round.
so if that makes sense, I will take us to the next action. Item here.
Which is getting the simple stack. Trace. Idpr ready.
My update here is that I have. Just before the meeting pushed a conflict resolution, because, the my Pr. Was from before we had sort of profiles, dictionary message. And so I had to rework things a little bit. But I think the code change is ready to review. But I was planning to also update the Pr description a little bit, because things have moved on a little bit on terms of why we're doing it. And and
I want to explain it in detail, link to your benchmarks as well, which we didn't have when I started this. And then I would basically change it from draft to ready for refuse and a message to the Cncf.
I'll do my best to do this before the weekend, so we'll have plenty of time to to go over it before the next meeting, and then the goal would be to get this approved by the next meeting and and have this out of the way or or even before offline, if we don't run into any last minute concerns or issues.
Yeah, if anybody has thoughts or questions feel, raise them. Otherwise I'll just catch up on notes quickly and take us to the next item.
Jonathan Halliday (IBM) 00:39:55 That's really about the representation, not the id right? It's it's a simple stack, trace id.
the issues we had around.
Do we have profile, ids and things of something different.
Felix Geisendörfer 00:40:08 This, it's not about profile. Id. This is really just about, how do we represent.
Jonathan Halliday (IBM) 00:40:12 Yeah, trace id versus profile id, it's it's really representation. Okay? Good.
Felix Geisendörfer 00:40:18 Yep. Yep.
Jonathan Halliday (IBM) 00:40:19 Yeah, that's the last big one I need for getting the the SDK finished. I think.
Felix Geisendörfer 00:40:26 Yep.
and then the next item on the to do list would be can we have hotel SDK, communicate process level information.
So writing process, environment variables, I guess there would be Naf.
Nayef Ghattas 00:40:44 Yeah, I can take this so this, this was feedback from the document to present last week on being able to share process level information specifically to be able to access hotel SDK resource attributes from the open dynamic Vpf profiler and be able to append them to profiles.
The short answer on whether we can write to environment variables is no, because the open tenet 3 Bpf profiler cannot see the environment. Variables that are written via setenth by processes, because when you use Setenf to write environment variables, they are not reflected in the Procfs file system in Linux.
So they're just available to the process itself. But you can't access them from from another process like the open dynamics and upf profiler.
And even if it was possible writing environment. Variables is not threat safe. So if the program is reading environment variable at the same time that we write environment variable, it might crash
so as a next step related to that, we were, we were going intending to write a document for proposal 2, that is, specifically focused on sharing resource level attributes between hotel Sdks and the open telemetry. Bpf. Profiler. That would recap all the information I just gave and
also that would talk about the use cases and the features that would be enabled by something like this.
Felix Geisendörfer 00:42:29 Okay, and that document's gonna be available soon.
Nayef Ghattas 00:42:32 Yeah. Hopefully. By next Sig meeting.
Felix Geisendörfer 00:42:39 Okay. Then I think we'll just wait for the document before we go into deeper discussion, unless somebody wants to challenge the the set environment thing. But I I think it's pretty clear. It's basically it's not a Syscall. So let's see which means, it's not
visible from Ebpf, at least, not unless we go really crazy, and we try to. You probe it or things like that. But then it's not threat safe. So it really seems like a dead end to do the environment levels.
Okay, given that, nobody spoke up about this, we'll try to move forward. We're now done with the review action items. So the next agenda item is drop default sample type. For those who haven't seen it. There was a Github discussion
involving Alexi Florian and a few others. Thank you for all the comments. And yeah, basically, I think we aligned on
removing the default sample type. And yeah, Florian and Christos have already approved the Pr. Which I guess means we could send it off to the
brother people for for approval. But yeah, I'm wondering if anybody has had a chance to see it yet. It's from 5 h ago. So probably not. Yeah. I'd like to go for it.
Alexey A 00:44:02 Will we add an attribute for this
to make sure that the pro profiles can be represented.
Felix Geisendörfer 00:44:11 Yeah. So the the Pr that I raised specifically proposes this. So my proposal is to add, a Pprof dot profile order, attribute to scope, profile attributes the name can be discussed. There's also other solutions that you hinted at in the discussions, Alexi, but I think the the attribute one seems the cleanest to me. And.
Alexey A 00:44:32 Okay.
Felix Geisendörfer 00:44:32 That will allow us to basically do the round trip from pre-prof to hotel and back without losing data. So
that's not part of the Pr itself. But the commit message, essentially, or the Pr. Essentially says, that's what we're how we're going to resolve that. So that's what you would be approving. If you approve.
Alexey A 00:44:49 Okay? Yeah, I think that's that should be. That should be fine.
It's the default default attribute, is.
It's a Ferrell in niche thing. So I think attribute is attribute, makes sense.
Felix Geisendörfer 00:45:06 Yeah, I mean, we still have it. We're basically just saying the profile order is the default attribute. So that I added a comment. To specifically call that out. That's the very 1st profile in
in the payload is is the one that a fewer should prefer if it needs to show a single one. But of course, viewers are free to do whatever they want. It's just a suggestion.
Alright.
Alexey A 00:45:27 It.
Felix Geisendörfer 00:45:28 So our our main concern with default sample type is just to make sure we scroll it something similar ways, so we can do the round trip. But yeah, I think the ordering, we say the order of the profiles is, was this in the original Ppro? Then we can basically also restore the
default sample type.
Wait a minute.
Alexey A 00:45:49 By by order. Do you mean like it would be like a list type? Or do you mean that this is specifically default sample type, name.
Felix Geisendörfer 00:46:00 So basically the
the way it would work is if you have 2 sample types and the default, one is sample type one. Then to convert to hotel, you would basically, I mean, 2 sample types would turn into 2 profile messages, and you would change the order of some. So basically profile sample type, one would be the 1st profile and simple type 2 would be the second one.
Yeah, I see.
And so then if you convert back to Pprof, then default, sample type will be populated by looking at the sample type of the 1st profile. So that's how that works. But then, in order to get the sample types in the same order that Prof had them. That's where the profiles order comes in which essentially tells you in which order Pprof would like the sample types in order to not. I don't think it's actually of great consequence which order the sample types are. So we could also just say, This is good enough for a round trip.
but that just makes validation more cumbersome. If we have special rules on certain parts of the people of message being considered equivalent, even if they're out of order, like, if it's a list and we accept reordering it. Yeah, it just seems complicated.
Alexey A 00:47:08 Okay.
Felix Geisendörfer 00:47:15 Yeah. Take your take your time to to review it. Offline. We. We already have a few sums up. But I I think, basically just can sit until the next meeting, give people a chance to look at it. And unless we find any reasons not to do this, we we can watch it at the next meeting.
Maybe what I can do is maybe I'll add a comment to spell out the
an example of like how the conversion back and forth would look like this is in place. Because I I just realized I kind of hinted I'm hinting at it in the Pr description. But I'm not spelling out an example.
Okay? Then
we are at the next item, Florian, can we drop the Hes things? I feel like we had discussions about this before, but I'll let you take it away and introduce any history there.
Florian Lehner 00:48:16 Will forward discussion back in December, I think. Alex. Say, started a Pr. 5, 9, 5.
That would allow us to drop. The has function line numbers, inline frames.
booleans, and just introduce an enum. This was what simplified a lot of things, and also, I think, simplified a protocol and
We could go also, I think, without the enum and without the rules. It's more like, Hey, someone has them to figure out. Hey, is this value set. So it's more like decoding effort to check if file name is set.
Yeah. So
it's also in our burn down list as we wanted to discuss discuss this. That's why I brought it up as it was also asking our side again. Hey, what's about these fields?
For the Ebpf profile I can say we don't use and set these fields.
So that's just from how it works. At the very moment.
yeah, overall. Maybe Alexi can say, maybe something about these has fields as they directly come from Prof.
Do you see a big value from them? Or is this more of a historical
technical debt that is kept.
Alexey A 00:49:49 Piprove does use them to see.
like what is the level of symbolization for a particular mapping, and, for example, whether it needs to be
re-symbalize at better quality. In many cases you can infer that from just looking at the data. But if it's a large profile, then looking at the data can be expensive like you don't when you just oh, imagine you open a profile in people of cli, and then it wants to quickly check. Should it, should it? Should it try to resymbalize, like to symbolize the profile against local binaries? People off cli. Does that? Does that check?
And then it quickly checks this pulling fields, and if it's like, if you have, if you already have, like in lines and in line frames, then it will not even bother to try to search for a binary and debug info
and if it's a large profile, then just trying to scan through all locations for the particular mapping to figure out. Okay, like, do we have all everything
is can be, can be expensive. So people does use that. Whether it's useful universally as part of protocol. I'm
I I honestly because because I'm so biased to people like I would say like, probably yes, but but that's because I know how people uses it. So I know that, like for round trip, and for for the usage and people, we would need something, but it could also be attributes like we could put this into kind of like people of namespace for attributes for per mapping
so, and like, I think, making Boolean attributes that just like one to one mapping
with the existing bullying fields and removing them from the protocol. That would probably be the easiest in terms of just getting something landed
with. When I propose the enum, I will. I basically made an assumption that this is going to be universally useful, and also Booleans are even like internally, in people off and in our use of profile. Pro of people off proto, like Booleans, are quite
because you can have, like 16 combinations with 4 booleans, but only a few of them make sense, so within them. I also tried to kind of like reduce the complexity of
of that. But if we say that this is people of specific, then I would just go with bullets, because
that will be just a simpler conversion. If you want to with if we want to make it, and if people find it useful as part of protocol, then I would say, the enum makes more sense, because I think it's just more organized.
Felix Geisendörfer 00:52:33 Yeah, I think I would like to make a case for this being a people of specific thing. And the reason is that
I would venture a guess that most open telemetry
components will not be in the in a position where they'll see the binary together with, like the profiling data. It's very much a use case for local fewer
and
even for local Fuhrer. It seems like this is just a convenience thing, right? Like you could a decide to always look at the binary, to to get symbols when when there's none. If you have conflicting symbols, obviously between the profile and the binary, then I don't know, having some conflict resolution strategies useful. And I guess these fields can be seen as such. But
then, again, that can also be a user choice to say like, Hey prefer binary or prefer what's in the profile. So I think we definitely need to restore the round trips for Eprof. But I would say that
most of the users of the open telemetry signal will be sort of cloud
use cases. And and in the cloud you will typically not see the symbols as a binary. I mean, they'll flow through like
other mechanisms. But I I think the general idea is, if there's a simple pipeline, bringing samples into the cloud, and those are the preferred source of truth, and not whatever was maybe recoverable from the original profile. So
I I. Yeah, I would make a case that we should turn this into attributes. Long winded way of saying that.
Florian Lehner 00:54:17 I think you're mute, Alex.
Alexey A 00:54:21 Sorry. Yeah, these are definitely not fields that users of profiling tools regularly look into. These are more kind of like pro data processing
bits for artifacts. Sometimes you look at them for debugging like, oh, why am I? Why does my product look odd? And then you look at? Oh, is it symbolized or not? But other than that, it's it's fairly exotic.
not exotic, in the sense that it's not needed, more exotic like for users, for for end users to look at that.
So I can. I can drop that Pr and propose attributes instead.
And this is second example, where we should also agree on some convention for naming people of specific attributes. Probably people of.is something that Felix
suggested for for the other one. And yeah, maybe
there should be going a separate file. For because I remember, actually, I think, attributes in some in semantic convention
repo, they are organized by kind of like domain. There's like Asia dot something like Gcp, dot something. Maybe we would have like people of Dot, something.
Florian Lehner 00:55:33 Speaking about the semantic conventions, we might to used profiles prefix
because semantic convention tries now, or has an hard requirement or
tends to apply our requirement to attach profiles more to a signal, so they can be more. And people try quite generic. Maybe Josh can directly jump in.
Josh Suereth 00:56:01 Yeah, so can you hear me? I'm having some internet issues.
Felix Geisendörfer 00:56:07 Yeah, you're good.
Josh Suereth 00:56:09 Good. Good. Okay. So there's there's 2 things that are true in semantic conventions. One is, you need a namespace that is reasonably unique
right? So if Pprof is actually generic to the point where we think something that is not profiling, Pprof could have that namespace, then use something that has a prefix. However, if Pprof is always profiling
and always peep rough.
and we don't think that there's risk of that. You can actually use Pprof directly. The thing that you were saying about having signals that back the attributes. What that is about is we would like the ability to have actual instrumentation that provides these attributes
before we stabilize semantic conventions. We don't currently have a way of defining the profiling signal in semantic conventions. So you guys are kind of at this awkward state, where, if you're defining attributes that would be in an open telemetry resource, we have a way to define those.
If it's in scope, the open telemetry instrumentation scope. We do not have a way of defining those. Actually.
we have some that have stabilized. But that's a different story. And then for the profiling signal itself. We don't have the ability to define those in semantic conventions yet, if you have like attributes, you want to stabilize, which is why you were having trouble flooring, because we need to define that. That doesn't mean the attribute needs a profiling prefix. It means we need the ability to define them in the semantic convention. Yaml, model.
right? The profiling prefix we were recommending for you specifically was, if you want an attribute
that is specific to like open telemetry profiling. You would use profiling there to denote it, because we didn't have any other namespace to put it within. And we want things to have at least one namespace, but it only has to be reasonably unique. So Pprof could actually be fine. The second thing I want to call out is, we have a whole compatibility set of conventions.
So there is an Otel namespace where it's hotel Dot. Whatever that namespace is not used by opentelemetry itself. It's used to describe the attributes or tags or labels, or whatever we would use when opentelemetry data
winds up in a different system.
we have similar kind of attributes coming into semantic conventions, and I think Pprof. Kind of fits there. So I think it would be reasonable if you want to put things in a Pprof namespace if you'd rather have them in a profiling Pprof namespace. That is also fine.
So that's kind of a long winded answer. But I wanted to make sure you understand the rationale behind these things. That second bit of we cannot define. Profiling semantic conventions today for lack of yaml support is something we should probably talk through. I can represent the semantic convention tooling group there, because I actually work on that tool. But that's probably a discussion we should have at some point
not not not needed right now. But yeah, if you need, if you need attributes, it'll be harder for you to get in, because we can't use our normal process, but we can still make something happen.
Felix Geisendörfer 00:59:23 Thanks. Yeah, I I guess the summary is that for this particular use case, we could try to start with the ploss prefix and then, yeah, for the other stuff. We'll come back to you. Josh.
okay, any more thoughts on this or other last minute topics. We have roughly 50 seconds left.
Florian Lehner 00:59:45 So we can conclude that we want to drop the the
pools for the attributes right.
Felix Geisendörfer 00:59:54 I think so. I think that's the conclusion here.
Florian Lehner 00:59:57 Okay.
Christos Kalkanis 01:00:03 For consistency. Like, if we, you're always using profiling as a prefix for the other attributes we define. And maybe it's better to have profiling to people. Just so. Everything is under the same namespace because people by itself.
you know it. It's relevant to what we do. But it's it's outside of that namespace.
Florian Lehner 01:00:22 Yeah, I'm.
Alexey A 01:00:23 Currently we have the profiles namespace that is used as example for frame types.
Yeah, I'm looking at the files as well. We have profile and then we have common dot yaml registry dot Yaml, maybe we can just have people off dot yaml in that in that directory, and then attributes would be like profile dot Prof. Dot X.
It's I. I kinda also tend to think that, having
having that on the profile kind of just groups, things better.
Christos Kalkanis 01:01:02 Yeah, it's it's also from a discoverability perspective. Right? Everybody?
Right? Right? Yes.
Alexey A 01:01:07 Yes.
and also it will have a better chance of being reviewed by appropriate people rather than just becoming a separate sandbox.
Josh Suereth 01:01:18 One thing I will say, because this is kind of evolving. The semantic conventions will have single specific registries.
so there will be like a registry for profiling that will have your namespaces in it isolated from the general attribute registry.
So the general attribute registries, attributes that are available for any signal. We already have a registry for entities. You don't see it on the website yet, because we're still that, for there's always like a month delay between semantic convention launch and the website launch.
But you, there is a registry that will say, like, here are the things that would show up on opentelemetry resource, which is an entity right? That we're trying to bring that also for logs and metrics. And we'd like to have that for profiles whenever that exists. So you would have like a space that is here. The profiling, specific things
so like don't over correct on how attribute registry works today
in terms of discoverability. But I think discoverability is a completely fine reason to have a namespace.
Felix Geisendörfer 01:02:18 Okay?
I, I think we have pretty
much consensus that the profiles dot people off would be maybe preferable here. So let's let's go in this direction, for now I think we have consensus to drop the pool fields.
And any details beyond that could be hashed out. Offline isn't
then, unless anybody has any last minute things
I would say, thank you all for your time and all the work done in between the meetings. And yeah. Wish you all a nice local time.
Florian Lehner 01:02:54 Thank you.
Felix Geisendörfer 01:02:55 Yeah.
