SIG: Specification SIG
Date: 2025-07-29
Duration: 26 minutes
Zoom Recording URL: https://zoom.us/rec/share/GI2hYNA7q3bdcMKkpG8aMUpo99swNOM-dRpqFmN_tMJZLJCRqyJ4Yzs92jfq6aRQ.iqrMqbQ2p8TmSS4R
============================================================

## Zoom Recording Transcript

**Carlos Alberto Cortez** 01:37 Hello, everybody. Let's start in 2 min.
Okay, let's start in 1 min.
Okay, I think we can start. We have 11 people. Things are kind of slow, anyway, in summer, people are taking a break.
So let me share my screen if that makes sense. But here we are perfect.
Okay, let's go over the items.
the 2 items there are mine. So I forgot to put that
they should be taking 5 min each.
If there's something more that you would like to talk, please add that.
Okay, so in that case, let's start. The 1st one is a Pr that has been open for a little while. And it needs more eyes.
Basically, we want to be able to add user agent enrichment to the exporters.
And this is a very general one.
About basically, the agents may expose
a configuration that will allow you, you know, to specify
what's the agent? Basically, this is for custom distros
I guess that the important part that I see is well, the the thing that I would like to get people to review is this part which he says that such option must not be available as an environment variable. That means that if you want to override user agent
but at the exporter level you cannot do that. Ever be an environment variable.
any comments on that front?
Okay, no comments. So in that case, please consider reviewing this, it has enough reviews for us to merge this one.
Yeah. So please take a look would be super great.
**Daniel Dyla (Dynatrace)** 05:56 Actually, I do have a quick comment on that. If it's meant to be used by distributions.
Is it?
Is it meant to be configurable by Andy like
I'm thinking of could it be like a a protected class property, or something like that, where the distribution would extend it? Or do we want it to just be like a regular configurable option, because users may configure that as well.
**Carlos Alberto Cortez** 06:27 Right? That's good. A good question. And one of the things about this period that it's kind of a big, but in general it doesn't specify that the only strong thing about this one is that it shouldn't be done to environment variables. But besides that.
yeah, it's well. This part is, probably, I think it's vague if you ask me, like, as the case makes for similar configuration options.
And me, you know, by a signal specific option. That's very general.
**Daniel Dyla (Dynatrace)** 06:58 Yeah. The the reason I ask is this, because it seems kind of weird to specify like that it should be hidden from environment variables, I assume, to prevent users from overriding it. But then, if it's available in code, they can just do that. Anyways, I don't understand that it seems like a contradiction to me.
**Carlos Alberto Cortez** 07:16 Yeah, that's a good question. A good point. Yeah.
**Daniel Dyla (Dynatrace)** 07:22 Okay, I'll I'll make a comment on the Pr.
**Carlos Alberto Cortez** 07:25 Yeah, it would be great. Yeah, I think that's a good call out, I think that yeah.
hiding these from environment variables.
It's not enough. Yeah.
okay, thank you. On that front. Actually, I saw a pair of comments.
Okay, think it's cover.
The second one is one. I don't know whether we have some entity entities. People here. I see, I said, Josh, so
I don't know whether you want to discuss that, otherwise I would like to get some general discussion on this one.
Basically. The entities group would like to have a new environment variables.
A new environment variable. Sorry to be able to specify entities values.
So 1st of all, we have auditorium. Which can be
it can, you know we can do exceptions?
But they have to be properly justified.
And one of the things is whether configuration, like file configuration, which is with Jack and Tyler, have been working on. That's something that is enough. Or you still need environment variables. And the second part is this, pr, has their own grammar, you know, on how values should be specified. So it's not a straightforward like, comma separated values
is just a actually a specific way to do this. Yeah.
**Josh Suereth** 08:59 Let let me let me let me talk in 1.st 1st of all, this was in the Otep for entities that is justified. So let's let's talk to the 1st thing. This is not configuration at all.
In fact, the usage of this environment variable will be something that the configuration file will say whether it interacts with it.
So there will be an a resource detector that will say, you know, I interact with the environment
as an explicit thing you would configure or not configure.
It might be default on right
but that is a thing that you that is independent. So there's a configuration that will say, I will get information about who I am from the environment.
And then this environment is the design of that detection. So this is the idea that as a platform provider like, let's say, Google, azure Amazon, Alibaba Kubernetes. You know, Heroku, you know, if if I what's the the one from hashicorp nomad, right?
I can provide an environment variable. That explains who you are when you run. So you don't have to go do all sorts of lookup calls and like Rpcs, and that kind of thing to identify where you're running. I can push it via an environment variable.
What we want out of this Pr is an environment variable that
one platform can provide and another platform can augment without blowing away the previous. But like so they can work together. So if Kubernetes provides an environment, variable azure can provide more to it about azure information, and they work together
as opposed to a part. So that's that's what this is designed around.
But like, imagine. And again, this is something we do internally at Google is, instead of
having resource, detection. Go make Rpc calls at the start of processes that could fail right and look things up.
This allows us to push it as an environment variable.
So the identity gets actually pushed down into the system.
And that's the thing that we want to try to enable in open telemetry. So this is completely orthogonal to configuration. There will be a separate configuration piece that turns it on and off.
But the second thing is to evaluate this is this, a format that we feel multiple platforms can participate in. If, say, you know, someone is running Kubernetes and that someone wants to add information. And Kubernetes is also pushing information. Will it work together. So Dimitri put together a specification for this
and and some implementation to like show like what it looks like. This is the proposal. This is in the Otep for entities. If you want to read where we had a whole bunch of discussion about that with Jack
about like how this is different. There's a bunch of bugs that I don't know if they're linked on here, but I can link to them where we're talking about the need for environment, variable driven identity. That is not configuration.
But so I'm happy to provide that as well.
But that's that's the gist of what this is and why it exists, thoughts and concerns go.
**Carlos Alberto Cortez** 12:02 No, thank you for the clarification. You actually have the impression based on the tab that they were orthogonal. I just wanted to get a, you know, confirmation of that. Yeah.
Also, I think that these grammar should probably become part of general hotels. And anyway, details, you know.
And I am mostly asking, because, there were some people here asking about this and whether this can be done through configuration. But yeah, since you mentioned they are terminal. So yeah, it.
It seems that we still need that
mark is not here. I think
so we cannot discuss that with him. So maybe offline, I guess.
But yeah, basically explaining what you just told us.
**Liudmila Molkova** 12:46 I have a question. I I really support this change. I
really like the hotel resource attributes, and it was by design was that the the idea behind it was super useful for azure functions.
Have a question. So the entities are intended to be concatenated.
Right? So if you are telescoping. And let's say you're running container on a virtual machine. You might want to include both in the same environment variable.
Have you folks thought about having multiple environment variables and using the prefix. And or should they just go and read dot app and learn why? It's not the good to date idea.
**Josh Suereth** 13:30 You. You should read the Otep, and I don't know Daniel's here as well, so I don't know if you want to speak up. I don't remember if you dropped before we had that discussion. But, I did propose allowing multiple environment variables as an option here.
What what Dimitri went with instead is actually, you can prepend a I think, a comma or something
to everything that you add. So in the grammar syntax there's an optional comma at the beginning. So if you want to provide multiple entities, you can actually just take the environment variable and append, comma your entity, your bundle of stuff, and they should all be additive.
Oh, it's semicolon. There you go.
or yeah, that's a semicolon. I sorry it's too small. I can't tell if there's a comma or a 2 dots, anyway.
**Liudmila Molkova** 14:21 It makes sense.
**Carlos Alberto Cortez** 14:37 Any more comments on that one.
In that case I would really suggest that entity Entities group, please. You put your mark there, you know, approve that?
Yeah, I know the things, as I said before, are kind of slow in summer. But if you guys have cycles, please consider doing that.
so it can be signaled to other people. You know.
**Josh Suereth** 15:01 Yep, the the other thing I'll I'll advertise the entity Sig meets Thursday at this time.
so if you'd like to join us, we'll probably be discussing it there, and and any of the concerns we'll probably walk through live as well if if they haven't been discussed on the Pr. So if you want to talk about it in person, more in depth, feel free to join us.
**Carlos Alberto Cortez** 15:23 By the way, Josh, sorry that since there's nothing else in the agenda, I would like to get your eyes on this one likewise this is put by Dimitri just including the entity references as part of the stability guarantees.
basically just saying that. That's how it, you know, works with semantic conventions.
**Josh Suereth** 15:46 Yeah, yeah, for context, semantic conventions actually already has policies in place. To to preserve this, we put that in place early in semantic conventions to match. So, yeah, this is. And you saw, I already approved this pr, but this is updating
for those of you who aren't aware with context, semantic conventions operates separately from the specification, and when we pulled it out of the specification
we have a file in versioning stability that denotes what semantic conventions will preserve and what is in scope for semantic conventions. And so we wanted these things to be in semantic conventions defined by semantic conventions. That's basically semantic conventions had already been defining these. It's just it wasn't like formal. So this is making it official that semantic conventions will will preserve the entity type names and the identifiers.
and then semantic conventions has a bunch of like policies and stuff in place around it. If you want to see the semantic conventions, policies and stuff. I can link you to some of those Prs, but that's what this is doing is it's just it's that link from the spec to Semconf to say, Okay, here are things Semconf can do.
**Carlos Alberto Cortez** 17:02 So are we good merging this? I don't know whether you need more eyes, otherwise it looks fine. We can just go ahead and merge it.
**Josh Suereth** 17:10 I. Personally, I would like to have 2 folks from the entity Sig. Approve these prs generally. So that would be like Daniel or Ted or Nathan. But it's okay to go with just one. I just I'd I'd like to get one more. I don't know. Do you have thoughts there, Daniel.
**Daniel Dyla (Dynatrace)** 17:29 Yeah, I'll I'll take a look at it. I don't wanna just approve something synchronously on a call, but I'll I'll take a look at it. As soon as we're done with this, I did have a quick question about the environment variable one which
maybe I don't know. Maybe it's a stupid question, but I'm gonna ask it anyways. There's no SDK specification yet. So how is this meant to be implemented
like what's even interpreting this or sending it anywhere.
**Josh Suereth** 18:01 You could. You can implement this with existing resource detectors, and you would just provide the raw attributes
like we it. I know that this sounds dumb, but we don't need
the entity SDK for this to work initially with, like the existing way, resource attributes are pooled.
But yeah. So you're asking about like, how would a prototype? How do we have a prototype for this.
**Daniel Dyla (Dynatrace)** 18:26 Yeah. Like, as far as I know, there's no sdks released anywhere that have entities support like we have the prototypes. But I don't think there's any released sdks that have entity information at all. Right.
**Josh Suereth** 18:37 No, no, but you could implement this against existing resource detection, just to provide raw labels on resource.
**Daniel Dyla (Dynatrace)** 18:43 Speed is, pull the labels out, attach them to the resource and call it a day. Yeah, okay, I gotcha.
**Josh Suereth** 18:48 I also think this this spec is in experimental. So this is like the 1st of the entity spec that we can have.
Can you check that, Carlos, because I didn't get a chance to actually review this formally.
**Carlos Alberto Cortez** 19:02 Yeah. What part did you click? Sorry?
**Josh Suereth** 19:04 The is. Is the the file still marked? Experimental?
Oh, yeah, it is. Yes.
yeah. I don't think it's touching any any of the stable parts of the spec. So this would be the 1st part of the
the 1st part of entities that we have. I also like we did talk in the entity Sig about. And and I think, Daniel, you're getting at this. Whether this should be in the entity SDK specification
because it says it's an SDK environment variable. Or if this should actually be its own specification, for, like how platforms provide entities. And I I'm this that's probably going to be my Major feedback to this Pr. We already discussed it briefly in the Entity Sig, but we ran out of time, you know.
2 Thursdays ago. So we'll talk about again this Thursday. But yeah, like to what you're saying. I don't think this is an SDK thing. I think this is a here's here's a specification for sending, I resource identification context from a platform in environment variables. And so I think this probably belongs in some other area of entities that it so in the entity spec, but not an SDK area.
Does that make sense? Or am I going off the rails here with.
**Daniel Dyla (Dynatrace)** 20:11 Yeah, no, I get you and I. And I understand that the backwards compatibility angle on it. It just strikes me as like building a house and starting with the door handles
like I. I don't know
what problems will run into when we start actually specifying the SDK and building implementations that would feed back to this and say like, Oh, well, we already made this. I guess if it's experimental it can be changed. But it it just seems like a little bit backwards to me.
But
that, that's not like a blocking concern. It just. It surprises me if if you had asked me, what is the 1st part of the specification that I think I would see? Environment variable wouldn't have been in my top 10 on that list.
**Josh Suereth** 20:59 I I think this is mostly we're dividing and conquering the work. So the SDK specification is that Pri put together, which is on hold, because we're talking about an Api now.
I do have a prototype where I which I haven't pushed publicly where I was pulling in environment variable which is not shaped the way Demetrius had it.
And so Dimitri took went and provided like, okay, I'm going to just focus on the environment variable piece of this problem
and is posting this this pr independently. If we'd like to make this, we can talk about this again in the Entity Sig as well, or with Demetrius offline
if you wanted to make this a draft until more of the prototyping is done. That's fine. But I honestly think we know enough about the problem
of the environment variable based propagation that and we know enough about the merge algorithm from the prototypes we had for the Otep and from the existing prototypes that this is something I think we can execute on independently. And you're you're right that it looks weird because we're dividing the work up, and the other work probably should land.
But I honestly think we know enough to divide and conquer, and that's what's happening here.
**Daniel Dyla (Dynatrace)** 22:11 Okay, yeah, that I don't mean to sound like contrary. I I'm not trying to block it or anything. It just struck me as as weird.
**Josh Suereth** 22:17 No, it's it's a good observation. And these are things you should challenge like. We should all not like one thing what there's a there's a law in in any like design by committee that everybody goes along because you all assume that everyone has talked about it, and you're the one with the like. Oh, that seems weird. And if we don't say things like that, we end up going down weird paths because we all assume someone else feels strongly, and none of us do
feel. Please challenge all the time man like that kind of stuff. That's a good challenge. So if what I'm saying doesn't make sense, and you disagree. We should put this in draft and hold off.
**Daniel Dyla (Dynatrace)** 22:54 Well, the fact that it's development makes me feel okay about it. But in my experience users don't like when you break things, even when they're marked as development. They don't tend to care about that distinction as much as we as developers do.
It's an important distinction to have, but I would prefer to avoid breaking things when possible. Yes, you're correct. We know a lot about this. I think we can do it in a way that that makes sense, and probably not break it in the future. But I just there's a the little thing in the back of my brain says when we start
developing the SDK, what is going to cause breaking changes in here that we're not foreseeing?
And I just think, yeah, I would not do this first.st
But that said, I think I can evaluate the Pr. On its own merits. I just think, as an overall strategy, that's not the strategy that I would take.
**Josh Suereth** 23:52 But let's do this, then we can talk to Dimitri. We can mark it as draft for now. But I do think we need a public shared understanding of this end, variable for the prototyping. Because I want what you're doing with Javascript and typescript to be the same as what I'm doing in Java and the go prototype? Right? So we want to make sure the prototypes are all working against the same spec.
So let's leave this at least somewhere public. So we all work against the same initial spec for the prototyping of that feature. But we can leave it in draft. I think that's that's reasonable.
**Daniel Dyla (Dynatrace)** 24:33 It sounds almost like you were dangerously close there to proposing another document status.
**Josh Suereth** 24:41 I I think we changed development document status. By the way, like development is supposed to be. Remember, we moved from experimental. And now there's development. There's Alpha, there's Beta, there's release candidate. So when you see development in the spec as a user, you should not use it ever.
**Daniel Dyla (Dynatrace)** 24:57 Yeah. So maybe it's fine.
**Josh Suereth** 24:59 So. So I would challenge that. I think development is the right
document status here. And we did create it for that purpose.
But if there's reservations. If we're worried, people will start depending on this or building out on it early.
I'm fine being cautious there because we we do need. We have a lot of things to work through.
and we do need to make sure the prototypes work with this. So I'm fine, like, either way, I'm fine here.
**Daniel Dyla (Dynatrace)** 25:24 Okay, and I will look at both of those Prs
soon as we get off the call here.
**Carlos Alberto Cortez** 25:37 Perfect. Thank you so much for that.
And as you can read, there's nothing else in the agenda.
so if there's something you would like to expose. Now, please raise your voice in the next 5 seconds.
Okay, I guess we're fine. Yeah, thank you so much. And see you around tone.
