SIG: Event WG
Date: 2025-11-18
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 04:48 Hello.
**Pellared** 04:52 Hello?
**Liudmila Molkova** 04:54 Sorry, I forgot about it.
I'm fine, thank you.
**Pellared** 04:58 It's fine, not sure if anyone else will join.
**Liudmila Molkova** 05:03 Let's see…
What are we working on?
**Pellared** 05:12 We are, or am I… Firstly, working on getting rid of jet lag.
**Liudmila Molkova** 05:31 And we can cut it short. I just want to see if… Or is something…
we can do? What… what should be the next steps?
Stabilize new attribute value types.
**Pellared** 05:51 Do you agree?
**Liudmila Molkova** 05:52 Huh.
**Pellared** 05:53 I just thought about talking what are the next steps that we want to basically, you know, take to make it happen.
And the second one, which I'm not sure is how much coupled is to it, is about the attribute limits to any value.
which are also… because I added, like, some, definition to the attribute limits, you know, for any attributes, but I'm not sure if there is, consensus, or even a compromise, compromise, or the thing that basically was defined in my PR.
So I also… and I'm also not sure if we can stabilize complex attributes without having this
you know, limits stable or not, I think it's a gray area, because this is mostly about behavioral changes, so I could imagine that, you know, SDK schools to commute in a way that would say that this can change.
But, yeah, it's a grey, grey area. Oh, trust me, do you know what I mean?
**Liudmila Molkova** 07:11 Hi, Trask.
**Pellared** 07:12 Hello, hello.
**Trask Stalnaker** 07:14 Can you hear me?
**Pellared** 07:17 I hear you.
Good.
**Trask Stalnaker** 07:20 Alright.
Sorry, I'm a little… Basey today.
**Liudmila Molkova** 07:28 So we're talking about stabilizing new attribute value types.
So just to remind myself, we are doing this so we can stabilize Logs SDK.
**Pellared** 07:45 So… forego it is… Not really needed.
In theory, we could basically create logs API SDK, which would not support it.
But, yeah, because we could add it entirely later, these types.
But I just… I just want to, you know, keep this moving forward, and I just want to ask you what are, you know, what are the plans? Do other languages want to support it, you know, in some experimental Java, for instance, or things like that?
basically was the plan for making this table. And also, I also said Ludamua that I'm also a little bit concerned about the attribute limits, so there's a second issue about stabilizing the attribute limits for any value.
And if they need to go stable together, or we can first stabilize just adding the new types, and then stabilizing the behavior of the limits themselves later.
probably a question that will probably be better answered by the TC, that's my guess. What are their opinions?
**Trask Stalnaker** 08:51 So, going in reverse order, the,
The limits… I think as long as the… if we are thinking the default limit is unlimited.
That could potentially come… Second.
I mean, it wouldn't be a breaking change.
**Liudmila Molkova** 09:13 It wouldn't. What could be is that if Somebody implements limits.
From regular attributes, unextended attributes in some funky way.
If we underspecify it, right?
then… once we introduce it, there could be breaking changes in weather.
**Pellared** 09:38 So, my PR already introduced the limits for this, just in a very simple way. So, if you go down to the bottom, there is this PR is mentioned, just, yeah…
Yeah, here… And if you go even to the changes, I think…
Or maybe… or maybe even… just… maybe even just find the document.
But yeah, if you, you know, just find the limit in file changes.
It's a common reason?
And here on the bottom… oh, yeah, that would be the easiest way.
The limbs are here, yes?
That's… weird. There should be some experimental things here.
I do not know what happened.
You're on my, you're on my, fork. This is not late.
That was strange.
**Liudmila Molkova** 10:47 Yeah.
**Pellared** 10:50 Yeah, so we have these attribute values here, and we have those four development bullets, which have been added.
Which defines how the limits will work for a byte array, for an array of any value, array for a map.
And the count limits how they should work for nested value pairs.
Basically, for attribute count limit, It's a no op.
Because it says that it applies only for top-level attributes.
For, for, for the attributes.
values, limits themselves, is basically, you know, value on the count, or all the values itself. I remember Tiger was asking about the key, the string of the key, but I said it's called even attribute of value.
count, so I just think that we just need to… yeah, I just propose that it goes to the leaves, and, you know, checks the attribute count of the leaves. I think it's the safest way. It's not an aggressive one, of course.
people can still overflow the memory, but that, yeah, that's what I proposed here.
**Liudmila Molkova** 11:57 Essentially, we already implemented this, right? It's just not stable.
**Pellared** 12:02 Yes, you're correct.
**Liudmila Molkova** 12:04 So should we close this issue to start with?
H?
Can we just close this issue?
**Pellared** 12:18 We can create another one for stabilizing it, or we can consider stabilizing
You know, attribute, but this one also establishing the attribute limit count.
Do you think it makes sense?
**Liudmila Molkova** 12:35 Yeah, and I think it's quite a… covers it.
I will probably…
**Pellared** 12:40 Probably it would be better to explicitly say that also, you know, the attribute values and limits
Yep.
And then we can close the other one.
**Liudmila Molkova** 13:05 Yay!
They're super productive, Roberts.
**Pellared** 13:11 Thank you.
**Liudmila Molkova** 13:12 Okay.
**Pellared** 13:12 You're helping me.
You close the issue.
**Liudmila Molkova** 13:17 That's how… that's for my home. Wonderful.
**Trask Stalnaker** 13:25 We're stabilizing, java, so on… I have a PR…
For supporting these in the incubating module.
Jack actually commented that he was hoping that we could just merge it straight into.
**Pellared** 13:46 Wow.
**Trask Stalnaker** 13:46 Stable.
I don't know we can't until Jan 15th anyways, because of, the 6 months after OTEP was merged.
So there's definitely interest. I did not implement… attribute limits, though. So…
I will add a comment on my PR that I need to do that.
**Liudmila Molkova** 14:41 Okay.
So then it…
**Pellared** 14:45 Regarding takes 6 months, in the OTAP, was it, like, a strong… Requirement, or just a recommendation?
It was…
**Trask Stalnaker** 14:55 This is one of the things that people fought for.
**Liudmila Molkova** 14:59 So…
**Trask Stalnaker** 15:00 I would prefer to honor that.
**Pellared** 15:04 Yeah, of course. I just want to be sure it is, you know, OTAP and all language specific, or it's mostly about Java, that Java wants to have, you know… Oh, it was in the OTAP.
**Trask Stalnaker** 15:16 It was to give back-ends
Point was to give back-ends time to…
Be ready to accept complex attributes.
**Pellared** 15:33 Mmm…
I see.
Okay.
**Trask Stalnaker** 15:46 Jan 15th is just around the corner.
With holidays.
It'll be here.
**Liudmila Molkova** 15:52 Given that…
**Trask Stalnaker** 15:53 No time.
**Liudmila Molkova** 15:53 Yes.
**Trask Stalnaker** 15:55 Yeah.
Like, if we get all our ducks in a row and we're ready to…
release on Jan 15th, that would be amazing.
**Liudmila Molkova** 16:07 Okay, so it means that,
This will be emerged and maybe released around January?
And… It also means that… We have to…
Right, the two implementations, Go and Java.
**Pellared** 16:31 Go is just a prototype, it won't be merged.
Because it's not stable.
**Trask Stalnaker** 16:36 Does… fine for… actually, we can use, yeah, we can use MyPR as one of the three prototypes.
Whether it is merged or not.
**Pellared** 16:47 But I think.
**Trask Stalnaker** 16:47 Yeah.
**Pellared** 16:47 stabilizing, like, needs to be, or I do not remember what was the agreement, or is there anything, you know, written in stone regarding stabilizing in the specification?
**Liudmila Molkova** 17:00 I think two implementations, or.
**Trask Stalnaker** 17:07 I think it's 3 implementations, but I…
I think it is a little… might be a little vague on what That means, like…
Because whether that can just be a branch, Or a PR…
I think there was… Something that he…
**Pellared** 17:27 I think there was some agreements that forego
a fork or PR is okay-ish, because in theory, someone can basically use a fork as a, you know, implementation. Nobody almost does it, which kind of
Release me?
**Trask Stalnaker** 17:48 Yeah, that's what I recall also.
**Liudmila Molkova** 17:56 Prototypes in three languages.
Good.
**Trask Stalnaker** 18:02 The third bullet down there, prototypes can be unmerged PRs.
**Pellared** 18:09 But this is just about… this is not about stability.
Yep.
This is just about anything.
**Trask Stalnaker** 18:18 Oh, okay, I see.
**Pellared** 18:22 So I am not sure if the rule is even defined.
**Liudmila Molkova** 18:26 I don't know.
**Trask Stalnaker** 18:28 It's first.
The bullet below there, prototypes can be unmerged PRs.
Right below, next one down, that one.
**Pellared** 18:38 Yeah, but this is not about stabilizing.
**Trask Stalnaker** 18:41 Yeah, yeah, I understand, but this is my recollection of our… Current practice, at least.
**Pellared** 18:50 to go.
**Trask Stalnaker** 18:50 For stabilizing is that they have to,
it needs buy-in. It's not just random prototypes, also, it's sort of like buy-in from the maintainers that it would be merged.
**Pellared** 19:04 Okay, that's fine, because… Nature Street will make it never stupid.
**Liudmila Molkova** 19:15 I'll follow up, with the TC folks. I, I, I have a vague memory of doing… of having
This discussion around stability, like, there is some special practices, and maybe we should just document them if they're not documented.
So… we need to re… We have Python.
Prototype from me that's approved.
And I can actually go ahead and polish it and,
Make it mergeable, back in the mergeable state.
**Trask Stalnaker** 19:56 Cool.
And did you implement attribute limits?
**Liudmila Molkova** 20:03 I think so.
I would imagine it would… it cannot be merged.
Either because of the same… Problem, but if it's approved, then… It might be good enough.
**Trask Stalnaker** 20:30 Yeah, I… I… That's my understanding, that it doesn't actually have to be… release.
As… because in some languages, that's…
**Pellared** 20:42 Copy and paste and do the same for Go.
**Liudmila Molkova** 20:49 Yeah, but don't make me work on Go.
**Pellared** 20:51 No, no, no, no.
**Liudmila Molkova** 20:53 Yeah. It's a joke.
Worst case, if we're merging it on January 15,
then we will stabilize… we should be able to stabilize in January. And realistically, I don't think we…
We would not stabilize in December anyway.
**Pellared** 21:17 End of December.
What's the day?
**Trask Stalnaker** 21:21 I think we can merge… I think we can stabilize the spec sooner.
Or at least we could.
make an argument for that. It's the SDK stabilization that
We need to honor that 6 months.
**Liudmila Molkova** 21:42 Oh, remember, there was this discussion that we should not stabilize API without SDK.
We, we went… throw it with the instrument enabled, right, or with something.
Robert, you probably know.
**Pellared** 22:03 I think for… I think for both Java, Go, not sure about ours, attributes are, like, on the API level.
Is it not?
**Trask Stalnaker** 22:12 And we have a… And we have a…
My prototype, at least, covers both.
API and SDK.
**Liudmila Molkova** 22:24 Right, okay, so let's try, right? So we can actually, create a PR,
that stabilizes things, we can, I don't know, draft it and see just what does it mean to stabilize everything around it.
And… but we can probably push for…
Start getting feedback on it, and collect. If anybody wants to push back, we will, well…
**Trask Stalnaker** 22:50 Does your, does the Python prototype, do cover OTLP exporting?
**Liudmila Molkova** 22:59 Yes, it should.
**Trask Stalnaker** 23:02 Awesome.
**Liudmila Molkova** 23:15 There is nothing in the RTLP that changed. It was the API SDK problem for Python, anyway.
**Trask Stalnaker** 23:27 Oh, did you already have an any value?
**Liudmila Molkova** 23:32 Prologs, yeah.
**Trask Stalnaker** 23:35 Right.
**Liudmila Molkova** 23:52 I think, before stabilizing, we need to…
polish the wording. Like, based on today's discussion and the spec, there is a lot we can do to improve wording in the current spec.
**Pellared** 24:12 What do you mean, precisely?
**Liudmila Molkova** 24:16 So, currently, what we say Is misleading, the issue you brought up on the speckle.
**Pellared** 24:24 But this is regarding logs API end user, and this is only about complex attributes. I think these are orthogonal things.
**Liudmila Molkova** 24:31 Oh, I see, I see.
**Pellared** 24:33 We'll work on it as well, but in parallel.
**Liudmila Molkova** 24:35 I see, okay, sorry, I…
**Pellared** 24:37 This can be applicable, you know, for spans, metrics, and even for the bridges, if people have bridges right now.
Break, yeah, okay.
**Liudmila Molkova** 24:48 I see, so essentially, what you want first, we're not talking about the log stability, but just the extended attributes, the complex attributes everywhere stability. I see, okay.
**Pellared** 24:57 Thank you.
I also think, based on discussions, that for the confusing part, it's mostly about, you know, improving clarity and specification. I don't think we will…
at anything.
you know.
controversial thing. Regarding, you know, specification and compliance, I think you can just add a sentence like, a language may
add additional friendly… user-friendly logging API.
If the existing one is not convenient for the end user.
So, for the opt-in feature, basically, because I am not sure that even we need one for Go. Basically, I would prefer first people try using directly Go's API, and adding it if, you know, people will be unhappy with it.
For sure, for Java, it will be very handy as far as the Java API. I think people would want it if…
They'll be wanting to visit directly.
And also improving this README about the use cases which Josh described, when you want to reuse it, when not, etc.
So it's more about clarity, because right now it's… yeah, I agree, it's confusing.
**Liudmila Molkova** 26:18 Cool.
**Pellared** 26:20 Also, maybe, trust, because you're also a Java maintainer, to Jack's point regarding configuration.
I added it also to the specification doc. The thing is that different languages have different powers regarding the configurability in the logging libraries.
So, you know, there are logged for J, log for NAT. Also, similar thing is for Rust, which is very powerful, but not each ecosystem has this. For instance, Go doesn't have anything like that. And also, I think that the long-end user journey
It will be that people would use, you know, the declarative config for configuring all, you know, metrics, tracing, and logs as well.
And the developer would just, you know, be concentrated on a meeting telemetry.
and someone, some SRE will be, you know, concentrated on declar… or using the declarative construct to figure out what are the pipelines.
Can you hear me, or has my connection dropped? Okay, because you were frozen. I was not sure if you were listening to me, or is my connection broken? Yeah.
**Trask Stalnaker** 27:30 Yeah, no, sorry, a little frozen by the whole conversation, spec conversation, today,
I…
**Pellared** 27:48 No, no, actually, it's just, you know.
**Trask Stalnaker** 27:51 Yeah, I… I think it's a… this is a long-term journey.
**Pellared** 27:57 migration story. Yes, this is a migration story, and yeah.
**Trask Stalnaker** 28:00 Yeah, and even… even where…
where we end up with OpenTelemetry logging. I… I can definitely see…
A future where people want, you know, would really
want to do everything in the declarative config for… where people start thinking of logs as telemetry more, and they want that to all be under open telemetry and declarative config, and, not have also
Log4J, or log back, or whatever.
But I feel like that is… Yeah…
And we may or may not… that may or may not evolve. I don't…
I think that we need to push.
in that direction, I think we kind of need to listen for feedback on if that is a direction that
users want… that people want to take the OpenTelemetry project in.
At the same time, as you said, I think it's totally fine for… languages to…
Take small steps to make that story work better for users who want it.
Jack was already asking in the Java chat about adding more… Sugar, Around our log API.
So, I think…
I think all of those things can be true, and I don't feel like we need to, like, put a pin in it of the, like, nail it down of, this is what we are doing.
**Pellared** 29:56 Yes.
**Trask Stalnaker** 29:56 once and for all, like, I think…
**Pellared** 30:01 But I also know I…
**Trask Stalnaker** 30:04 on the spectrum of living with… living in the gray areas, or living in… with ambiguity, that's something I'm very comfortable with.
And there's a spectrum, right? And so…
I'm trying to respect that as well, but I'm totally fine with the ambiguity of…
that we don't know exactly how this is all gonna play out today, and I don't feel like we should…
Push to define exactly how it's gonna play out.
While keeping the options open and allowing multiple things to evolve.
**Pellared** 30:51 Yeah, I'm with you here.
Okay.
**Trask Stalnaker** 30:56 Just to cover Riley's point about, like, what do we say when people ask us for a recommendation?
I don't think we need to make a recommendation, I think we need to give them pros and cons.
**Pellared** 31:10 Exactly.
**Trask Stalnaker** 31:11 Wait.
**Pellared** 31:11 What are the trade-offs? Exactly, so I agree.
**Trask Stalnaker** 31:17 At this point, at least, given that there are so many… there are a lot of trade-offs, we can't… you know, like, if somebody asks us what tracing solution they should use.
**Pellared** 31:26 I think…
**Trask Stalnaker** 31:27 We have an obvious answer.
**Pellared** 31:28 I think even… our common, our current README for logs.
It's kind of structured like that, that it…
provides different options, and try to describe what are the benefits and cons of each of them. Because there's also the description of getting from the, from the files by the collector, etc, you know, like the fluent bit kind of stuff, so I think… I think
I think it can even play well to describe it, even right now, into the README. You know, what are the possibilities and what are the trade-offs.
So yeah, I will try to work on it.
do my best.
ChatGPT or Copilot will help with this journey.
**Liudmila Molkova** 32:12 We have Copilot as one of…
**Trask Stalnaker** 32:17 Such a blessing for, I would assure for people who are not native English speakers.
I mean, it's a blessing for me, I hate writing stuff.
Anyways… But even Polish, writing Polish is also difficult.
**Pellared** 32:39 Okay.
Shall we go further?
Oh, you want to add something to the mirror?
**Liudmila Molkova** 32:46 Let's go further.
We… Have our login board.
**Pellared** 33:03 I try to make it up-to-date, so we can, you know, for instance, each month.
To discuss the things and priorities. You know, look at the, you know, stuff on the left column, and decide if they're important, if we should close it, if we should work on it, etc.
So, the things in progress, I think, are actually in progress.
Yes, I want to discuss quickly the last PR in progress, the last one. I have forgotten about it.
**Liudmila Molkova** 33:36 This one?
**Pellared** 33:37 Yes.
There's one, opened conversation.
**Liudmila Molkova** 34:20 So I think that the… Discussion here is around whether
semantic conventions, events should Have a buddy.
**Pellared** 34:35 Exactly.
That's correct.
**Liudmila Molkova** 34:40 And I think we all think that they should not.
**Pellared** 34:44 Yes, initially we thought it is, but we are all leaning to that it should not.
That's exactly what…
I think it's just the event name and the attributes. These are what we should have in the conventions, and it will be basically following the same pattern which we have for metrics and spans.
And we'll have the tooling, also.
**Liudmila Molkova** 35:06 The confusion here, the only reason we have this discussion is that
Sija… okay, so Sija thinks that… okay, if they would define events in Rust, that…
These events might also have the body, which is human-readable to ring.
**Pellared** 35:26 Which is fine, it is optional.
I don't think we need to…
Say, or do you want to discourage using it?
There's chunky!
What's cup.
I think that in semantic conventions, we just should say what should be used. In my opinion, we should have that event name should be used, severity number should be used, and attributes should be used. I think severity text is also potentially, you know.
something which can be a boilerplate, body can also be a boilerplate, but if someone has reasons to use them, because they can, I don't know, add some, you know, human-readable, for its severity level, if there's some reason to add the body for a severity exception, or whatever.
I'm not sure if we have…
Right now, if we're in the position that we know what… if these recommendations of not using them would be good.
**Liudmila Molkova** 36:20 Yeah, so what we had in the past is we didn't talk about the body, right, at all. We didn't explicitly.
**Pellared** 36:27 We did.
**Liudmila Molkova** 36:28 should not.
**Pellared** 36:29 It was 3031.
**Liudmila Molkova** 36:35 No, we're…
**Pellared** 36:36 Type of the body, and we want to get rid of this one.
**Liudmila Molkova** 36:41 Now wait, so if I have an event, and it has a buddy for whatever reason.
The event name should… You should not have…
Two different events with the same name, but different incompatible types of the body, right?
If one of them is…
**Pellared** 37:02 And this is why I'm not sure. What if there's something coming from different languages? If it's a problem?
**Trask Stalnaker** 37:12 Then it's not a semantic.
convention.
**Pellared** 37:17 I mean that, the body couldn't send, for example, a raw event.
And the attributes can have it, you know, like, parsed and converted.
Like, for exceptions, for instance.
That should lay a sweep off.
**Liudmila Molkova** 37:31 For exceptions, we would define, I don't know, if we would ever… no, let's not go there.
**Pellared** 37:36 Yeah, but…
**Liudmila Molkova** 37:37 We are not going to have buddy for exceptions, because we don't.
**Pellared** 37:40 Okay.
Okay, yeah, that's true.
**Trask Stalnaker** 37:46 Yeah, I think both things can be true.
Right, we can… Discourage using the body, should not use body.
And if you do happen to use body… The event name still… Uniquely defines the structure.
**Liudmila Molkova** 38:12 I think to address CJ's concern.
You can just say that events defined in semantic con… open telemetry semantic conventions, events should not use body.
**Pellared** 38:29 Then, if it will not, then how will you know what type would you use for the body?
**Liudmila Molkova** 38:36 So you can, you just shouldn't.
Like, you can define hardcode generality attributes on metrics, you just shouldn't…
**Pellared** 38:45 No, no, I mean something else, I mean…
Okay, now I think I follow.
You mean that this rule should be only for the open telemetry semantic conventions?
**Liudmila Molkova** 39:00 Yeah, this document is for semantic conventions.
**Pellared** 39:08 These are cities, right?
I think there are two things here. One, these are, you know, semantic conventions, like general practices, which we recommend also to, you know, for custom things.
And second thing is the semantic conventions which we put here. So my question is, is it only a rule for the semantic conventions that are applied in this repository, or if it is a guideline that is applicable for all, you know, even custom semantic conventions?
**Liudmila Molkova** 39:39 So I think this is definitely applicable to semantic conventions defined here. Once we start defining semantic conventions in, let's say, Rust, the Rust-specific semantic conventions, I think they should use them as a default.
What we have here.
They might deviate somewhere, but this is the starting point.
Users and their applications.
I…
They can use it as a best practice, but they're not obliged to follow in any way. That's true.
**Pellared** 40:13 That's true. Okay, so, you all think that body should not be used, that we do not recommend using body.
**Trask Stalnaker** 40:24 The only… yeah, I mean, the… if you scroll down to see Joe's example.
So… Is the… is this just supposed to be, like, a…
A user-friendly, like, a human-readable version in the message?
**Pellared** 40:48 Right, like, I don't…
**Liudmila Molkova** 40:57 My impression that it's just a human readable.
**Trask Stalnaker** 41:01 Yeah.
**Pellared** 41:02 a waste.
**Trask Stalnaker** 41:07 Did you know we have this somewhere… Let me discuss… a…
Maybe it wasn't on logs, I don't remember.
**Liudmila Molkova** 41:21 I remember we discussed that log bridges should definitely put messages.
**Pellared** 41:28 Yes.
**Liudmila Molkova** 41:28 into the body. So the thing she just talking about is a combination of an event, And log.
**Trask Stalnaker** 41:45 Oh, we had something called, like, we were thinking of, like, event.summary at one point?
Something that… event.description, something that would be, like, like, something that could…
bridge us back into Log World, like, if people wanted to have, you know, something to show what the event looks like in a single line.
**Pellared** 42:12 Like a matrix, like a metric description.
Instrument description, I see.
**Liudmila Molkova** 42:17 But…
**Trask Stalnaker** 42:19 Maybe.
**Liudmila Molkova** 42:20 In theory, like, you can look at events as logs.
And… Why would you use event.summary for events and body for logs if it's the same?
Bing.
**Trask Stalnaker** 42:42 at this point.
I'll share the… I was just trying to… Refresh my memory about… Why we were…
Considering event dot… Summary, event.message, event.description…
**Pellared** 43:28 The attending message is redundant, yeah, I was worried about it.
Optional property.
**Liudmila Molkova** 44:34 I don't think we have any conclusion on this one.
**Pellared** 44:38 I will say that most people saw that if someone would want it, then the preference was to have an attribute, and it should be an opt-in.
Because it's an additional noise on the wire.
**Liudmila Molkova** 44:54 I mean, yeah, but, like, this is… this is a good example. So this thing CJ is creating here, it serves two purposes. Like, it's intended for human beings as a debugging mechanism, right?
If it was a common line, too, it would definitely… would go to STD out, regardless. Like, humans should see this.
Right? And the fact that it has a name, it's almost…
Accidental. It's actually a log, but it also has a name.
**Trask Stalnaker** 45:30 But it's serving two different purposes.
I think.
One is… the human log… Viewer, and the other is… Alert.
**Pellared** 45:42 Controls with the system, yeah.
**Liudmila Molkova** 45:44 Right, they are, like, redundant, so they represent the same thing, like, name and the.
**Trask Stalnaker** 45:50 To two different consumers.
**Liudmila Molkova** 45:52 Yes, okay.
**Pellared** 45:54 Like, I think that… you know, beckons…
Call, if the semantic conventions have a description.
Basically, you know, the backends could, you know, produce and say, you know, basically emit those human-readable things on the backends without having sent them on the wire.
You just think we throw a little buffer?
**Liudmila Molkova** 46:17 Yeah, but yeah.
That could be.
Like a localization, for example, you can localize the message.
**Pellared** 46:26 In theory, in theory, there could be even, you know, a processor in the SDD auto-exporter which does it.
It doesn't have to be in the record itself.
**Liudmila Molkova** 46:37 It doesn't have to be, but yeah. So, like.
And for these things, the body is…
the string clog body intended for humans. It's a different representation of the event itself.
**Pellared** 46:53 Yep.
**Liudmila Molkova** 47:03 I kind of…
**Trask Stalnaker** 47:04 Combination event log.
**Liudmila Molkova** 47:12 I kinda don't want to specify it, though, and I think should not…
is good enough. Most of semantic convention events would be…
Better to start without a body.
annually.
**Trask Stalnaker** 47:34 Yeah, I think…
I agree, and, you know, we can even say that, you know, to see Joe, that, like, we would consider layering in some sort of
human-readable.
opt-in.
Option, and that… Whether that goes… gets stored as an attribute, like event description, event summary, or…
In the log body.
I mean, I don't… We could still debate that later.
**Liudmila Molkova** 48:17 So, we keep… this one.
This one.
Attributes, body.
**Trask Stalnaker** 48:29 Oh, yes, it's in there already. Cool.
**Liudmila Molkova** 48:32 Yeah.
Attributes should be used, should not use body.
**Pellared** 48:41 I just have a question.
If we are only… if we only want to use…
Attributes and not use a body.
Do we really need to say that the evidence… the type of the body is important? Because we do not care.
Is it really important?
Relevant.
**Trask Stalnaker** 49:03 But we're not saying must not use body. If we were saying must not use body, then…
I don't think we would.
**Pellared** 49:11 We cannot say must not, because the record anyone has this field, so anyone can use it anyway. The thing is, if it's a problem, if someone uses it, and we have different types.
Do we need the backends to, you know, kind of make sure and process and stores that are of the same type, if there… we do not have any conventions for it?
**Trask Stalnaker** 49:32 We don't even… we're not even suggesting that backends do validation of the event structure. Like, we're not… I don't think we're saying that backends should reject
telemetry. This is more targeted for instrumentation authors of what they should
Emit, what good telemetry looks like.
Not what any telemetry looks like.
**Pellared** 50:02 Okay, but given we say that the body type is important, does it mean that, in my opinion, it would mean that in each semantic conversion, would you need to say that type of the body is
Like, n-none.
**Liudmila Molkova** 50:21 Sure.
**Pellared** 50:21 And…
**Liudmila Molkova** 50:22 Which is equivalent.
**Pellared** 50:24 No, no, like, none type of the value is none, basically. We are setting none value.
This is the title.
**Trask Stalnaker** 50:32 I mean, that should be the default.
That should be the default for all the semantic conventions, yes.
**Pellared** 50:40 Okay.
If we're good with it, then it's fine.
**Liudmila Molkova** 50:48 So the text we have here, it seems good enough, it's just maybe it would be useful to just say that it applies to semantic conventions alters.
Like, like, what do we… Oh, maybe, oh, maybe this can be improved, right?
**Trask Stalnaker** 51:10 Yeah.
**Liudmila Molkova** 51:10 Because we are saying must document.
**Pellared** 51:16 And what would you… what you would like to improve here?
**Liudmila Molkova** 51:20 So we… they don't… they don't… they are… don't have to document the type of the body.
**Pellared** 51:27 I disagree. If it's the same structure, then it must be
defined. Otherwise, you are not sure, you're not able to make sure that it will be consistent across different implementations. If we say that… Yep.
**Liudmila Molkova** 51:43 what Trask is saying, that there is a default, none.
**Pellared** 51:47 It's never described… it's not described anywhere.
**Liudmila Molkova** 51:53 It could be, so, like, the tooling can take care of it, it's just some… .
**Pellared** 52:00 Then the… then the tooling will describe it.
**Liudmila Molkova** 52:08 So, Chair said, even if the tooling provides a default.
By not specifying it, you're documenting it anyway.
**Trask Stalnaker** 52:17 But Robert, we don't defy, like, in semantic conventions, we don't… Comprehensively list every single… field…
**Pellared** 52:28 But that's also why… yeah, yeah, I agree, this is also why I put this if-any in parentheses.
For the body.
Yeah, I understand.
If it's not listed, then it means that there's none.
**Trask Stalnaker** 52:54 I mean, I guess the question… I guess the argument could be made that if you do add a body.
Does it now not follow that semantic convention?
**Pellared** 53:05 I think it will not.
Because it would be a different structure.
That's why I was…
thinking about, you know, removing this kind of body information from the definition of, you know, of structure, that it needs to be the same.
**Trask Stalnaker** 53:41 We could say the body is… The default is none.
If it's not defined.
**Liudmila Molkova** 53:58 Maybe we do this, because we don't have to list everything that… Here.
Must document the event name and its attributes.
**Trask Stalnaker** 54:11 I think this is…
**Pellared** 54:12 I see proposed…
**Trask Stalnaker** 54:13 and then…
**Pellared** 54:15 I still think we can… Get rid of, you know, type of the body.
I think we just need name and attributes. I'm not sure if we really needed this body.
We have no examples when it will be needed.
**Liudmila Molkova** 54:37 I mean, we can remove any mention of the body from this document, but that it's equivalent to people coming and asking us questions, should I use body? And when should I use body?
And without the answer, you shouldn't, probably.
**Pellared** 54:51 Yeah, so we have… we have this information already that you should not use it. It's in a bullet point, so I would keep it.
I just suggest removing the body from other places, so it even further discourages using body.
That is basically meaningless in our… in the semantics.
**Liudmila Molkova** 55:10 In the semantics, okay, I agree with you. In the semantics, yes. I think what we have here, we should have something for…
events here.
Event name.
Class diversion should uniquely to both attributes and body.
So, okay, maybe we can remove it from the semantic conventions.
That's fine.
**Pellared** 55:38 This will be a breakthrough.
**Liudmila Molkova** 55:39 But we… we should not remove it from the spec. The cement.
**Pellared** 55:42 You're right.
**Liudmila Molkova** 55:43 are opinionated, right? SPAC is not.
**Pellared** 55:46 Yes.
**Trask Stalnaker** 55:47 Yep.
**Pellared** 55:48 Yeah, I was not aware that it's here.
It's shools, but yeah.
**Liudmila Molkova** 55:59 Okay, so then, so the agreement is, let's remove body, mentions… Of the body from… some conf…
**Pellared** 56:16 Maybe attitude, CGS, suggestions… What do you think?
**Liudmila Molkova** 56:23 Okay.
**Pellared** 56:24 Just a summary here.
**Liudmila Molkova** 56:37 Oh my gosh.
Okay.
**Pellared** 57:38 I think we can also add information, then, for human-readable information…
We… one could add, event description attribute.
And that it will be done on some, you know, processor level, or on the backend. It does not have to be even done on the, you know, on a meeting group record.
And we are running out of time.
**Trask Stalnaker** 58:16 Type fast.
**Pellared** 58:21 You cannot post it after, you know, after the time you don't.
**Liudmila Molkova** 58:26 Okay, I can, actually.
I will finish writing it down. We don't have to… you don't have to see my embarrassing typing.
**Pellared** 58:39 Is there anything else that we should work on for this week? Anything that you want to bring up?
**Liudmila Molkova** 58:46 I think we have enough to work on.
**Trask Stalnaker** 58:48 No, we did.
**Liudmila Molkova** 58:49 I do.
**Trask Stalnaker** 58:49 Did good today. Yeah.
**Liudmila Molkova** 58:51 Yeah.
**Pellared** 58:53 It's close.
**Trask Stalnaker** 58:54 We're gonna go implement attribute limits.
**Pellared** 58:57 Yay!
**Trask Stalnaker** 58:58 VR.
**Pellared** 58:59 Good luck! See you!
**Liudmila Molkova** 59:00 See you.
