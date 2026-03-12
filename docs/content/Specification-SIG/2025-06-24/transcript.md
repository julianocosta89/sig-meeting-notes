SIG: Specification SIG
Date: 2025-06-24
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 03:28 Hey! Everybody.
**Trask Stalnaker** 03:34 I
**Josh Suereth** 03:35 Okay. I'll do.
**Trask Stalnaker** 03:42 Not too bad.
**Jack Berg** 03:57 Hi, everyone, one.
**Josh Suereth** 04:08 I forgot to check the whether or not is Carlos here?
We should be.
**Trask Stalnaker** 04:15 Right now.
**Josh Suereth** 04:16 There he is. Okay.
**Carlos Alberto Cortez** 04:19 Hey? Hey? Sorry for being late. We have a short agenda this week, anyway.
At least so far.
Oh, okay. I see 2 more items. Okay, let's start. Then. Sorry for me, like again. Sorry, like network. Stop like more slow, etcetera. The 1st item goes to trust.
**Trask Stalnaker** 04:37 Yeah, I'll I'll share So this came up during the Graduation review the Cncf Graduation Review. Where they're looking for a Consolidated release.
Document. So we talked about that last week, I think, and we got that Austin got that in and thanks everyone for the comments and feedback on that one of the things that they came back with is that the teams, the release people? You people outside of the org can't view those which is just a github thing.
And so, as far as looking for solutions to that We'd like to have a place where we display those team members publicly.
With that we can link to reference.
And we could certainly create a new place for that, and you know, generate that from What's under github?
And that's still. That's still might be a good solution.
But the other solution I was thinking of, since we almost have that already in most of the repos have the maintainers approvers triagers in the readme if we eyes standardize that a little bit more at least, creating anchors for those sections. Then we could use that to link to so just kind of gathering feedback here on if you think that is a good idea. I kind of looked through several repos to kind of see best common practices and best practices. I liked some of the things that some of the repos were doing. I liked this little blurb here. we've got maintainers approvers. Anyway. So I'm thinking to. If I was gonna try to automate this partially we'll see if that's success. How successful that is, I have a guess that maybe something like 80% of repos maybe will conform close enough that I can automate that, at least for those pr send some of those hotel bot Prs to repos.
I know also, though we highly value our repo independence. And maintainers kind of getting to control what they like. So I mean, I don't think I think the only thing that wouldn't possibly would like require would be this. The only thing we need really is this and so if people don't like those Prs, they could change them, do what they want anyway.
I know one other thing I know, like in go, it's listed in the contributing Doc, potentially. That's also still okay, we could link over to this, Doc.
I don't know how important consistency at is there. If people, if maintainers really do have a preference for having it over in a different place.
This is like, oh, I guess I should the kind of the what it would look like, anyway, I'm not necessarily expecting people to have too much opinion about this. It's pretty blah is just kind of formatting more or less.
**Josh Suereth** 09:29 I I like what you're trying to do. By the way, like.
**Trask Stalnaker** 09:31 So if I don't, I'll probably quote.
so I'll probably go ahead and see if if this is I've been having fun automating stuff with copilot. It's my little way to play with the new AI coolness. So I'll see if that's easy and easier or not.
And yeah, feel free to, though, for maintainers to do what you want to with those Prs. As long as we get those anchors in. I think we're good. Thanks.
**Carlos Alberto Cortez** 10:19 Daniel is asking a question in the chat like he's wondering whether we were could be used for this or not in the registry.
Commit ripple.
**Daniel Dyla (Dynatrace)** 10:29 Yeah, I was just trying to think of ways to like automate this. And we we have a way currently to map you know to to auto generate these Markdown files. And obviously the terminology wouldn't be the same. But it might work just fine. It might also be trying to use a hammer as a screwdriver, though, so if it doesn't work, it doesn't work.
**Josh Suereth** 10:52 So I will say, as a Weaver Maintainer, I think that might be a hammer as a screwdriver, but the idea that you can easily. Just push a Yaml or Json document at a template and have it auto generate code that that's completely reasonable. And I think something that would make this a lot easier. So like if you have all the Maintainer stuff maintained in a very tiny file that expands into a bigger one. That might be something we could provide support for. But I don't think you want to use Weaver's like group resolution download from multiple dependency crap. That would be really awkward, I think, but I like what you're going with there. It's just we'd have to add something completely new to Weaver for this. I think.
**Daniel Dyla (Dynatrace)** 11:33 Got it. Yeah, I wouldn't. I wouldn't bother adding something to Weaver for this.
**Trask Stalnaker** 11:39 Yeah, generating just that central markdown from the Github teams is actually something that I mean, from my experience with doing other things with copilot like a prompt. It's very good at generating that script in python for me.
So this is kind of I I was just thinking of what we could do, maybe beyond that.
**Daniel Dyla (Dynatrace)** 12:04 Yeah, I mean, if you, if you can generate it directly from the teams, then that's awesome. But, like, obviously, the emeritus is not in the teams.
**Trask Stalnaker** 12:15 Yeah. Oh, yeah, no, it's it's gonna have to parse what's there already and move things around.
we'll see if it's successful or not. I'll I'll report back on the issue. Yeah.
**Carlos Alberto Cortez** 12:31 Perfect.
In that case, let's move on. I will share, as usual, if somebody wants to share again. Stop sharing for you. To just let me know.
Okay, then it's 1, Robert.
Yes, I'm.
**Robert Pająk** 12:51 Here. Yeah. So I'm just asking for maybe last day of feedback and suggesting to merge tomorrow we have a lot of approvals. I know that even in some previous comment Tigran was also in favor of reserving 0 to represent unspecific value, and any follow up like maybe things related to the comparisons to the values be beyond 24, or below or below 0 value. I'll be addressing them in the separate issue, as I think it's a little. It's a little bit more complex.
and I do not want even to right now discuss it, because I 1st want to describe everything in an issue, and I need more time to do so.
But this further changes will not be conflicting with this one.
because this is the current status quo, basically, in most of the languages as described. And yeah, that's all from my side.
**Carlos Alberto Cortez** 14:02 Okay, perfect. Let's merge that tomorrow. Then.
thank you for doing a follow up in that soon, Jack.
**Jack Berg** 14:12 Hi.
yeah. So this Pr title says it all. We'd like to mark declarative config as stable. We recently cut a release candidate for the open telemetry configuration repository which holds the the data model, the schema for declarative config. And you know what I want to do in terms of timing is, I want to let a little bit of time pass to let the release candidate burn in and have a chance to find any, you know, issues and and receive any feedback. And once we're feeling comfortable with that, I'd like to in quick succession mark the specification portion as stable and also cut a release.
The 1.0 release stable release of the open telemetry, configuration, repository. And so you know, this Pr is out there. I'd like to people to take a look and provide feedback. And you know, assuming we get the enough approvals, I would kind of coordinate between doing those 2 tasks that I just mentioned in in lockstep. So yeah.
I wanted to mention that here. If anybody has any comments. Happy to discuss this. You know, one of the interesting things is I linked to this. You know, open telemetry configuration. 100 issue. Yeah, this, the the status of different implementations. And so there's 4 really solid implementations of this Java C plus plus go. And Php. And I know as a maintainer of Java, we've had a number of discussions related to this and users who are picking this up, and it solves a number of key problems. And then another really interesting note is that the go implementation is integrated into to the collector as a part of, you know, configuring its internal telemetry, you know where it goes, and and all the options for that. So yeah, that's that's what I have to say. See, I see Robert has his hand up, so take it away.
**Robert Pająk** 16:23 I have this one question regarding pro the process. Is there any idea to 1st track the specification compliance for this language implementations? Just to be sure that we are not stabilizing things, that stabilizing the specification. And then later, it will occur that the implementations are not specification, not are not compliant with specification.
**Jack Berg** 16:47 That's that's a good point.
you know, the people that have been building these prototype implementations. There's kind of a a tight knit group of us that are all sort of maintainers and approvers of the Configuration repository, and also maintainers in their respective languages. And so you know. I guess I'm taking it on their word. But I could go and review their implementations.
**Robert Pająk** 17:14 The thing is like. Usually, for example, when we, during, you know, just a second pair of eyes, because people have different, you know, understanding of the specification and implementation. And right now, for instance, in go, it's mainly just, you know, the very development we have not put a lot of intention of checking if it's specification. Compliant or not, we just were focused on making sure that collector just have. You know things that their needs that you're just unblocking things, but we are not very careful. At least I was not regarding the specification compliance.
**Jack Berg** 17:53 Yeah, so I'm trying to think of who would be the the people that could boot do that type of task? You know. I I certainly can. I've been involved in a lot of things. You know that. And just looking at these languages here, I know a little bit ago, a little bit of Php, basically, no c plus plus. So that's that's a problem.
**Robert Pająk** 18:15 I mean, I do not. I do not. I do not say that you need to do all the work. Maybe just, you know, creating issues and asking the Maintainers, or, you know the groups that are involved into implementing it to double check. I think it's I. I do not say that you need to verify everything. I just think that it will be good to double check some implementations. Maybe it will also, yeah.
**Carlos Alberto Cortez** 18:43 Tristan, and didn't trust.
**Tristan Sloughter** 18:45 Yeah, I was just gonna say, couldn't we create some example? Configuration files that and say, this is what should happen when this is read in and started, and then each sig can say, yes, this is the setup I got when I read this file in. So it it's working. It would be hard to automate kind of like.
but maybe if they just do it manually, that would be some kind of verification.
**Jack Berg** 19:15 Yeah, yeah, no. We've had that discussion in the in the declarative config. Sig. You know, it'd be really great to have some sort of automated process to verify the implementations of this. And I think it is hard to infer what a particular implementation is doing, and that it it, you know. It interpreted all the properties correctly. You know.
as a outside observer, it's sort of like a black box problem like, can you tell what's happening inside the black box like as an outside observer, and I think it'd be really difficult to set up that type of automation. But you know I like where your head's at in terms of the you know the manual process of that. We have these example files that exist today. And so you know we could.
They're kind of self explanatory in terms of what the desired configuration is, but you know, kind of taking Robert's point and your point together. We could open an issue with these implementations, and, you know, ask them to double check. According to the spec. Ask them if you know, when interpreting these certain example files. If the behavior is as expected. And you know, kind of treat that as all one big sort of collective task to review implementations.
**Trask Stalnaker** 20:38 Robert, I wanted to just ask if you could clarify whether you were see, seeing the this verification step as a gate, or spec stability or a gate for the implementation, stability.
**Robert Pająk** 20:55 So, yeah, I I will say that your question was is exactly what I want to discuss is more about stabilizing parts of the specification. So the order even think about not stabilizing everything as a whole, but taking each fragment. For instance, right now I, checking some parts of the SDK specification which, for example, talks about SDK extension components.
And I adapt, for example, each language has this support, and I imagine that, for instance, this part of the of the specification could be in development. Because it's also a should. I just think that we should just focus 1st on stabilizing the most crucial parts. But I'm also not sure if the stabilization here which the issue is about, is it only the stabilization of the yam structure, Json, Schema, or the specification itself?
**Jack Berg** 21:53 Yeah, yeah, I can. I can elaborate on that. So it's it's basically everything in the specification except for this part, this thing. That's, you know, the the instrumentation config api which is this piece where instrumentation modules can participate in configuration, read properties and initialize accordingly. That has not seen enough, you know, implementation or rigor. I don't think, to to go stable, but the extension components piece, rob.
I think that's absolutely critical in this. The usefulness of this whole concept is diminished a lot when extension components cannot be referenced in these files. And you can only use built-in components. That's 1 of the things we're leaning on pretty heavily.
**Robert Pająk** 22:37 Yeah. So, for instance, this is something which is very limited, supported in go.
So that's why I'm just thinking about double checking these features which are critical for stability or not.
**Jack Berg** 22:50 Yeah. And so, yeah, that that's that's definitely something we should do. I I do want to go back to Trask's comment, though, about. You know whether a review like this is a gate for implementation, stability or spec stability? You know.
I'm just thinking about in the past what what has been our our precedent for stabilizing spec features. It's been you know, the the process has generally been okay. We have one sort of Pathfinder implementation which is developed when the specification is initially written and and then other implementations. Other prototypes follow suit. And after we get enough prototypes, you know, we say, hey Are we comfortable stabilizing the spec? And there's some subjectivity in there as well. There's some discretion on the part of the the Maintainers, the Tc. Of the spec that says like, yes, in in addition to, you know, having the required number of implementations, we also feel comfortable with the state of this thing. So we'd like to market as stable but the key part about implementations and reviewing those implementations in terms of, you know, conforming to the spec. That's been a separate task. Typically, that has been like a Tc type of task. It's part of the Tc's charter. It's 1 of these we've just been reviewing the Tc's charter extensively, and it's like one of these things like when a language implementation wants to. You know, mark a key part of it logs, metrics, or traces, as stable. They, you know, open an issue and request the Tc. To review as like a sort of double check and and so I I'm not. This is, this is kind of like an interesting thing, like, you know, it's a there's like a chicken. And the egg problem almost asking the the implementations to be perfectly conformant to this spec before stabilizing it.
**Robert Pająk** 24:52 Like, yeah. So that's why.
**Trask Stalnaker** 24:54 I raised the issue is just because it from a past practice. We it's that feels like a gate on implementation stability and not a gate on spec stability.
**Tyler** 25:11 Yeah, maybe I could just provide a little context, though, because I think what Robert's getting at, though, is that like a lot of the times when Go goes to stabilize a particular signal or component, it finds a lot of inconsistencies in the specification is, I think, where he's coming from on this one. And you know things that maybe aren't necessarily like.
not implementable, but just something that isn't clear or something that isn't like, I think, well drawn out, and I think to his point, he's just he's just asking to maybe not have it so that he has to work against a stable specification when he comes to these sort of things reviewing the implementation, trying to stabilize that.
But I also think that maybe, Jack, you've kind of assumed the the responsibility that he's kind of talking about, and maybe I would ask that like we could ask, like Robert or the rest of the Go Sig to spend a little time in the next week, and just going through and asking people who haven't already looked at the specification to go, you know, actually do the review of the implementation and check it out, because I think to his point, like it actually makes a lot of sense. When you have new eyes come out of the situation particularly. Maybe not you or me, Jack. Yeah.
**Jack Berg** 26:19 Definitely.
**Tyler** 26:20 Like, yeah, to give some sort of like sanity check and making sure that like things are actually making sense. And I think maybe I was speaking for Robert, and you can chime in. But like that's, I think, a great idea is to just have you know, people from our the ghostig. And if we can get other people from like C, plus plus ornet, or something like that.
to go take a look at existing implementations and see if, like, they're compliant in this next week, maybe put a time box on it as well.
you know, that's also something. Because, like, if if they're not going to get involved. And and I think you can't just hold the specification up as well. So maybe that's that's the way you want to go here.
**Trask Stalnaker** 26:56 Yeah, that I like that. That was my only worry was putting a gate on like the spec stability that wasn't under sort of the control of the yeah that could force it to extend for a while.
**Jack Berg** 27:15 Yeah, I would love it. If people, you know, there's always this kind of critical point where a spec sub working group or Sig, you know, is wants to bring its its work back to the mainstream right? So that's kind of what this stabilization stabilization exercise is. We're merging the config sig back into the the core spec. Sig, and you know, marking it as stable, and we'll be actually winding down that sig afterwards. And so you know it, it becomes something that is part of the the core. Spec. Sig. Now, and all the people that have.
you know, the can land eyes it. It would be fantastic if you if you could do that, and I'd be happy to you know, respond. And and and, you know, react to any issues or inconsistencies, or just like phrasing things that come up in the process. So.
**Tyler** 28:10 Yeah, okay, I'll definitely have this as an agenda item for the ghostig this week. And so maybe the ask for other maintainers on the call is, if you could do the same and go through a review of the specification and see if you can be compliant. If you aren't have an implementation yet, and if you do have an implementation, just double check, the the details of it would be great.
**Jack Berg** 28:35 That's a good way to put it. Actually, Tyler, like as a Sig maintainer. If you could review this coming from the perspective of like, can you be compliant like? Is there any language in here that you know? Just it seems like it would be very difficult or impossible to be compliant with, based on the, you know, the constraints of your language.
**Carlos Alberto Cortez** 29:05 Okay, I would like to call time of this one. I think there's a clear set of steps to follow up with.
yeah, okay, perfect. Thank you so much. In that case.
Let's move to the next one.
Extending attributes to support complex values. Trust you want to share. Probably it's too short. Right?
**Trask Stalnaker** 29:27 No, no, you you can share. So after last week's discussion, we ping the Maintainers got several Maintainer approvals on it.
So is looking better on the number of of approvals.
There's a couple of folks.
Josh, Daniel, Dyla, And Sam who have commented on the Pr. But haven't that. If you all would have time to, that would be amazing.
I only got feedback from one person as far as they don't. You know they're just not gonna approve it? But not block it. So that was. Still, if you are in that camp let me know I was kind of wanted. That was one of my worries was that there might be like a silent majority of folks who just didn't.
didn't care or didn't think it was a good idea.
Since there is some. It's a little contentious as far as this breaking, whether it's since we're reverting a some language that said it would be a breaking change.
That's it.
**Carlos Alberto Cortez** 31:14 Okay, perfect sounds good. Yeah. So yeah, it's up to you. Trust yourself when you feel that this is ready. Look, waiting for a little more of time. But in my opinion, I think end of the week could even be done. Given. We have enough reviews, but it's up to you. I will let you read it.
Sure. Yeah, thank you, sweet.
Okay. Next one entity. SDK, proposal. Josh, you want to share.
or you're okay with me sharing.
**Josh Suereth** 31:48 You can share, you can share. So basically, this is an Fyi. This is still in draft because we had the Entity Sig doing some reviews, but I want to give everyone a heads up that we are making a cut at the SDK specification. This is based on things from the Otep, and some things from the prototypes, things that change from the Otep that I just want to call out. Basically, we're going to add into the SDK a thing called entity, a thing called entity detector. Those are both in the Otep.
We want to create something called a resource provider. But there are existing implementations of resource provider, even though it's not specified. And so the name might be taken. And that was like a problem with the Java prototype that we elevated, so we called it entity Provider. But we're not happy with that name, and we would like to use the name resource provider, if possible.
So that's something we have to kind of discuss and kind of think through as a group. You can read the the proposal and see what we're providing or what what this thing does for now. There is future work on that component. But I yeah, go ahead, Daniel.
**Daniel Dyla (Dynatrace)** 32:53 Is it not possible in Java to just extend the existing resource provider? Is it doing something fundamentally different, or is it somehow difficult to extend for language specific reasons given that it's a part of the SDK, not the Api. It seems like sure, fairly easy.
**Josh Suereth** 33:10 No, it's all of the above. So it's it's any package which is not technically part of the SDK. But then, once you create something in the SDK with the same name. All your imports get really weird and you have to specify full packages for one versus the other.
For context, resource providers part of their auto configure interface but not part of the SDK, and so you can create it in the SDK, but then imports get really weird, and it might not be source compatible for some people if they well, anyway, it is source compatible till you make an import, and then all hell breaks loose, and it looks really weird. So yeah, it's it's just it's really awkward, because the term got taken. And it's not in the SDK.
**Daniel Dyla (Dynatrace)** 33:53 Okay.
**Josh Suereth** 33:56 It also uses like types that are not available in the SDK, so like the one thing you could say is, let's just make the interface of that thing be the same as what's in the SDK. Anyway, there's language specific complications there, that is something I can actually try to start working out with the Java folks if if we want to go that direction. I don't know if there are other languages that use resource provider as a name. But yeah, like.
anyway, I agree with you. Entity Provider is not a good name for it. We probably need to find the right name, but the but the capabilities of that thing I don't think change.
Okay, if anyone has questions feel free to ask, we have 2 prototypes that are kind of reviewable. One is in Java against the current. Otlp proto. One is in go, which is against kind of the original thing, that one we plan to bring more up to date against this current specification, and I don't recall the status of the Javascript prototype, but I think we plan to provide one of those as well.
**Daniel Dyla (Dynatrace)** 35:05 And Js prototype just doesn't have the. I think the entity provider.
But other than that, it's almost yeah, almost done.
**Josh Suereth** 35:14 Awesome.
Yeah, but I'm gonna take this out. Well, I might leave it in draft while we argue about what the name of entity provider should be. But the the contents and be behavior of those things won't change. So just looking for feedback from folks.
Yep, this is just a heads up.
**Carlos Alberto Cortez** 35:35 By the way, what happened to that was related to this.
**Josh Suereth** 35:40 It got close to stale.
and the expectation I have is that Otep will get renewed eventually, and that behavior will be added to this part of the spec eventually.
So it it is important to have that as context, I think I don't. Yeah, I I included. So the stateful behavior for Nc. Resource and entity provider is in that does not address in the bottom, and I have a link to the Otep so you can. That's Ted's Otep there, which is closed. That is something that we think will come to entity provider. But it's it's not in this part of the spec. This is the the foundation. First.st
**Carlos Alberto Cortez** 36:21 Okay.
**Josh Suereth** 36:22 Yep.
**Carlos Alberto Cortez** 36:23 Makes sense. Thank you.
**Josh Suereth** 36:25 Cool.
I think I had one other one after this, but I don't know if someone else was before me.
Oh, they would have questions first.st Yeah.
**Carlos Alberto Cortez** 36:34 Do you need access to a comment in the chat like about Javascript?
**Josh Suereth** 36:42 Oh, yeah, about how trying to avoid implementing things that is on the spec. Yep.
**Daniel Dyla (Dynatrace)** 36:46 Yeah kind kind of an aside. Just we we always try to avoid. We turn people away all the time because they're trying to implement stuff that isn't specified, and we sometimes annoy people because of that, because we tell them to go to the spec and spec things out.
But in cases like this it pays off.
We don't have a resource provider.
**Josh Suereth** 37:12 One thing I will say that is challenging with this work is as we're exploring different SDK implementations of resource. I think the fact we're trying to change. Resource is catching some of the sdks off guard.
I think. Yeah.
**Daniel Dyla (Dynatrace)** 37:26 It was pretty stable.
**Josh Suereth** 37:28 Yeah.
Yep. So we're we're being very careful with that. And you'll see that in the SDK, of how this, how this looks, how this works. There should be a compatibility layer that that like lets you onboard to this over time and not break users. Okay, my second topic, if is it okay? If I move on cool. So there's a context propagation guideline for SQL. Server. This is really cool. By the way, if you look at this, this is basically how to get trace ids into the SQL. That you send to SQL. Server in a way that you can get metrics by trace Id and that sort of thing, or get get data by trace. Id right in SQL. Server. So this kind of explains how to take trace parent context, and W. 3 C. Ids. If you will, and put them into SQL. Server. It's very, very specific to SQL. Server.
Now, there's a second link here.
So this is a proposal, for in the specification there's a second link, which is the compatibility considerations for aws. And this is how to do context propagation in the context of the X-ray format and lambda and the Aws Sdks. And this is basically how to get data in and out of the end variable or property variable, that the SDK has for doing context propagations very, very specific to Amazon, and it is in the open telemetry specification under a compatibility guideline. Now there was a point raised in semantic conventions which I think is powerful. That is this kind of document and specification right? If folks who are doing instrumentation come to semantic conventions to do instrumentation. Does this belong in semantic conventions?
Right? To begin with, because that's where you, as an instrumentor come to understand how to do instrumentation, and that we should centralize that information in that specification. So actually.
you know, my my thinking is following priorities. One is all context. Propagation related. Customization docs that we have for people should be in a central place.
right as priority number one. But priority number 2 would be probably that should belongs in semantic conventions going forward. And so I think I would like to talk to this group about should we move both of these things out of the current spec and into semantic conventions. We have a version of that doc in semantic conventions like it links to the other one. There's like a dependency that's awkward. So I'm suggesting we move all of it into semantic conventions. Bluemilla. Just just answer that one good. But go ahead. If you have more you want to say.
**Liudmila Molkova** 40:12 Yeah, I I want to emphasize that people that would see instrument one part of instrumentation like which attributes you said, which spans you, create and semantic conventions, and having to go to the spec to understand how to inject or extract this context feels weird, but also to your point. It's the same document. We just forgot to remove it. There is no link.
really. I I must have missed that. Okay.
**Josh Suereth** 40:45 Why don't we just remove this from the specification completely, then, because semantic inventions has to depend on the specification. So we have to be the same if we have the. Does anyone have any concerns with us? Kind of removing this kind of platform specific, you know guidance from the specification and moving it all into semantic conventions somewhere, probably in non-normative.
**Carlos Alberto Cortez** 41:11 Even if it wasn't a duplicate, I would be supportive of moving everything to same column, for now at least.
**Josh Suereth** 41:19 Okay, cool.
That's that's it. Then let's if anyone has any concerns, please raise them and we'll we'll make sure that we do that.
**Liudmila Molkova** 41:32 A a question on this. I think, Sam, you have a Pr. Up and against the Spec. That SQL. Server.
But after this discussion we probably want to come back to the sum Conf. Pr. Right.
**Sam** 41:47 Yeah, I'm okay. With that, I I just post this as a demonstration like how it looks like.
**Josh Suereth** 41:56 We should also make a pr to remove the aws things from the spec as well. So.
**Liudmila Molkova** 42:05 I'll do it.
**Josh Suereth** 42:06 Okay. Thank you.
**Carlos Alberto Cortez** 42:07 Thank you.
**Liudmila Molkova** 42:08 Thank you.
**Carlos Alberto Cortez** 42:13 Okay here. No more comments on this one. So thank you so much, Josh, and we change. We switch to the other. Josh, please.
Good share are 2 min, probably short.
**jmacdonald** 42:23 No, thank you. Just a quick note. To everybody here. So 3 prs have now merged over the last 6 months, describing a new proposal, a new, a new approach to consistent probability. Sampling and this includes a design for new Apis and SDK features related to sampling. I am here to remind us of this, and offer myself as an advisor to help with the implementations of this sampling Sig meets every other week.
and the next meeting will be the following Thursday, not this week, but next week. That would be a great place if you felt like this was a good like. If you had questions and wanted to talk about the specification work. We'd be glad to talk about it. There you can. DM me if you'd like help with this as well. And lastly, I've implemented prototypes for go and for rust. So I'm gonna reach out to go to see if my prototype can be helpful. I'll reach out to Russ to see if my prototype can be helpful.
and that's what I have. Probably in the next week I'll file issues in the S. In the various repositories, asking for this explicitly. Thank you.
**Carlos Alberto Cortez** 43:31 By the way, just will comment on this one on random requirements following the trace contact level 2 Sergey or somebody else feel an issue, or or put a comment about that hotel could help to make this stable on the W. 3 C. Part.
**jmacdonald** 43:46 Yeah.
**Carlos Alberto Cortez** 43:47 I don't know whether we should do some help there. So the actual sdks and Apis can implement this, you know, in on our side, you know.
**jmacdonald** 43:56 Because I'm.
**Carlos Alberto Cortez** 43:59 So I'm saying.
I was trying to work on the job implementation for the trace radio, which is this part just modified existing traceity radio based sampler. But this part is missing, you know from this the public part, you know, the public Api.
**jmacdonald** 44:15 Why don't we talk about this offline? I think I'm a little confused, but I'd be glad to help Carlos.
**Carlos Alberto Cortez** 44:19 Perfect. Yeah. But anyway, I guess, yeah, yeah, okay, let's do that.
The second question that I have is that once we start making this part stable like the you know, the composite samplers.
This is a big challenge, to be honest, you know, and it's nice. But currently I think that a lot of the stuff that is implemented, for example, in the case of Java, it exists in country correct.
and I wonder whether it stayed there for long or should eventually be moved to I because I was thinking, what like, yeah, it. It's a big chunk of work, you know. And I, once we become stable, I wonder whether it would hurt to keep it in country.
**jmacdonald** 45:03 That's a good question. I wouldn't. I'd love to hear what others think. I'd actually like to hear what Trask thinks. I would add that Go has a similar situation. There's a legacy sampler that that I implemented several years ago. It's in the go contrib so like in samplers, consistent probability, and it should be deleted because it's it's a lot to maintain. I don't know if it's if it's required any work, but it's a lot of code.
and I don't know. I I think it would be. It's a good question. Should we put this stuff? It can be additional. It can be added on, it doesn't require it's not required to be in the core, since it layers on top of the existing sampling interface.
so yeah, open question. Should we let this be an optional? SDK feature that can live in Contrib?
That would be that would be interesting.
of course, you know, there's a reason that we're adding these specs on that, and.
**Trask Stalnaker** 45:54 Topic.
**jmacdonald** 45:54 Head, Trask.
**Trask Stalnaker** 45:58 Yeah, i i i think that's historically decision. Act that that we. If something is in the spec, we do put it in core. That's kind of our general barometer, for whether it goes in core or not. So now that it's spec I think that probably we would move it into core.
**jmacdonald** 46:36 This sounds good. You know. The the next step for this group, by the way, is to approach the the configuration working group because we we feel that what users have asked for is ways to configure their samplers with rule based configuration. And that's what we're after. So that would be the next step. Just so everyone can understand where we're heading to be able to configure the sdks. I don't know if it would be possible to have configuration in the standard config object, and then have your sampler implemented in contrib.
**Jack Berg** 47:04 It is possible with this thing that Robert and I were talking about earlier, this idea of extension components. So declarative config has facilities to reference. All the SDK extension Plugin interfaces by name. That aren't part of the built in implementation. So exporters samplers, whatever.
And yeah, this is a perfect match for declarative config.
and you know, I've talked about this in previous spec meetings, but I would love to see us get to a point in specification development where every new proposal to the SDK. Comes with a proposal for what the corresponding configuration story looks like. I think that's a great way to to visualize what the user experience is going to be when we're developing new components. I'd love to take that for a test drive with this new sampler concept, and we have facilities in declarative config for experimental portions of the schema as well. So our stability story does not interfere with this new sampler work.
**jmacdonald** 48:10 Thank you.
**Trask Stalnaker** 48:12 I, Josh? I had a question about have you discussed the sort of steps to stabilization?
Spec stability?
Because it sounds like you have. Potentially, it sounds like you have 3 language prototypes already.
So I mean, potentially, you could start pushing towards stabilization, which is a great signal for getting broader like it's sometimes hard to get. You know. Then the the long tail of languages that we have to pay attention to things invest in things that aren't stable.
**jmacdonald** 48:53 Truth is, I wouldn't blame people for not doing this yet. I'm saying that out loud. But one of the things I'm working on to try and make this more appealing to everybody is the collector has some components that that ought to be leveraging this information better. So right. Now we have a probabilistic sampling processor for the collector that does span level sampling according to the specs. And that's already done. That was actually, I would count that as a prototype as well. We can make that 4 prototypes.
So the the currently I'm kind of working on the tail sampling processor in the collector which ought to be able to use this information to to accurately sort of sample, and then and then a span to metrics component would give us metrics from sampled spans which we could do from tail sampled spans. That's the idea. Once that stuff's ready, I think it'll be a lot more compelling to get this feature done. So don't, don't rush. If this isn't interesting to you, there will be reasons to do this later.
Thank you.
**Carlos Alberto Cortez** 49:56 Perfect. Thank you so much. Yeah, let's talk offline about my last question. Okay, other than that. That's all. In the agenda. Do we have anything else?
Okay? I think we don't. So thank you so much. 10 min back. So have a coffee or something. Stay safe. Ciao.
