SIG: Semantic Convention Tooling
Date: 2025-06-25
Duration: 39 minutes
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 04:01 Hello!
**Jeremy Blythe** 04:14 Hello! There
I am!
Could we just need to wait for a few more folks, and I'm just
filling around with the schedule the the agenda
in the Google Doc right now.
Well, we might.
**GZ Gregor Zeitlinger** 04:55 By the way, I just joined because
I heard Weaver so many times, and that it's a cool project that I wanted to learn a bit more what you're actually doing.
**Jeremy Blythe** 05:10 Okay, well, we can.
I can definitely explain some more about that. If none of the year usual folks turn up and
we can go through the whole thing.
**Alexandra Konrad @Elastic Security** 05:29 I think there should be somewhere video, and
maybe even presentation from Josh and Laurent about because they have presented it last Kubecom
in London. But I need to find the link.
**GZ Gregor Zeitlinger** 05:50 Oh, yeah, be nice.
**Jeremy Blythe** 05:58 Yeah. One of the items that I'm working on right now is a better.
hopefully, a better read me. That's a bit more of a showcase for the application.
so the moment we're very sort of focused on, I guess the detail of
how it's made and what it does rather than kind of showing off the purpose behind it.
Here it is. Let me paste this in the chat.
**Alexandra Konrad @Elastic Security** 06:25 Yeah, I have posted the link to the
A Youtube presentation like, talk by Josh, and.
**GZ Gregor Zeitlinger** 06:44 Where did you put it?
**Alexandra Konrad @Elastic Security** 06:47 Here, here in the chat.
**GZ Gregor Zeitlinger** 06:55 Okay. Now I got it. Thanks.
**Alexandra Konrad @Elastic Security** 06:56 Yeah.
**Jeremy Blythe** 07:24 Okay.
they seem to be quite low on people today.
**Alexandra Konrad @Elastic Security** 07:41 Josh showed he is quite tight. With his work so double review on that, John, as well.
**Jeremy Blythe** 07:55 Well, in that case, then, maybe this will be brief, but I will
let me share this our usual stuff, and we'll go through it.
Share my screen, this guy
hopefully, you can.
You can see the agenda and stuff there on the screen. And I'm showing the right things.
Okay?
So 1st off, we normally go and have a look at the semantic Conventions Project board.
So
let's go there.
So I'm not personally working on anything in here right now, but.
**Alexandra Konrad @Elastic Security** 09:17 I mean, I'm working on this. A life working. Yeah, I have made the proposal, but there are like no comments on it. Only you
made a comment, and no one else
like. If I should proceed with
enumeration as they are right now, or you should think about them as a 1st class citizen, then move them to the type.
and there are like No, and the comments, that's fine, right? I think it.
**Jeremy Blythe** 09:57 I mean I
I I mean I gave you my opinion. I guess we need to.
I see that the mill has joined.
I wonder if the minute do you have any
opinion on this stuff? So we're looking at this ticket that was around enumerations enums.
My suggestion in here was that we make enum's a type
so that they can be reused in multiple places
based on that's based on some things that I ran into personally when trying to define things so.
**Liudmila** 10:45 Yeah, Hi, yeah, I I'm currently on my phone
**Jeremy Blythe** 10:51 Oh, I see it's really hard to.
**Liudmila** 10:54 See. Okay, I found how to zoom.
So what? What?
Thank you.
**Jeremy Blythe** 11:06 Yeah. The original ticket was this one which was about.
**Liudmila** 11:08 Yeah, this one I know.
**Jeremy Blythe** 11:10 Yeah, okay, so we were talking a little bit. And
my my suggestion, let's say, is that we pull.
We pull enom out so that it's actually something you define
at the at a top level, like in like a new type
rather than it being embedded in inside of the definition.
And then we had.
**Liudmila** 11:40 To use it.
**Jeremy Blythe** 11:41 Reference it.
**Alexandra Konrad @Elastic Security** 11:46 I think we just need more comments on on the issue like should we proceed with existing variant and ways to update or change enumerations when they are referenced from their definition. As this was originally a proposal, or we should
could go like completely different way and define them as their own type.
And yeah, diverge from there. So I think we just need more eyes on this ticket. And
**Liudmila** 12:25 Yeah, I think the main problem we want to solve is that we want to change
the enumeration when referencing good.
**Alexandra Konrad @Elastic Security** 12:34 Yeah. So like, this was the. This was the original task.
**Liudmila** 12:39 Yeah, that's that's the problem we have. So
regardless of how enum is defined.
We need to figure out how to modify it.
**Alexandra Konrad @Elastic Security** 12:53 Yes, this is this is what the what which proposal I made. And then there came this additional request. I mean, maybe we can split them, that
in order to possibility to to modify it and update it. We also need a
option to kind of rename them like to use the same enum within one event, or like within one entity, but with different names. And Jeremy just had like that example that he had something this time. Yeah, so that it started ended, etc. And the enumerations
the same. Essentially. So you just need to define the same enumeration, but under different names.
**Liudmila** 13:48 Yeah, but I mean, I don't see a big need in in share in sharing like it saves us maybe
a hundred lines of of code. But it doesn't.
It's not a problem to have multiple enums that define started stop. And and things like this, yeah.
the real problem is more of a take the attribute and refine the members on the enum.
And I'm not like it creates so much problems like, what what do we do with?
Let's say, code generation, do we? Do we declare a new enum type?
Or do we just hard code a specific value in some cases? Or I think we need answers to
all of these questions. I think there are some some comments on the issue about this.
**Jeremy Blythe** 15:15 Okay, so how do we proceed? Then we just we just need to
get some more opinions in here and have some more discussion. Right?
**Liudmila** 15:27 Can we take a look at? What? What does the refinement, mechanism.
**Jeremy Blythe** 15:34 So this one.
**Alexandra Konrad @Elastic Security** 15:37 Yeah, I have posted here the
the original idea that we had that we have
the kind of base enumeration. And then we might differ from that enumeration by adding some new members or removing
the members. Kind of you you provide here what members you want to have in your
It's a bit later. So this is the.
**Jeremy Blythe** 16:16 Formal definition. And then I made a couple of examples. When you want to add, or when you want to remove some of the values.
**Liudmila** 16:31 What what do we do?
To generate if you want to generate code from it. So what we did today, we just generate
enum in the corresponding language.
But it's it's 1 enum.
So how should we handle core generation for those refined ones.
**Jeremy Blythe** 17:11 That's why you need a new.
That's why I'm suggest. I guess that's 1 of the reasons why I was suggesting a new type
is that you could, you could still like
than copying and pasting each type, you can still use a refinement mechanism like this if you so wished to say, like, Oh, I'm I'm copying this type, and I'm making these subtle changes.
Maybe maybe that will save some error errors like
like you're inheriting an enum or something.
**Liudmila** 17:43 Right, so it should be like an extended, expandable enum r, so that you can.
**Alexandra Konrad @Elastic Security** 17:51 Like.
**Liudmila** 17:52 This custom value. I probably cannot do anything about reducing the number right? We wouldn't do anything
but for core generation. Additional members would be
generated dynamically like from, let's say, Patch.
they want to be part of the original enum.
Okay? So one option, we find a full closure all possible members across all possible refinements.
and we generate the enum type that covers all of them.
Or we say, Okay, there is the base enum
and dear languages, you should start generating them in the way that they are expendable, and we
in some cases we will have additional members.
**Alexandra Konrad @Elastic Security** 19:01 In in case of 1st option, when we have like all possible
values, there is then no enforcement or like how we could enforce that only specific values could be used in the particular usage of enumeration.
like, because then.
yeah, because right now, it's kind of similar like, this is what we're doing right now. We are putting all the values into the enumeration, and in the particular usage we put in comments, I think in info. Like
note in note we put which fields from enumeration should be used for this particular case
and like, but there is no strict check.
So you can it. It just, you know, just a note.
And I have this problem for hardware metrics, because there we have a type which has all hardware metrics, let's say 12 or like 15, and for every metric the type should be only that particular like, let's say hardware. So what I do like I have the metric in as a Sorry. I have the type as the common attribute
which has all the possible types. And then
for each metric. I say in notes that for this metric there should be this type so something similar, which is extreme case of reusing the enumerations
about that.
**Liudmila** 20:51 We have.
**Alexandra Konrad @Elastic Security** 20:52 Other cases. Yeah.
**Liudmila** 20:54 Yeah. And we have a similar story with database system name messaging system where we have, let's say, 50 different systems.
**Alexandra Konrad @Elastic Security** 21:02 Yeah.
**Liudmila** 21:02 But each particular convention only needs one value.
And I'm thinking, maybe we should solve this problem instead.
If we solve this, there will be actually, no, no enum problem, no enum expansion problem.
**Alexandra Konrad @Elastic Security** 21:15 But this is not only about this. We have cases because this originally came from
system metrics where we have depending on where exactly those metrics are used in CPU, or like in some other type of hardware. You
have different states. I'm not sure exactly what was it? But I need to find the issue, but that was that we have 3 in this state and 3
other in this state, where 2 of them are common. So in like in reality, like, they have created one annum with all, let's say, 5 possible options. And in the notes they mark that. Okay for this type, we need only this 3 values. And for this one we need only these 3 values.
So I think this is where this originated. It's not only about one specific case, but also when you have intersection of different values.
So that's why this solves this exact problem. But I'm I'm not sure about instrumentation, how the
the best way of doing like probably the best way would be, create every time a new enumeration.
**Liudmila** 22:46 And logical.
**Alexandra Konrad @Elastic Security** 22:47 It means.
**Liudmila** 22:48 Support that only needs one value from the enum you just you just use this value. If you wrote this code.
**Alexandra Konrad @Elastic Security** 22:56 In yes.
**Liudmila** 22:57 You know, for one single value.
**Alexandra Konrad @Elastic Security** 23:01 In this extreme case. Yes, but we need also to have a solution, for, like the set of possible cases out of all
existing.
**Liudmila** 23:16 Yeah, we cannot define a new enum type in the code, because the type compatibility, it should be the same type as the parent. Well, we can have a
enum like class, and we can extend the class, and then it would work.
**Alexandra Konrad @Elastic Security** 23:33 Yeah, this is also what I thought about
struct, or a class like depending on the language.
**Jeremy Blythe** 23:47 So if I'm getting that right, you're saying that in Cogen, we.
the code that we generate can't exactly model what we're trying to express.
Yeah.
So we're saying familiar, because you're saying that
it doesn't make it doesn't make sense to make an individual enum
each time that it's an alteration from the original, you should have one enum.
That is, the superset of all variants.
**Liudmila** 24:18 Oh, I'm yeah. That's also not what I'm thinking is that the the to me that
the problem of okay, I have a list of 50 database system. But in this convention I only use this specific one.
It feels fundamentally different from the use case. Okay, I have an enum like CPU state or something.
and then it's slightly different, depending on. I don't know OS or the context. It's used in.
**Alexandra Konrad @Elastic Security** 24:53 Yeah.
**Liudmila** 24:59 And then the way we generate the let's say, dB, system is that
where we generate the big enum
from the base definition, and then are, we'll just
use the specific constant. We need to say, Okay, this, this enum.
It only has this specific value. It cannot have other values. And there's just one ever.
and then we just use it as a constant.
**Alexandra Konrad @Elastic Security** 25:33 Maybe we should split this problem actually. And because, like, they really look
different. One is, as you say, this is a constant, and you don't really need to know about all the possible cases available there, because you just use that only one for specific database or in in the hardware for the specific part of the hardware.
And it doesn't make sense to introduce. Like to have Enumeration Day. It's just that we don't have that const in semantic convention. Yeah. So we cannot define something, as Const does always have the same meaning. But because this would be useful, and that would solve this problem of from many to one.
But we still need to solve the problem of multiple values for different representations.
Oh, like such a.
**Liudmila** 26:32 I feel like, if we solve the Const problem, we will not need selected members thing, because if you
need to define additional, so you can always put
the common part and the base enum and
add members wherever you reference it. So you don't need to remove members
unless you only need the constant.
So instead of selected members, maybe we can figure out how to say, Okay, this is always
with that reports, Chris.
**Alexandra Konrad @Elastic Security** 27:23 Yeah, I understand what you mean.
Yeah, let let me write this in the ticket that this is essentially 2 problems. Yeah, that we're trying to solve, and maybe we should
solve them also differently, including Cogen.
**Liudmila** 27:47 Yeah.
But for the Cogen I kinda like Jeremy's proposal defining in inheriting enums.
When we generate an enum, we should not generate the language, the number should generate the
the one that can be expanded instead, a class that can be inherited as well.
**Jeremy Blythe** 28:38 So what are we saying about my use case? Where I've got 2 attributes?
They've got different names. The the attributes are different.
but they both use the same, you know.
So to today, say, I had an enum with a hundred members in it.
I would have to.
I'd have to maintain 100 member enums twice in this use case
and make sure that I don't make a mistake because I can't refer to.
I can't do this where I'm saying
I've got a state machine that has a thing called a current state, and the next State, and I want them both to be States in the State machine, and these are all the possible States.
**Alexandra Konrad @Elastic Security** 29:30 Intersects a bit of the data that we have.
or using the reference with the new name,
**Jeremy Blythe** 29:45 But these are 2 attributes.
**Alexandra Konrad @Elastic Security** 29:50 Yeah, this is like, probably came a bit later. We were discussing it last year, the embedded functionality where you can reuse the
already existing
class, or like it, could be a new one, could be just a field, etc. But under different name. And this is useful like I had an example for the file where you had diff like in the event. You have 2 files. One file is the file that is open, and another file, I think, is
a file to the past that opened this file to the process that opened the stuff. That's like something like this. And we couldn't solve this problem right now. In semantic convention, because we cannot
define 2 files under different names. So so you need to solve it a bit differently.
And.
**Liudmila** 30:53 I read it.
**Alexandra Konrad @Elastic Security** 30:53 There's.
**Liudmila** 30:54 I think it's super useful to define one enum. So the enum and or the type, and then reuse it. Jeremy, do you think like it looks like a change on top of this, right? It's a parallel
problem.
**Jeremy Blythe** 31:09 It is. Yeah. So the all yes, and all of the stuff that's up here to do with like how you might refine it. This is like.
these are instructions. These are like edit instructions to some sort of top level enum where you'd say, well, I want it to be like this, but edited in such a way that
it has this new member.
These members are removed, and I'm going to make a new type chord
some other enum. And that solves this case like the use case here.
But I think, yeah, in parallel.
it feels like it would be nice to be able to
actually define it as a type like you would in like in Codegen. What we're doing is we're pulling this out of here. And we're making a type where we could actually define the type.
**Liudmila** 32:02 So if we do this, I well.
long term, I kind of. I would much prefer write something more similar to quote than what we do today.
**Jeremy Blythe** 32:12 Yeah.
**Liudmila** 32:14 And in this way, like having separate type definitions from the attribute definitions is
awesome. And then, if we let's say we want to solve the problem of refinement. We would
essentially have an enum inheritance mechanism, right.
**Jeremy Blythe** 32:36 Basically because I think that's what we're defining here. Really.
**Liudmila** 32:40 Yeah.
**Alexandra Konrad @Elastic Security** 32:41 I think I have here even base class or no, I don't. Yeah.
**Liudmila** 32:53 I like this direction, actually.
And it brings us to the point where, like, I see, when people describe protocol and type in typescript, I actually want to write semantic conventions in typescript
in this weird something.
**Jeremy Blythe** 33:19 Okay. So the conclusion is then that
so Alexandra is going to.
You're gonna split the.
**Alexandra Konrad @Elastic Security** 33:40 Yeah, I, I split them in these 2 problems like the cons definition, when we just define one out of many. And the actual expansion
problem. Yeah, where we want to.
Have some base, maybe at attribute and expand it with additional members, or alter it with additional members.
**Liudmila** 34:11 I think, like the first, st the 1st problem, the constant. It's
at least in my experience. It may be 80% of all all cases where we need it.
**Alexandra Konrad @Elastic Security** 34:21 Yes.
**Jeremy Blythe** 34:21 Okay.
Okay.
alright, move on.
I don't know that there's gonna be much
Well, that was useful, because you've been wanting some feedback for a while. So
there we go. It was fortuitous that we're only the 3 of us here today. But I think the thing that's happening in Weaver right now is
we all seem to be really busy with other things. And so it's kind of tough trying to get these. This release to go out. Lauren's looking at it. Millie, you gave some feedback for Lauren
for the import stuff on the schema.
**Liudmila** 35:18 Yeah, just some docs and minor stuff. So if if you feel it holds the release back, I can approve, and we can
follow up.
**Jeremy Blythe** 35:28 No, I think I'm I think it should. It will take him like 5 min, so.
**Liudmila** 35:34 Okay.
**Jeremy Blythe** 35:36 That's fine, but I don't think that's we're in a bit of a.
My work is taking up like all my time right now, and I feel like that's the same for Josh.
That's clearly Lauren's not even his
in a bit of a in a bit of this of a lull. I I guess right now.
so I don't know. There's a great deal to talk about on that. And then the final thing you had from
last time was config. Is there enough audience here to
to go through that today, or should we defer again? What do you reckon.
**Liudmila** 36:15 Yeah, let's differ because we have a long debate with Lauren, and it would be not fair and not right to talk about it without him.
**Jeremy Blythe** 36:24 Yeah, okay, it looks like our discussion of of enum's meant that Gregor left. So
I prefer to think I had a conflict.
Alright. So I think I guess we'll just have a short one today, then. And this is.
there's anything else you wanted to bring up. Anyone.
**Liudmila** 36:53 No, I'm in Denver on the Ben Telemetry day. It's actually tomorrow there will be a talk about Weaver. I'll try to attend, and we'll see.
**Jeremy Blythe** 37:05 So! Who's giving that talk?
**Alexandra Konrad @Elastic Security** 37:06 In the cloud.
**Liudmila** 37:07 I don't know.
I'm sorry, Alexandra.
**Alexandra Konrad @Elastic Security** 37:11 Is it? Is it Lauren presenting, or.
**Liudmila** 37:14 No, it's just some person I've never heard of.
**Alexandra Konrad @Elastic Security** 37:17 Okay, interesting the one that never came to meetings, and like just who.
**Liudmila** 37:24 No, so dogs are enough. You see, we have good dogs.
**Jeremy Blythe** 37:29 Okay. So when when is that? Is that? Did you say today?
**Liudmila** 37:32 It's tomorrow. So.
**Jeremy Blythe** 37:33 Today.
**Liudmila** 37:34 There is some other stuff that I should be hitting forward.
**Jeremy Blythe** 37:39 Well, I'm intrigued to know whoever this mystery, whatever this mystery person says about Weaver, that'll be interesting.
**Liudmila** 37:47 Yeah, once I make my computer work, I'll share the link.
**Alexandra Konrad @Elastic Security** 37:52 Invite him to our meetings.
**Liudmila** 37:56 Yeah.
**Alexandra Konrad @Elastic Security** 37:57 Valuable contributor.
**Jeremy Blythe** 38:00 Yeah. Did you see the the blog post and the
The Youtube from what's his name?
Is it, Andrew? Anyway? I can't remember his name, but I think it's Andrew Gardner.
You know you did a whole.
**Liudmila** 38:15 Maybe that's this person.
Oh, no, no, no, I didn't see. Can you share the link.
**Jeremy Blythe** 38:21 Yeah, it was in. It's in the slack.
**Liudmila** 38:24 Oh, okay, I'll find it.
**Jeremy Blythe** 38:26 Yeah, yeah, he did a whole thing about live check.
**Liudmila** 38:31 Yay!
**Jeremy Blythe** 38:32 Yeah, it's pretty cool. There's a whole blog post. And then a Youtube video
going like, Look, do it. It's a cool thing. So.
**Liudmila** 38:40 Yeah, that's wonderful.
**Alexandra Konrad @Elastic Security** 38:43 It is Adam Gartner. Yeah, maybe this one.
**Jeremy Blythe** 38:48 Yeah. Yeah.
And he was inspired to do it. So I asked him, why, how did he do it? And he was inspired to do it, but from a conversation that we were having in that instrument instrument score slack
about that where you popped into that Lamilla, and you were like, hey? But there's this weaver thing.
He then went across and looked at it, and he liked it so much that he did a Youtube video.
**Liudmila** 39:10 Right. You see it, though.
**Jeremy Blythe** 39:12 Yeah, it's quite cool.
**Liudmila** 39:15 Yeah. The feature is super cool.
Okay, folks, I need to go great to see you.
**Jeremy Blythe** 39:21 Alright! Cheers.
**Alexandra Konrad @Elastic Security** 39:22 Thank you all.
**Liudmila** 39:23 Yeah.
**Jeremy Blythe** 39:24 Bye.
**Alexandra Konrad @Elastic Security** 39:25 Bye.
