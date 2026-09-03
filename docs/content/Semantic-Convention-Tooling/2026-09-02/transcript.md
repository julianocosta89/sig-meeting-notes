SIG: Semantic Convention Tooling
Date: 2026-09-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Arianna Vespri (OllyGarden)** 00:49 Hello?
How are you all good?
**Josh Suereth (Google LLC)** 00:54 Yeah, yeah, just been… been busy.
**Arianna Vespri (OllyGarden)** 00:57 Yeah, yeah, I know the feeling.
**Josh Suereth (Google LLC)** 01:01 I feel like all I do is code review at this point, you know?
**Arianna Vespri (OllyGarden)** 01:05 Yeah, yeah.
Sorry for not, using the video, but I'm, like, I've just moved in a new place, so it's, like, also the internet connection is not… sorry.
**Josh Suereth (Google LLC)** 01:14 No worries at all. Like, that is not something that has ever bothered me.
**Arianna Vespri (OllyGarden)** 01:19 Okay.
**Josh Suereth (Google LLC)** 01:20 Yeah, like, I know everyone has their own comfort level with video, and not a problem.
**Arianna Vespri (OllyGarden)** 01:26 No, normally it's okay, it's really just a technical thing, but yeah, I agree on what you said.
**Josh Suereth (Google LLC)** 01:32 Yeah, so, like, I wouldn't… I wouldn't even, like, ask, generally, you know, because, like, sometimes it's a… it's a thing, and sometimes it's not. And… It doesn't matter, really.
**Arianna Vespri (OllyGarden)** 01:41 Yeah.
**Josh Suereth (Google LLC)** 01:42 Participating, that's what matters, yeah.
**Arianna Vespri (OllyGarden)** 01:44 Yeah.
**Josh Suereth (Google LLC)** 01:46 Cool.
We want to cut a release… Merge V1, V2, split.
with, cload and fix… Running in upstream.
Tips now… okay, do we… do you want us to talk about your pool requests?
**Arianna Vespri (OllyGarden)** 02:13 I, like, I have lots of merge conflicts right now, so…
**Josh Suereth (Google LLC)** 02:18 I know, I know, you might want to… like, I would actually… I would think about moving your pull request into, like, a new branch, or… yeah, sorry, what… we made a decision last week to cut V1 and V2 apart.
**Arianna Vespri (OllyGarden)** 02:34 Yes, but I started… I started, like, I started working on them, so it's… it's gonna be okay. I mean, it's… it's not… if I really see that it's really, really, really, really impossible, then maybe I can… But one thing that I wanted… one thing that I wanted to ask, and it's just very loosely related, is that Now that we have the videos on the Linux Foundation thing, where do we find the recordings?
**Josh Suereth (Google LLC)** 03:02 That's actually a problem. We lost them.
**Arianna Vespri (OllyGarden)** 03:06 Oh, okay, so it's not just me, like, unable… okay.
Okay, that's really appealing. Sometimes it's really useful to, like, go back to what was told, live, and okay, but at least I know it's just Not me, not finding things.
**Josh Suereth (Google LLC)** 03:29 Yep, it's not you.
Okay, I'm not presenting, am I?
**Arianna Vespri (OllyGarden)** 03:57 No, I cannot see anything.
**Josh Suereth (Google LLC)** 03:59 Okay, let me… let me do that. I… Yeah. I was actually just searching to see if I had any information about the videos, and I don't.
So that might be something we want to ask the governance committee. There's probably someone trying to figure it out.
But I didn't… I didn't see anything.
Okay, and then I'm gonna ping on Slack to see if anyone else is able to join today.
Okay, Ludmila will be 15 minutes late.
If not, we can talk through your PR if you have any, like, questions. I did review it, by the way, like, briefly, but it was still in draft, so I didn't make comments yet.
Because I didn't see anything actually worth commenting on, like, that I had problems with, it looked fine.
Do you want to talk through that at all, or do you… or would it be better for us to spend time on other things?
Because, yeah, you added links.
And I think links were… convert, spam, link, attribute, right?
It was all the kind of mechanical things. Where's Link?
It's under spin… Yeah, has a signal ID… Requirement level… Oh, this is… this is one… Right, so the main feedback I had, which I didn't know how to phrase, because I didn't look at the rest of this, you have span links implemented all the way through Infer.
Forge, and… did you do Weaver Live Check?
Oh, you're muted now, Arianna.
**Arianna Vespri (OllyGarden)** 06:24 Sorry. The thing with infer is that because otherwise it wouldn't compile.
**Josh Suereth (Google LLC)** 06:29 Oh, yeah, yeah, no, no, I know, I know.
So, that's fine, and, like, Infer, we can hook it up, but you haven't done live check, right?
**Arianna Vespri (OllyGarden)** 06:36 I don't think so, let me… Okay.
**Josh Suereth (Google LLC)** 06:39 I didn't… I didn't see it in here.
I don't think you have to do live check in the first PR, by the way.
**Arianna Vespri (OllyGarden)** 06:46 Yeah, I mean, this was the thing that, you know, as I told you, this is gonna be more than one PR, for sure.
100%. Yeah.
**Josh Suereth (Google LLC)** 06:53 The reason I mention it, though, is the hard question to ask here… like, there's two questions we ask, generally, around models. The first one is, how do I do code gen?
And I think, like, that is fully answered with what you have here for SpanLink.
The second one is, how do I do live check without having, like, spurious failures or spurious warnings?
**Arianna Vespri (OllyGarden)** 07:16 Yeah.
**Josh Suereth (Google LLC)** 07:16 And that's one that I don't… I don't know what the answer is here.
And I was gonna… I… like, I can wait until the live check codes get… gets written, because we can always update this like, it's not… we're not locked in stone yet for free… for our syntax, right? So we can evolve it.
**Arianna Vespri (OllyGarden)** 07:33 Yes.
**Josh Suereth (Google LLC)** 07:35 But that was, like, my only feedback on this PR was, that was something to think through of how that would work, or briefly sketch it out.
**Arianna Vespri (OllyGarden)** 07:45 Yeah, because of course, it's something you have to keep on the back of your mind, because it, you know, it might influence how you do things, even in the first PR.
**Josh Suereth (Google LLC)** 07:53 Exactly, exactly. So for me, it's more, do I have enough confidence that I can implement LiveCheck with this definition? And, you know, the main thing there is basically, I get a span in OTLP, How do I tie the correct span link definition in Weaver, so that I know this span has the span, like, I think you have what you need with this ref. Like, I think this is enough, but I didn't have enough time to think through it in depth, so I wasn't sure if you had done that yet or not. That's kind of my only real feedback.
**Arianna Vespri (OllyGarden)** 08:26 I mean, like, I, you know, I thought about that, but then it's like, as I said, I thought that the, like, the first kind of batch of things that I pushed, I thought that it was already, like, in a good state, but then, but then, like, you know, I went through it again and everything, and it was really… like, as I said, it was, like, at the resolve stage, it was rejecting the things that it was supposed… it was promising that it would have… Would have added. So, and so… I'm… then with all these merge conflicts, my god, I have left to move things around, so I'm really not sure about a lot of things right now.
**Josh Suereth (Google LLC)** 09:13 Yeah, I think… so, I mean, the thing that sucks here, the merge conflicts, what we tried to do is make it so you can add this to V2, And V1 is kind of a completely separate… so SemConf had source, where, like, group and registry are here. These moved into a V2 folder.
**Arianna Vespri (OllyGarden)** 09:34 Yes.
**Josh Suereth (Google LLC)** 09:34 Or, sorry, V1 folder. And we're trying to be very crisp and clear of when we're on V1 versus when we're on V2, because right now, to implement this, you have to… and you can see the code in here, right, where span link shows up also.
**Arianna Vespri (OllyGarden)** 09:48 It's convoluted.
**Josh Suereth (Google LLC)** 09:49 Yeah, as kind of, like, a hidden thing, because you have to go through the resolver, and that sucks. It's, like, really awful to work with. So, what we're trying to do is actually completely split V1 and V2, so as soon as we can deprecate and remove V1, we have a clean slate. We can just, like, drop those things, and yeah. So that, that was what that refactoring is that hit you. So Paul, you can blame me for that, Paula.
**Arianna Vespri (OllyGarden)** 10:15 But no, that's good, that's actually good, because actually I got… because actually, you know, I got confused when I was first working on this, because, you know, you told me, rightly, you know, this is just for V2. But then, I was like, yeah, but in order to do it for V2, I also have to change code, that it looks like I'm doing it for V1. And then I was like, yeah, but… but what he meant… but what he meant is that it should be, like, user-facing V2, then what happens under the hood is you do whatever, you know, you need to make things compile. And that's why also I wanted… I wanted to retrieve the video.
But also because, you know, the thing is, when you, when you, check, you know, when you, when you log in, into Zoom through the, now, the Linux Foundation thing, they, they, they tell you, if you, if you log in, you know, with your credentials, not as a guest, then you have access to the videos.
So there's really something going on there, you know.
Sorry.
**Josh Suereth (Google LLC)** 11:11 Yeah, that's weird. Yeah, I mean, there might… there might be video… it was documented on the community repo when we were using our own thing, but I don't know… what it would be now, you know? Like, I have no idea. Exactly.
**Arianna Vespri (OllyGarden)** 11:26 No, no, there's nothing there, there's, like, there's nothing there. I mean, there's the old stuff, but there's nothing, since they, yeah, in any case, sorry. But, yeah, but I mean, I'm actually very happy that you, that you did this separation, because it's, like.
like, from… it's just, like, the logical thing to do, so…
**Josh Suereth (Google LLC)** 11:45 Well, yeah, the separation I did was the first part. I will wait on the rest until this lands, I think, but the, Right now, you're still gonna have to do this shenanigan of this, like, hidden field, right? Where you skip serializing, you have to have it in V1, Resolver works with it. The next thing I want to do is actually… Take the resolver and have it work on, Where's… yeah, all… where's your… did you make resolver changes? I don't think you had to, because you just had to do the V1 and the V2.
Oh, no, you did, yeah. We did.
My next… the next thing that I need to do, now that V1 and V2 have a hard separation, is in Resolver, you know how we have, I can show you.
We have these, like, group summary things.
**Arianna Vespri (OllyGarden)** 12:35 Yes.
**Josh Suereth (Google LLC)** 12:36 Which is generic, and then we have a thing that pulls group summaries from V1, and a thing that pulls them from V2. The next thing I want to do is actually get Resolver fully ripped away from V1 and V2, if possible, if feasible.
So that we have a more clear idea of what's going on. I mean, the… The reality is, it's pretty nested right now, and we would break users if we get rid of V1.
but, yeah, this code here is really awful to maintain.
**Arianna Vespri (OllyGarden)** 13:09 Yes.
**Josh Suereth (Google LLC)** 13:10 and debug. It's really frustrating. So that's where I think it… it… we really want to, like, clean this up and make it more clear what's going on.
Yeah, so… I'm hoping to work on that in a little bit, but for now, we decided… we had a whole bunch of bugs with V1 and V2 where we weren't being explicit, so, if I were to show you… The basic gist now is, we have a set of rules.
If you look at a crate, Right?
**Arianna Vespri (OllyGarden)** 13:45 Yes.
**Josh Suereth (Google LLC)** 13:46 Weaver Semkov.
**Arianna Vespri (OllyGarden)** 13:48 Yes.
**Josh Suereth (Google LLC)** 13:50 V1, there should be no import of a V2 thing in V1, right now.
The things that we hide, we actually put as, like, private stuff, if I recall correctly. So where do we have… Attribute group visibility shows up here.
And we… as a V1 thing, oh, come on, what are you doing? Attribute group visibility spec. Okay.
And we do have the skip serializing, and we'd say that it's only used to convert.
So, it does, like, you will be duplicating things in V1 and V2 for Resolver for now, which sucks, but that is what it is.
**Arianna Vespri (OllyGarden)** 14:35 Okay.
**Josh Suereth (Google LLC)** 14:36 And then the resolver only works on this schema.
Effectively, and converts things down into, like, into V1.
And then there's the, the conversion things. So then there's always a convert.
**Arianna Vespri (OllyGarden)** 14:51 Yes.
**Josh Suereth (Google LLC)** 14:51 in V2, and you need to get to V1, there's a way to convert between them, so it's always in this convert thing.
And then every crate consistently has this for you to deal with the pain of having two versions. So if we go to Resolved schema, like the published one, right, it has the same structure. You have a convert, which can convert from V1 to V2, or from V2 to V1. I think this one only does V1 to V2, yeah.
But this is where all the conversions are, and then in, in V1 and V2, it's the same thing where everything is completely isolated, which means we actually created, there were a lot of places in V2 where we were using V1, as our definition, but we're planning to break it. So, like, that was, That was one of the things that we, we have now, is if we want to go in, for example, We wanted to get rid of requirement level on, or deprecation, I think, on.
**Arianna Vespri (OllyGarden)** 15:53 Yes. Yes.
**Josh Suereth (Google LLC)** 15:55 Yeah, so now we can come in here, and in common fields… oh, it's actually uncommon.
Where's Common Fields? Where did I put it? Is it in mod?
I think I put it there.
Did I not put it there? Where did I put common fields?
Is it actually called a common? No.
Thought it was here.
**Arianna Vespri (OllyGarden)** 16:23 I don't think… I don't think I remember anything called common, as a file.
**Josh Suereth (Google LLC)** 16:28 Oh, it is in… it is in mod. I just don't know how to search. Okay. Yeah, inside of here… we're probably gonna remove, deprecated from stability. So this… this here… Oh, man, you know what? I didn't finish.
Yeah, so basically, we can create a V2 stability.
And then, this is still importing from a central place, so I need to move this.
I think deprecated got moved, but stability… no, deprecated's still the same for both.
Oh my god, can't believe I missed that. Anyway, I moved com… I'm an idiot.
**Liudmila Molkova** 17:16 Well, I specifically asked AI to check if there are common things, and I didn't find them either.
**Josh Suereth (Google LLC)** 17:24 I know.
I think it's because it's hidden here.
Yeah, because stability is here, and it's still here, it's not split.
Which is one of the reasons we were making the rewrite, but it's fine, I can go… I can go move this. I'll make another PR. The hard breaking… hugely breaking PR is done, so moving stability hopefully won't break too many people. But that is the goal, is… What?
**Liudmila Molkova** 17:47 Why is it breaking?
**Josh Suereth (Google LLC)** 17:50 It breaks your… it gives you merge conflicts. It's not breaking in the sense of, it shouldn't break users. Oh, speaking of whether it's breaking… Let's see.
Where is the… downstream chick?
How long does this take to run?
**Liudmila Molkova** 18:16 I don't remember, but if you look into the previous runs, it will show.
**Josh Suereth (Google LLC)** 18:23 I think it's about 20 minutes. It's still compiling, apparently, okay?
We'll know if it's breaking pretty soon, and then based on this, I want to cut a release. But there was a… The main reason I wanted to get that PR in was when we were debugging it and trying to fix unit tests, I found a bunch of bugs.
From, like, patches we had been making.
One of the things… Resolve schema needs a stable sort.
And AI really likes to hash map everything.
And a hash map is not a stable sort.
And so there were a bunch of, like.
there's… there's this one… that one giant function where it's like, make all the refinements, then sort the refinements, make all the, you know, make all the metrics groups, then sort them, make… right? And attribute groups got added, but without the sort function.
And it literally had a HashMap sort, like, on purpose, before it, for speed or something. It's like, okay, great. So, anyway… It's fixed, it's merged, we're doing the downstream check.
And then we can fix the stability bug and all that kind of stuff going forward.
Cool.
So, yeah, when that's done, I'd like to kind of release. What other topics do we have?
Do you have anything, Liudmila?
**Liudmila Molkova** 19:52 I have a PR… For the designing, I'm trying to remember what. Okay, so the enum problem, that we want to limit, enum members.
I don't think it's a good time to talk about it. I, I… I created it a couple of weeks ago, I totally forgot about all the details, and I think it can wait. I created it just to feel good about Span type, so that… It addresses, to a certain extent, how we can identify refinement.
And… I think it's called Design Doc, yeah, the one on the bottom.
Yeah, this…
**Josh Suereth (Google LLC)** 20:46 So, okay.
**Arianna Vespri (OllyGarden)** 20:49 Interesting.
**Josh Suereth (Google LLC)** 20:50 What is this? This is from July. Oh, you just updated it. Okay, that's probably…
**Liudmila Molkova** 20:55 I didn't even update it, it's an old one. I just, wrote it down along with the tap to… Yeah.
I don't even think that I like everything I wrote Adan, but, So I think the only important piece that I really want us to do first is The things like messaging system, Where we would pick a constant.
And there is a proposal… yeah, this friend.
**Josh Suereth (Google LLC)** 21:33 I remember this now. Okay.
**Liudmila Molkova** 21:35 Yeah, so when we declare a span, we would say, okay, there is a… Oh, it's a problem too. Okay, so here it's… There is a constant… there is a… oh, so wait, why is it the problem 2? You see, I forgot everything. So maybe you scroll down to problem 2, and that's the most important one I want to solve.
Bye.
Oh yeah, it's the same syntax, right? So, when we declare a span, We're saying… what… In which ways you're allowed to… Create refinements.
And it's not a single attribute, it can be a combination of attributes, but… For now, we only have one.
And we would say, okay, this is that attribute.
And then we can validate the uniqueness of refinements.
**Josh Suereth (Google LLC)** 22:34 Oh, yeah, this is where you can pick what refinement that you want to auth against, or validate against, yeah.
**Liudmila Molkova** 22:42 Right, yeah.
**Josh Suereth (Google LLC)** 22:44 Okay.
**Liudmila Molkova** 22:45 I think I feel pretty, well, not confident about other problems I want to solve. I don't know if I want to solve them.
And I propose a solution just because they exist, and we should have a solution.
But I was thinking that, maybe the hardest choice there.
Is, okay, we have these things like messaging systems, or database systems, and the list is long.
Should it even be an enum? Should it be just a string? Can we just say, okay, the refinements are the things that decide which constants we have?
And I think it would be a good choice if we started with it, like, X years ago.
But now we would need to declare the refinements for all the systems that we have documented, but don't have a special conventions for.
skinny.
**Josh Suereth (Google LLC)** 23:53 What is the direction we could move towards?
Honestly, like, that doesn't… that seems reasonable. The question I have… you saw Jeremy's design for live checks, like, matching syntax for spans, right?
Does that make sense for refinements as well?
**Liudmila Molkova** 24:14 So… The idea of matchers started in the conformance label.
And, yes, so the matcher would be that the GenAI provider name equals whatever.
And that's exactly the… the way… well, we can do better, right? So, it doesn't even have to be… like, this syntax allows to… for it to not be in the WVR TOML.
Because…
**Josh Suereth (Google LLC)** 24:44 Yeah.
**Liudmila Molkova** 24:45 LifeCheck would know about all the possibilities.
**Josh Suereth (Google LLC)** 24:48 Yeah, I like having it directly in the model better, because the less, like, configuration you need to make a working system.
Where the model just understands things, and LiveChat can make intelligent decisions without help is better.
Yeah.
I still don't know how I feel about refinements overall, and, like, having a refinement refer to another refinement, and all that kind of stuff.
**Liudmila Molkova** 25:16 Oh, by the way, you know we allow it by accident, I think.
**Josh Suereth (Google LLC)** 25:20 If we allow it, it's by accident. It's, it's, you can refer to it, because you can probably put refinement dot something to refer to a refinement, is that right?
**Liudmila Molkova** 25:29 Yeah, I think so.
Cool twice.
**Josh Suereth (Google LLC)** 25:32 You could say it's by accident and on purpose.
I wanted to have the resolver flexible enough we could do it quickly if we needed to, but I didn't want it to work initially.
**Liudmila Molkova** 25:44 put the bar.
**Josh Suereth (Google LLC)** 25:45 Okay.
**Liudmila Molkova** 25:46 I have a bug.
**Josh Suereth (Google LLC)** 25:48 I was just talking to Arianna. I might spend a lot of tokens in the resolver engine. Actually.
making it not be on V1 or V2.
Just having an independent resolver engine, and have, like, an adapter.
pattern, where we work on a type which is either a V1 or a V2, and it, like, knows how to access things on it the way LiveCheck does.
**Liudmila Molkova** 26:16 Yeah, I was…
**Josh Suereth (Google LLC)** 26:18 Oh, Two things first, though. One is, I'm probably going to write a bunch of criterion benchmarks for it.
Ahead of time, because Resolver's where we spend all our time.
And it's really easy to be inefficient.
And do horrible things there.
The second is, I'm nervous about our overall test coverage on Resolver, given how many times we've broken stupid shit. So, if I do this refactoring, right, no test should change. Everything should just work.
But I'm nervous…
**Liudmila Molkova** 26:54 Yes.
**Josh Suereth (Google LLC)** 26:55 No tests should change, and all tests should pass. I'm just nervous, the number of times we've broken things where all tests continue to pass has been rather high for the resolver, specifically. So, like, that's one… yeah. I don't know if we should go through and add more tests, or what, but I'm a little bit nervous about making that change.
**Arianna Vespri (OllyGarden)** 27:14 But also with Code Cove, it happens.
like, with the check on the CRM in… That, that beat me, like, continuously asked me for… for new tastes, so… it doesn't, it doesn't… it doesn't ask you that as well, for the resolver, or in general, just asks that to me.
**Josh Suereth (Google LLC)** 27:35 Github Copilot, you mean?
**Arianna Vespri (OllyGarden)** 27:38 Yeah, Code, Code Cove.
**Josh Suereth (Google LLC)** 27:40 Oh, co, yeah, it does ask you for new test coverage, but we've been able to successfully have 100% test coverage and still have bugs.
**Arianna Vespri (OllyGarden)** 27:48 Okay, but that's a talent too, I think.
**Josh Suereth (Google LLC)** 27:51 Right, right, but that's kind of… that's actually the concern I have, is, like, we've had 100% test coverage and broken Semconf somehow, right? So, that's one of the things that has me a little bit nervous about doing this refactoring.
Anyway, Liudmila, you had some thoughts. Do you want to walk through them?
**Liudmila Molkova** 28:11 I mean, the first one is… We… usually had the most interesting problems from Semconf, but that's not the case anymore, because there are no There is no resolution except that within one registry.
Right, so we don't have a good… Real data to work against.
Yep.
So, taking this point away, the other thought I had… okay, so you know how, like, when you do the backend development.
they tell to never combine the data model with the output you give to users, or even your own representation of this data model. Yep. And, like, along with this awesome refactoring to separate V1 from V2, I think we should separate the, schema and the models that are part of the definition and resolution from what's inside, and I think this is exactly what will happen if you do the resolver change.
**Josh Suereth (Google LLC)** 29:18 Yeah, that's… that's probably how this is gonna actually work.
is… and I'm kind of debating how to do that a little bit, Ludmila, like… do we… Do I make a trait for a particular concept, and then that trait has an implementation for V1 and V2?
Do I make a new data model completely for Weaver Resolver?
and then we convert from the SemCom V1, V2 into that data model, run through resolution, convert back. We already have, you know, group summary, which is… like, a version of hacking around V1 and V2, and your PR around making ingestion more flexible was, like, my… That triggered me to, like, realize, okay, yeah, we have to pull that.
Soon. So, okay.
**Liudmila Molkova** 30:11 What if we don't change V1? I know it's crazy, it would mean, like, we will keep the frozen resolver.
in its current shape, whatever it is, and we only do the V2 part cleanly.
**Josh Suereth (Google LLC)** 30:27 I don't know if we can do that, because we allow both V1 and V2 inputs in the same call, because the decision to use V2 for your definition of profile And that possibly was a giant mistake.
**Liudmila Molkova** 30:44 We can fix it.
**Josh Suereth (Google LLC)** 30:46 Well, here's the thing, though. You know how you have the dash dash V2, which is how you choose your output?
We might be able to swap to that. So, like, we could make a new instance of the resolver that is used when you have dash dash V2 defined.
And then, if you define dash dash V1, you use the V1 resolver with all the back ports to V1, and when you're in dash dash v2, you use a V2 resolver that's baked for V2.
I still have concerns about that. So… how about this? I don't think we're gonna resolve anything in the next 30 minutes. I'll write some stuff down. Like, I'll come back with a proposal.
it's probably better to say, like, do a little bit of design. I mean, with AI, my new approach is actually just have AI go implement something real shitty and never show it to you, and then use it to figure out if my design was a terrible idea, and then write a good design.
**Liudmila Molkova** 31:42 Oh, that's cool.
**Josh Suereth (Google LLC)** 31:44 So, I do that a lot, actually. Like, the number of broken Git commits I have that I've thrown away is pretty high.
That's interesting.
The cost of prototyping's… well, I wouldn't say it's cheap.
But it's not timely expensive.
**Liudmila Molkova** 32:05 It's not your brain cells expensive.
**Josh Suereth (Google LLC)** 32:09 Yeah, yeah.
And, like, there's something satisfactory about having AI go off and do something horrible and then killing it, you know? Like, like, oh, I don't need this branch anymore, cool, I can throw away all that trash work and I don't have to let it weigh on me. But I also know that maybe that's a bad venture, you know?
**Liudmila Molkova** 32:30 We'll learn. You have Agency MD committed, right? It's on Maine.
**Josh Suereth (Google LLC)** 32:35 Yes, yeah, yeah, yeah, so we now have an AgentMD, we have a knowledge base to start recording knowledge about… oh, yeah, let me, let me, let me share this in case you didn't see this, Arianna, because I think there's human aspects of this as well.
**Arianna Vespri (OllyGarden)** 32:50 Okay.
**Josh Suereth (Google LLC)** 32:50 Because I don't believe in doing things only for agents. I believe everything should be useful for everyone. We now have an Agents ND.
That has baseline knowledge document for folks, and contributing.
And then, just small guidance to try to help specific agents. This is meant to be minimal, so it shouldn't be contentious, so you can overlay your own trap on it if you're using it, but this doc's knowledge is meant to actually be useful for humans in India.
**Arianna Vespri (OllyGarden)** 33:20 Great.
**Josh Suereth (Google LLC)** 33:22 So Doc's knowledge is basically, like, W results and Rust style. So our Rust style is all the things that we care about when we write Rust.
This should be human-readable, this should be, you know, helping folks write comments about how we like to see comments. This is way more important for modern Claude, if you haven't seen Claude's comments lately, they're pretty bad. This helps a bit.
That's from Jeremy. And then, this is, like, I wrote this up with… well, I had AI format the tables and that kind of thing, but this should cover idiomatic patterns around how to do, warnings.
in Weaver.
And… I had a whole bunch of trouble with, Gemini, just not knowing how to deal with W result, and how to make warnings, and do the warning design. And since we're doing something kind of non-standard in Rust, it's kind of standard, kind of non-standard, with W result versus result, where W result means it's a result that can have warnings.
We wrote this up, and it's kind of just a guide of, like, how to use that.
whole… thing. It is in the Rust like, this is a copy of Rust Dock a little bit.
But this is something that you don't really do in Rust stock, of like, hey, how do I accumulate non-fatal errors across loops? How do I validate in-place error, you know, collection, that kind of crap?
**Arianna Vespri (OllyGarden)** 34:56 That's super useful.
**Josh Suereth (Google LLC)** 34:59 Yeah, if this… if this… it should help both you and your agent, and if it doesn't, that's the idea behind everything, knowledge… and the idea for a knowledge codebase comes from the Java folks, and what they do with agents, so thanks for pointing us at that, Liudmila.
It was, I really like this, I think this is gonna work out pretty well. If there's things you think need to be in here, open a bug and we'll try to add them.
Cool.
**Liudmila Molkova** 35:26 The downstream check has passed, so we're good.
**Josh Suereth (Google LLC)** 35:30 Sweet. Right. Okay, so we can cut a release.
I can probably do that, actually, right after this meeting, if you want. I'll go through the process and cut the next release. I think we're going to 0.26, right?
**Liudmila Molkova** 35:47 Yes, I think so, yeah.
**Josh Suereth (Google LLC)** 35:49 Oh man, it's been 2 months. Okay, this could be an exciting one.
**Liudmila Molkova** 35:54 to do a hotfix.
**Josh Suereth (Google LLC)** 35:56 Yeah.
And then we have, the question I have, should I merge any of these?
Before we do that.
**Liudmila Molkova** 36:06 Are they green?
**Josh Suereth (Google LLC)** 36:07 Quick.
Yeah, this is green.
**Liudmila Molkova** 36:08 Mentioned ES leaned… Doesn't matter.
**Josh Suereth (Google LLC)** 36:11 This one… yeah, it's just… it's just V-Day. Like, it's not… This is the UI. I don't think it's urgent to get those in right now. We'll put them in later.
And I don't think we had any other… Yeah.
Cool. Alright.
I don't think I have any other topics, outside of… Oh, I did have one more.
So, I'll put up together a proposal.
Did we talk about the security bricks one?
**Liudmila Molkova** 36:50 No, no, no, we didn't talk about security fix, I thought it's about the refactoring resolver.
**Josh Suereth (Google LLC)** 36:56 No, this is… this is an interesting one. I consider this a security, like, threat issue that we have to… I don't know if we have a threat model for Weaver, but the notion that we bind 0.0 It's unfortunate Jeremy's not here, so we might want to take this up in the… Maintainer's chat, too.
I think this is, like, 100% reasonable, is our default should be something that doesn't put you at risk. So I think the default should be to bind to localhost, not to the public IP. And I think there is a flag For you to decide what port to bind to.
So, this to me seems like something we should fix.
Somewhat urgently, too.
**Liudmila Molkova** 37:41 I mean, I can burn some tokens, it's probably relatively trivial.
**Josh Suereth (Google LLC)** 37:48 I think it's literally a one-line change, yeah.
**Liudmila Molkova** 37:51 Okay, can you assign it to me? I'll try to do it as soon as possible.
**Josh Suereth (Google LLC)** 37:56 Sure.
I will wait on the release then.
I don't know, do you think we should put this in the release or not? That was… that was my… I have it on two considered, or should we just do a patch fix later? Like, I'm fine either way. I think it's one line.
**Liudmila Molkova** 38:13 If we call it now, I'll probably, in the 20 minutes till my next call, I'll probably have a fix. So we probably should do it now.
**Josh Suereth (Google LLC)** 38:22 let's… let's do that. I'll wait for the release, we can call it now and do that. Cool.
And I will hold off on the next discussion, because maybe we want more maintainers, but I don't know if we have a security threat model for which we evaluate security bugs against Weaver. And since we are kind of more of a CICD pipeline component.
**Liudmila Molkova** 38:45 We are so much in a deck.
**Josh Suereth (Google LLC)** 38:47 What?
**Liudmila Molkova** 38:48 We are part of the supply chain attack?
**Josh Suereth (Google LLC)** 38:51 Yeah, people can supply chain attack with us, and so I think that should be what our security threat model is. I can propose one, I don't know how people feel about whether we need one now or later, but since we've never had any security vulnerabilities reported against us.
I don't know what the urgency is, but I feel like we should get one together sometime.
**Liudmila Molkova** 39:12 Maybe… can you create an issue, and we decide by V1? I think it's a good time.
to do it.
**Josh Suereth (Google LLC)** 39:20 Oh, yeah!
**Liudmila Molkova** 39:22 stable.
**Josh Suereth (Google LLC)** 39:23 100% blocker for V1, cool. I will open an issue, and with that.
Thank you, everybody. I think that's it for the meeting.
**Arianna Vespri (OllyGarden)** 39:30 Thank you so much. Bye. Bye-bye.
**Josh Suereth (Google LLC)** 39:33 See ya.
**Liudmila Molkova** 39:33 Good to see you both.
