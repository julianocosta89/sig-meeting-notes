SIG: Semantic Convention Tooling
Date: 2026-06-03
Duration: 46 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:00 This meeting is…
**ariannavespri** 00:36 Nope.
**Josh Suereth** 00:45 Hey, sorry, I'm just getting booted up here.
I'm fighting, like, a head cold, so apologies, I'm a little…
**ariannavespri** 00:55 Oh, no, Ken, I'm sorry, it's because of the weather?
**Josh Suereth** 00:58 No, I think I, I… we did a… I went on vacation, then we had a summit at work, then I went on vacation, and I had, like, tons of people and stress all at the same time.
**ariannavespri** 01:11 Oh…
**Josh Suereth** 01:11 Basically, the stress kills your immune system, the people bring all the stuff, so I think I just caught something, that's all.
Yeah.
**ariannavespri** 01:19 Okay, maybe, maybe now if you're, like, settled down, more relaxed, also the, you know.
Immune system is gonna get better, you're gonna get better soon.
**Josh Suereth** 01:27 That's what I hope. I'm feeling a lot better than I did, yesterday, so that's for sure. Fantastic. I sound like my voice isn't quite there, yeah.
**ariannavespri** 01:36 It will get better.
**Josh Suereth** 01:37 Yeah.
Right. I don't know who else is going to be coming, but, we can… you pinged offline about, issue 970. Do you want to talk about that?
**ariannavespri** 01:49 Yeah, but… yes, it's just that… so, let me… Let me retrieve it, because… I was just asking because, like, I wasn't super, I wasn't always there during the last weeks of the meetings because of… You know, like, incidents, and because of, we had an off-site, like, last week, so that kind of thing where you, like, your schedule from… from when you wake up till you go to bed is basically, you know, it's always something that is… There to do… okay, let me see, because it was… So this was one of the first things that, basically, you assigned to me, and I was just wondering if this is still relevant, and if I, you know, if there is any other, you know, larger PR that maybe would advise against tackling this right now?
Because I'm a bit lost right now, you know, with all going on, because I… I wasn't there, as constantly as I would have loved to.
So that was basically my, my questions.
**Josh Suereth** 02:58 I think this one, probably would be worth putting a… maybe a design proposal? Like, this is… this is describing a solution, but maybe actually just putting together, like, a, hey, here's what I think it should look like in YAML would be fine.
I think that's the state of where this is. I don't see anything super blocking here.
**ariannavespri** 03:19 Okay.
**Josh Suereth** 03:23 I'm trying to think…
**ariannavespri** 03:25 I mean, it has been linked to another issue, but I haven't looked much into that, so…
**Josh Suereth** 03:30 This is the… this is the issue that I think was raised first, which was, yeah, we can't… we can't define span lengths right now in some interventions.
So this gives all the background for why you would want it. I think… This is from 2022, man.
**Liudmila Molkova** 03:49 I think this is a very hairy problem. I don't… Oh, boy, Shariana, you… to deal with this, but the YAML definition is a little bit… easier. At the same time, I think there are issues that are more relevant. This one is irrelevant for messaging.
But messaging seekers and pods.
Okay.
It's probably not, like, it's awesome to do it, but somebody will start using it In a year.
**ariannavespri** 04:22 Okay, so that was exactly my question, because as I was telling Josh, I haven't been, like, you know, I missed a couple of meetings in any case, so… and, so if you could point me to something that is more relevant, while I, you know, I get into the swing of things again.
I could work on that, or I mean, at some point, I should also… I would also try to help you with reviewing things, so… So that's it.
**Liudmila Molkova** 04:52 Yeah, do we have any V2 work, or… R.
Oh, Josh, you're on mute.
**Josh Suereth** 05:03 Sorry. All the issues are triaged, so, you should be able to come here.
And, what do we want to… like, V2 model work, you think?
**Liudmila Molkova** 05:16 Or… Something that's active.
**ariannavespri** 05:19 Whatever you think is… whatever you think is best.
**Josh Suereth** 05:24 I think this one… This is a dumb one that's minor and probably not important, so let's skip that.
There's a bit of… I don't know if the namespace and stuff is easy to pick up, either.
that's, like, a decision we have to make, and… this was documentation. Yeah. Okay, so that's that. Let's take a look at the project.
**Liudmila Molkova** 06:00 Maybe there is some life check work.
**ariannavespri** 06:03 Huh? Yeah.
**Josh Suereth** 06:09 Some of this I think we might have already done. Like, this… don't we now generate JSON schema from Rust?
Should this be closed?
**Liudmila Molkova** 06:16 I think so. Maybe not everything, but it's… Yeah, I think that that's closed, yeah.
**Josh Suereth** 06:25 Yeah.
Winder, thanks.
Enough of this… Alright.
Apologies, I'm fighting a head cold. Alright, generate JSON schema from Rust models, define span links in YAML. Yeah, so this… I think if we go down here and find something that's higher priority, that would be good.
Here's one that I don't think I had a chance to do.
And it's relatively simple, but basically, For identifying attributes in entities, we want them all to be required.
By default, and we don't really want people to allow optional. Like, that's the whole point of an entity with the identifying attributes, is you know what identifies it. There's not really optional identity.
So, this would be when you define Like, we need to update the schema so that you cannot define requirement level on identity of entity. I think there's a couple ways we could do this, but that's basically what that task is. I don't know if that one's too complicated or not.
The outcome is simple, but the code might be ugly.
**ariannavespri** 07:38 I can give it a try, you know, so…
**Josh Suereth** 07:42 Yeah. Yeah, if you're interested in this one, this is, 986.
**ariannavespri** 07:47 Yes, I'm gonna take note. Thank you so much.
**Josh Suereth** 07:50 Okay, maybe we'll keep going and see if we find an easier one, too, or a, like, a higher priority one. Decide what public attribute groups are and how they work in Weaver model.
This one, we're kind of halfway there, right?
We do have to sort out each of these. It could be that maybe one of these could be worked on.
Do you have an idea of what you want LiveCheck to do with attribute groups, Jeremy?
**Jeremy Blythe** 08:25 I'm not sure what this is about.
**Josh Suereth** 08:29 So, we have, attribute groups as a signal type.
**Jeremy Blythe** 08:33 Yeah.
**Josh Suereth** 08:34 Like, code exception thread, right?
The question would be, how are we enforcing those in LiveCheck?
**Jeremy Blythe** 08:53 Are they just… are they defined as, like… Oh, I see. They're not really defined as being, Recommended, or whatever, on the actual As soon as I could.
**Liudmila Molkova** 09:06 They…
**Jeremy Blythe** 09:07 If there's a metric, it doesn't say… You know, exception… is recommended. It's just sort of implied that these things can go anywhere.
**Liudmila Molkova** 09:19 Yep.
**Jeremy Blythe** 09:21 Interesting. Yeah, I don't know what we would do. At the moment, it would go… what would it?
**Liudmila Molkova** 09:31 Nothing.
**Jeremy Blythe** 09:33 You would see… it would just go, here was a… here was an attribute.
Provided that it's an attribute that is in your Registry that you've loaded.
He would just go, oh, I found this here.
**Liudmila Molkova** 09:46 Wait, but you… Would you know that?
The span.
Let's say is supposed to include this public group, let's say exception, or an event.
And then, based on the definition, you would know that this group is included, and then you can expect All of them.
It's like, if it's present on a log, then… No, something non-identifiable. You do nothing about attribute group, but if it's on a Signal that you can… you could find a definition for.
Then you can use that definition to understand what should be on it, including public groups.
**Josh Suereth** 10:43 Right, that's… I think the issue is we have no way to tie, like, a signal, like a span or a log, or a metric to a group.
Unless it's explicitly reffed.
**Liudmila Molkova** 10:53 Yeah.
**Josh Suereth** 10:53 Reft, you are, like, it's already there. These are, like, loose groups, so this is, like, code, exception, thread, I think are loose. They're not really attached to anything.
**Jeremy Blythe** 11:03 I agree.
They're not attached or anything, they're not defined as being… you know, such and such a metric has this as a requirement, or a recommendation, or even an optional. It's just… it's just, you can put A code dot something, anywhere you want.
So, LiveCheck provided code.
is imported into the registry that you've got loaded in LiveTrack.
LiveCheck will check that that attribute is correct.
But it's not gonna do one of the checks, like… You know, it's required or recommended, because it doesn't… there's… there's nothing that's tying it that way.
So it will do an attribute level check.
**Josh Suereth** 11:44 Yeah, does it ignore it, or does it warn, like, hey, you have this thing that's not in required, optional, or whatever?
**Jeremy Blythe** 11:52 No, it allows additional.
Okay.
**Josh Suereth** 11:58 Alright.
So it could be there's nothing to do here, then, if we're okay with that as the behavior.
**Jeremy Blythe** 12:08 we want to say that additional… like, that's a general, like, assumption that I made, is that… Extra attributes that are found are okay, provided they're in the registry.
Across the hall.
Across the board.
**Josh Suereth** 12:26 Yeah, for anything.
it depends, right? Like, if I'm… I think we're… we're allowing that for the most part. If we're trying… we're not using this for doing backwards compatibility.
We're using Rego policies for that, so yeah, I think from a live check perspective, that's fine.
**Jeremy Blythe** 12:52 then I think it's covered.
**Josh Suereth** 12:55 Okay.
Maybe we should bright this up, and then, mark, this one closed, too.
Okay.
Last one was… span refinement to override name, note, and definition 2. I thought we had a PR for this.
**Liudmila Molkova** 13:15 Copilot PR.
Of the low quality.
Copilot PR of a low quality.
**Josh Suereth** 13:22 Oh, right. Okay, co-pilot didn't finish.
**Liudmila Molkova** 13:26 I… yeah.
**Josh Suereth** 13:29 That's fair. Okay, so this one… Go ahead.
**Liudmila Molkova** 13:33 Maybe it wasn't too bad, it's just maybe I, I… Didn't have a chance to polish it enough.
**Josh Suereth** 13:40 if I remember looking at it, now that… now that you mentioned it was the co-pilot one, it defined… it defined something for refinement, but it never actually implemented it.
The actual, like, override.
Like, it just wasn't there.
Last time I looked.
**Liudmila Molkova** 13:55 Okay.
**Josh Suereth** 13:56 Yeah.
But that was… that was a while ago. I've been kind of out of it for, like, a week and change now.
**Liudmila Molkova** 14:03 I didn't change anything.
**Josh Suereth** 14:05 Okay.
Alright, so unfortunately, I don't think there's any other… Super important options there.
We could triage some of the new things that came in here.
And figure out if any of these are important to pull in.
What do you guys want to do with the rest of the meeting? Ariana, I think you have one thing to look at, so that's good. Let's get back to the meeting notes.
Get some eyes on 1458.
**Liudmila Molkova** 14:40 This is, to… Yes, to mark things invisible in the… core repo, so we can… When resolving GenAI, we will ignore it.
**Josh Suereth** 15:01 Oh, right, this is our dependency resolution decision for… the… yeah.
**Liudmila Molkova** 15:06 Yeah.
**Josh Suereth** 15:08 Okay.
So, where does this mostly manifest? We have a source group.
Oh, interesting.
I'm gonna have… we'll have to have some talks about this then, yeah.
**Liudmila Molkova** 15:30 Okay, yeah, it's been a while, so I'm currently blanking on what… how exactly it's been done.
**Josh Suereth** 15:37 Yeah, effectively, we're starting to do a lot of stuff where we have to track The provenance of, groups through resolution, so we can make important decisions with dependency resolution. So I had something I was doing, it looks like you added a new thing here.
That's fun.
Oh, this is…
**Liudmila Molkova** 15:57 We have a conflict.
**Josh Suereth** 15:58 Right. So this is fine. What?
**Liudmila Molkova** 16:01 Will we have a conflict?
**Josh Suereth** 16:04 I don't… I don't think we will, I just, I'll rebase off of yours.
**Liudmila Molkova** 16:08 Okay.
**Josh Suereth** 16:10 But, I wanna… let me… let me take a think about this quick.
And make sure this is the right place to hang it, or if we want to hang it somewhere else. It could be that, like, this local versus dependency, we can just make a helper method.
**Liudmila Molkova** 16:24 Based on the provenance?
**Josh Suereth** 16:28 Yeah, but group summary might not have enough in it, right?
I forget.
**Liudmila Molkova** 16:32 Yeah, that, that's…
**Josh Suereth** 16:40 Yeah.
Okay.
Alright, I'll take a look then. It'll take me a little while to get to it, though. Apologies.
**Liudmila Molkova** 16:49 Yeah, that's okay.
**Josh Suereth** 16:51 Cool.
Oh, why am I highlighting everything? Alright.
Metric requirement level, can we have a similar one for span, event, and what about entity? Yes.
Should we just put requirement level at the top level instead of call it metric requirement level?
**Liudmila Molkova** 17:08 Yes, I think so. I remember we had… two discussions. The first discussion is that maybe entities don't need it, But I'm looking… I'm looking at it in the context, okay, I'm an instrumentation, a resource detector, entity detector.
I can detect… I must detect certain things.
And some other things are… I don't know.
To her boss.
Does it make sense at all for entities?
**Josh Suereth** 17:43 Like, if I declare… like, if we declared entity detectors, said this entity detector detects these entities, and I have required entities that it should provide, yes.
But… I mean, the issue is, you're, like, detecting where you were running.
So, we kind of don't know.
Like, the only entity that we guarantee in OpenTelemetry is service that has to show up on SDKs.
**Liudmila Molkova** 18:13 But this is on the distro level, right?
let's say I'm, docker or Kubernetes, Attribute Processor, or something, detector.
What are the things that I'm required to detect?
To make sense in general, and some of them might be optional.
**Josh Suereth** 18:36 The issue is, if I'm a Docker detector.
and I am not running in Docker, I should not return anything.
**Liudmila Molkova** 18:45 Oh, yes, yeah, of course, yeah. To put all the conditions under it.
**Josh Suereth** 18:50 Sure. I mean, but effectively, every entity is conditionally required.
**Liudmila Molkova** 18:58 And, well, there are a lot of people who are happy to drop the most verbose entity, like service instance, because… to save money, not because it makes tons of sense, but to save money.
**Josh Suereth** 19:10 Yeah, you probably want to look at Dimitri's proposal around, this entity scope thing, where you can actually drop Stuff.
that… that would be… Because I don't… how do I want to phrase this? Like, with entities, we have, like, different… pieces of the entity tree. So there's, like, the physical entity tree of, like, this container is running this process.
And then there's the logical entity tree, which is, like, I have a service instance, it's part of a service namespace or something, you know? You might have both of them in a resource, and you could kill one, because you can infer the one from the other, kind of a thing.
That's all kind of TBD design.
So I'd be a little hesitant to just put, like, requirement level on it without really knowing how it would be used. Like, I still… I wouldn't know how we would enforce requirement level required, you know? I could see it on, like, an aggregate set, where we'd say, if you see this entity, you should probably see this one, too.
in this context, right? So, like, if I see a, process entity I should expect there to be a container or a host, you know? And that's a thing I might add, but that only makes sense if I'm in the… like, cluster.
world.
**Liudmila Molkova** 20:34 Yeah, it's not special for entities, though. Like, it's not enforceable on the pure river life check, but it's enforceable… if I'm instrumenting GenAI library, then I expect GenAI spans, or metrics.
I see, yeah.
**Josh Suereth** 20:53 The resource detect… like, yeah, so we could have requirement levels for resource detectors, that's fair.
Yeah.
How are we gonna tie it to a resource detector, though? I think requirement level right now for spans and things is implicit to the instrumentation, right? We're saying if you're implementing any GenAI spans.
Like, all the required spans should come out.
**Liudmila Molkova** 21:15 Right.
This is the custom code. We don't support it yet.
**Josh Suereth** 21:21 I see.
In that case, yeah, let's add it to entity for now. That would make sense. I think all of them might… or a lot of them will be required.
Some of them will not be… some of the stuff coming from service and deployment, probably.
**Liudmila Molkova** 21:37 Oh, we have added metric requirement level on main, it's not released.
And it would make sense, Dan, to do… Before the release.
To fix it now.
Well, it's not a big deal, because we can always keep the backward compatibility with the metric requirement level and requirement level for metrics.
But it's a difficult exchange.
**Josh Suereth** 22:06 Yeah, yeah, okay. Let's change it before release, but that sounds reasonable to me, is let's just put requirement level on everything.
**Liudmila Molkova** 22:14 Yeah, and by the way, Ariana, this could be a reasonably scoped problem that we actually depend on.
**Josh Suereth** 22:22 Yeah.
This is actually a way higher priority than the other one, yeah.
Cool.
My internet's really slow, so… apologies. Am I… I don't know if anyone else is seeing the stuttering, it's probably just me.
**Liudmila Molkova** 22:40 Yo.
**Josh Suereth** 22:41 Okay.
**Jeremy Blythe** 22:42 Bye.
**Josh Suereth** 22:43 Great. Alright, let's move on to fuzzing. Does that sound good?
**Jeremy Blythe** 22:48 Yeah, so, last week, I was talking about this with Laurent a little bit.
so… I just… I can't… I'm trying to make up my mind whether it's worthwhile or it's a little bit, sort of, security theater to do this thing, because really the problems we're finding are in the libraries that we use.
And when they go wrong, they're going wrong in really extreme cases. However, what was fun?
was I did… it… it did… the fuzzer did find a problem in, in, JAQ.
Jack, I don't know how you say it.
And I started looking into it, and it turns out, well.
Actually, that problem goes away if you upgrade to the latest version of it.
So this was a… this is the changes needed to move track.
forwards. And then the fuzzle… The fuzzer's happy with that, but it's still breaking the it's still failing on every PR because, Mini Ginger has got a… Let's got a… Thing that the fuzzer exposes.
I, and the only way, really, to fix that is to do an… is to write a PR the mini ginger, which I could do.
Interestingly enough, if you go to Mini Ginger, they open Telemetry Weaver is mentioned on the README.
On Mini Ginger.
Fun fact.
**Josh Suereth** 24:17 Are we, like, the number one user?
**Jeremy Blythe** 24:19 No, in… they've got, like, sections where it's being used, and one of the sections is documentation and code gen.
And it talks about Weaver.
**Liudmila Molkova** 24:29 User.
**Jeremy Blythe** 24:30 That's one of our commits.
**Josh Suereth** 24:32 Wait, where… where is this?
**Jeremy Blythe** 24:33 Scroll down, and you'll see it.
I think.
Yeah, code generation, look.
**Josh Suereth** 24:42 Wow, that's awesome. Okay.
**Jeremy Blythe** 24:44 Yeah. Yes, man.
So, the… my question is, like, are we… are we annoyed by, like, every PR having a red cross on it, because the faucet? It's… it's a non-blocking workflow check, so you can carry on and… But are we… are we upset by seeing red crosses on every single PR?
**Josh Suereth** 25:07 I mean, is it annoying? Yes. Has it stopped me in OpenTelemetry, because it's kind of common? No.
**Jeremy Blythe** 25:16 -
**Josh Suereth** 25:17 Like, there is… there is a question of, like, you know, are… A test that is always ignored is not useful.
**Jeremy Blythe** 25:26 Yep.
**Josh Suereth** 25:27 So, I would say that, like, what we want to do with the Mini Jinja thing is just be like, hey, Mini Jinja, we're having trouble fuzzing.
Because of this bug.
Could you look at maybe adding fuzzing yourself?
**Jeremy Blythe** 25:40 They have fuzzing. I went… I went and looked. They've got a fuzzer, but their fuzzer was… they implemented it, like, 4 years ago, and they're seeding it with their own seeds, so they're not using, like, the Google Cluster fuzzing thing.
They've got their own seeds, and their seeds to the fuzzer don't expose the problem.
Which is… turns out to be an unwrap on a… on a float and integer comparison that overflows It overflows because the int doesn't fit into the float 64 bits properly, and so… And then they just unwrap instead of doing something about it. And that panic.
It's, like, so obscure.
**Josh Suereth** 26:32 It's so obscure, but it is a crash, and it's good to catch it.
We know it exists now.
Yeah, I… I think we just open a bug against MiniGinja and say, hey, our fuzzer caught this, Yeah. You know.
See what happens, yeah. If we have time to throw, like, even… I think that sounds like something we could throw AI tokens at, see if they accept a PR, but it could be, like, so annoying to fix and so performance-sensitive that they don't. I don't know.
**Jeremy Blythe** 27:04 That… yeah, because I started doing that, and it's like, ugh, this is ugly now.
**Josh Suereth** 27:10 Yeah.
Is there a way we can suppress just that failure from the fuzzer, or not?
**Jeremy Blythe** 27:20 Yeah, I could stop… I could stop the fuzzing of mini ginger.
**Josh Suereth** 27:29 Stop the what?
**Jeremy Blythe** 27:30 I could stop fuzzing Mini Ginger, our entry point into Mini Ginger.
**Josh Suereth** 27:36 Yeah, maybe what we do is we… we take the entry… like.
We could have a job that just fuzzes Mini Jinja that we know fails nightly, so we can see if it ever succeeds.
And then we can just remove Fuzzing Mini Ginja from the every PR, so it's not… Oh, yeah. Yeah.
**Jeremy Blythe** 27:55 Yeah.
**Josh Suereth** 27:58 I still think you should open a bug against them to see what happens, especially if we're listed right on the README.
You know?
**Jeremy Blythe** 28:04 I know, right? With, with… Yeah.
**Josh Suereth** 28:08 That's… that's pretty awesome.
**Jeremy Blythe** 28:11 It was quite fun finding that the other day.
**Liudmila Molkova** 28:15 If I'm not mistaken, the maintainer was… Maybe involved, and up until after rest earlier.
**Jeremy Blythe** 28:24 Huh?
**Josh Suereth** 28:26 Really?
**Liudmila Molkova** 28:28 I might be wrong, but I think I've seen him before in the context of Fatale.
**Josh Suereth** 28:37 Huh.
Yeah, we'll have to take a look, then.
**Jeremy Blythe** 28:50 That'll be an issue and see what happens.
**Josh Suereth** 28:52 Yeah.
I wonder if someone else has already opened something like that.
**Jeremy Blythe** 28:57 I didn't find it.
**Josh Suereth** 29:00 Okay.
Cool. So, in terms of next steps, we have, We have this we want to do before we cut a release. I'm still a bit behind on the dependency management stuff, so I'll follow up on your PR, Ludmila.
And then, what else, what else do we have going on that… again, I'm a bit behind.
What else do we have going on that's urgent? Should we look at our project board, or is that super out of date at this point?
**Jeremy Blythe** 29:29 So, oh, sorry, go ahead.
**Liudmila Molkova** 29:31 No, go ahead, I was going to say that I think nothing is going on in the… in the… schema world.
**Josh Suereth** 29:40 You mean, like, no changes are going on in the schema world, or… We need to pick up work in the schema world, because we're not doing anything, and we need to do more.
**Liudmila Molkova** 29:49 But we need to finish what we've started.
**Josh Suereth** 29:51 Yeah, okay.
Yep.
Alright.
So, I think for… to consider for next release, right?
Allow updating enum values when referencing an attribute. I think this just needs to actually get implemented at some point.
Did the… did we actually make an implementation? No.
**Liudmila Molkova** 30:09 No, it's a big, hairy problem. I… I don't think we… we can… We need a design to start considering it. Maybe we should move it to…
**Josh Suereth** 30:21 maybe instead of… I'm gonna make a new thing here. No, I don't want to add to that. I wanna… how do I do this?
Come on, GitHub.
new column.
means design.
We'll make that purple. That sounds fun. No.
Make it yellow.
Right. Then we're gonna slide this over in front of To Be Considered for Next Release.
So, these are possible things we work on. If we feel like something needs a design, I'm gonna fling it into here.
And then this can be our release train. Does that sound reasonable?
**Liudmila Molkova** 31:00 Yep.
**Josh Suereth** 31:01 Cool.
Alright, enable strict mode when Jinja 2 behind a CLI option. Let's… Yeah, we can still consider that one, I don't think that needs a design. Weaver should resolve full URL.
**Liudmila Molkova** 31:16 Yes, design.
**Josh Suereth** 31:21 I remember this one, yeah.
**Liudmila Molkova** 31:23 Oh, you have a design.
**Josh Suereth** 31:25 Just a simple proposal, it's not a great design, but yeah.
**Liudmila Molkova** 31:29 We now have more fun.
was federated stuff, and we need a… Maybe full URL for everything.
It should be part of the manifest. Wow, oh no, I don't want it.
**Josh Suereth** 31:44 I'm gonna move it into Needs Design, because I think we want to take that straw man and turn it into, like, a, here's what we would do, and we agree to that, and then implement it.
Weaver cannot load registry directories beginning with dot. That is a very annoying thing that, can get fixed.
CICD post-commit hook to regenerate published JSON schemas using latest Weaver.
Yeah, that's just another… that doesn't mean a design doc, that's just a to-do. It's not a bug either, but I can turn that into a bug later.
Pre-built binaries, right. This one, did we end up fixing this or not? I can't remember. We ran into issues, right?
I'm trying to build for Arch 64. Did we ever add this?
**Jeremy Blythe** 32:30 I can't remember. You can, why don't you tag me on that one, and I'll… Wonderful.
I can't remember.
**Josh Suereth** 32:39 Tripping.
Alright, I tagged you as an assignee.
**Jeremy Blythe** 32:43 Thanks.
**Josh Suereth** 32:45 Multi-dependency support, this is the one that I'm working on now.
Then I have a bunch of random… abandoned branches for. Registry-r commands allow V2Resolved to be loaded straight up. I think this was fixed, or was this not fixed?
I feel like this… I put this in here, and then someone actually fixed it, because I didn't implement it. This is where, if you patch to SR and give it a schema URL, it will resolve the resolve schema, instead of trying to pull in the definition. Did we fix it, that, to do this, or is that still not fixed?
**Liudmila Molkova** 33:30 I think we… we did it.
**Jeremy Blythe** 33:32 Yeah, yeah, yeah.
**Josh Suereth** 33:34 Okay. Yeah, I thought we had fixed that, so let me.
**Jeremy Blythe** 33:37 That's done.
**Josh Suereth** 33:38 Move that to done.
Alright, then… SSL dependency decisions into features, right.
This one, this one is just a hairy breast issue.
Hairy slash thorny.
Monster-like rust issue.
I don't… what do you think the priority of this is, Jeremy?
It's, like, Laurent's not here, because I think they're using it in Otel Arrow, so I think they're the ones who paid the biggest price. But we do have people who are asking how they can get certificates into the Docker image, for example, and we don't have a good answer for that.
**Jeremy Blythe** 34:40 I don't know, really. I mean, we've had one or two requests, but… That doesn't mean it's urgent.
**Josh Suereth** 34:47 I'll leave it where it is, and hopefully someone can self-service, like the Hotel Aero folks, but yeah.
Okay.
Panic when using policy uses commit shah ref spec. I think this one got… oh, you have a co-pilot fix for this, right? Did this actually get fixed?
**Liudmila Molkova** 35:05 No, it's a cockpilot fix.
**Josh Suereth** 35:07 Okay.
So we're still.
**Liudmila Molkova** 35:09 This one is pretty annoying, yeah, so if I have time, I'll try to publish it.
**Josh Suereth** 35:15 Yeah, I saw what the fix is doing, and it makes sense, and that's really frustrating, how that behavior is in the code. So, okay.
Cool. And then, consolidate V2 unstable format warnings.
**Liudmila Molkova** 35:32 Oh, yeah, so, you know, I, I love your thoughts on this. So, you know how we… Every time they see a definition slash 2, or every time they get a certain warning, where… write, an output about it.
And then… what I've seen was metric requirement level, because we added it, but we want it to be default, and we warn if a metric doesn't have it. If you run Weaver main today on SEMCONF, you would get quite a lot of output, and it leads to some funny consequences. For example, it, Exhausts, pipe, buffer.
If you don't read from the pipe. So I think it's pretty annoying. It's not too bad, but I would love to find a way to group these things and say, okay, the… this problem happened on these different files.
It's hard to do in a generic way.
But it's easy to do for certain errors, or especially warnings, because, It's kind of annoying that you get so much output. Maybe there are better ways. So, I have the change here, it's pretty naive and pretty stupid, and I think it's not… it will not survive for long.
So I might spend a bit more time thinking about it.
**Jeremy Blythe** 37:08 Yeah, I ran into that. I was just… When I was saying, I was doing something, I wanted to look at the outputs.
Stats or something.
And then there's so much… I ended up just piping standard error to DevNol, so I could see the stats output.
**Liudmila Molkova** 37:22 Yep.
**Jeremy Blythe** 37:26 Or redirecting, I should say.
**Josh Suereth** 37:31 I like the idea of, like, a generic error make nice… feature set, right? Like, our first goal was to make sure that we can produce multiple errors instead of… have them all, like, stop at the first one, and then you don't get all the errors with your code, if we could detect multiple. But then phase two of, like, let's clean that up so we're not spamming you with the same set of errors a thousand times, and bundling them, that makes a whole lot of sense to me.
So, I think this is just a generic feature that we could reuse, like a place in the code where we can say, hey, if you see a thousand errors that are all of this shape, like, convert them into something easier to read, is awesome. Like, that… I think that matrix.
**Liudmila Molkova** 38:15 Don't we have it? This is the diagnostic template, is it?
**Josh Suereth** 38:18 Yeah. You might be able to use a diagnostic template to do it.
**Jeremy Blythe** 38:22 If you want.
**Josh Suereth** 38:22 If you love ginger a lot.
**Liudmila Molkova** 38:25 I don't care now because of AI.
**Josh Suereth** 38:28 Do you like reading AI's Jinja templates?
**Liudmila Molkova** 38:33 Nobody ever read it, let's be honest here.
**Jeremy Blythe** 38:37 Does it work? Yes, no?
**Liudmila Molkova** 38:42 Well, so maybe it's a JQ and Ginger. We already get these errors, and I can just update the default template to group by Error type, and then print these things nicely. Lily stuff, things that went wrong.
**Josh Suereth** 38:59 Yeah, and so we could, like, deduplicate the same error, like, a thousand times. That…
**Liudmila Molkova** 39:04 Right, yeah.
**Josh Suereth** 39:04 That makes a lot of sense, yeah.
**Liudmila Molkova** 39:07 Cool, I'll leave a comment on this one so I don't forget.
**Josh Suereth** 39:18 Alright, so the only thing I wanted to do next is, We have to consider for next release. We have needs design. I do want to get, with V2 schema, I want to get to a point where we have a, what we call our release candidate, or, like, GA, if you will, of V2.
with publishing and all this. So, I don't know how we want to necessarily track that. I don't think everything in V2's schema needs to be done For our first release.
So what I'm thinking is, if we're all amenable.
We get everything that we think needs to be.
That is mandatory for a release into some backlog.
and then we go from there, right? So we have, I think we had this Schema V2 proposal that was a work in progress.
I think we could probably close this, because we're actually now… we're really executing on this. I don't think this needs to be open anymore. And then there was another one I had for tracking that I think might also be worth closing, and we make a new, like, tracking issues we want to resolve before we cut a release. Does that sound reasonable?
**Liudmila Molkova** 40:40 Yes, before we call it stable. We can cut or release at any moment, yeah.
**Josh Suereth** 40:45 Oh yeah, we can cut relieve… well, sorry, until we remove the… the warning that says it's unstable, yeah.
Okay.
So let's do this. Okay.
Closing this bug, as we are now in full… Execution stabilization mode. So let's do that.
I had another one here that was… Do you remember if it was in here?
No.
**Liudmila Molkova** 41:25 Which one?
**Josh Suereth** 41:26 the other tracking one I had for, like, all the things we had to do for V2.
**Liudmila Molkova** 41:31 It was here, yeah.
**Josh Suereth** 41:34 Maybe I already closed it.
Okay, and then we'll make a new, ad item.
Okay. So… V2… schema.
Stabilization tracking… okay.
Create new issue. It's on Weaver. It is a blank issue, because this is going to be a tracking bug.
is in.
Issued. That will track all… Issues, features we need to complete.
Before firing… V2 flags.
It's stable.
Okay.
Cool.
We also will have to make a decision of if we flip the V2 to flag and V1 flag and all that crap, but this sounds good. Issue type is a task.
Priority… effort… yeah.
I'll tell Weaver Project what milestone are we gonna put it in.
And we'll just create it for now. I think it's gonna go under V2 schema.
There we go. Okay, so we'll start using this to track what we need to do, and add, bugs and features into it going forward. Sound good?
So feel free to add anything you think is a blocker to it.
And I will do the same.
**Liudmila Molkova** 43:04 Sounds good.
**Josh Suereth** 43:06 Cool.
And I think… Yeah, we can create sub-issues, or… I believe if we just do this… And put… an issue number.
Like, crap. I need an issue number quick.
The multi-dependency one, I think, is actually kind of a blocker. Multi-dependency… That one is issue… Well, we have 2.15.
Specific, so let's put your 1455, just as an example.
So we make sure this works… yeah.
then… okay, yeah, then when that closes, we'll see it turn to red, and if you do create sub-issue, I think it pops up in that… list as well.
**Liudmila Molkova** 43:57 I believe.
**Josh Suereth** 43:59 Cool. Alright.
So, I think maybe that was it for topics, unless anyone has anything else.
Why don't we call it and take some time to add issues to this independently? Does that sound good?
I need to go make 15.
I, I'm…
**Liudmila Molkova** 44:16 Sorry.
**Josh Suereth** 44:16 My voice is gone.
**Jeremy Blythe** 44:19 Just while you were doing that, I added a couple to the to-be-considered for the release to do with the entities. Remember we spoke a couple weeks back about having all of and one of in the entity thing? I think I'd like to get that in, so I put that in the to-be-considered.
**Josh Suereth** 44:34 Yes, is that at the top? No.
**Jeremy Blythe** 44:40 So there's… that is a PR, which was the live check NBC stuff, and then the… it actually came in as an issue, it's called ergonomic something something. If you scroll down a bit, you'll probably see it in the 2D considered.
Wait for that.
I think you've gone past it a couple times.
Hmm.
**Josh Suereth** 45:02 Nope.
**Jeremy Blythe** 45:04 There it is, in the middle there, ergonomic.
**Josh Suereth** 45:07 This one.
**Jeremy Blythe** 45:09 Yeah.
**Josh Suereth** 45:09 Okay.
Cool. I'm going to put that in… I'll put this one… this into the, release tracker.
bug.
That way we know, and then your issue is related to that, right?
**Jeremy Blythe** 45:31 LinkedIn.
And then I've got a PR that… At the moment is treating entities as an all-of.
Which is incorrect, and it should be one of.
**Josh Suereth** 45:44 Gotcha.
**Jeremy Blythe** 45:45 We wanted to add the all-of capability Which is also why that issue is related to, from whoever that was, from Dasho.
**Josh Suereth** 45:54 Yep.
Okay.
And then we should put our discussion about all of and any of into that issue, so we know what we're gonna do. Yeah, okay.
**Jeremy Blythe** 46:03 Yeah, I'll do that.
**Josh Suereth** 46:04 Sounds good. Anything else that you added into the… to be considered?
**Jeremy Blythe** 46:09 No, just those.
**Liudmila Molkova** 46:14 I will create an issue for requirement level, and I'll put it here in that area, and if you want to take it, take it. If not, that's also fine.
**ariannavespri** 46:23 And I will try to take it.
Thank you so much. I was just about to ask if the… if the issue was already there, but…
**Josh Suereth** 46:29 Thank you so much.
**ariannavespri** 46:29 much.
**Liudmila Molkova** 46:31 Thank you.
**Josh Suereth** 46:33 Awesome.
Cool. Well, I think that was pretty productive. Thanks, everybody. Sorry I missed a few… missed, like, 2 weeks in a row, I think. Yeah.
Feels like forever.
**Liudmila Molkova** 46:44 But glad that you're back, and take care.
**Josh Suereth** 46:47 Yep.
Yeah, alright, we'll see y'all.
**ariannavespri** 46:49 Bye, get well soon, bye.
**Jeremy Blythe** 46:51 Yeah.
**Liudmila Molkova** 46:52 Bye.
