SIG: Semantic Convention SIG
Date: 2025-10-27
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:20 Hey, everybody.
How we all doing?
**Joao G. (Dynatrace)** 01:28 Alone.
Oh, good.
**Josh Suereth** 01:35 Alright.
Didn't have a check to…
see if anyone… oh yeah, we do have some messages on chat, be there in a minute, okay.
Cool.
Right Mission Triage. So, quick question for you, Yao. Do we… do we do,
PR triage or issue triage, which one's more… better to focus on, in our time box?
**Joao G. (Dynatrace)** 02:06 Hmm, good question, good question. I guess…
PRs, maybe? I've been doing issue triage, like, every day, trying to clean up, but I guess we can, yeah, decide. I think maybe…
**Josh Suereth** 02:22 the PR is better, if there's blocked things, and we can move on.
Okay, I'm not sure.
What?
I also want to…
**Joao G. (Dynatrace)** 02:33 yeah, think about the PR triage board a little bit more. I'm still not entirely happy with
the columns, I feel that there is a in-between state that's missing when it's, like, in discussion.
**Josh Suereth** 02:49 Yeah.
**Joao G. (Dynatrace)** 02:51 Yeah.
Whatever, we can talk about it later.
**Josh Suereth** 02:54 You know, that's…
I honestly feel like we need that for, PRs as well. Like, a thing to throw it onto in discussion, where, you know, to check the discussion, as opposed to, like.
Yeah. Not knowing if you should check for… like, just so you, like, from a triage standpoint, so we know what to check on.
Alright, cool.
Do things automatically get added to this still? I don't remember if that…
**Joao G. (Dynatrace)** 03:22 Yes.
**Josh Suereth** 03:22 Okay, good.
Okay, just real quick, these chores… I'm gonna throw them… I've been doing this when I have a chance in the morning, which I didn't this morning. Throw them immediately into needs more approval.
Because basically, these are things that, we maintainers should be checking, updating, and merging quickly. They're just…
Generally, it doesn't involve a lot, but…
Anyway, I don't know how the rest of you feel about that, but usually I throw them into needs more approval, and then do a quick review of, like, what changed in that version.
Okay.
**Joao G. (Dynatrace)** 03:58 Yeah, I do the same as well.
**Josh Suereth** 04:00 Okay, cool.
Alright, so let's go through these backwards.
Rename system process status to Process State.
Looks like this has all the approval from the, the SIG, so this is just waiting for a maintainer approval.
Cool.
I don't see any open comments either.
So…
Yep, that one just needs a little bit of approval, and where's… where's my link? Here we go.
An alias for free. Well, actually, no, we should go through blocks, sorry. We should make sure that we're making progress on block. Brain dead moment. Alright, let's start with retrieval span support.
This one was blocked. I don't think there are any comments after that.
And this is a first-time contributor.
**Liudmila Molkova** 05:03 We had a discussion about this in the GenAI SIG.
There is an interesting question on whether
there is an abstraction over database in Gen AI space, and whether we want to, document it as a span,
There are some action items from the SIG meeting there. It's in progress.
**Josh Suereth** 05:25 Okay, so this is in progress, and it's being discussed in the SIG?
**Liudmila Molkova** 05:29 Yeah. Okay.
**Josh Suereth** 05:36 Should I move it to awaiting Konos or approval, or is it actually blocked, blocked?
Let's move it to awaiting Code Owners approval.
Okay.
Alright, update Heroku semantic conventions to match official documentation.
**James Thompson** 05:51 That's unblocked.
**Josh Suereth** 05:54 That is now unblocked.
Okay.
Alright.
It's hard to get a gist for all these comments right away. There's no easy CLA, so it actually technically is blocked.
I'll make a comment.
Alright, cool.
Alright, so once the CLA is accepted, we can take a look at this.
**Liudmila Molkova** 06:24 I would imagine the moment this PR is updated, it will be closed by the automation, because nobody owns Heroku.
**Josh Suereth** 06:35 Yep.
That's a good point.
And this is a bunch of things about Heroku. We… should we comment?
about having the Heroku people possibly own Heroku conventions?
The Heroku telemetry team, is this actually… actually working at Heroku.
Can't tell.
**Joao G. (Dynatrace)** 07:04 Yes, we should… we should ask that, yeah.
**Josh Suereth** 07:06 Yeah.
So they have non-documented attributes and officially documented attributes, and they're doing OTEL resource attributes and service name.
Yeah… I'll… I'll make a comment here.
And across, okay.
Alright, does this sound reasonable?
**Liudmila Molkova** 08:11 Yeah, sounds great.
**Josh Suereth** 08:13 Cool.
Alright, we are out of time, Box.
And I don't know how much agenda we have, let me take a quick gander.
We have two things, one is 25 minutes, I'll tell you what, let's, defeated. Cute.
Shoes…
Okay, let's get through the agenda, and then we'll come back to some triage if we have time. Sound good?
And apologies, I was afraid to click Fit here.
No one wants to know how…
small my monitor makes everything.
Trask, Open Telemetry I.O. Pool Request. I think I pulled this up.
Where is it?
Right here.
**Trask Stalnaker** 09:12 Yeah, so there's a couple of things…
**Josh Suereth** 09:16 hear that…
**Trask Stalnaker** 09:18 Would be good to discuss from the semantic convention perspective.
1… is, this… Like, when… Previously, we've always said that
Instrumentations can… OpenTelemetry… instrumentations published by OpenTelemetry can only be marked stable if the semantic conventions have been marked stable.
And so… Question is, is that… Should we revisit that statement?
Based on… The alternatives…
are… there's a couple alternatives. One would be… Seeing…
I mean, the one extreme, the far extreme would be
Instrumentation, telemetry stability. Instrumentation stability does not imply telemetry stability.
Don't love that.
I think…
I think a nice medium middle ground is saying that instrumentation stability implies telemetry stability for that instrumentation, meaning it won't
break… Without a major version bump of the instrumentation.
But it doesn't mean that the underlying semantic convention has been marked stable.
In fact, I kind of feel like that should… be the default,
Just to give more flexibility to, like, that…
meets the definition of stability that I think we desire, which is not breaking people.
And takes pressure off of… I'm worried… one of my worries is that, there's gonna be… Like…
whip.
**Josh Suereth** 11:28 A renewed effort on stabilizing instrumentations.
**Trask Stalnaker** 11:31 Could create kind of a crash on the semantic convention.
Repository of stabilizing, trying to stabilize things.
Which, I mean… Maybe that's good.
Also… .
**Josh Suereth** 11:49 So…
So, just, just for context, the… that decision, I think we have to bring it to the specs, so I think it's good to talk about it here. Yeah. But that was, yeah, that was driven,
One of the reasons I'm participating in SEMConf and I'm driving things is because
of that specification change that said you cannot have stable instrumentation unless you have stable SEMCOV, and so then it was like, okay, how do we accelerate SEMCOV? I think we're at the limit of how far we can accelerate SEMCOV healthily.
At this point. So I agree with your concerns.
That said, I think the spirit of the change, and what we should argue for, is that stable instrumentation should have three qualities to it, okay? One is, you advertise the data you're generating. There should be documentation that says, here's the shape of my data.
The second quality should be that you don't knowingly break it. There should be some integration tests that make sure it's the same shape, you should have some kind of control that says from version A to B, right, I'm not making a change that would break users and alerts.
and so that's what the whole schema URL and transformation thing is, right?
And then the third would be that you communicate, major version bumps, where you are allowed to have breaking changes in some fashion.
We don't have a way to really do that in SEMCOF, the major version bump thing, because we're not using
like, that's still a hole, I think, in semantic conventions. However.
given what we've built in semantic inventions in the state of Weaver, I still think Weaver needs a little bit of polish, but I'm always gonna think that, because I'm working on it. But,
I think we could lift the restriction as long as we keep 3 principles, which is…
you write down what you're generating, and it's documented well if you're in OpenTelemetry, so you have a definition of your schema.
Somewhere. It doesn't have to be semantic conventions, it could be locally in your project. That's fine.
Second, you don't break it on regular version bumps, and you clearly communicate what it is, right? So it's like, here's documentation for it, I make sure it doesn't break.
That is the second important thing. And then the third is that there's some major version bump capability that comes with telemetry schema URLs that says, here's how it changed from version A to B that we can use in transformations, or schema transformation, right? So, if we have those three things of, like.
it's well documented, it's kept from breaking when it shouldn't, and then we have transformations for major breakages, or for major version bumps. I think we can allow those definitions anywhere.
With the caveat, that things like HTTP, I do think we should prevent throwing out…
you know, stable versions that are completely incompatible with all the boat. Like, I think there are some things we have to protect, but there's some things where we can say, cool.
this thing is fine to be defined outside of SEMConf.
We actually don't think it will come into SEMCOV, necessarily.
And you can stabilize it the way it is.
**Trask Stalnaker** 15:20 So, from a… let's take a practical, from the Java… instrumentation perspective.
So let's take messaging semantic conventions.
We can… we can do these first two things.
Today, I'm not sure what…
this means for us practically today. Is this something we can do today? Is this something we need to go wait on? Something?
Oh, sorry, I…
**Josh Suereth** 15:58 Oh yeah, I…
**Trask Stalnaker** 15:58 I'm acting like I'm sharing.
**Josh Suereth** 16:00 The third, the third.
Yeah, yeah, so this, this, I think,
You can do that today if you define your own schema for messaging.
Like, if you were to say, here is a schema URL for Java messaging.
Right? And you give that thing semantic versioning. So you'd say, here's the Java 2.x of messaging.
When semantic conventions bumps, you wouldn't bump. You would keep it at 2.0. And then when… if you want to take on a breaking change, you'd have to, like, provide a 3.0 or some sort of transition thing for your…
messaging data you're generating. Like, the idea here is a user understands clearly when they will be broken, if they take an upgrade.
And they understand what that transition looks like.
If you were to change things from, like, you know, 2.0.1 to 2.0.2,
And it would break someone's observability, that's the thing we want to avoid.
**Trask Stalnaker** 17:01 So that means we couldn't,
use the existing, like, say we just want to pin to the current semantic convention schema URL.
The currents… can we use that
We couldn't use that because that's not going to be major version bumped.
**Josh Suereth** 17:22 I think you could use that in… what I'm saying is, in Java, right, you'd create… so… and again, I might be getting too detailed, but in Java, you'd pin to that version number for all your messaging stuff.
And you could allow changes that are non-breaking.
But what you would do is when the messaging stuff stabilizes, if it is a breaking change, you would have to do some kind of a major version bump.
Or a clear signal to users of how to do the transition like we've always done.
But you would.
**Trask Stalnaker** 17:55 We're…
**Josh Suereth** 17:56 that we've had locked until that happens. Yeah.
**Trask Stalnaker** 17:58 Yeah, we're good with doing… doing major version bumps is not a problem for us.
I just wanted to check the schema URL itself, if you were saying that the version in the schema URL needs to be major version bumped.
**Josh Suereth** 18:18 Oh,
We don't require… okay, so the ver… what would I like? I would like for that to be true. Yeah, yeah, yeah. But no, that's not… that's not a thing you have to do. However, you could actually have your own schema… like, with schema dependencies, you could define your own schema URL.
For Java specifically.
**Trask Stalnaker** 18:39 I'd rather not.
not do that, I'd rather it to the semantic convention.
One that we implement.
**Liudmila Molkova** 18:48 Can we add the suffix to it? The DAF one, or the… whatever the status of this thing is?
**Josh Suereth** 18:59 Are you asking me?
**Liudmila Molkova** 19:02 Just the audience in general.
**Josh Suereth** 19:05 I… I think we have to do that split soon. It's… it's… yeah.
**Trask Stalnaker** 19:12 Split across all of GemCon's.
Yeah. And have two different… have a stable schema URL and a unscathed stable schema URL. Yeah, I like that.
**Josh Suereth** 19:25 Yeah, we've been pushing on, we're trying to change the syntax.
To be easier to write and use?
And once… once that's done, we're going to update the publishing.
So the URL schemes, schemas and things. Lyudmila had a great idea to, like, have a dev and a regular for regular semconf, so anything that is not stable would go under, you know, version underscore dev, and anything that is stable would be in the major version, so you would know, when you look at the schema URL, what's stable and what's not.
That doesn't necessarily solve this problem, because the problem is not about whether… again, if we communicate things in schema URL, how many people here look at schema URLs?
Ever.
Ever.
When you use OpenTelemetry.
**Trask Stalnaker** 20:18 Yeah.
**Josh Suereth** 20:18 I do, but only because I check what instrumentation is going out of date, and, like, whether or not people are upgrading. But that's…
**Liudmila Molkova** 20:26 You either look at schema URL, or you look at the instrumentation Version.
The library version, right?
**Trask Stalnaker** 20:36 We don't even currently emit the schema URL from Java. I just sent the PR to add that for HTTP.
Yep.
**Josh Suereth** 20:45 That I knew.
Again, I don't think people are engaging with Schema URL, so basically having it gives us the capability to use it.
But in practice, it's… the thing that we need to solve is advertising compatibility to users, and making sure it's clear to them when things break, and why they're breaking, and what actions they can take that are safe or not.
So, from my perspective, the schema URL is the least important bit.
Well, sorry.
I should be careful. Me, this is Josh speaking, not the TC. The schema URL is the least important bit. Your version number, and advertising what the shape is, is the most important bit.
And so, as long as we have that.
having schema URL to back it so that some changes can be safer using schema URL going forward? Great!
But the most important bit is that you are advertising your shape, you're preventing it from breaking.
And that users know when they're taking a break and change.
As long as we have those things.
**Trask Stalnaker** 21:50 Yeah. I think we're okay.
Great.
So in the, prop… in the blog post proposal, which I know is just, like, like, there's still a whole OTEP, and, like, we'll get to all the details, but the one other thing I wanted to call out for the SEMCOM
crew is the, this idea of beta SEMCOM.
Of potentially marking a… Kind of, like…
Saying, hey, anything that we think is de facto stable today, marking it as beta.
As a signal hadn't… So this, then… this is a little different, saying that
Then that would be the key for whether you could mark instrumentation as stable.
So, I'm not sure, I totally agree. I kind of prefer what we just discussed, where the instrumentation stability is not really tied to the semantic convention stability.
**Josh Suereth** 23:00 I think this has to be an OTEB, Trask. Like, this… I don't think this can just be announced in a blog post without…
**Trask Stalnaker** 23:08 Agreed.
**Josh Suereth** 23:08 The lifecycle thing.
**Trask Stalnaker** 23:12 Yeah, maybe just leave a… I mean, there is a comment already on here that I thumbs up, and I don't think there's any worry of… it's gonna be discussed tomorrow.
In…
**Joao G. (Dynatrace)** 23:22 There's gonna be an old type as well.
**Trask Stalnaker** 23:26 Yeah, the question is whether we can… whether we should be releasing a blog before the OTEP, or sort of after the OTEP, because…
Sending it before the OTEP.
Kind of makes it sound… What is that?
French accompli, A fate.
Yeah, anyway, I can't.
**Christophe Kamphaus** 23:51 They are complete.
**Trask Stalnaker** 23:53 Thank you!
**Josh Suereth** 24:02 We all get a French lesson for free today. Thanks, Trask.
No, yeah, I agree, I agree.
That, so, so what…
I… yeah, if we can push on this to make sure that instrumentation can be stable without having stable SEMCOM,
Unless that instrumentation is Semcov.
So, I think we still, like…
an HTTP library should be against stable, like…
you either need to be using the stable semconv, or if you're publishing something else, are you really open telemetry? Still, right? Like…
That's where it gets a little bit iffy to me.
So, messaging SEMCOM, for example. I'm comfortable having a stable open telemetry thing prior to Messaging SEMCOMF be stable. But once Messaging SEMCOMF is stable.
the expectation would be that you move to that, and you have a version bump, right? So there's a little bit of flexi- like, flexibility we can give, but there's a little bit of control. I wouldn't want a new HTTP library
to come out that's stable, that doesn't use HTTPSMCOV, right?
Okay. This, this, though, like, yeah, I don't think we want… A new stable beta phase.
I do think that we generally need to treat things that are beta as more stable.
By the way, I'm talking a good bit, apologies.
I've been thinking about this particular issue, around,
Improving defaults for stable components for a bit.
And this is just not quite… like, I don't think this actually solves the problem, this, this here.
**Liudmila Molkova** 25:55 From… from a simple…
**Trask Stalnaker** 25:56 What… oh, go ahead.
**Liudmila Molkova** 25:59 So, I was thinking about the criteria we could have used for better, and it would be the presence of instrumentation. Somebody actually went ahead and
Created the instrumentation.
And then we would be more cautious about making any changes to semantic conventions, or we'll consult with reality. So this is the opposite. The moment you have instrumentation.
The semantic convention corresponding one is… is bumped in its… Status.
So, all this to say that the distinctions I find useful is whether semantic conventions is fully theoretical, or is actually implemented.
And this maturity status is that… well, we can't tie them to this, but…
It's not something instrumentation should care about.
**Josh Suereth** 26:55 We also just had a giant OTEP around stabilization maturity model.
Where we changed everything just recently to have a whole bunch of stages with meanings.
So, I… if… if we want… if we want to do something, we can change the meaning of that model.
But… Yeah, I…
**Trask Stalnaker** 27:17 I'm not sure.
**Josh Suereth** 27:19 The thing I'd like to focus on, if we can, is basically, we have a bunch of…
Semantic conventions with no ownership that's de facto stable.
I went through a survey of a bunch of things that I think need to get, prioritized, and I was trying to motivate internally in our company, contributors to those areas. Because I think we're… to some extent, we're lacking people to, like, come in and, like, drive pieces.
But if you think about, like, de facto stable pieces that kind of don't really have ownership today.
The cloud provider ones are, like, one that me as a cloud provider is worried about. I'm sure, Trask, you look at those every once in a while.
I think we need to go through…
The things that don't have owners.
that are crucial to open telemetry. Like, anything that you have to engage with.
to be a successful OpenTelemetry user, and we need to figure out what we want to do about those pieces. So, you know, what this is, I think, proposing is we just take them as is and mark them as stable.
And if that's what we want to do, okay. That doesn't really make me super happy, though, because I think we have a lot of open issues on them.
That just aren't being addressed because no one owns it. So, what I'd like to do is try to motivate ownership on those parts before we do crazy new parts, and get
you know, get a prioritized list of, okay, here… when people come and propose SEMCOMF, we can actually say, here's the top SEMCOMF that we need owners for. Instead of just letting anyone come and say, oh yeah, I want to do SEMCOM for X and SEMCOM for Y, we say, here are the things that need owners, in a list that we've prioritized as maintainers.
Anyway, I have… I have my own list there, I can put it… I can write it down if you want, but…
**Trask Stalnaker** 29:20 No, I mostly just kind of wanted to have a little pre-discussion here with this group before tomorrow's kind of specification meeting.
**Joao G. (Dynatrace)** 29:34 Did this, announcement come from the CNCF, CNCF thing? Like, the project?
Moving to another level, or something?
**Trask Stalnaker** 29:48 It came… it was motivated by feedback that we got during the graduation process from the CNCFTOC.
But, you know, they're… they were clear that they're not…
There was… they're not giving prescriptive
like, how to do stuff, they were just kind of more, like, calling out the problem of stability that, users… they did, adopter interviews, and that came up multiple times. So this is…
So yeah, I think, you know, we have flexibility how to address the stability question, just we want to…
Write down and work, you know, re-kind of…
Focus the community on the stability Question.
**Josh Suereth** 30:46 I'm gonna give another 2 minutes, if anyone else has thoughts they want to add here. I know I talked a lot, so apologies, but if anyone else has thoughts they want to add here, we have another 2 minutes for some discussion, and then we should probably move on.
Alright.
Let's start working our way through the agenda. Next up, entity rendering cleanups. So I'll just show this. One thing I wanted to fix was, we were going through and, as part of the service and deployment, SIG made a PR,
That, made some changes to entities, and realized that all the embedded snippets don't actually render entities with identity and ownership.
So what this does is it actually changes the identity and ownership. This is actually a bad one. Let me find a better one.
Where's, service? Might be the best one.
This changes the identity ownership to, first of all, make sure when you render things, it shows the appropriate stability level.
But then also,
the identifying attributes of the entity and the descriptive attributes are called out separately. This is done to kind of look like the data model table that's in the specification.
So that things line up. Ludmila had a comment that, like, having a flatter table looks better. I…
partly… partly agree, but partly don't. I want this to be front and center, that people understand, like, what these mean, and that this group is identified, and this group is descriptive. But I wasn't able to do fancy HTML rendering of tables with nested tables, and joined…
Columns, because, you know, it's marked down.
So this was my workaround for making it pretty, compared to what I made in a dock, so…
Anyway.
that's basically what this does. It does this, and then the other thing that it does is if you look at, say, the README for resource, this now, when you render a snippet for an entity, it will render the same table
as… the entity registry would.
So they look exactly the same, they actually share code now.
So, if you're doing a snippet for entity, or you're doing the entity registry, everything shows up the same.
Yep, so that's basically what this does, and it makes it clear. Oh, the other thing is, there's a warning, so that one is fine. I think maybe OS is bad.
There's a warning which is generated, which was not before, which is basically letting you know that you cannot stabilize an entity until you define an identifying or descriptive set of attributes, or you actually have to have identity, but
You can't have attributes that don't have a role, so I put them in this other category.
For now, so… and then with the warning above it. So now it shows up in the markdown you're changing, it shows up in the registry. It's possible someone made a change, they didn't realize that, like, you can't stabilize this entity because it's not showing up in the right spot, but I want to make sure folks are aware of what it takes to stabilize entities going forward.
Cool.
Any thoughts on that? I know, Lyudmila, you had some proposals for making this render better. Go for it.
**Liudmila Molkova** 34:24 I'm not married for this… to this proposal, so I don't mind either way. I wanted to check about the stability, so what you run there, you change the stability on service to mixed.
Because I assume it has a mixture of… attributes, right?
**Josh Suereth** 34:45 Yeah, here's… yeah, that gets fixed in a separate PR, hold on.
So, yes, service today has a mixture of attributes that are unstable, and so you can't stabilize service, but there's a separate PR,
From the, the service SIG.
Oh, come on.
Hold on, I guess it'll… we'll look for ones for me.
There's a separate PR to fix that. So, this one is still under discussion, but this was… this is the current plan for service. The service entity gets split into three pieces, service, service instance, and service namespace. And then, service is… you can see it here.
A namespace has services which have instances, and now it is stable.
Because,
This one, by the way, isn't with the fix thing, but if you notice, all the attributes are marked stable.
**Liudmila Molkova** 35:41 Because of how we split them up across the different entities.
Yeah, the entity itself has stability status, and it's stable.
And I think there is a special,
thing in regal policy is that even allowed to have unstable attribute unstable.
entity. So I think we should render the actual status, and the fact that it's…
**Josh Suereth** 36:07 That it's allowed to be mixed is bad, yeah.
**Liudmila Molkova** 36:10 Well, it's, it's…
**Josh Suereth** 36:11 So…
**Liudmila Molkova** 36:12 Yeah, okay, yeah, go ahead.
**Josh Suereth** 36:14 But what you're saying… what you're saying should be true.
It's not today.
We actually don't… we don't require it on entities, because we're still working out the details of entities, and it's still awkward.
**Liudmila Molkova** 36:26 Yeah, but then our YAML lies, and it's worse than when our Markdown lies.
**Josh Suereth** 36:32 Yeah, agreed. But I think our YAML is lying today, if I recall correctly, because, if we look at entity for service.
**Liudmila Molkova** 36:40 It is stable.
**Josh Suereth** 36:42 It is marked as stable, and it has things on it that are unstable.
And it's also an exception, because effectively.
the pieces of service were marked stable without all of it, prior to…
like, the entity thing showing up, so…
I think… I think it'll get fixed to the point where we don't need to have it as an exception with that,
proposal from the, or with this proposal from the SIG.
Once we… if we agree to split them apart. But I agree with you, like, that's problematic and does need to get cleaned up.
**Liudmila Molkova** 37:18 Yeah, hold on.
**Trask Stalnaker** 37:19 Entity be stable, given that we haven't stabilized entities concept itself?
**Josh Suereth** 37:27 we unlocked the ability to stabilize the modeling of entities. Yeah.
We don't think the model of entities will change, the models in the spec, we're pretty confident. If you want us to actually stabilize that part of the spec, too, we can.
But this was… this was a way to make progress, because service… again, there are resource attributes that are so core to OpenTelemetry, we want them to be stable. So… Yes, I think with.
**Liudmila Molkova** 37:55 Quest Resources, but then we rename them to entities.
**Josh Suereth** 37:59 Yeah.
**Trask Stalnaker** 38:01 Okay.
That's fine.
**Josh Suereth** 38:03 I think we actually renamed entities before we mark this table, but we can…
I can go back and show the PR if you want to see it.
**Trask Stalnaker** 38:11 I don't.
**Josh Suereth** 38:12 Okay.
**Liudmila Molkova** 38:15 I would actually try to not to lie in the markdown.
and just render whatever status there is. We know there is a problem.
And we allowed this problem to happen, and…
**Josh Suereth** 38:29 Okay.
That is an easy fix.
It's actually way easier than what we're doing now to try to show mixed.
Okay.
Alright, let's get back to…
If anyone has thoughts about that, again, the goal is just to make sure that we render the same thing both places, and to make sure that the identity and the description are called out and used everywhere. Alright.
**Trask Stalnaker** 39:00 For what it's worth, I… I kinda like the, lenmilla's suggestion of the tags?
The one place where it breaks down is the example you showed where there were no identifying attributes, and then it's really unclear.
**Josh Suereth** 39:20 I might…
**Trask Stalnaker** 39:20 We have so many dimensions that are useful to break down on, like.
It for spans, like, whether it's required, or whether it's a sampling attribute, or… Like, these are also…
Maybe not quite as important as resource entity, identifying attribute.
They are… Yeah.
**Josh Suereth** 39:42 Well, remember that the resource thing only shows up
When you're rendering an entity or resource.
like, that table is specific to Entity Resource, it doesn't… none of the other tables were changed.
**Trask Stalnaker** 39:54 I just mean that, like, we don't have this layering, this hierarchical, anywhere else.
**Josh Suereth** 40:01 Oh, yeah, yeah, Between Things? Right.
And so…
**Trask Stalnaker** 40:05 Yeah.
**Josh Suereth** 40:06 We're also planning, by the way, for identity, there might not be a requirement level. Everything is implicitly required.
So that's another change that might be happening, just… just so you know. So, like, the table itself… I… we debated between two tables and one, and decided to go with one.
But, like, the requirement level might be, not applicable for identity, whereas it would for others.
So…
**Trask Stalnaker** 40:32 Yeah, I, I just mean I like the flat.
I had a slight preference to the flat.
**Josh Suereth** 40:39 version.
Let me go back… I'm thinking about splitting the difference. Where is it? Okay, come on.
I don't know where Ludmilla's thing is, but, what I'm thinking about doing, We'll go back to service.
And then,
what about if we have it flat, but we put Lyudmila's badge on a, so instead of having identity and other, like, in sections here, they're actually in line, where it'd say other, other, other, other.
**Trask Stalnaker** 41:16 We're not seeing what you're showing.
**Josh Suereth** 41:18 Oh my gosh, okay. Instead of having identity and other as, like, major sections with just blankness here.
We would have… we would have the badges that Ludmilla said right in line.
**Trask Stalnaker** 41:29 Sure.
**Josh Suereth** 41:30 Yeah.
**Liudmila Molkova** 41:31 But as a separate column, is what you're saying.
**Josh Suereth** 41:33 It's a separate column, yes. Yeah, yeah.
And it would be on the left to call out, like, the distinction of it for you.
Cool. That's easy fixes, so thanks. I will do both of those.
Alright, let's move on to release time.
**Liudmila Molkova** 41:52 I just noticed we didn't release in 2 months, and it's a good time for us to cut the release. I can do it this week.
Unless there are any objections?
Or any other volunteers.
Okay, I'll cut there always.
**Trask Stalnaker** 42:13 Thanks.
**Josh Suereth** 42:28 Cool.
Let's move on.
So, James.
**James Thompson** 42:35 It… My main question is, what's the next steps for this?
Because it has a lot of maintainers approval.
Are we happy with it? And I go through rebasing it, or what do we want to do?
**Josh Suereth** 42:52 I think you have enough approvals, this can get merged.
Did, like, was there any contention on this?
**James Thompson** 43:01 No, not after the last change, which was just…
Changing one of the titles back.
**Liudmila Molkova** 43:08 The only reason I didn't hit merge is because there are tons of merch conflicts.
**James Thompson** 43:13 Yeah, and I didn't want to go through and merge it, rebase it all, and then have to wait another couple of weeks, right? So, if you're happy, I'll rebase it tomorrow.
**Josh Suereth** 43:22 Yeah?
Yep, just… Yeah, I mean, it…
**Trask Stalnaker** 43:26 Ping me or Lydmila on Slack, We'll hit merge right away.
**James Thompson** 43:31 Before there's any new merge conflicts.
**Joao G. (Dynatrace)** 43:35 Yeah, or you can ping me as well, I think our time maybe aligns earlier, so you can just ping me on second, and then my morning tomorrow, I can merge it.
**James Thompson** 43:44 Yep, okay.
**Josh Suereth** 43:46 I moved it to ready to be merged so that it's clear that this is ready to be merged, we just need to get rid of the conflicts.
**James Thompson** 43:51 So that one should go in before anything breaks it, so we can.
**Josh Suereth** 43:55 I'm gonna put a hold. Okay.
Cool.
Alright, next up, Mac. Yeah. Hopefully…
**mackenzie.jomard** 44:07 Ugh, I edited this one.
**Josh Suereth** 44:08 Yep.
**mackenzie.jomard** 44:09 So, I have a use case where I need to be able to differentiate,
data that's coming between… like, coming from EKS, and to know whether it comes from EKS Fargate, or…
regular EKS, so… I believe it runs on EC2 otherwise, so…
So I suggested a few,
like, 3 ways to… to do it, 3 conventions to add… well, we only need to add one, but I suggested ways.
And I saw it was moved to… needs Sig, so that's why I'm bringing it here.
**Josh Suereth** 44:44 Yeah, this is… this is where we don't have, ownership for cloud yet. Like, there's not a group of owners who own the cloud semantic conventions. They kind of predate the semantic convention effort a bit.
And so, we haven't actually taken a crack at what it means to stabilize them, what they should look like, are they up to speed with latest thinking from, like, HTTP and database system?
Design. So, yeah, you're…
The problem you'll have is you're stuck with, like, the general Sencon maintainers helping you out, and we're a bit overloaded with the amount of
120 pull requests and 648 issues to go through, as opposed to, like, a dedicated set of owners for cloud.
So thank you for raising this. Basically, you just need the ability to understand if something's Fargate, right?
**mackenzie.jomard** 45:33 Yeah, EKS, if it's, normal EKS on EC2, or Fargate.
**Josh Suereth** 45:38 Yeah, okay. So, Cloud Platform is an option that would mean that resource detection would have to figure this out. I guess my question would be to you, you've…
We'll go through each of these three. For this one here, is the OpenTelemetry Collector, or places that do Fargate detection for Cloud Platform, are they able to detect Fargate?
**mackenzie.jomard** 45:59 Yeah, so this is… this, semantic convention is actually blocking the next work that I want to do, which is adding resource detection, like, the collector resource detection processor, adding detection that it is Fargate, and adding this convention.
**Josh Suereth** 46:12 Yeah, okay. So you are able to do that in the collector, and you have the code ready, we just need the stable convention for it?
**mackenzie.jomard** 46:19 The code's not ready yet, but I'm aware of a way to detect that we are an EKS Fargate. Like, basically the pods…
that run an EKS Fargate have a label, which… so if we check that… if that label is present, we'll know that we're an ECAS Fargate. So there's a way to do it, but I don't have a draft PR or anything.
**Josh Suereth** 46:37 Okay, so you can detect it from within the pod, gotcha.
Okay, and then, I guess it's similar for these. I'm not familiar with the AWS conventions as much, apologies, to know, like, which one you should put it in. I do know that Cloud Platform tends to get used for these things now, and also we're moving this to use dot conventions for new things instead of underscores.
**mackenzie.jomard** 47:00 Cup.
**Josh Suereth** 47:00 So, I don't know what other folks feel, but I do… I would like to unblock a lot of these cloud support things, because I think there was… there was one from GCP that just got, reviewed that is a similar concern for, the new, agent
engine thing that you can push stuff on. I forget what it's called, but it's like a way of running agents, kind of like Cloud Run. So I think we should…
I'm personally, if you were to put a PR together around Cloud Platform.
I, I would sponsor that, if you change these to dots.
**mackenzie.jomard** 47:37 Cool.
**Josh Suereth** 47:37 The thing that you have to do, though, is it will get automatically closed and rejected.
**mackenzie.jomard** 47:42 Yeah, that's what happened. I had opened an ODPR, and that's what kept happening.
**Josh Suereth** 47:47 Yeah, there's a way for us to get around this, so if you post the PR in chat.
in the OTEL SEMCOM chat, one of the maintainers, we can sponsor it and make sure it gets through. For, like… and I…
Again, I want to check with the other maintainers, but for, like, specific use cases like this, if I need to sponsor something, I have code that does it. I think it's okay for us to continue to rely on Cloud Platform. It doesn't make the situation worse with not having ownership.
But I wanted to check with, like, Ludmila, Trask, and, Yao. Is Armin on, too?
Yeah, Armin, like, what do you guys… how do y'all feel?
**Trask Stalnaker** 48:28 I had a question for y'all on the automation,
I thought that if we mark the issue as… accepted, then… The PR.
**Joao G. (Dynatrace)** 48:41 No, you have to market PR.
**Trask Stalnaker** 48:45 Okay, got it, thanks.
**Joao G. (Dynatrace)** 48:47 Yes, so if you mark the PR with the label, then it should not close anymore.
**Trask Stalnaker** 48:53 Okay, so there's no way to avoid the initial closing of it.
**Joao G. (Dynatrace)** 48:57 No, no, I mean, unless you know already that there's no area, and then you just add the label before.
any changes, so, like, if there's a PR that you know already will be closed when the author updates, then you can already add the label, and then it will skip.
**Josh Suereth** 49:16 But I want to be clear about that label, though. We don't want it to get abused. Yeah, exactly.
**Joao G. (Dynatrace)** 49:23 Like.
**Josh Suereth** 49:24 Like, you shouldn't add that label unless you have a maintainer sponsoring your PR that is saying, yes, we're willing to pull this into general maintainership.
**Joao G. (Dynatrace)** 49:34 Yeah, exactly.
That's why I even saw Josh's comments about the label, maybe I'll change it to add a specific label, because, yeah, just to make sure that the thing is, like, an exception.
Yep.
But I didn't… didn't have a good name in mind, but I'll think about it.
**Josh Suereth** 49:56 Okay.
**Joao G. (Dynatrace)** 49:57 Yeah, there was… there was another, there, in our issue triage board, there is a…
a column that shows, like, needs info, and there is one issue there about adding AWS code owners.
that pinged, like, two people that were in the, that were, like, involved in the convention, and Ludmila pinged them, and I pinged them recently, because I was cleaning up the backlog, and none of them replied, and one of them even is not with AWS anymore. I saw in their GitHub profile, so…
That might, yeah.
that might signal that, yeah, the AWS things are a bit, like…
alone there, and I feel that they should probably…
We should probably find a way to drag them, because…
Yeah, I guess there's enough AWS people that could be owners of this.
Maybe they're not aware of it, I don't know.
**Liudmila Molkova** 50:58 I think we have to have AWS people for stability. There is an instrumentation that adds something for AWS.
Dad.
Like, documenting something for the hotel instrumentation.
Even if it's not stable, makes sense to me.
**Joao G. (Dynatrace)** 51:20 Yeah, I agree.
**Josh Suereth** 51:25 Alright, well, all the more reason we need to get some of this cloud, the cloud conventions, a SIG, and a group of owners.
**Liudmila Molkova** 51:34 I, I, I think even, even then, it's, it's actually… like…
Well, I'm not part of Azure anymore.
But I would have no idea about specifics of AWS.
ECS…
Fargate thing, and we would need an expert, and someone who created the instrumentation is probably in the most expert position.
**Josh Suereth** 51:59 I also think that, like, in lieu of having someone who actually works on the things.
Just having someone who uses it on a day-to-day basis and relies on it being accurate is good enough.
Right? So, if we get a bunch of people who use AWS and are like, here's what we want to do, even if AWS engineers aren't necessarily on it, that's fine.
So… Cool.
But, as evidenced in that Heroku thing, if we can get the people who work on it to define the conventions, and then provide it via n variables, I think we're winning overall. Because then no one has to care about it.
Except the people who own it. But that's… anyway, that's a long-term play. Alright, let's,
Do you have what you need, Mac?
**mackenzie.jomard** 52:46 Yeah, thanks. I'll open up your… Thanks.
**Josh Suereth** 52:50 So in the last 5 minutes, just FYI,
governance committee elections are open, this is an important part of OpenTelemetry.
Thank you. I think Trask is the only current GC member. Daniel had previous service, but this is how you can participate with OpenTelemetry, governance, keeping the project healthy. Thank you for your service. Trask, do you want to speak to the importance of the GC, or what you all do, and why people should vote for…
leadership here?
**Trask Stalnaker** 53:19 Sure, yeah, the… sort of the…
Similar to the technical committee, which kind of is the…
kind of holding together all the technical… like, OpenTelemetry is a very broad, project. There's so many different repos, so many different languages, so many different projects happening, at the same time, and so trying to
make that into a cohesive, large Uber project is…
It takes a lot of time and work, and so the technical committee works, on kind of consistency and… and pulling those pieces together, threads together at a technical level.
And the governance committee is, tries to pull those threads together from, organizational and community, level.
So, go vote!
**Josh Suereth** 54:28 Awesome. With that, I think we might call it. We only have 5 minutes left, which I don't know if that's enough time to dive into any triage. So, thank you everybody for your time, and yeah, see y'all next week.
**Joao G. (Dynatrace)** 54:43 Bye-bye.
**Trask Stalnaker** 54:44 8.
