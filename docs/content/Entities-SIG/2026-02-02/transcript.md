SIG: Entities SIG
Date: 2026-02-02
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:09 Ayy.
**Daniel Dyla (Dynatrace)** 00:11 Hey there.
**Josh Suereth** 00:12 Long time.
**Daniel Dyla (Dynatrace)** 00:14 Yeah.
**Josh Suereth** 00:17 Oh, alright.
Well, I have one topic I have to raise here, so… To me.
**Daniel Dyla (Dynatrace)** 00:24 Petrie won't be here today.
**Josh Suereth** 00:27 Yeah, the hotel unplugged is this week, so I just assume we're gonna be missing a few people.
Okay. I'm sad I couldn't manage to get out there for that, but… Yeah.
We were having our own leadership summit, internally, so it was, like, really bad timing.
You enjoying your cold?
**Daniel Dyla (Dynatrace)** 00:52 It is, it is really cold.
We're getting an inconvenient amount of snow here, too. I don't know how it is where you're at, but, like, it's snowing every day.
Which is…
**Josh Suereth** 01:05 It's been… we've been getting light dusting, but not quite snowing every day. We're not…
As close to the lake as you are.
**Daniel Dyla (Dynatrace)** 01:12 Yeah.
**Josh Suereth** 01:13 Yeah, like, I'm a good bit further south, so…
But we did have a construction vehicle come in, like, one of those,
backhoes, I guess, and fill up a dump truck full of snow, and then drive it off, because otherwise, I don't know what you do with it.
I don't know where they took it, either.
**Daniel Dyla (Dynatrace)** 01:33 Took it to the Bills Stadium and dumped it there, probably.
**Josh Suereth** 01:36 Oh, there you go.
Yeah.
Alright, well, I think it might just be you and I, then. Do you want to…
**Daniel Dyla (Dynatrace)** 01:47 Yeah, I think so. Based on normal attendance, it's usually the two of us and Dimitri, and maybe one or two other randoms.
**Josh Suereth** 01:55 Nathan's usually here, but sometimes quiet, yeah.
**Daniel Dyla (Dynatrace)** 01:59 Yeah.
**Josh Suereth** 02:00 Alright, well, let's keep it short and sweet then, because I, it's…
**Daniel Dyla (Dynatrace)** 02:04 Did you see…
**Josh Suereth** 02:05 Coast.
**Daniel Dyla (Dynatrace)** 02:06 Okay. Did you see I opened the PR for the, for a new version of the prototype in JS with all three signals?
**Josh Suereth** 02:15 Yeah.
**Daniel Dyla (Dynatrace)** 02:16 Okay.
**Josh Suereth** 02:17 Yeah.
**Daniel Dyla (Dynatrace)** 02:18 I mean, that's…
I don't have much to say about it other than it works and matches the OTEP to the best of my
Knowledge.
So… I guess as far as prototypes go.
**Josh Suereth** 02:34 I think we're good.
**Daniel Dyla (Dynatrace)** 02:35 Yeah.
**Josh Suereth** 02:36 Yeah, so,
Yeah, I didn't have a chance to dive into it deeply, I just looked at a few things. I think I chatted on Slack about it, right?
Maybe. Maybe. If you did, I didn't reply.
Well, I knew the second part.
**Daniel Dyla (Dynatrace)** 02:59 Yeah, no. I mean, I only posted about it on Friday, so… at 4.30 PM.
**Josh Suereth** 03:05 Oh, yeah, and I put, I put the, little.
**Daniel Dyla (Dynatrace)** 03:09 reaction, yeah.
**Josh Suereth** 03:10 Reaction. I did not comment on it, huh?
**Daniel Dyla (Dynatrace)** 03:13 Yeah, I mean, that's fine.
**Josh Suereth** 03:16 Wow.
**Daniel Dyla (Dynatrace)** 03:17 I ended up going a way simpler route for the metrics SDK than… I essentially blew away everything I had, and…
Instead of trying to dig into the metrics internals and create a bunch of shared things.
It just creates a new export pipeline that shares the exporter, and call it a day.
It just… I basically just copied the config and reused it and created a new export pipeline, and that seems to work just fine.
**Josh Suereth** 03:50 If you can do that, that would have been my preferred way to handle metrics, but I was unable to do that.
**Daniel Dyla (Dynatrace)** 03:56 Yeah, so… to do all the shared stuff, but there's no point. It doesn't matter, so…
**Josh Suereth** 04:01 Yeah, yeah, like, as long as the export… like, that's why I love your spec, because we know what needs to happen, and anything you do that gets away with that.
As long as it's not, like, crazy overhead, yeah, and then we can figure out if we need to share something deeper later, optimize
Yeah.
I do have an unrelated thing to talk to you about, when this meeting's over, so just remind me, we're using Node…
node in, Weaver, and our build is atrocious, and I kind of beat NPM now. Like, I feel like it's possibly the worst package manager I think I've ever interacted with.
**Daniel Dyla (Dynatrace)** 04:42 Yeah, I… you won't hear me arguing. It's been most of my career fighting with it, so…
**Josh Suereth** 04:48 Okay, well, I just started my career fighting with it here.
why does CI not work? NPMCI? It's supposed to be cool, we're not gonna go change your dependencies, we're not gonna change package lock. We want our releases to use NPMCI instead of NPM install, right?
And it can't even handle minor version differences between the NPM version.
So if you have NPM, like, 10.9 versus 10.10, it will be like, I'm sorry, your dependency would be different, I can't resolve this. You're like, it's a frickin' minor release!
What the hell is wrong with you, NPM?
**Daniel Dyla (Dynatrace)** 05:27 Anyway… Yeah, if there's a…
If you want me to look at it, I'm happy to look and see, because that is what MPMCI is for, so… it should work.
**Josh Suereth** 05:40 Oh, it's… yes, I agree it should work.
I'll send you, I'll send you the PR.
**Daniel Dyla (Dynatrace)** 05:48 Okay.
**Josh Suereth** 05:49 Yeah, I did… I did some weird-ass shenanigans, too, where, the version of NPM everyone wants to use in OpenTelemetry I can't have internally. So I have this crazy-ass fallback where it'll use Docker if it can't find it.
**Daniel Dyla (Dynatrace)** 06:03 You have to use an older version internally or something?
**Josh Suereth** 06:07 I'm on Debian, and whatever comes out of the box for Debian is what it uses, and Debian is, what, friggin' stale as hell.
**Daniel Dyla (Dynatrace)** 06:14 Yeah.
**Josh Suereth** 06:15 Because they… that's one of their things. Stable.
Sometimes stable, stale.
**Daniel Dyla (Dynatrace)** 06:22 It's probably NPM6, because I know if you look at the stats, there's a weird…
**Josh Suereth** 06:27 No, it's in… it's NPM9.
**Daniel Dyla (Dynatrace)** 06:30 9, okay.
**Josh Suereth** 06:31 It's NPM9, and then, the latest LTS is, like, 10 or 11.
**Daniel Dyla (Dynatrace)** 06:37 Yeah, I think it's 11.
**Josh Suereth** 06:39 Yeah.
**Daniel Dyla (Dynatrace)** 06:40 There's, for some reason, there's a… if you look at, like, download statistics, there's a big bump at NPM6, like, something is… some significant number of users are still tied to it for some reason.
**Josh Suereth** 06:51 Okay.
**Daniel Dyla (Dynatrace)** 06:52 probably something like Debian. Maybe my knowledge might just be out of date, it might be 9 now.
**Josh Suereth** 06:58 Yeah, I… that would not surprise me, that tends to be how those things work, is like, you get a major Linux distro with out-of-the-box support. Yep. Alright, but every… right now, every time someone makes a change to Weaver, they submit a new package lock.
It's not… not good.
**Daniel Dyla (Dynatrace)** 07:17 Okay.
**Josh Suereth** 07:20 Anyway, let's talk about… about the entity stability policies in SEMCOF.
**Daniel Dyla (Dynatrace)** 07:25 Yeah, this is what you were just talking about in the spec meeting, I guess.
**Josh Suereth** 07:29 Yeah, I don't know… can you read Rigo yet? Or… if I should.
**Daniel Dyla (Dynatrace)** 07:34 I have never done any Rigo. Is it… is it fairly obvious from…
I don't know. I don't know the answer to that question.
**Josh Suereth** 07:44 I'll show it to you, and then you can tell me if it's obvious.
**Daniel Dyla (Dynatrace)** 07:47 Okay.
**Josh Suereth** 07:49 Alright, so here's the policies. By the way, I'm working on, extracting out all the policies, making them compatible with our version 2 syntax. We're making a whole,
like, we now have an OpenTelemetry Weaver Packages repo, where we're gonna put our policies in there to be reused across OTEL, so if you find.
**Daniel Dyla (Dynatrace)** 08:07 Okay.
**Josh Suereth** 08:08 functions, like, these will get…
This way, if you're doing the whole stable-by-default federated semconv, and you define JS-specific conventions.
you have to abide by all the stability policies. Like, it doesn't matter that you're not in SEMCOM. You still have to be stable. It's just, you can, you know, launch your thing independently of SEMCOM, and then move them over and have a transition from stable to stable later.
**Daniel Dyla (Dynatrace)** 08:33 Got it. Cool, okay.
**Josh Suereth** 08:34 Alright, so what we have, what we added… we added stuff specifically for entities, okay? So entity association, I'll just give you an idea what Rego is. This is making a set. It's saying, I want a set of all of the group names from all of the groups where the type is entity.
**Daniel Dyla (Dynatrace)** 08:54 Yep, okay.
**Josh Suereth** 08:56 Okay.
And then we say deny, meaning this is a violation. You get an entity association violation if…
You find some group.
Where there's an entity in the entity associations of that group that's not in the known entities. And here's the description of the problem.
**Daniel Dyla (Dynatrace)** 09:15 Okay, so you can't associate to an entity that doesn't exist.
**Josh Suereth** 09:19 Exactly. That one seems reasonable, right? That's… this one I have no problems with. And I don't have problems with the entity stability one either, so this one we have…
We have a few, and this is the human readable, right? But we say, cool, if you have a group that is an entity and it's stable.
And you're not in the list of exceptions, which, by the way, there's nothing in the set, so there are no exceptions yet.
**Daniel Dyla (Dynatrace)** 09:44 Okay.
Just placeholder, I guess.
**Josh Suereth** 09:46 We always allow exceptions in our policies, just in case. Like, there's… you're never, you know…
**Daniel Dyla (Dynatrace)** 09:51 Yep.
**Josh Suereth** 09:52 But you need… first of all, you have to understand Rego to know that this is here, which means there's only, like, 3 people who can do it. And secondarily, you know, there's a higher bar for that. But, okay, we… this is where we create a list of all your attributes that are the role identifying. You have to have one.
**Daniel Dyla (Dynatrace)** 10:12 Yeah, if it's less…
**Josh Suereth** 10:13 This is a one.
**Daniel Dyla (Dynatrace)** 10:13 And then…
**Josh Suereth** 10:14 Then this is denied, yeah.
**Daniel Dyla (Dynatrace)** 10:16 Yeah, okay.
**Josh Suereth** 10:17 Similarly, for this one, this is basically, if you have any attributes, if you try to mark yourself stable, and any attributes don't have a role.
We deny.
That's it. Those are the two things we have for stability.
**Daniel Dyla (Dynatrace)** 10:33 What is… what is an attribute role?
**Josh Suereth** 10:36 This is whether it's… so, right now, and we're fixing this with version 2 of the syntax, you have to define an attributes block, and then inside of the attributes block, you say this attribute is identity or description.
**Daniel Dyla (Dynatrace)** 10:50 Oh, so role is the identity or description, I got it, okay.
**Josh Suereth** 10:54 So, we check to make sure that you have an identity here. This is where we say if the role is identifying, we know that that's your ID.
In the future, we can actually get rid of this, because we're actually just going to have an identity section, where we can just check the size of it, but yeah, we…
**Daniel Dyla (Dynatrace)** 11:11 But you can't define… Attributes that don't say whether or not they're identifying, which seems reasonable.
**Josh Suereth** 11:20 You, you, well, you have to define them as being identifying or descriptive.
**Daniel Dyla (Dynatrace)** 11:24 Right, yeah, yeah.
**Josh Suereth** 11:25 you have to pick one, you can't leave it blank, because then we assume you haven't picked. Right, okay. So you can't stabilize until you've picked, even though there's a whole bunch of the… right, right now, there's a whole bunch of stuff that isn't stable. All right.
So then, here's where things get interesting. We have, compatibility checks between base and baseline and current.
And I think… did we do entities yet in here?
I don't think we do any baseline versus current checks for entities.
**Daniel Dyla (Dynatrace)** 11:56 Okay.
**Josh Suereth** 11:56 So there is no, like, stability check here that needs… that would need to get added. But for example, we do, like.
an attribute cannot be removed.
from the list of all attributes in Semcov, so once you've registered something, it stays forever.
Attributes cannot degrade stability, so you can't go from stable to alpha, for example.
That's… those are those kind of rules. And then we have things around the news. For metrics, and I think this is what we would base entities on, and I can add this if we decide on that, metrics cannot be removed, so once you add one, it's there forever.
They cannot become unstable, which is the same as degrading stability levels. You can't go from beta back to alpha, you can't go from stable to beta, for example.
Right.
**Daniel Dyla (Dynatrace)** 12:49 Okay?
**Josh Suereth** 12:51 Units cannot change, instruments cannot change. I think for entities, we would actually say the identity cannot change. Description, I think, can change. Identity cannot change.
**Daniel Dyla (Dynatrace)** 13:02 Yeah, definitely can't remove or change…
Can you add an… I guess the question is…
If you add an attribute to identity, Can you say…
like, I have this old entity that is a true subset of these new entities, are they the same or not? I mean…
Is it okay to have that just be a maybe state?
Or… Do we want to disallow it?
**Josh Suereth** 13:36 Yeah, I… this is why I think what we should do is, by policy, disallow it.
Allow…
**Daniel Dyla (Dynatrace)** 13:43 And if it comes up in the future, potentially an exception.
**Josh Suereth** 13:48 Potentially an exception, and then we can refine the policy, and.
**Daniel Dyla (Dynatrace)** 13:51 Yeah.
**Josh Suereth** 13:52 Policy works.
**Daniel Dyla (Dynatrace)** 13:53 We can always…
allow things… it's much easier to allow new things in the future. The only question I would have is…
If we specifically say we're not going to do this.
Will backends then depend on that? And then we find a situation where we need it, and back-ends get mad, or, you know, people get mad.
**Josh Suereth** 14:14 My theory… well…
I think, and then we can't do it, and I think that's fine. Here's the thing. I think that back-ends need identity to be stable.
To begin with. Like, straight up. I actually don't think we can…
I don't think it's viable to have identity change over time. I think we're talking about releasing a new version of the entity, like a major version bump.
Or we're talking about, make a new entity.
That you report differently, yeah.
**Daniel Dyla (Dynatrace)** 14:46 Entities don't have… versions, per se, though. I mean, making a new entity, obviously, is one thing, but…
**Josh Suereth** 14:55 No, I mean of, like, semantic conventions, right? So if I.
**Daniel Dyla (Dynatrace)** 14:58 Yeah, but you'd have to rev all of semantic conventions to do that, right?
**Josh Suereth** 15:01 That's how intense I think that change actually is, yeah.
**Daniel Dyla (Dynatrace)** 15:04 Okay.
**Josh Suereth** 15:06 Yeah.
And, yeah, we've never revved the semi-off version to 2.
even though… there will come a time where we probably have to do it, but yeah.
**Daniel Dyla (Dynatrace)** 15:20 Yeah, forever is a long time.
**Josh Suereth** 15:22 Yeah.
Never, never say forever.
**Daniel Dyla (Dynatrace)** 15:26 wouldn't…
**Josh Suereth** 15:27 Never… or… what's the joke? Never use absolutes? That's what it is, yeah.
**Daniel Dyla (Dynatrace)** 15:35 Okay.
**Josh Suereth** 15:36 Okay, so I…
**Daniel Dyla (Dynatrace)** 15:37 I think as a starting policy, it's reasonable. Yeah. It's… it's easier… to…
allow that in the future if it comes up, to refine the policy in the future. Like, this is… this is the REGO policy, it's not like it's in the…
specification where people are gonna point and say, you said this would never happen. This is more of a… a check for us internally, where we're telling ourselves, we're not going to do this.
**Josh Suereth** 16:08 Exactly.
**Daniel Dyla (Dynatrace)** 16:09 Yeah. Okay.
**Josh Suereth** 16:11 Here's the last one that applies to entities, and this one's a little bit more awkward to read. This one I have to rebuild for Semantic Conventions version 2, because we don't…
collapse everything to groups in that one. But effectively, this is about group stability. So if I define something as stable, this would be a metric, a log, a trace, an entity, okay?
With certain exceptions, because we have things that don't… abide by that.
So, as long as the group is not in the exception.
if I have an attribute that is not stable, and is not opt-in, then I get an error. Meaning, if I have, like, if I stabilize an entity, and you want an attribute to it, add one to it.
That attribute has to be marked as opt-in.
Because it is not… this is the stable by default principle.
Right?
**Daniel Dyla (Dynatrace)** 17:05 Yeah, okay.
**Josh Suereth** 17:06 I want to cha- you heard… you heard what I was saying before. I want to change this, where actually we could say,
where we might change how opt-in works completely, where it would say, this attribute is opt-in because it's experimental, but it will be required when it stabilizes, you know, or not required, recommended.
**Daniel Dyla (Dynatrace)** 17:25 Recommended.
**Josh Suereth** 17:26 Like, I think that would be fine for description.
**Daniel Dyla (Dynatrace)** 17:32 Yeah.
It's hard to think of examples where… I mean, just in the…
Because this only blocks stability. It doesn't block, like… it's not that you can't create a semantic convention, it's just that you can't make it stable.
**Josh Suereth** 17:52 Yes.
**Daniel Dyla (Dynatrace)** 17:53 Yeah.
**Josh Suereth** 17:55 And it blocks adding unstable attributes unless they're opt-in, which I think is fine.
**Daniel Dyla (Dynatrace)** 18:02 Yeah.
**Josh Suereth** 18:04 This is literally why that PR popped in, because this exception means that this wasn't triggering, but if you remove this exception, then it does.
**Daniel Dyla (Dynatrace)** 18:14 Right.
**Josh Suereth** 18:15 Because it comes…
**Daniel Dyla (Dynatrace)** 18:17 in…
Yeah, no, okay. So, this is the one that you're, that you're saying you want to change, though.
**Josh Suereth** 18:29 This is the one I would like to change for entities specifically, yeah. What I want to do for… and I'm not sure… I need to figure out
I can tell you what I want to happen.
how to write the policy, I think we might need to make some changes in Weaver, too. But what I want to happen is…
when you stabilize something, all the attributes have to go stable by default. Cool. Very, like, that's, that's what… that's option one. When I add a new attribute to an unstable thing.
Or when I add an unstable attribute to a stable thing.
Right? Because I want to explore adding new description to things, or in spans.
I like the… I like the thing that there needs to be opt-in with some sort of, like, you know, flag that turns it on.
But what I want to have be true is… it is only opt-in because it's unstable. It's not opt-in because we think it should be opt-in forever, it's opt-in because it's unstable.
**Daniel Dyla (Dynatrace)** 19:28 Yeah.
**Josh Suereth** 19:29 But when you mark it stable, I'd like to be able to make it become a different requirement level.
So I could say, cool, it is currently Beta.
And it is… there's a feature flag to turn it on. But when it goes stable, it will be recommended.
That's kind of where I want to get to, right?
**Daniel Dyla (Dynatrace)** 19:49 Yeah, because the recommended is on by default.
in our instrumentations. So, you want something that
You want the ability to extend the semantic invention with something that will eventually be on by default, but because it's experimental, you need a flag.
**Josh Suereth** 20:09 Yes.
So this is why what I'm thinking of doing is, we have this notion of…
Conditionally recommended, where you say it's recommended with, like, a condition?
I'm thinking that we would… we would basically do… we would have some way to denote
for unstable things, that they need a opt-in because they're unstable. And this would be, like, first class. So there'd be some kind of an annotation that says, this is recommended, but here is the stability… the opt-in because it's unstable.
And you could specify this in SEMCOM, we verify that it exists, so we change this rule to basically say, cool, any unstable feature of a stable thing has to have an opt-in.
**Daniel Dyla (Dynatrace)** 20:53 what's the… The advantage to this over… because you can… you can change something from opt-in to recommended.
So, why not just have it be opt-in when it's experimental, and then when you stabilize it, switch it to recommended? Like, what's stopping you from doing that?
**Josh Suereth** 21:13 This, is… let me actually check and make sure you can do that. I think that is under compatibility. I don't remember if we actually…
Stable attributes cannot change type, let's look at that one.
**Daniel Dyla (Dynatrace)** 21:30 But that's data type, right?
**Josh Suereth** 21:32 attributes.
**Daniel Dyla (Dynatrace)** 21:32 Can't… yeah.
**Josh Suereth** 21:34 There's one where we have… let's see where requirement level comes in.
Love it.
So we do have isOptin.
Stable metrics required recommended attributes cannot be added. That's just for metrics. Yep, okay. Yeah, you're right. Right now, we do allow that.
**Daniel Dyla (Dynatrace)** 22:02 Yeah, and, like, I think you just add a note to it that's like, this will be recommended in the future, or something like that.
**Josh Suereth** 22:09 And then, yeah, that's a lightweight way to do it. I do think this… I probably need to stop required attributes from getting dropped, though.
Like, if it's required, you shouldn't be able to flip it to be opt-in later. That seems bad.
**Daniel Dyla (Dynatrace)** 22:22 If it's required…
**Josh Suereth** 22:24 If it's stable and required, and then someone tries to flip it to be opt-in, we would not stop that today, but we probably should.
**Daniel Dyla (Dynatrace)** 22:31 Yeah, I guess the only… Reason anyone would want to do that.
is… Let's see… Is something that people think doesn't change, and then it turns out it… does?
**Josh Suereth** 22:48 Yeah.
**Daniel Dyla (Dynatrace)** 22:49 I don't know, browser user agent would be probably an example of something that people often assume never changes.
But… that isn't correct?
Or something that…
we think is safe, but turns out to be, like, a PII leak or something like that.
I would say both of those…
**Josh Suereth** 23:11 But,
**Daniel Dyla (Dynatrace)** 23:12 fall into the idea of, like, exceptional cases.
**Josh Suereth** 23:19 Yeah, both of those, I think, would be an exception.
Yeah.
Okay, so let me write this down. Forcing often for… Experimental… We need someone's bigger.
Entity is fine, leave a note.
With what it should stabilize.
into Zenda.
recommending, etc.
Intensity… Has to be required.
don't allow.
And then… Hopped in… What else were we seeing that… oh my god.
Somehow, I learned a hotkey right there that I don't know what I clicked.
Oh, I'm not sharing the right tab.
Identity has to be required, and… And… that's the opt-in thing.
Right, don't allow… compared to what I'm doing.
They're awesome, Carl, Carl Awesome. Okay, cool.
I think that's… that's mostly what I wanted to talk about, and then I wanted to do a quick follow-up of active PRs, if that's alright, and… and work.
**Daniel Dyla (Dynatrace)** 24:45 Yeah, that says don't allow required to opt-in, but also we wouldn't allow that to go to recommended either, would we?
**Josh Suereth** 24:54 Yeah, yeah.
**Daniel Dyla (Dynatrace)** 24:55 I guess… actually… The only difference between required and recommended is that… You can't disable required attributes.
If you switch it to recommended, it's still on by default. It would require configuration intervention to stop emitting it. Yep. That might be…
for both of those exceptional cases that I mentioned earlier, that might be a way to move forward, but it, yeah, it doesn't matter. I think as a general policy, we can just say, don't allow it to downgrade, and if something comes up in the future, we can address it later.
**Josh Suereth** 25:37 Yeah, the other thing I'm thinking about
Is whether or not descriptive attributes should ever be required.
**Daniel Dyla (Dynatrace)** 25:46 Descriptive attributes.
**Josh Suereth** 25:48 Yeah.
**Daniel Dyla (Dynatrace)** 25:49 I would say…
Yeah, I mean, we'll definitely want them to be recommended,
I guess, like, if you're emitting… identity-only entities…
**Josh Suereth** 26:12 Because implicitly, we think it's fine to drop
descriptions, right? So, that's why I think…
It should never be required that you have a descriptive attribute.
**Daniel Dyla (Dynatrace)** 26:24 Yeah, because the whole description might be dropped.
Yeah.
**Josh Suereth** 26:29 So you need the system to work in the event that the description is dropped.
So…
**Daniel Dyla (Dynatrace)** 26:37 Yeah, that seems reasonable.
**Josh Suereth** 26:40 Cool.
So then, let's see, we have,
Did I… did I open… I didn't open this yet.
Alright, let's look, let's look at our project board quick.
We had a bunch of stuff in progress and active. I tried to move things around here. So, entity merge algorithm. Did you have a chance to take a look at this again?
the PR.
**Daniel Dyla (Dynatrace)** 27:08 No, I have not looked at it.
**Josh Suereth** 27:11 Okay, I updated all the things, I'm just waiting for… apparently I screwed up one of the links. Just waiting for the entity sig to,
basically…
approve this, but yeah, updated all the things from our discussion. So, the merit grounds, it's split into the resource part, the entity part, you know, it talks about handling failures. The thing where I was trying to be clever and, like, allow more things to go through, I locked down, so…
you just drop the one entity, if there's any kind of conflict with attributes now, so…
**Daniel Dyla (Dynatrace)** 27:44 Okay.
**Josh Suereth** 27:45 Yeah.
Alright, that's the merge algorithm. The startup specification, I think you were working on the prototype, so I assume these are still pending that, right?
**Daniel Dyla (Dynatrace)** 27:57 Yes.
**Josh Suereth** 27:58 Okay. Yeah.
**Daniel Dyla (Dynatrace)** 27:59 I wanted to finish the… Multiple resource prototype first.
Just so you know, as far as prototyping work goes, I'll be gone end of this week and all of next week.
**Josh Suereth** 28:15 Then I'm home for 2 weeks, and then I'm gone…
**Daniel Dyla (Dynatrace)** 28:18 For 10 more days.
**Josh Suereth** 28:19 So, I have…
**Daniel Dyla (Dynatrace)** 28:22 limited availability over the next 2 months, I guess.
**Josh Suereth** 28:25 That's… that's fine. Mostly what I… I want to get the merge algorithm in, and I want to start actually getting entities to show up in SDKs.
I've gung-ho on that. Like, I really think we need to start getting the resource merge algorithm implemented in SDKs, entities showing up.
the ability to define entity detectors, the ability for the config group to rely on entity detect… so the config group defined a resource detector with a name which matches the entity that we have, so I want to leverage that and have that actually detect the entities when that.
**Daniel Dyla (Dynatrace)** 29:01 Okay.
**Josh Suereth** 29:01 So, yeah.
That's… that's actually what I'm more gung-ho about. Okay. New resource entity references, proto-message, this was collector work. Dimitri's in here, so…
And then he was working on, the other phase here. Alright, I think I added something else in here.
MD to Jen.
Breaking chain specification resource. Yeah, this, this we still have to figure out how to…
To note to people that, attributes are no longer considered immutable in the resource specification.
Which I… I don't think we're ready to do until we actually have a specification we're ready to start stabilizing, right?
**Daniel Dyla (Dynatrace)** 29:49 Yeah, I agree.
I mean, maybe… the first communications should probably be around…
Like, the initial availability of that spec.
**Josh Suereth** 30:04 Yep.
Yep.
Okay.
And then… this here…
I think we are getting lucky in that I can archive this, we don't need this anymore.
**Daniel Dyla (Dynatrace)** 30:20 You're already doing this.
**Josh Suereth** 30:22 We're making a version 2 file where it's not gonna be diff-based now anyway, so…
We'll have everything we need from Weaver going forward. Okay.
I actually just put out
a PR, where now you can resolve from remote things with dependencies.
So, we can actually publish a schema file, we can resolve that schema file, and use it to resolve, like, our own
conventions?
**Daniel Dyla (Dynatrace)** 30:49 Cool, okay.
**Josh Suereth** 30:50 So, like, for JavaScript, if you wanted to depend on Semconv.
And then, define your own, and have that, like, layered hierarchy, and it all works now.
We're not…
**Daniel Dyla (Dynatrace)** 31:03 Yeah.
**Josh Suereth** 31:03 We cut a release where people can start trying it out, but the, there's still a few more things for us to do. It's not clean, but it's all working, so that's.
**Daniel Dyla (Dynatrace)** 31:12 There's definitely two… two major use cases that I think that'll be useful. The first is…
Like, language-specific runtime metric things that are, like, there's no reason to stabilize it across all the other languages, because…
Why would Java care about, like, node runtime metrics?
And the second is, like, prototyping… Unstable instrumentations and publishing…
You know, before it's ready for the main STEM comp.
**Josh Suereth** 31:45 If…
**Daniel Dyla (Dynatrace)** 31:47 Yeah, cool. Okay.
**Josh Suereth** 31:49 Right, and I don't think I see anything else in here.
for us to really talk about right now. I had a bunch of comments on Dimitri's relationship spec that I think we need to dive into deeply, but…
You know, without…
**Daniel Dyla (Dynatrace)** 32:05 He's not here.
**Josh Suereth** 32:05 It's worth just the two of us.
**Daniel Dyla (Dynatrace)** 32:07 He said he's gonna push, the entity event spec PR changes today. It looks like he hasn't done that yet, but.
**Josh Suereth** 32:16 We should review that then.
Cool.
So I… there was something else in here that I remember… Okay.
I… I… I want to get these, specification PRs through, because I want to start getting NC Detector in.
When do you think it's worthwhile trying to push, like, Java prototypes, to actually be merged into the SDK?
Like, do you think we're at that stage now, or do you think we should finish… oh, god.
**Daniel Dyla (Dynatrace)** 32:53 We only have OTEPs, we only have unmerged OTEPs, we don't… there's no spec, so…
**Josh Suereth** 33:00 We have… we have merged OTEPs, we have no…
And we have some spec merged.
But I think the important bits of the specification are not merged yet.
**Daniel Dyla (Dynatrace)** 33:09 We only have the data model spec merged, as far as I know, right?
**Josh Suereth** 33:12 Yes, we don't have any SDK spec merged.
**Daniel Dyla (Dynatrace)** 33:16 Yeah, I think we need at least some experimental spec merge before we can start pushing any languages to start merging things.
**Josh Suereth** 33:23 That's what I'm thinking. Okay, so I… I'd.
**Daniel Dyla (Dynatrace)** 33:26 And it's fine to just call it experimental, and like, you know, that's why the prototypes are there. We show… we prove the concept, merge it as experimental, start to get implementations in, and see if there are problems.
**Josh Suereth** 33:39 Yep. Okay. So, I think the next step would be that entity merge algorithm is my number one to get merged in from the data model, because that was the foundation to then make the spec.
**Daniel Dyla (Dynatrace)** 33:50 Okay.
**Josh Suereth** 33:51 So, and I'd like to get a-spec PR out.
Maybe when you get back in March, I don't know.
But… Okay.
Cool.
Alright, I gotta go, because my cat's probably gonna…
actually disconnect me pretty soon anyway, for some reason.
**Daniel Dyla (Dynatrace)** 34:13 Yeah, well, have a good one. I'll see you, yeah, probably not for, like, 2 weeks.
**Josh Suereth** 34:18 Okay, alright, we'll see you then, man. Have a good trip.
**Daniel Dyla (Dynatrace)** 34:21 Yep, thanks.
