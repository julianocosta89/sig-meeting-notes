SIG: Semantic Convention SIG
Date: 2025-12-15
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:07 Hi, everyone.
**Kai Kirsch (Broadcom)** 02:12 Hello.
**Donal O'Sullivan** 02:14 Blue…
**Liudmila Molkova** 02:17 Let's give people a few minutes to join.
And in the meantime, Feel free to add your topics to the agenda.
I'm not sure, where is everybody?
But let me see if we will have a… Oh, hi, Trask.
**Trask Stalnaker** 03:42 Hey folks!
Quiet last week of the year.
**Liudmila Molkova** 03:50 Yeah… When was… when are we back? What's the meetings?
**Trask Stalnaker** 04:02 Jan… Huh?
What's the… yeah…
**Liudmila Molkova** 04:10 The second.
**Trask Stalnaker** 04:10 June 5th.
**Liudmila Molkova** 04:22 Oh, hi, Josh. Okay, so we have a quorum.
**Josh Suereth** 04:26 Yeah, apologies. Wonder.
**Liudmila Molkova** 04:28 No worries.
So let's take a look at the triage board, We have something blocked, the service criticality… I think it was blocked because of the merge conflict and some… Unexpected.
So I think the… the service criticality Because of the merge conflict, then they tap on the service instance instead of the service entity.
And… We just need the PR author to come back and… Updated.
**Josh Suereth** 05:12 Okay.
Interesting.
We… we talked about this one in, the, service thing, and I think there was general agreement on the… Yeah.
Anyway… I… does anyone have any contact with the PR author to, like, just ping them offline?
Oh, oh.
**Liudmila Molkova** 05:33 They know. They, agreed. They just didn't make the change.
**Josh Suereth** 05:39 Okay, cool.
**Liudmila Molkova** 05:45 Cool, we have something that needs more approvals, it's a trivial fix with some white spacing, Trasky already took a look if you wanna approve it, let's… let's get it merged.
**Trask Stalnaker** 06:03 Okay, will do.
**Liudmila Molkova** 06:05 Things. And we have a bunch of things that are not triaged.
And… let's just a little bit… Yay!
Is it pass? Yay!
So this is the Weaver, the next version of Weaver, that contains our schema changes.
**Trask Stalnaker** 06:32 Oh, the V2 stuff?
**Liudmila Molkova** 06:35 The V2 stuff, yeah, like, 19…
**Trask Stalnaker** 06:37 Wow.
**Liudmila Molkova** 06:38 9% of V2 stuff, or maybe 90, but still, I… I think I might start, bringing some changes. For example, we can switch our schema generation script to V2.
Or policies.
**Josh Suereth** 06:59 That feels good.
**Trask Stalnaker** 07:01 Let's go.
**Josh Suereth** 07:02 See? No issues, yeah.
**Trask Stalnaker** 07:04 Yeah, yeah, no, backward compatible.
Very impressive.
**Liudmila Molkova** 07:12 Okay, let's just take a look at the few things that are not trashed, and let's try to get them in.
Somewhere?
This is… Of 18.
This one is a very old one. I wonder what we should do with it at all. It's some GCE stuff.
Alright.
Oh, sorry, GCP.
Josh, do you have any context?
**Josh Suereth** 07:51 Yeah.
We are detecting instance… so, for context, if you use instance group managers in GCE, it's where you, like, create a, a VM image, and then you have it auto-scale, so you can, like, duplicate VMs. There was a need to actually have this detected, so the collector got updated with these exact semantic conventions.
And I think, there's… there's a requirement where they want them in semantic convention registry for the collector.
part of that federation thing. So, from my standpoint, these are all exactly what we want. If you look, we had to go with region and zone being different, because we discovered A managed instance group can be in a zone for which the VMs are in a different zone, which throws the whole cloud availability zone into chaos in semantic conventions.
So it went with keeping it somewhere else. I'm… I'm fine adding these myself. This, I think, only adds the registry, it doesn't add the entity, though, if I recall correctly.
**Liudmila Molkova** 08:57 Yeah, it seems so. Process-wise, we should probably have a group for GCP.
The, co-owners group.
**Josh Suereth** 09:07 Yeah, I think if you… if you want a code on this group for GCP, I can collect that information, but I think it would start with, like, Aaron Abbott and David Ashpel, who I think own a lot of the GCP resource detection, across OpenTelemetry. And then, if you want non-GCP people there, that's fine too. I don't, like, whoever's maintaining the code.
But… oh, and myself, I should say. Like, that was the first thing I did in a hotel, was write all the resource detectors.
Yeah.
**Trask Stalnaker** 09:35 Yeah, let's do that. It's fine if it's all GCP.
Folks, let's get, approval group and areas.
yeah.
**Josh Suereth** 09:50 To me, it's more important that the people who own the resource detection own the group, and so that happens to be mostly GCP folks, so that's, yeah, David Ashbel, Aaron Abbott, myself.
**Trask Stalnaker** 10:02 Cool.
**Liudmila Molkova** 10:05 Would somebody create an issue? Or… I can create an issue for the community.
**Trask Stalnaker** 10:20 for the GCP, yeah.
I, I can, I can do that.
**Liudmila Molkova** 10:26 Okay.
Thanks.
**Trask Stalnaker** 10:29 I'll just ping you, Josh, to add a list of users.
**Liudmila Molkova** 10:40 Cool, so then we will, wait for the code owner approvals on that one, before it keeps going.
Let's take a look at the agenda items. The service peer name…
**Michele Mancioppi** 10:58 Hello, hello.
**Liudmila Molkova** 11:00 Yay!
**Michele Mancioppi** 11:02 I, just managed to, install YAML lint after much tribulations.
And I am pushing the, the fix for the last check that fails.
I have… not heard, or at least if there was feedback about the investigations that I was asked to run.
I missed it.
So, I wanted to check if… But there's something else that needs to be done there.
**Liudmila Molkova** 11:33 Can you repeat? What did you miss?
**Michele Mancioppi** 11:35 I was asked, probably one month ago.
in a, SIG meeting where I was not there. I was asked to do some investigations about the usage of peer-added service.
Which is in the comments that are now on screen.
And then I've gotten a few comments from Josh, which I have addressed.
And I would like to understand, what else is needed to get this over the finish line.
**Trask Stalnaker** 12:07 Did we end up pulling out, peer service namespace?
**Michele Mancioppi** 12:15 No, because it's really needed. I explained it in the… In the comments, that you… if you do not have a peer service namespace, but only… sorry, a service.peer at the namespace.
and you only have service.pr.name, you cannot describe the full identity of the service on the other side.
Okay, my only… there's not enough.
**Trask Stalnaker** 12:41 Yeah, while I agree with that, I'm… it's… We have no existing usage.
of that?
Right, like, people… it hasn't been needed?
So… .
**Michele Mancioppi** 13:02 I don't know, that was… I just wanted to flag that.
I know you're.
**Trask Stalnaker** 13:07 I still don't need.
**Michele Mancioppi** 13:09 They are not part of the auto community, they will not go and speak about it, but… Roughly one user site every 10, and there's zero users' namespaces, if that helps.
**Trask Stalnaker** 13:25 Yeah, thanks. Go ahead, Josh.
**Josh Suereth** 13:28 I was just gonna say, the… if we discuss something in a SIG, and it's not written on the PR in a comment.
let us know. All of the things discussed in the SIG should end up on comments, so, like, apologies if that happened. In terms of addressing comments, yeah, the last state of this PR, apologies, I didn't have a chance to get to it, after you made your changes and responses, I was, I'm going on vacation very soon, and there's so much on my plate, I haven't been able to come back to everything. I'm trying to make comments on behalf of the service SIG, in addition to, like, myself. So, some of the comments I'm making are on behalf of the SIG, some aren't. I'll try to make that more clear in the future.
The concern in the servicing was about, like, names… the namespace. I think this would already be merged if namespace wasn't there, and we could, like, entertain namespace as separate PR if you want things to move quickly.
Because I think the… you have a response, you have comments, it's just getting people who can approve it to agree with that. From my standpoint, I think… the… My main concern with namespace is just that we don't have a great way to do that, and I think you addressed all my concerns, but I haven't looked at the details. So, this is, like, this was already on the edge of my approval, and I think it probably is there now, just for context.
But you'll need a second person in the SIG to approve it. So, it's like, as long as the rationale you wrote kind of resonates with other people who can approve, great. That's… that's the next step. But apologies, I didn't have a chance to look at your update.
**Michele Mancioppi** 15:02 Last week. Who are the people I can…
**Josh Suereth** 15:06 So, Trask, Zhao, myself, like, coming to this meeting and asking is a great place, because you should catch most of us. I think Zhao had a.
**Trask Stalnaker** 15:16 Yeah, I…
**Josh Suereth** 15:17 Unable to make it.
**Trask Stalnaker** 15:19 I'm in the… I'm with you, Josh. I'm pretty much on the verge of approving it, so I think… Getting the two of us to approve it is… will be good.
Josh, just to clarify, we… we did… we did post on the issue after that meeting, all the questions that we had.
**Michele Mancioppi** 15:43 Yep.
And that's how, I mean, I saw the comment there, and then I went and looked at the video for the SIG meeting, and then I got all the additional.
**Trask Stalnaker** 15:53 Yeah, I linked… I linked the video, and the timestamp in the comment.
**Josh Suereth** 16:00 So we're getting better at offline discussions, hopefully.
**Trask Stalnaker** 16:03 Like, hopefully that was useful. Online, offline.
**Josh Suereth** 16:06 We're trying to make it so you don't need to come to these meetings to make progress, even though that's still true a lot, no tell, but we're getting there. So that's step one, is you got all the context you needed. Great.
**Michele Mancioppi** 16:20 And, what type of information would you need to be convinced that we actually do, in point of fact, need not to break service identity in this PR?
**Josh Suereth** 16:37 Sorry, the… can you… can you elaborate on that? Like, what do you need to prove that it doesn't.
**Michele Mancioppi** 16:41 So, when you go and look at the service namespace.
It, it has service name and service namespace, and there is a comment somewhere in there about, the fact that service name and service namespace are identifying attributes.
Because when you get both of them, it's like first name and last name of a person.
**Josh Suereth** 17:05 Yeah, so we have been qualifying this. So for context, we just made changes to the service data model.
Where… and it's following this entity data model. So the idea behind… The idea behind this all is this notion of telescoping identity.
So… you only need service namespace when service is not unique enough and you need both together, then you need to be able to produce both together. And so, your point's still valid.
But we wanted to make people successful if they're only using service name, because we think that's also something that's happening. So if you look at the new service.
identifying attributes. There's a service that has name as identifying, and there's a service namespace that… where the namespace is identified, and they're separate entities. And when you need service in the context of a namespace, you provide both.
Right? Cool. That's the model we're going towards. That said, you, for peer, need to, like, if somebody has service and service namespace, you would have to support both.
So, for the same reason, you need both, yes. Like, I… I buy that. We were just looking for instances of instrumentation and, like, how much this is used was kind of like the feedback of, you know, we are trying to consistently require Usage before definition.
Because we get a lot of, like, proposals in SEMCOM that just aren't founded in practical examples. I don't think that's the case for you, it's just we want it documented so that other people see this, so that the process sees this, and so we can evaluate, some of the changes we're making around entities. Are they abiding by what you need, right? That kind of thing.
**Michele Mancioppi** 18:44 Hello?
**Liudmila Molkova** 18:46 Should it…
**Michele Mancioppi** 18:46 Is it fair to say.
**Liudmila Molkova** 18:47 Say the task here is to add the new attributes to entity?
No?
**Josh Suereth** 18:55 No.
**Michele Mancioppi** 18:55 No, I think the ask…
**Trask Stalnaker** 18:58 I think the ask is to, document the usage of service.peer.namespace, since we don't have any usage in the OpenTelemetry org today.
**Michele Mancioppi** 19:15 It is a bit of a chicken and egg problem, right? So, you're asking me to implement it in their zero?
Without knowing.
if this is the form that gets landed, because I would very much love not to do something that goes… that is not compliant with the upstream.
**Trask Stalnaker** 19:35 Yeah, so that is our process.
As Josh mentioned, but if you can make a case.
in the, I would put it in the PR description.
Here, make a case for that this is… that there is de facto usage of this.
**Michele Mancioppi** 20:01 It's, it's more than factory usage, that there is de facto usage of service.namespace, which implies that we need this one. It's, Yeah, so just…
**Trask Stalnaker** 20:12 admit.
So the ask is to make that argument in the PR description, so that we can follow the process and say that, okay, we, you know, we're allowing an exception here to our rule of requiring usage before landing semantic convention attributes.
**Michele Mancioppi** 20:33 pull some data.
**Trask Stalnaker** 20:35 Great.
And then the… the next step would be, stabilizing.
And the same… Requirement there around stabilizing is around usage, and requires more usage.
Generally, for stabilizing things.
And I think the service… pier. You know, I think we'd have probably enough usage of that to justify stabilizing that.
Quickly.
**Michele Mancioppi** 21:13 I'm fine making the experimental attributes perfectly, yeah.
I, I agree that it should not be stable if there aren't enough usages. I also believe that in this case.
it's, going to be difficult to see usage supported, As first-class citizens in, open territory components, because there is very little support for surface namespace.
As it is.
So, users that are trying, for example, to use service namespace are not having the easiest of times.
Hey guys.
They don't have the equivalent of… AutoService nameset. So, going to the overhead of doing, All the resource attributes as environment variable and set those things kind of curtails.
the ease of use. There's some stuff that… we're thinking of doing in their studio to make it more likely for people to do that, because namespaces are useful on large sites.
So it's a bit of a chicken and egg issue.
**Trask Stalnaker** 22:22 Yeah, what, are you seeing users… encode this into… programmatically, or are you generally seeing users using the Java agent and supplying the host name to peer service mapping?
**Michele Mancioppi** 22:42 the, it's mostly manual, in manual instrumentations.
**Trask Stalnaker** 22:49 manual, oh, so not… The facilities, the automated facility of the Java agent?
**Michele Mancioppi** 22:55 Much to my shame, I didn't even know they existed until a couple of weeks ago. They're not what advertised.
**Trask Stalnaker** 23:01 Okay, okay.
So that… that was what the… I was assuming, since you were… saying these were mostly LightStep X LightStep users, that's what the, the LightSteps folks had added that to the Java agent, because it was important to their usage.
**Michele Mancioppi** 23:22 Yeah, but Java is by far not the only language being used nowadays. It's a different time.
If we had asked the question 5 years ago, yeah, if the Java agent has it, 80% of the people using GoTo are covered.
I see way more, Node.js and Python nowadays than I see Java, especially in North America.
If it's.
**Trask Stalnaker** 23:57 Sorry, I wasn't quite sure how that was relevant.
**Michele Mancioppi** 23:59 Because the, the reason why I'm saying that is that the implementation of this being supported in the Java agent.
is nice. I have not yet met anybody who knew it existed, much less used it. I see it in manual instrumentations, where people go and encode it, for example, in stub clients they generate from OpenAPI specs.
It's also not everybody doing that. It's large sites that honestly need service namespaces.
Those are the more likely to go and set the namespaces and come across the difficulties for doing this kind of things. And they're also the ones that are more likely to have observability platform teams and the service teams that will generate stop clients, where this kind of stuff can be seamlessly incorporated.
**Trask Stalnaker** 24:51 Yeah, so, then… Right, the… this whole PR is, sort of outside of our normal process.
Where we want… and that's why we were focusing on the Java agent implementation, because that actually follows our process, that shows usage of the attribute in OpenTelemetry org.
So what I would do is, I think you just need to make the argument in the PR description.
That both of these are… de facto used outside of the OpenTelemetry org, and that it's… we need to make an exception to the usage rule, because they're just ad hoc, they're used in manual instrumentation. We just need somebody to make that argument so that we can… justify… Bypassing our process.
**Michele Mancioppi** 26:00 I understand, although I feel we're going a bit in circle on this one.
nobody is using today service.peer.name and service.peer.namespace. It's names that we came up in the SIG over the past few weeks. People are using the things that are going to match on their site, that is service name and service namespace.
**Trask Stalnaker** 26:21 That's fine, it doesn't have to be exact wording, it just has to be the use case.
**Josh Suereth** 26:28 Yeah, we want to show that people are using attributes of this nature in the, like, in the way that you're suggesting they are in semantic conventions, right?
That's the key. So you're saying, hey, I want this peer thing that represents service and service namespace. We just need proof that those are actually used by companies And that open telemetry as a whole will benefit by defining this, right? But if it's, like, one of the things, one of the reasons we have this process is it's not supposed to be, like, cool.
**Michele Mancioppi** 26:59 It's terrible.
**Josh Suereth** 27:00 Amazon or Google get to say, here's an ID, and I get to use it, no one else does. That's not what we want.
**Michele Mancioppi** 27:06 I understand. It's gonna be, the companies that, on behalf of whom I'm doing this kind of… this particular thing, they're not likely to want to go on record.
Because they have difficult processes about, going and share. It happens in Europe. It happens.
**Trask Stalnaker** 27:27 We… We trust you, we trust you, but we want, like, specific, like, numbers of, you know, and examples. You don't have to put names of companies down.
**Josh Suereth** 27:38 You can also say that, like, your platform supports it, and more than one platform supports it. Like, that's the other part. If it's just one company doing it that's different, then if we say, cool, there are several companies in the open telemetry ecosystem that do a peer-style annotation.
That's enough for this to say, okay, it makes sense to put a standard around this.
**Michele Mancioppi** 28:02 What? The only other company I know are doing connection metrics?
Just Google.
So, do you support, having namespaces there as well, or only service names?
**Josh Suereth** 28:14 We… we… we don't today.
**Michele Mancioppi** 28:17 Then the answer is I know anyone.
In the interest of getting this through, I'm fine dropping this, I will remove.
service the PR, the namespace, and implemented in TerZero as a non-standard extension.
And then we'll see how it evolves.
Yeah? Little.
And I'll do it right away.
**Liudmila Molkova** 28:47 Thank you.
Okay.
So, let's move forward. We, had a discussion, you can still pursue the service namespace, but with the caveat, so you remove it, Thanks for the discussion.
**Michele Mancioppi** 29:12 I will remove it for now from the PR, and Then we'll say again, if the usage… if more people come up and say, hey, we need namespaces because of entities, then… We'll revisit.
**Liudmila Molkova** 29:29 Okay, moving on to the next topic, Sundar Shan, is it how I should pronounce your name?
**Sudarshan S** 29:38 So, yes, yes, yeah, yeah, I… Good to meet you.
Is it clear from my side?
Yeah, yeah, go ahead.
Yeah, thanks. Yeah, so, I started, so I had contributed for, semantic conventions for Oracle Database initially. That was being, reviewed from Sorry… Lutmila, I mean, is… can I pronounce this correctly? Yeah. Okay. Yeah, yeah, thank you. So, it's been reviewed, and it was submitted.
I mean, it was merged. So the… there were further inputs on the current semantic conventions, standard, especially for attributes like db namespace.
So, the comments have been incorporated, and I have raised a PR, which would address a few of the comments, and there were some internal comments as well, so I have addressed all those inputs, and I have raised a separate PR.
to describe the db.namespace for Oracle database.
So, that is, one thing. I mean, so essentially, we want that, Oracle database semantic standards, specification to… to mark it as stable, so that, the drivers can… I mean, it helps the applications to integrate, and so the comments have been incorporated.
And the other request is, to make this process easy, and… and the Oracle database… standard, I mean, the attributes discussion, and there are some specific, attributes for Oracle database we have added, so that they are applicable for various kinds of service, global service and local service.
So, we would like to create a separate group, for Oracle Database Client and Server.
Semantic standard attributes, and we would like to hear feedback from the non-Oracle team, obviously, and we would like to add some Oracle team members into it as well.
So that we have the attributes, being defined and… Got a good feedback on that.
So, those are the two requests. One is, we would like to create a separate approvers group for Oracle database client and server.
Semantic attributes.
**Liudmila Molkova** 32:21 Yeah, thanks for coming. So, you probably heard we created a group for Oracle Cloud, and I just want to confirm with you that is this the right course of action? You would like to have separate groups for Oracle Cloud and Oracle databases?
**Sudarshan S** 32:39 Yes, yes, we would like to have a separate, group, as we internally are also a separate organization of the business.
entity. So, Oracle Cloud is a different business group, and Oracle Database Client Server forms a different group.
And the domain technologies are a little different, people are different.
Yeah, we'd like to have a separate group.
**Liudmila Molkova** 33:05 Yeah, and the other… question I have. So, you, do have some conventions where maybe we used to have some conventions, some attributes for Oracle specifically in semantic conventions, but you don't have to keep them in semantic conventions repo.
You could host them yourself, you could document them yourself, we'll provide… we provide tooling. There might be rough edges currently to use this tooling outside of SimConf Repo, but you can own them, you can follow your own process, and you… you don't… really have to do this in Open Telemetry. You can import OpenTelemetry semantic conventions and build on top Would it be something you could consider?
**Sudarshan S** 33:53 Yes, yeah, that is for, which are specific to Oracle database, right? The… Okay. Yeah, I can get back on that, yeah, we can… We can maintain those attributes specific to Oracle in a separate repo, and yeah, that's an possible option. I will just get back on that.
**Liudmila Molkova** 34:19 Yeah, thank you.
**Trask Stalnaker** 34:20 And until we have a better discovery mechanism, we could add link… I think it would be… I think it would be okay if we added links in our semantic convention.
to yours… Discovery is the big… problem, I think, right now, still, of doing it externally.
**Sudarshan S** 34:49 Yes, yes, yeah, true. Yeah, definitely we want a pointer from this standard, semantic conventions, yeah.
**Trask Stalnaker** 35:01 Eventually, we'll want to decentralize even more, and just have, like, a registry. I think, Josh and Lydmilla have more of a, know more of the vision there.
**Sudarshan S** 35:19 Okay, yeah, okay.
**Liudmila Molkova** 35:23 So, the reason, I think it might be, more reasonable course of action is that, first, we, in this group, we don't have enough expertise on Oracle databases.
Oracle Cloud may be a little bit specific, because there are instrumentations in Java… sorry, in OpenTelemetry ecosystem that actually, have the Oracle, attributes. I don't know what your folks' plan is, but, like, we… we currently don't set any Oracle-specific attributes in Open Telemetry.
And just, it sounds like if you own it completely, and definitely you can come to this group and ask for guidance, or advisors, or any help with tooling or conventions. Like, you would have full ownership, you would move at your own speed.
If we proceed with, this ask.
We would need to make sure That, you folks both are in Ottale org.
I think you also understand, I'm not sure about your… Click.
**Sudarshan S** 36:36 E-E-S-S-C, yes.
**Trask Stalnaker** 36:38 Yeah, they're… they both are.
**Liudmila Molkova** 36:40 Oh, okay, cool.
Yeah, so then, we… it would depend, like, how it works. You would be the code owners for specific Oracle files, and then there will be the second review needed from the, general SemConf group.
And we would, like, you've come… we've talked in the past, so we would need to learn a little bit from you about the Oracle every time we… Work on something.
**Sudarshan S** 37:14 Yes, yes, yeah, sure, sure, yeah, understood.
**Liudmila Molkova** 37:22 Cry.
**Sudarshan S** 37:23 Yeah, yeah, I mean, you, you want to hear now? Yeah, sorry.
**Liudmila Molkova** 37:30 It's up to you.
**Sudarshan S** 37:31 Yeah.
**Liudmila Molkova** 37:31 If you have any thoughts right now, let's talk.
**Sudarshan S** 37:37 Yeah, I mean, I just, I mean, I work in, what I call database, data access group, so both on the client and the server.
So, I mean, primarily my work was on the database drivers, on the client, JavaScript and Python.
And, Sharat, my colleague, has been in a project management role, so we both have been, even maintaining the Node.js driver for Oracle Database. Yeah, I mean… Yeah, there was a request from customers to integrate OpenTelemetry in their applications, so that's where we have written an OpenTelemetry module for Node.js, and it has been having the current semantic conventions been implemented in that OpenTelemetry module.
And it's been released, and I think… It's since, I think just 6 months back, or 3-4 months back, it's been released.
So, we'd like to add, I mean, a few more attributes and metrics, or in progress. So, yeah.
That… that's a brief thing.
Yeah, we definitely want to add a few more people, just that they are not part of OpenTelemetry members and all. Our architecture team, we would like to add one more person. So, yeah, I will request one more ID, probably in A few weeks' time.
Yes, Yeah, that's it. I can… I mean, we can keep discussing. I mean, I would like to hear more from your team. So, on the… I will… I will… so I have added for the DB namespace, similarly.
whatever enhancements, we would like to… I mean, we have new features, and we would like to bring it up here and have a discussion, yeah.
**Liudmila Molkova** 39:49 Okay, sounds good. So, I hear that you would discuss it with your team, the idea of federation and hosting your own conventions, but it sounds like you're, pretty much on the way to, Your preference would be to be in semantic conventions. Is it what they hear?
**Sudarshan S** 40:08 E, yes, yes.
So he… So, sorry, I missed that. You were asking, Instrumentation for the standard attributes, yeah, we would like to at least have A group created and get it… get the feedback across, yeah.
Yes. Is that… does that answer?
**Liudmila Molkova** 40:40 Yeah, yeah, I think it does answer my question.
Does anybody trust Josh? Do you have any thoughts?
**Trask Stalnaker** 40:51 I think that the… I see a difference with the cloud platform, providers, that there's a little bit more of an… At least short-term argument for them being in the semantic convention repo.
I think if we did bring the Oracle database, SEMCONG into Semantic Convention Repo… We would probably, at some point… at some point, when we try to decentralize things, that… that would be one of the things that we would… Try to push… Out.
So if it's… if it's acceptable to host it externally to start with.
I think that would be ideal, and, it would also give us, it would also help students, and it would also help us as a, to get feedback on how that process works, because we do… we do need to go in that direction, because the semantic convention repo is not sustainable to be the host of everything.
But we haven't really… we're just starting to go down that path of decentralizing, so as one of the early, sort of adopters of that, your feedback would be really useful for us.
**Sudarshan S** 42:31 Okay.
Sure, trust… yeah, we, yeah, I will discuss that internally and get back on that, yeah. I will keep updated. Yeah, I will update on that, yeah, sure.
**Trask Stalnaker** 42:43 Thanks.
**Sudarshan S** 42:43 That's a pos… yeah, that's a better option, as far as I understand, yeah, but I will get back, yeah.
**Liudmila Molkova** 42:54 Awesome, thanks a lot.
**Sudarshan S** 42:57 Yeah, thank you.
**Liudmila Molkova** 43:02 Thanks, okay, Kai, adding KBMMQ as messaging system. Is Kai here? Oh, hi.
**Kai Kirsch (Broadcom)** 43:11 Yep, everyone.
So, I'm here on behalf of the Autel mainframe SIC, and we have a small enhancement request, here in the messaging context.
And this is basically about, like, adding IBM MQ, so the message broker from IBM, to the list of, well-known messaging systems.
The attribute and the value are, actually already used by the hotel spans that IBM is producing. So, we're just following up here, and… making the request, basically, right, to add IBM MQ to the list, and I created a PR, however, it gets automatically closed, right, because there is no active messaging group, so I'm here to basically, asking for guidance on the next steps.
**Liudmila Molkova** 44:07 Yeah, thanks for coming.
So, yeah, messaging group is on pause, and we don't consider contributions in this space, If it was on, we would probably ask to document how IBM MQ spans look overall.
So, like, you could see there are the, GCP, PubSub, Spence.
defined in the semantic conventions, but there is no IBM MQ, Spons, and URPR. It's just the attribute. And in the past, we've had some problems, like, so we, I don't know, had 50-plus databases, and some of them were not even databases.
So, we kind of are being conservative, around just adding the constants, especially to the, namespace… sorry, to the area that's on us currently. I'm curious, why is it important for mainframes? Like, what is the… How do you depend on this? Why is it, why do you want to do this?
**Kai Kirsch (Broadcom)** 45:18 That's a good question. So, basically, right, IBM MQ is not only for mainframes, right, it's also for Linux and Windows, and we have the… often the connection that you have one message broker on Linux, Windows, and then going, right, into the mainframe.
And, first of all, of course, to trace the connection, but also to… have one default standard, because we did a little bit of research, and some vendors do, right, IBM.MQ, some vendors do IBM underscore MQ, so we were thinking having one default everyone agrees on with the naming might be beneficial for Not only vendors, but also for the end users.
**Liudmila Molkova** 45:57 And when you say vendors, who are the vendors that report IBM MQs, pants in whatever spelling?
**Kai Kirsch (Broadcom)** 46:06 Yeah, so we have, of course, IBM, which now supports, or has natively support for OpenTelemetry. Here, I'm from Broadcom, right? We are creating metrics and spans, supporting also OpenTelemetry as well, and then you have, I think, all the other big APM tools, like Dynatrace, Datadoc, right, they all provide, or create IBM and Q spans and metrics in some kind.
**Liudmila Molkova** 46:35 Yeah, thanks for the context. I mean, I see the benefit of defining this, it's just I'm, concerned that if we define just the constant, it's not enough, and we don't have currently a messaging group on to take this contribution. So I would… encourage, like, I think we can, if we… there are a lot of people who are interested in messaging conventions, and if they came along and, decided to resurrect messaging group, I think it would be possible.
But it didn't happen.
Does anyone else has any thoughts?
Okay.
**Trask Stalnaker** 47:47 Yeah, it didn't seem… Sorry, same story about, Kind of… we're struggling with the semantic conventions being the… Growing, Consuming everything, and, so we are trying to… Push things out, decentralize, try to, not just add everything, Until we, you know, have groups.
Who are responsible for it.
We realize it's not… Convenient, though.
**Kai Kirsch (Broadcom)** 48:34 But it's understandable, so basically the next step would be, or basically to wait, if our, the messaging group is started again.
**Liudmila Molkova** 48:45 Or help to resurrect it.
Make it happen.
**Kai Kirsch (Broadcom)** 48:49 Yep.
Understood, okay, thank you.
**Liudmila Molkova** 48:53 Yeah, thank you, I'm sorry.
**Trask Stalnaker** 48:56 Ludmila, do you think… Messaging is next after RPC?
**Liudmila Molkova** 49:05 I would be happy to support it if there is enough, energy.
among vendors, or somebody who works at messaging to bring it back, but I would support it.
After our PC.
**Trask Stalnaker** 49:22 Yeah.
**Liudmila Molkova** 49:24 What, what do you…
**Trask Stalnaker** 49:24 You know, we've… I would… I would join… that effort, I think. I think, for me, messaging would be… Next.
we've been going through… unfortunately, we're a little, ludmila and I have been doing these, stability efforts, from HTTP, then database, and now RPC, and… Sort of for the core pieces, and I do feel like messaging is… Probably next.
But yeah, we lost, we had somebody who was great at leading the messaging work, But let ended up… Getting a, leaving the community for other work.
**Liudmila Molkova** 50:33 Okay, Dan, thank you all.
And this is the last call for this year.
We'll be back on January 5th, and I hope everybody will have a great vacation, or if you take any vacation or holiday season.
Whatever holidays celebrate, Merry Holidays!
**Michele Mancioppi** 50:51 One last thing to close the year with a hoorah.
I retract my previous statement about removing a service that appears on namespace from the PR, because I realized there is no reason to, go and break peer-to-service without having extensibility. So, I will build a case.
per service period namespace. I just pulled the data.
a third of the tested organizations in Europe, so accounts, are setting, serving the namespace on their own data, so… I hope it's a strong enough case.
I'll show some statistics.
**Trask Stalnaker** 51:27 Well, they're setting service.namespace, but, the question for here that we need to make the, we need the argument is that they would set it, on the peer side if they could.
**Michele Mancioppi** 51:44 I don't know.
**Trask Stalnaker** 51:44 They would go through that.
**Michele Mancioppi** 51:47 In that case, in that case, interstello will implement it for them, so it's like.
Anthony, it's a bit of a chicken and egg problem here.
So, if we just go and name peer.service to service.pierre.name.
I think it makes no sense to deprecate something that people are using for an extensibility we don't intend to use right away.
I hope the argument makes sense, because the only difference between peer.service and service.peer.name is that service.peer is extensible later.
But it's an extensive.
**Trask Stalnaker** 52:24 Right, and so it's… but that's… That's required for us to, stabilize it.
Red, like… stabilizing is import… is important, and so I think we all are supporting the… Peer.service to service.peer.name.
Rename, because that… gives us… I think we feel confident, then, to mark that as stable soon.
Which is… golden, right? Like, that's… that's the goal of all the SEMCON right now, is to find things and stabilize things that we can.
**Michele Mancioppi** 53:09 In the changelog, instead of talking about the service identity, let's assume that I do pull service.peer.namespace, and just go with service.name, then the nature of the changelog changes entirely.
It's no longer about extensibility, it's about stabilizing it.
Effectively.
**Trask Stalnaker** 53:29 It's about the pots, it's about… It's about the… sure, but part of stabilizing is extensibility.
Right? Like, we don't want to stabilize something that's not extendable in the future.
**Michele Mancioppi** 53:44 I understand. I also can imagine people that would get angry and say, you changed period of service with no actual semantic change in the values of what is going on. I have asked somebody.
**Trask Stalnaker** 53:55 Oh, yeah.
**Michele Mancioppi** 53:56 Engage implementations, I would have a problem with that, if it was only that.
**Trask Stalnaker** 54:01 We understand, and we get, we get that feedback. We had all, just cdeployment.environment.
**Michele Mancioppi** 54:13 I felt that on my skin, yeah. But that was okay, I felt it.
**Trask Stalnaker** 54:17 I mean, but that's the same thing, right? Is… it was… it was a rename, for future extensibility.
**Michele Mancioppi** 54:27 Alright.
Good.
I, I hope I know what to do.
**Trask Stalnaker** 54:35 Okay.
**Michele Mancioppi** 54:37 Bye, everyone.
**Liudmila Molkova** 54:39 Awesome.
**Trask Stalnaker** 54:39 Feel free to bug me on Slack.
Yeah.
**Michele Mancioppi** 54:44 I will.
Cheers.
**Trask Stalnaker** 54:47 Bail out.
**Liudmila Molkova** 54:48 Bye, y'all, Happy New Year.
**Sudarshan S** 54:52 Thank you.
I think so.
