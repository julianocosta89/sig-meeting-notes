SIG: Semantic Convention Tooling
Date: 2025-12-03
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/xOMskHhyNPNWaOScVBJ3_FOYHk3frJ5dUBocB6FI-vf0Dclv3FDPAuhau5OQrdOU.oslEe3YqIlvYyHjr
============================================================

## Zoom Recording Transcript

Jeremy Blythe 00:02:19 Doesn't look like we're gonna get too many people.
Nathan Smith @ Elastic Observability 00:02:26 Yeah, I just came to listen in, so… I don't… I don't have anything.
Jeremy Blythe 00:02:33 Okay.
Yeah, I'm just looking on Slack, Josh is looking… offline. Liva is showing away, and Laurent is on vacation.
So… I think… Oh, hang on.
And as if by magic.
Josh Suereth 00:02:58 Hey, sorry I'm a little late.
How are we all doing?
Jeremy Blythe 00:03:01 Good, I was just like, oh, I wonder if anybody's coming today. There you go.
Josh Suereth 00:03:07 Yeah, it's, Sorry, I had… I got distracted. I'm actually writing some Weaver code, and I got enwrapped in it, so…
Jeremy Blythe 00:03:16 Fun times.
Josh Suereth 00:03:21 Okay.
Let's get started. What do you say?
I want to do a quick, triage, if that's, if that's alright, Jeremy?
I haven't looked at the triage board in a while.
Jeremy Blythe 00:03:42 Cool.
Josh Suereth 00:03:44 Okay. Or at least look at issues that came in.
And then… Okay, so… Let's do this.
Add missing features in telemetry schema.
Liudmila Molkova 00:04:12 Should we kill it?
Josh Suereth 00:04:15 Yeah.
I forgot these are… these are kind of old. One thing I wanted to do as well.
I didn't close this, the Rego policy violation properties, but should I close this with the one The violation rework.
I see.
Liudmila Molkova 00:04:49 It should be closed, it's done.
Josh Suereth 00:04:52 Yeah, alright.
Sorry, that was an itch I had to scratch, and apologies if that came hot and awkward.
Let me get… The pull request to mark it as closed.
What was that one?
Here we go.
Come on, GitHub.
There we go. It does… it never updates, yeah.
Fixed with blank.
This is actually a bad view, this is not the view I wanted, unless we have things added here.
And… I want to go to the very… the newest things. Okay. Zeus Active.
Jeremy Blythe 00:05:41 I think that's some weird spam.
Josh Suereth 00:05:45 Yeah.
Okay, nose.
Relevant.
Slash incomprehensible. 2.
Okay.
Is that too harsh?
Jeremy Blythe 00:06:02 The account… I looked at it this morning, the account associated with this was opened a month and has made this one issue and done nothing else.
So, I think it's just a spam bot thing.
I'm weird.
Josh Suereth 00:06:14 Right.
dependency dashboard… Oh, this is, this is Renovate, where Renovate is. One thing about Renovate that I found, there's a bunch of chores here around, like, metadata actions, setup, build X, build push.
download artifacts, upload artifacts. All of these things it's trying to do are conflicting with, cargo discs.
So, literally all the PRs cannot be made because Cargo Dist owns those versions. So, I think we need to either teach Renovate about Cargo dist, or find a way to remove that from its… list, and I haven't figured out how to do that yet. The other one here is Scheemars has a 1.0 release. I tried to update to Scheemars because it fixes the bug.
Where we couldn't, like, where we had to, like, manually copy-paste things. In the 1.0 release, Scheemars removes access to the data structure of schemas, so it broke a couple things.
Unfortunately, we have to wait for the entire Rust ecosystem to support Scheemars 1.0.
It's breaking change.
So, we can't take that one in yet, either.
Yay.
Some of these other ones just need some time. Rigorous, going to 05, I think we should pull in soon, etc, etc. Okay.
That's that.
Allow attributes to be excluded hidden from signal definition.
We ought to define a view of an entity such as process, which is tailored for an implementation windows. In the case of an instant to the process like secret attribute would be excluded.
Oh, this is, like, in refinements, we want to hide things from the parent that aren't relevant.
Liudmila Molkova 00:08:04 Or, I think if we support identity refinement, Then… we don't.
Then we could have a base definition that's the most common denominator, and add things to refinements.
Josh Suereth 00:08:22 Okay.
So, I think this is kind of a to-do figure out how to solve then, but not… not on the shortlist, I think, for now.
But I'm not sure. Okay.
Define profiling signals using Weaver, that's TBD. Instrumentation scope.
This is about… Setting scope. We've kind of removed that feature for now.
Of being able to define instrumentation scope at all, or the collection of attributes?
I think I'm gonna leave this as, like, a TBD, Min-max event severity definable in model.
This one, I think, should just be… an annotation. What do you think?
Liudmila Molkova 00:09:08 So we… oh, actually, we talked about it yesterday on the LogSig, and… Turns out… okay, so, there is a good portion of feedback that there are tons of logs without severity at all, and it sucks. And we actually want, event authors, both applications and semantic conventions alters to provide severity.
But severity is contextual, and it's not mean and max, like, why should we do mean and max? What we'd like to do is to have a default severity.
And maybe it can… I don't know. The exception is error by default, but it can go lower. The page view is, I don't know, info by default, but it can go higher.
And… We want to enforce it.
I think we should have a, like, a policy that, in life check, that, marks events and logs without severity.
And it should be a property, the top-level property.
Josh Suereth 00:10:27 There it is.
Great.
I'll just make this comment about… and then we can rephrase the issue and repurpose it. Sound good?
Okay.
Liudmila Molkova 00:10:39 Thanks.
Josh Suereth 00:10:41 I'm gonna put that under V2 schema as well.
Actually, no. Not gonna put it under V2 schema. We'll move it over when we're ready to work on it. Alright, is… Other issue that came in that's not in this board?
Recently.
I don't think so, I think that's it.
Go ahead, Jeremy, sorry.
Jeremy Blythe 00:11:04 I was just wondering if we could have… like a tag, maybe, for live check, so anything that's to do with live check, we could just tag it.
Josh Suereth 00:11:11 I don't know, just an idea.
Yeah, yeah, yeah. If you… I think you have edit access to add a tag. Do you want to add a live check tag and then throw it on there? Yeah.
Okay.
So… Next up, I just wanted to check, V2's schema. We have generate schema from Rust models. I think this is now done.
But we haven't finished actually using it, so there's now a command that does JSON schema. I just updated it to V2, where you can dump the V2 resolve schema and dump the V1 resolve schema separately. Thanks for reviewing that, Jeremy. So I think we can actually close this. The only difference is… We don't have… we don't check it into the repo.
So we would actually want to make some kind of a GitHub automation process that would dump that into the repo at some point. My… I think people might be using the main version, so we have this awkward problem where I would love to have it auto-update as we write code.
And then people use the tagged version of the schema from GitHub instead of pulling in the main version.
But I'm not sure what we want to do there. We can also actually… we can also include it in release artifacts, so… I can show what that might look like.
How do folks feel? Like, add it to release automation, or do something else?
Liudmila Molkova 00:12:42 I think we can add it.
I mean, I don't… I'm not worried about people who use main version.
Josh Suereth 00:12:50 Like…
Liudmila Molkova 00:12:51 They should switch to tags.
Josh Suereth 00:12:54 Alright, the next question is, should we add it to… when we make a release, should we actually have it as part of the release assets?
Would this be the best way to send it?
Liudmila Molkova 00:13:08 And the way… the way we do this today is that we just take the raw GitHub URL.
Yep. You give it to your VS Code config or something, and it caches it, and there is no problem at all with the current approach. We can include it, maybe?
as if… File…
Josh Suereth 00:13:29 I think it's included as an asset, I think you can still download it pretty easily, but you also get this attestation junk, so you can make sure that you're using the one that we provided. Not that that's important, that's for schema, but, you know… I'm just trying to figure out what's the easiest automation path here.
We either need something which will commit to the repo.
after a PR that updates the schema.
which I think is a little awkward, or we can publish it as part of a release.
Jeremy Blythe 00:14:00 we could… We could, like we do for semantic conventions, right? We run a thing that checks to see if it is different.
And then it fails the build, and then you run it locally. It's a little bit clunky.
Josh Suereth 00:14:15 Yeah.
Jeremy Blythe 00:14:16 It kind of ensures that it's done and it's part of a release.
Josh Suereth 00:14:21 Yeah, I mean…
Jeremy Blythe 00:14:22 It flags it than if you're making something that would change the scheme of you to go and have a look as an author.
Josh Suereth 00:14:27 You should take a look so you can see it in the div. Yeah, that's fair.
I'm okay with either of those. I prefer… I personally prefer just shoving it in here and having it be part of our release process, but.
Jeremy Blythe 00:14:42 Then we would have to make sure that in… Users could go and access it.
Like, we would be able to create the URL to go to this place and get it from here, because it won't be in the repo, right?
Josh Suereth 00:14:54 Well, this is… I don't know if you can see the URL here.
I'll put it… we'll come back over here.
triage.
Jenking schema.
So that would be, like, let's say I called it, you know, weverse email.json or something. That would be the URL.
Jeremy Blythe 00:15:18 Okay. Yeah, no.
Josh Suereth 00:15:20 which I think is reasonable. I don't know if that works with Visual Studio Code, but I'd love to try it, I guess, if you're okay experimenting with that for one release. If it fails, we'll go to the other method.
Liudmila Molkova 00:15:34 I-I'm trying it now, and… there is something in this, if I just… oh, okay, so this… there is a redirect. Anyway, so if I just take the… this URL, and I paste it in my browser, it will first redirect, then it will download a file.
Versus the current state of things is, that they do the raw URL, and it works nicely.
Josh Suereth 00:16:03 It shows you the file and doesn't force you to download it, yeah.
Liudmila Molkova 00:16:05 Yeah.
Josh Suereth 00:16:06 But I guess the question is, if, you know, for Visual Studio Code, will it work if I just copy-paste it in there?
Like, is it a problem? You're saying that when people configure this, they just want to take the URL and post it somewhere, and have Visual Studio auto-validate with that, right?
Liudmila Molkova 00:16:24 Yeah, so… Let me see. We can keep going, I'll just try with some random file, and we'll see what happens.
Josh Suereth 00:16:32 Okay.
Alright.
Liudmila Molkova 00:16:35 So, let's get on to the main agenda then, because that, I think.
Josh Suereth 00:16:42 Alright, all that remains here is to figure out how to automate, Weaver registry, JSON schema.
And dump the output into… consumable… Locations on our releases.
Tags. Okay.
Cool. That is… let's see, was there anything else in here?
Disallow requirement level in the identity section, that is a to-do, I'll take a look at that. Define spanned links in YAML.
Is this something we want to do? The ability to define links?
And required links when you generate a spin.
Liudmila Molkova 00:17:33 I'm gonna be a business.
Josh Suereth 00:17:34 Yeah.
Liudmila Molkova 00:17:36 It was important for messaging.
We currently define it in… Mark down.
It's important, I think, for valid… for life track, for example.
Josh Suereth 00:17:46 Y-yes, but I guess how… how are you validating the links, right? Like, when… Is there a particular span type where you know that there will always be a link?
If the answer's yes, then cool, I think we should add it. If the answer's no, I think we probably define links as their own thing that get validated.
And we say, like, like, think of it the way, you know how entities, there's an entity ref, and we validate that, like, you're associated with an entity of a particular type? Imagine if we define links and say this link will be associated with spans of this type.
Does that make more sense than to define spans having a sub-thing called link?
Liudmila Molkova 00:18:33 I see, so… There are multiple ways to… Define links, and it's not the burning need.
Josh Suereth 00:18:43 Yeah.
I guess… well, let's just ask the real important question. Do we think we can add links in a non-breaking way to V2 schema?
Liudmila Molkova 00:18:52 Absolutely, yes.
Josh Suereth 00:18:54 Great. Then let's defer this. How do I… Maybe we make a new label that says, you know.
like, V2 Phase 2 or something, like, these are features we will add to the V2 schema.
post-V2 adoption.
that we think we can do in a non… like, I wanna… I wanna actually denote what we think we can add this in a non-breaking way. I'll just add in a comment for now.
We… Add expand links to V2 schema.
None.
Breaking away, going forward. So, we're going… Defer this work until after.
G2, Lance. Okay.
Great.
What else did we have in here? Generate JSON schema from us, disallow, requirement section, and decide what public attributes are and how they work, and then we have a model. This is still TBD. This is probably a bigger discussion than I want to spend time on. Let's get to Jeremy's, if everyone's okay with that.
Okay.
Cool.
Message templates. Tell us more, Jeremy.
Jeremy Blythe 00:20:11 So… Martin had this, idea request that, LiveCheck produce log records, so I'm… So… I was adding that in a PR.
And Caleb an example.
And he's like, oh, but can't it do… can't it do this? Surely this is how everything works, was kind of how it seemed to be phrased. I'm like, I don't know, I've never seen this before, so… I guess the question is… And there seems to be some uncertainty as to… This… well, for one, this seems like a specification on top of…
Josh Suereth 00:20:54 Doing logging.
Jeremy Blythe 00:20:55 Right. Logging, open telemetry logging doesn't say… All logging must be message template.
So, when I read the OpenTelemetry, because I don't do a lot with logs, but when I read the OpenTelemetry, like, profile or whatever, it says the body of the… Log record can be the human readable string, or it could be a complex multi-line thingamajig.
Whereas this message template thing implies that you put… Like you're seeing here, you put in the body of the log record something that has the template Of the human readable string.
Not the interpolated human readable string.
And then you provide those pieces as attributes elsewhere, and I've never seen this before.
And so, I guess we need to decide, is… Someone who knows more about logging than me.
can tell me, is this, like, is this how the world works? Is this what everyone does? And therefore, is it, like, super obvious that this should be the way that log records work?
That we emit from… Weaver? I don't know.
Liudmila Molkova 00:22:13 This is how the world works, but varying my open telemetry, log-seq, had I would tell that The… the… do we want human-readable messages that are different, like, the… that are formatted?
Like, why?
So, the reason this world works this way is that the formatting is lazy, and only the level is enabled.
But in our case, well, it makes sense, it saves some performance, still, but, Ideally, if we write it the console, I want them to be formatted.
Right? It's the users who read it, like, from top to bottom.
If we write it to a backend as a telemetry.
Then, presumably, there are tons of them, and somebody would query them.
And they rarely care about, like, the human-readable messages, at least that the human-readable messages contain all the information.
So, we already have all the information, actually, for querying in the structured part.
Right? So… It… I don't even know why we… Have to include a human-readable message.
And I don't care how it's included, anyway.
Jeremy Blythe 00:23:42 So what I… what I implemented… So my, my naive implementation was… I go and get all of the attributes that are to do with The live check sample, the finding… And I put them in the attributes section of the log record.
And then the… Rendered message, let's say, that we normally put into the console.
I'm taking that rendered message, and that's the body of the law record. That's what I've… that's what I implemented.
Liudmila Molkova 00:24:13 This is the common convention, so, like, if you look into what OpenTelemetry does in general, is that we take the fully formatted body.
And we… If, let's say, use some Rust login thing, we would take the fully formatted body.
And put it in the log record body.
This is a typical way. I think Martin, what he wants is makes sense, but I don't think this is what we usually do in OpenTelemetry.
Jeremy Blythe 00:24:42 Okay.
Liudmila Molkova 00:24:44 I think we even had, an attribute for this, or we had an active discussion, Let me find it.
Josh Suereth 00:25:03 So, the specific ask here is what?
Liudmila Molkova 00:25:10 I think Martin wants the… Template, not the formatted body in the log body.
Jeremy Blythe 00:25:17 Yes.
Josh Suereth 00:25:18 from when Weaver generates logs, because we're saying policy findings would generate log records, and we would put the template in there.
Okay, one of the problems I have is, do we… like, when we have custom policies, is the custom policy gonna be a message template or not?
Like, we… this is a significant shift for all of our policies. Right now, we just changed policy where it's a human-readable message string and a context that could generate the human-readable. If we want it to be a template string and a context for that template.
We could do so, but that's not just a live check question, that's a, like, olive Weaver question.
So, I… I'm not against it, honestly, but we would need to be able to render these templates into human-readable in, like, a helper method or something.
Liudmila Molkova 00:26:16 And also, what Martin wants, I think, is the finding ID. It's already the low cardinality, Identifier.
Josh Suereth 00:26:28 Yeah, finding ID, we all… yeah, the… we already require that to be lower cardinality, right?
Liudmila Molkova 00:26:36 Yeah.
So, I'm pasting a link to the some kind of discussion on… I love this.
What should we do as template?
Josh Suereth 00:27:07 Because you're showing the… body here…
Liudmila Molkova 00:27:12 So the selection, if you look into the selection below in the screenshot.
Josh Suereth 00:27:20 Selection below in the screenshot, right here.
Liudmila Molkova 00:27:22 Yeah, so this one. So you see the namespace… oh.
Now, this is the body, right?
Josh Suereth 00:27:28 Right, but that's the body, which is the human-readable part. The actual, ID is here.
Which is the low carriageability thing. Yeah.
Jeremy Blythe 00:27:37 All… all of the… All of the things are there.
So the section where it says Weaver Finding Context… dot?
Blue.
Yeah, that, so what I… so… In a policy finding, there's a JS… there's a JSON block.
And so what I… what I'm doing is I'm… I'm… going through that JSON book and flattening it, so anything that's mentioned in there appears after context dot, so that's like a… it's a template.
Josh Suereth 00:28:08 That's a template type, right?
Yep. So everything is present.
Yep.
Jeremy Blythe 00:28:16 But I'm not providing a templated string anywhere.
Josh Suereth 00:28:20 Right, but I think that's… policy doesn't do that, right? If we go to…
Jeremy Blythe 00:28:24 It doesn't, no. It just has a string field.
Josh Suereth 00:28:27 That's why what I was saying was, if we do… is that under di… Oh, it's not under source. It's under Weaver Checker?
Is that what policies are?
Jeremy Blythe 00:28:37 Great, so yeah, we the trick guy, yeah.
Josh Suereth 00:28:40 So if we look at our finding, sorry. If we look at a finding, right, we have a context and we have a message.
What I'm suggesting is, if we want to adopt Henrik's thing, which I'm okay doing.
We would actually define this as a message template.
That would match this.
And it would use context to fill it out. And then we would have Code in Weaver that can construct the human readable string by filling out the message template, and then when you log to OTLP, you would still have the template. But the problem today is, literally you can't do what he's asking, because we… We are forcing this to be human-readable for our own logging.
And so if you make it a template, we have to have something that erases the template anyway.
So, I'm okay going that direction, honestly. Like, if you wanted to make the change, Jeremy, to say, this is now a message template string.
and we changed the toString on policy finding, I don't remember where it is, the thing that just writes message, to change it instead to, like, render the template.
I'm fine with that. I think that makes a hell of a lot of sense for policy from Weaver, right? It gives us a lot of flexibility.
Liudmila Molkova 00:30:00 Then there wouldn't be a body.
And, immediate thing.
Josh Suereth 00:30:07 I think our logs don't need a body at that point. Or, your body would be the entire log, and you would also send the message template, which is an explosion in size.
Liudmila Molkova 00:30:23 Right. I mean, the message won't be included, and if there are some… any reasonable, interesting information there.
It's lost.
Josh Suereth 00:30:32 No, you can regenerate the message.
From the template. So theoretically, if you have a message template.
And you have… and it… and it fills its data from context, you should always be able to create the human-readable string.
Liudmila Molkova 00:30:47 Yeah.
Josh Suereth 00:30:47 Cool.
Liudmila Molkova 00:30:49 But, to your point, people are writing custom advises, custom policies.
Josh Suereth 00:30:55 Yes, and it puts another layer of abstraction to that. So instead of using string format, which we're using now in all of Rico policies, you would have to understand that Weaver will string format on your behalf with this message format thing.
Jeremy Blythe 00:31:21 For me, it's not a… so much a question of… It's more of a question of… Is this a… Is this a convention that we should be… Hold on, like, yeah. Bye.
It's an expectation that this is what we should be doing.
But for… for use… for… Users of this new feature.
Because straight away, Martin was like, this is weird, the body doesn't have a message template.
Liudmila Molkova 00:31:55 This is not the typical convention for OpenTelemetry. In OpenTelemetry, we use fully formatted log body in the message. We are free to break open telemetry convention here if we think it makes sense.
Jeremy Blythe 00:32:08 Right.
What do we… what's the…
Liudmila Molkova 00:32:15 Implementing it would be a big deal.
Jeremy Blythe 00:32:18 Yeah.
Liudmila Molkova 00:32:20 And is it really that important? I don't think it is.
Jeremy Blythe 00:32:24 I think that's where I'm coming to, really, is, like, it seems like a lot of work, and if it's I'm like… If it's something that's… You know.
I think my problem is I just kind of… I'm coming at this as someone who doesn't really use logs at all.
Like, everything we do in my company has spans and metrics, and I very rarely touch logs, so I'm like, I don't have any sort of world knowledge of You know, there's a spec, and then there's, like, what do people expect?
So, that's why I'm a bit stuck. But if what we're saying is, we're open telemetry, we're making an OpenTelemetry tool, we're going to provide things according to OpenTelemetry.
then we would do what I've done.
Liudmila Molkova 00:33:20 Right, and I sent a couple of links, if you open the second one, this is where we actually discuss, having a special attribute for the template, if you want it.
Josh Suereth 00:33:39 And… You said the second one is the one with that? That's the first one I caught.
Liudmila Molkova 00:33:46 And it…
Josh Suereth 00:33:48 No, the second one's the first one I copied, so…
Liudmila Molkova 00:33:51 Right.
Josh Suereth 00:33:55 Okay.
Yeah, I think this is basically saying there is no consistency on this message format thing yet. So, if we did it, it should be optional.
That's my take.
I… I think, Jeremy, given the amount of crap we're dealing with right now, it… architecturally, you don't have the ability to take a suggestion without major changes to how Weaver Regal policy works.
Right? And changing all custom policies to support it. So, my suggestion here is, let's defer this, and if we want to make the braking change later because we think it's important, great. If we want to make it an optional thing we support later, we can do it in a non-breaking way.
Jeremy Blythe 00:35:07 Okay.
My next question, then, is I heard amongst that… that… We shouldn't be… we shouldn't have a body at all.
What's that?
Right.
Liudmila Molkova 00:35:16 No, the semantic conventions, events should not have a body, as a rule of thumb.
Jeremy Blythe 00:35:22 Okay.
Liudmila Molkova 00:35:22 But… Any logs that are emitted by the applications or tooling is… are absolutely free to have them.
Jeremy Blythe 00:35:32 Okay, so I'm emitting these as events, so I'm giving them an event name, which is… We, the something… policy finding, or something like that. I can't remember what it is now.
Weaver life check policy binding, something like that, as an event.
That's the event name. So does that… that means this is an event, and therefore that means it should not have a body, is that right?
Liudmila Molkova 00:35:59 For semantic conventions, events, like, if we define this event and semantic conventions repo.
We would not recommend to have a body.
Jeremy Blythe 00:36:09 But…
Liudmila Molkova 00:36:10 even if we did this and defined it in semantic conventions, and you would come and say, okay, the body is actually very important there.
We would be very interested to learn why, and maybe we would change the policy, because this is… we're starting very restrictive, and if we see a good set of examples that events need a body.
we would, reconsider, like, relaxing it.
Jeremy Blythe 00:36:38 Okay.
Because I… what I was thinking, I would just put Weaver Finding Message.
And put what I've got in body into a weaver Finding Message.
Josh Suereth 00:36:47 Yep.
Jeremy Blythe 00:36:49 My leap body empty.
Josh Suereth 00:36:51 I think that's totally fine, but then you match the structure.
Liudmila Molkova 00:36:55 But then, the body is… Redundant, right?
Jeremy Blythe 00:36:59 Yep.
Liudmila Molkova 00:37:00 But now it's redundant, and the body is, I think, the right place for it.
Like, all the structured information is there. Hiding it as an attribute doesn't… Open anything. You can just stop emitting the body at some point, if there is no use for it.
Josh Suereth 00:37:17 Okay, so you're saying we would have event name nbody, so you get a human readable string if you want it as body, and that's fine, that won't violate things.
Liudmila Molkova 00:37:26 No?
Okay. I think that the thing as they are today, it matches my mental model, and, like, we would print body in the… I don't know. Imagine we had a console exporter, which… which we, to some extent, do.
We would print this body in the console, it makes total sense there.
Josh Suereth 00:37:46 Okay.
Cool.
Jeremy Blythe 00:37:50 and what I've… so… you're saying what I've done, what you're looking at right here on the screen.
You're saying that's correct?
Liudmila Molkova 00:37:58 To me, that's correct. I will probably leave a comment, because I'm curious why we use advice in one place and finding in another, but, like this, structurally, it looks… like, what I would imagine. Totally matches my own… Idea of how it should look like.
Jeremy Blythe 00:38:16 Okay.
So my follow-on from this when I was doing this is… If Weaver is now creating things, it should be a good citizen and have its own conventions, right? So… Surely Weaver should have a set of… semantic conventions to… for itself. And then it should generate code for itself, right?
Josh Suereth 00:38:42 I don't…
Liudmila Molkova 00:38:43 It doesn't have to, but defining conventions, like, we should practice what we preach, and we should define them, we should be the guinea pig for this, for sure.
Jeremy Blythe 00:38:52 Yeah, I mean, if, like, we… we can't, you know.
I'm just throwing in random things here, like, I'm being… I'm being, like, pretty bad. I don't… I'm not following a model or anything, so… Feels like, we should practice what we preach.
Anyway, it seems… I seem to have opened a can of worms by just going, like, oh yeah, I can make logs quick.
Liudmila Molkova 00:39:21 Hmm.
Josh Suereth 00:39:22 I will… like, just frankly, I think the whole… Get rid of, body from events, and what we define in Weaver is… in an awkward spot. Like, from what… just… Defining events makes sense, but if there's going to also be logs that have bodies, and there's no way to represent them in Weaver, I get from semantic conventions we don't want that, but from a Weaver standpoint, people want to define logs. And we need the ability to kind of live check them, we need the ability to look at them, like, I… I wonder if we need some sort of a definition of a log.
even if… that includes body, even if, from semantic invention standpoint, we're not going to support that. Just because people can do it, people will want to verify it, like, doesn't make sense for Weaver to do it. We keep running into confusion here around this, so I feel like… I was… the thing that you're saying matches your mental model did not match my mental model at all, of whether or not you should include body. So I'm with Jeremy of, like, I think we need to be more clear here, of what… what is… what is going on with event, what is going on with log body.
Jeremy Blythe 00:40:41 Okay.
Josh Suereth 00:40:41 My thought body was basically disappearing.
Liudmila Molkova 00:40:47 Yeah, it's, it's, it's that.
Josh Suereth 00:40:50 Okay.
Liudmila Molkova 00:40:53 Ne- neither.
So, in my mental model, the, you can have a thing, which is log. You can look at it as an event, and then you probably don't care about body.
Because you query it. The main… the main persona is somebody who queries it and aggregates things, so it finds the needle in the haystack.
If you have a… you can look at it at the log… at the log, as a log.
And then, if you, let's say, printed the console.
Somebody can read these logs. But you're probably not querying it, you probably don't care about bodies when you query.
And it's just a human-readable representation of everything else.
And something can be both.
And this, this is an example of… Something that's both.
Jeremy Blythe 00:41:47 Okay.
Josh Suereth 00:41:57 Okay, so I think we should move on, but…
Jeremy Blythe 00:42:03 So, yeah, if, if, if,
Josh Suereth 00:42:06 Whether anyone wants to add comments on this.
Jeremy Blythe 00:42:09 PR, because I think I'm getting close to, like.
Wanting to take it out of draft.
In fact, maybe I will take it out of draft then, since we've had this conversation.
Yeah, I think you should.
Josh Suereth 00:42:20 Good.
Yeah.
Jeremy Blythe 00:42:22 Yeah, I've done some refactoring in here as well, because the advice The advice module was getting, like, really huge, so I've broken that up.
So if you… you'll see that I've… each of the advice types, I've put in its own module.
No? Because it was getting a bit out of hand.
There's, like, a thousand… 1,500 lines or something in one file that made me feel bad.
Josh Suereth 00:42:46 Yeah.
That's nice. That'll help review, actually. I noticed that when I was changing violation.
Jeremy Blythe 00:42:53 Yeah, it's getting a bit crazy in that.
Josh Suereth 00:42:56 Cool.
Jeremy Blythe 00:42:59 Alright, thanks.
Josh Suereth 00:43:00 Awesome.
Let's talk a little bit about V2 and the status of V2.
And work on V2. So one thing I started doing, was trying to make sure that everything is accounted for here. I talked to Lauren. I don't think he's gonna be able to work on DIF until January.
So I'm thinking about pulling in DIF myself, and, working on diff, directly.
There's a thing… there's a set of things with diff that I think will be interesting. For example, I want to know if we think we need diff for refinements, or just for, core signals, or both.
for telemetry schema purposes, we only need… signals. We don't need refinement diffs, because they should… one should account for the other.
But I am… I'm probably gonna do both in that. Am I… am I not sharing this? I'm not sharing this, sorry.
So yeah, that's Diff.
let's see, Registry Update Markdown. I was looking at this one recently. I have a refactoring PR that I'm about to send that actually shifts things around in Update Markdown.
it turns out that, you know how there's, like, a bunch of loose-hanging functions for how we resolve a schema and enforce policies, and it's kind of weird, Jeremy?
This uses the, like, an old version of that, not the latest one that everyone else is using. So…
Jeremy Blythe 00:44:42 I might take a crack at refactoring and creating, like, a…
Josh Suereth 00:44:47 thing called a weaver that has the… configuration that you've given Weaver Registry and Weaver Policy, and then that thing has a method called load, which loads all the files. It has a thing called Resolve, which takes a loaded set of files and turns it into a resolved set of files. On Resolved, you have a thing that says, like, here's the stuff to send to Forge, here's my other registry. Like, basically componentizing this into a more coherent workflow engine of how Weaver works.
and then, get LiveCheck to use it, get… well, get all the things to use this kind of workflow.
Instead of the raw functions.
The one most interesting function that I found out was the way we do a comparison against another repository. We have, like.
Part of the resolution step encoded in a weird way to avoid doing policies on the thing we're pulling in.
Jeremy Blythe 00:45:51 Yep.
Josh Suereth 00:45:52 Okay, anyway, I'm trying to basically clean all that up, and make that more… structured.
Jeremy Blythe 00:46:00 Okay.
Josh Suereth 00:46:01 and set, like, a lifetime for us. So, the… right now, I have 2… well, 3 lifetimes. I have… The configuration part, where I define my config.
I have a load thing where I basically load in all of the files and run before resolution rules and basic validation, and I have them all as raw instances. Then I have a resolve stage, where everything is resolved.
where I have, access to the optimized Resolve registry schema, and I have access to the forge schema, right? The thing that you send to render that is the unoptimized version, right? That you can use. So, it has both of those.
that's kind of my thinking right now, is we have those three stages, we make those three stages explicit, and we have things within those stages kind of hang off of structures as stuff that you can do. So I'm trying to get, like, checking policies to be a method On one of these structures that you can optionally perform or not.
Right?
So, instead of passing, like, 5 structures around.
function A, B, C. We have, like, a thing called a, you know, loaded… loaded weaver, a thing called a resolved weaver.
And on Resolved Weaver, you could call check after resolution policies. On Loaded Weaver, you could call check before resolution policies.
Jeremy Blythe 00:47:27 Hmm.
Josh Suereth 00:47:28 That thing will also have the policy engine that you would have access to in LiveCheck if you needed to… if you're getting your policies from the same place, the repository has them.
I think you actually load them from somewhere else, so I haven't sorted all that out, but I'm trying to… I'm trying to kind of clean up, if you will.
Because when we go to Adv2, all of the spaghetti explodes twice, and it's already kind of gunky from what I did initially, so I'm trying to go clean all that up.
Jeremy Blythe 00:47:58 So, with that… That's… that… that, from CLI to result… to, like, the completion of the resolution process. I think you're talking about that.
So…
Josh Suereth 00:48:13 Yeah.
Jeremy Blythe 00:48:15 Yeah, that bit is… Kinda ugly, yeah.
Maybe it's a… Maybe it's like a steam machine or some sort of builder pattern thing, where you go… I want this to be checked, and I want the then dot… run policies dot… Ding, ding, ding, ding.
Josh Suereth 00:48:37 Yeah.
Jeremy Blythe 00:48:38 Something like that.
Josh Suereth 00:48:40 that's kind of what I'm trying to sort out right now. If you have ideas for what that should look like, let me know. Let me show you real quick what I'm doing in Update Markdown, because this is the… one of my theories. What I did in Update Markdown to make room for V1, I'm actually creating a trait for the Markdown Snippet Generator that has the key methods that you would do, and the key actions that you would take.
And it… That's actually the default thing. This is the actual key action you take when you implement one of these, of, I want to update Markdown Contents, right? It doesn't tell me anything else about that, it's just to have a Markdown snippet generator that updates contents. If… And then I have a bunch of deleted code, because I moved it all. If we look in… that's the parser… if we look in V1, in V1, I create a snippet generator that uses the V1 stuff.
Right?
Template engine is not V1, but the Resolve registry is V1. So then I implement the V1 thing, and now what I can do in my code is I just say, if V1, use V1 implementation, if V2, use V2 implementation. I want to do that for the core loading algorithm in Weaver.
And trying to do that has been a pain in the butt, because of how decoupled everything is, and the, like, spaghetti. So I'm planning to do massive refactoring. That's the next thing I'm doing, is actually that refactoring. Because I did the refactoring for this, I did not implement V2 for Snippet Generator, because there's a lot of stuff to… deal with later, but I'm planning to do a big refactoring in the codebase around V1, V2 splits.
and that core engine loading, I'm gonna create something. If you have ideas for what you want it to be, let me know.
Because I am sort of hacking at this point. I don't have a clear, cohesive idea of what I want it to be. I'm sort of… Like I said, right now, the only stages I have are… there's a loaded stage, and there's a resolved stage.
and loaded is the peer files, and resolved is everything's been resolved. And you can go directly to the resolve stage.
If you load a resolved repo, That's why I have two.
Jeremy Blythe 00:50:57 Yeah, I kind of did something on this.
About a year ago.
to make it a bit better, because… At that point, it was… everything was copy-pasted.
Josh Suereth 00:51:10 No, the work you did has been… awesome to make it better, but yeah, I want to go further.
Jeremy Blythe 00:51:15 Yeah, for sure. The difficulty is that… We've got all those command line switches, like, you can have policies, you can have different policies, you can skip the policies.
You can compare with another model, you can, like… so there's loads of options in that… in that.
In that sort of loading, getting you to the… getting you to a resolved state.
There's a whole bunch of options in there that… I don't know whether… Yeah, they kind of need to… that state machine, whatever it is that's getting you to that… Point.
Those command lines which really belong to that thing.
Josh Suereth 00:51:56 Yes, yeah, and we're gonna sort that out, so… If this sounds reasonable, though, and this notion of, like, splitting things up into, Oh, wait, that's not the right one. This is the… Is it right?
That's… that's… there's impulse for, yeah, this thing, where we actually use a trait and kind of abstract out the core behavior.
Between V1 and V2.
If that makes sense, that's kind of what I want to go towards.
Jeremy Blythe 00:52:24 Okay. So…
Josh Suereth 00:52:25 you get a thing called a loaded, which is sprawl, you get a thing called a Resolved, or a, yeah, Resolved, which is after resolution. They both have the ability to fire at templates, they both have the ability to… like, you can go from loaded to Resolved, but I think we need the ability to load in a Resolved repository without doing Without looking at all the raw templates and doing the resolution step, which we don't have today.
So, this refactoring would just give us the ability to build that. It doesn't actually do it.
Okay, that's my big thing for V2.
Next I wanted to check quick, registry search… Should I just deprecate it now?
Jeremy Blythe 00:53:07 I think we just… I think we deprecated.
Josh Suereth 00:53:10 Or do we leave it and have it not support V2?
I'm not sure how to deprecate it, is the problem.
put it in…
Jeremy Blythe 00:53:26 We could change it so it says… Deprecated.
Josh Suereth 00:53:30 I can add that, like, that's an option, is I can just add a thing that says this is deprecated, and then we can remove it after a certain version and denote that, but I wasn't sure what to do about it.
Jeremy Blythe 00:53:42 I think that's what we can do, and then we don't have to, you know, we don't support it for V2.
Josh Suereth 00:53:48 Okay.
Jeremy Blythe 00:53:48 I think searches… I would really like a search.
Josh Suereth 00:53:52 Yeah.
Jeremy Blythe 00:53:53 I would really like a such, but I don't think this is the such.
Josh Suereth 00:53:57 No, this was getting the scaffolding so someone else would implement it. I don't think that person is gonna show up at this point.
Yeah, so I think we killed that. Alright.
V2… well, it also could be that we just go AI gen something and see what happens, but that is… I think we have to deprecate what we have today.
Alright.
Ludmila, how are the V2 helper functions going?
Liudmila Molkova 00:54:25 Oh, I'm sorry, I… I got stuck on the problem that there is no… Okay, so in the past.
we got definitions, attribute definitions, from, the groups. The groups starting with registry.
Now, we don't have these groups in the result schema. We have a list of all attributes, which includes references and definitions.
And… I've got stuck trying to find a good place in Weaver Code.
to, have the distinction.
So one way I was thinking about that we would, have… The attribute definitions in attributes.
And we would have attribute refinements, and we would put all the references and definitions there.
Similarly to signals.
But then there is some… some plumbing that needs to happen, and I've got stuck on how to do the plumbing.
Because it's… it's somewhere in the resolution code where I need to add it.
And if you have some ideas, I would appreciate it. I will spend more time this week, on this.
Other than that problem, if we solve this, the rest seems to be trivial, because what our GQ helper functions do today is exactly what we created in Schema V2.
And it just simplifies them, having the schema V2 in the first place.
Josh Suereth 00:56:13 Yeah, I think this is the kind of feedback that I want. Like, we need someone using this in anger on SEMCOM to do templating and stuff, so we can get feedback and fix this. I do want to do a Weaver release once we have basic V2, that is a either beta or release candidate of V2.
That we can start, like… I want to start pushing this hard. Like, by… I leave December 18th for vacation, for… until January.
I would love to, in December, cut a release that lets us start prototyping V2 things and behaviors in semantic conventions, so that in January we can basically run through just a bug fix phase to get this out the door. I think there's some features we need like, publishing Resolve Schema, publishing diff, and, and, and, What that's gonna look like.
I want to be able to spend time on that, and kind of get the core stuff cleaned up, if possible. So… It's more important to me that you give us feedback like this attribute tracking thing.
than actually the helper functions themselves. Right? Like… Yeah. Yeah. So, if we need new helper functions, great, we'll add them. I agree with you that I think the new format is a bit better, and so I'm… like, one thing to think about is the, the actual Jinja template functions we've written, do those work with V2 schema?
And where do those break, and that sort of thing. Okay. So, for attributes, I hear what you're saying. I have an idea. We can talk about… we're running out of time. We can talk about that a bit offline. I'm gonna add that as a to-do here.
Need to figure out, lineage tracking is one of the things I'm gonna add for V2.
when I add lineage tracking, or when someone else does, because it doesn't have to be me, that's where all of the tracking you need to solve your problem would happen as well. So it could be there's a pairing where we want to do those two, at the same time.
does code cleanup for overall running Weaver, that's the thing we were just talking about that I added. And then input policies can be different between V1, V2.
this… we can look at that issue and resolve that then. I think we might have already made a decision there. Okay. Like I said, Lauren's not gonna have time for DIF before January, so that's something I might tackle next week.
Stats for refinements, I might just not do them initially.
We have an initial signal, like, Weaver Stats. I don't know if you saw this, I thought there's some interesting things I want to call out there.
looking at stats of semantic conventions, I think, is more useful than than not, and it's interesting to look at what they are. Lastly, we gotta get documentation.
Is there anything on here that folks feel they could pick up?
Jeremy Blythe 00:59:15 You can definitely give me the search thing. I know it's trivial, but I can put my name on that.
Josh Suereth 00:59:21 Awesome. Thank you.
Liudmila Molkova 00:59:27 I'll happily pick up documentation once I'm done with the, core part of the Jinja. Oh, sorry, JQ.
Josh Suereth 00:59:35 Yup.
I think that… that, would be awesome. Okay.
Cool. I'll do my two major refactorings here and start getting some of these features worked on.
And we'll keep going. If you haven't seen this, we're out of time a little bit, but I'll just show you this.
Jeremy Blythe 00:59:54 Lydmilla, this is a dump from the stats on V2.
Josh Suereth 00:59:58 Stats on V1 are similar, but it's just interesting types of things. We have a 51 cardinality enumeration In semantic conventions. That's fun. I also think this is interesting. In metrics, the most used instrument is the up-down counter.
Liudmila Molkova 01:00:16 Makes sense.
Josh Suereth 01:00:18 Well, it's interesting because it didn't exist prior to OpenTelemetry.
You know, there were just counters, gauges, and histograms in Prometheus. So I think that's… that's an interesting statistic there.
Liudmila Molkova 01:00:29 I have way too many gauges.
Josh Suereth 01:00:31 We had way too many gauges, and then actually poor aggregation because of that. Under spans, we have 42, and of those, only 4 are stable and 38 are in development.
Mostly client-focused.
Which kind of makes sense, given what we've been doing. Lastly, for entities, this is the identity breakdown by length. We have 36 that actually haven't been officially modeled.
Because they have zero identity, but of the ones that are modeled, 14 only have one identity attribute, and 4 have 2, and 1 has 3. The only one that has 3, I just removed in the latest VR.
Liudmila Molkova 01:01:11 Nope.
Josh Suereth 01:01:12 It was super helpful.
Liudmila Molkova 01:01:12 I'll see.
Josh Suereth 01:01:13 Yeah.
So, kinda cool to watch this, right? Anyway, we gotta jump to another meeting. Thank you, everybody.
Jeremy, I really like the, live check stuff you've been doing. So, log support, dumping logs, beautiful work.
Jeremy Blythe 01:01:30 Yep.
Trying to make up for not telling the world about it, because of the… I have been, volunteered… I've volunteered to… I'm in the Honeycomb Champions group, and I'm doing a talk for them in January.
Josh Suereth 01:01:46 Cool.
Awesome.
Jeremy Blythe 01:01:48 Meh.
So, there we go.
I'm making amends.
Josh Suereth 01:01:54 Here we go. Awesome, man.
See ya.
Liudmila Molkova 01:01:56 Thank you.
Talk to you later.
