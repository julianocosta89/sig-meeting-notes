SIG: Specification SIG
Date: 2026-07-07
Duration: 66 minutes
============================================================

## Zoom Recording Transcript

carlosalberto 00:03:08 Hello, people. We have 5… Members.
of the group today. Let's wait a couple of minutes. In the meantime, please add yourselves to the agenda and add any important items. Five minutes ago there was only one item.
So we should have enough time to talk about different stuff.
Okay, let's start in one minute.
Okay, I think we can start.
We have, actually, yeah, don't forget to add your own names.
That those… helps.
Keep track for people who are around. Okay, so let's start.
We have enough people, I think.
The first one is I did it myself, although that was created by CEO.
Basically, it's an issue which has as of now, a PR open around this. This is for adding a cross-language guidelines for instrumentation library.
Outdoors, and basically, as he mentioned, there's already… Existing documentation of different seeks for doing this.
And especially, you know, in .NET Go, Java and Python, and specifically it talks about whether tracer provider or tracer and, you know, the other provider and their objects should be passed around.
How to manage errors, how to handle errors.
Propagation, et cetera, you know, so basically, I would like to get, some opinions on this one, on how important this is.
As you can see here, it has the label of community feedback.
So, see, you already created a PR?
For this one, By the way, which is very helpful. But yeah, we can probably also go and get some interest from maintainers here.
This is the related PR I was talking about, which tries to settle, you know, to a To provide a standard, initial document for this.
Liudmila Molkova 00:06:36 A lot of the things are in scope of semantic conventions.
And there probably is some guidance that should live in this pack, but.
Yeah.
A lot of them.
should be part of semantic conventions like instrumentation, scope, where usually context propagation or.
What else? Maybe even configuration.
carlosalberto 00:07:17 Yeah, that's a fair one. And I think that probably this document will have to move some of its contents to, you know, to the same comp repo instead.
Liudmila Molkova 00:07:27 We have a document in Semconf on how to record errors and exceptions, and maybe this should be just a short section that leads to that place.
David Ashpole 00:07:40 Just to clarify, I think for errors, it's… what happens if the instrumentation library itself encounters an error, not how to record errors on telemetry, necessarily. Those may be one and the same.
Liudmila Molkova 00:07:55 Oh.
David Ashpole 00:07:56 This is like, I think that there is something a little bit missing where like if somebody wants to go write a new instrumentation library, I don't know if there's one place where we have like a set of instructions written down. There is some stuff on OpenTelemetry.io.
But I don't know if, at least right now, there's, like, a single place where it just describes, like, oh, you're an instrument, or you're gonna write some instrumentation, here's all the things you should keep in mind.
If there is, you know, we can… just edit that and add to it, I think.
Liudmila Molkova 00:08:34 You're right, I don't think there is.
tnajaryan 00:08:38 Yeah, I think it definitely would be great to have this A sort of one document, which is guidelines for Anybody who wants to do instrumentation.
so that even if the information can be found elsewhere, scattered around here and there in the spec, I think it's still useful to have to have it in a single document. And I think I agree with you, David. It would be great to have this published somewhere else, which is more user facing rather than in the spec, or maybe both in the spec, and somehow we consume it in the in the website.
But I like the idea of having this document.
carlosalberto 00:09:14 Yeah, on that front, this could be, you know, a guidelines, not like specification itself. So yeah, it sounds good that it could be user facing, you know.
Okay, so, So, In that case… Let's just, sorry, that was… But that's not what I was planning to do. So what about we move these to actually like ready to be taken and Tiga already has a PR for that.
tnajaryan 00:10:07 Is that okay? Yep.
carlosalberto 00:10:09 Perfect. We'll assign that offline to not take more time here. Okay, thank you so much for that. The next one is Robert. He's offline, but he wanted us to talk about this one.
Add attribute value depth limit for race and map.
Maps.
David Ashpole 00:10:33 I'm also happy to introduce it as well, but it's a… It's similar in spirit to a lot of the other attribute limits we've been putting in place.
we generally try to make sure that.
You know, regardless of what people put in, you know, you can't DOS yourself.
And so this is one more limit, just to bound the… depth of nested attributes. So, you can only have 64 maps nested inside each other, and then Then you need to stop.
I thought it sounded pretty reasonable.
So I have approved, but if others could take a look, I think that would be good, too.
tnajaryan 00:11:11 We have the the attribute size limit.
As a concept. How is it defined for attributes which have nesting?
does it… what does it say for the attributes which aren't primitive types? I'm not… I'm just forgetting.
Is it silent about that at all, or does it just… Does it talk about the wire size?
Josh Suereth 00:11:36 I remember not being happy with it. I don't think it talks about wire size. I think that's what we wanted it to be. Unless someone made a change. because we talked about it, what, like three years ago or something? I believe that it is, it applies individually for every, like, component of the attribute instead of on the.
overall attribute.
And I think that is pro… oh, my camera's not on, sorry.
I think that is problematic. Like, I think, I think we probably… the intent was to have it be the wire size, Tigran, but we couldn't figure out how to enforce that. That was, I think, why we didn't do that.
tnajaryan 00:12:13 Okay, what I'm asking, the reason I'm asking that question is, you probably are most concerned about the overall size of the entire… thing, right? If it's nested, the whole tree, essentially, how much it occupies. The limit of the depth itself doesn't constrain that very much. Even with 64 depth, you can still have a very, very large tree.
So… In my mind, if we could… if we find the right way to limit the overall size.
That puts a natural limit on the depth in some ways as well.
And in that case, it may no longer be necessary to have the depth limitation.
Because… As an implementer, my concern is primarily about how much memory I'm using per attribute, not What the depth.
Of that nesting is really.
I may be wrong on this, but there's probably situations.
Tyler 00:13:23 You shouldn'.
tnajaryan 00:13:24 your depth matters, I guess.
Tyler 00:13:27 Yeah, I think it's, I think the wire format's fine, but, like, to your point around, like.
the memory usage, but it's also CPU usage as well, I think is where this is coming from.
memory and CPU. So, like, if you start doing attribute processing.
and you have like a recursion depth that can cause a stack overflow like that's that's a problem.
And if that attribute came from an untrusted source, that becomes an even bigger problem, is where this is coming from. And, like, you can probably still fit that within, like, some sort of wire, Data size?
It's more, I think, just about, like, how that gets unpacked locally on a system, I think is where this is coming from.
tnajaryan 00:14:13 Okay, so I guess we're talking about situation where On the wire, it's, let's say, a megabyte or something, which is reasonable for a wire size, but it ends up being a nesting of hundreds of thousands of elements, which then, if you process it recursively, poses you a problem. I think it makes sense. I agree. Maybe we need to have both.
I agree.
Liudmila Molkova 00:14:39 I think there are two types of limits that we have. The one is over the wire, what we have in the spec.
But I think.
Java. I'm not sure if Trask is back, and he is here. He'll keep me honest. I think Java is adding sometimes limits for things like database query, or… then future Http request body that protects the instrumentation, the memory.
and I'm not sure which limit is implemented here.
As we probably want the in-memory limit on everything.
And… It's by default.
And it's something ridiculous like megabytes of string text or you know.
Yeah, 10,000 is another example for the depths. And it's different than over the wire limits users would configure. And we might not need this to be configured by users. It's just a safe belt by the SDK.
carlosalberto 00:16:01 Since I am… I'm getting some silence from… After this discussion, I will add these comments about probably the need to have both limits and how this one would be needed by what Tyler mentioned.
Let's keep discussion out of line, if that makes sense.
Okay, thank you so much for that.
Ted, 10 minutes. You want me to share? I can share for you otherwise.
Ted Young 00:16:31 You can share, it's fine.
So the first thing I just want to note, so we have a security SIG. It was held down by Microsoft. One Microsoft person in particular, I believe, is moving on in their career.
We've looked, at Grafana Labs to kind of help staffing it, but we've had a lot of security-related things going on, you know, so we've been stretched a little thin. So I'm just noting that, this SIG, Is, is pretty thin in terms of staffing right now.
And maybe this is a good time, to… to talk about… about rebooting it, and, maybe get some input from maintainers about what they think would be helpful to have from a security SIG.
The point of the Security SIG was to basically expand beyond the TC and maintainers the number of people who have access to our security backlog.
Who are security experts, who can potentially, you know, help us, carry the load.
I think if we redefine the mandate for this SIG, we could sort of shake the tree, go back around to different contributing organizations, since security's on a lot of people's minds. But I think we would want to come up with a clear idea of what What this thing would be doing.
I do see Tigran saying we need Riley. It would definitely be helpful to have Riley for this discussion.
I was just curious for maintainers on the call, if you could get help with security, just what would be the list of stuff that you would find valuable to help you with your security backlog?
Nothing, everything's totally chill. That doesn't take up any of your time, so no big deal.
Josh Suereth 00:18:48 I'll jump in real quick from, maintaining, like, Weaver and Semconf. If… if there was a way to make, dependency updates less annoying, because the default config is awful.
And if there was, like, some sort of tool that would, like.
make it less annoying to deal with, or every day… I know Tigran had a rant about, it was either Dependabout or Renovate, I forget which one, about how you get a thousand individual commits, they have to go through, they're always out of date, because they always conflict with each other, like.
That's frustrating and is low-hanging fruit. But honestly, the other thing is, we did a review of all the security things in Weaver, like all the reported issues in GitHub. And there are some things where we don't know how to check all the boxes to get all the stars.
And so, the thing we would really want is, A, do we need all the stars? We don't think we do. Some of them are really hard to get checked, and maybe not useful. But B, you know, should we check all the stars? And if so, can you help us do that? Because some of them just seem like they're impossible without organizational support.
Ted Young 00:20:00 One question I have is, I know there's been an uptick in sort of, like, really low-quality reports by people basically sort of running… using AI to run scanners and other things, and then sort of, like, auto-post security things, and I know that's been kind of taking up people's time. I'm not sure how much a centralized security SIG could help maintainers go through that backlog, but I'm curious if that's another place, like, are there ways To take the load off of maintainers around triage, That.
Beefing up a security SIG could help with?
Armin (Dynatrace) 00:20:48 So, one thing that I could imagine SICK Security to do is to work with SDK maintainers to define like the the threat model and what's considered a an actual vulnerability that's something that the collector seek one of the most exposed ones and with the most like fractioned components with different entry points into the collector with each and every receiver and such that's something that they did on their own without the the help of or with assistance from SICK Security and review, and the TC also reviewed it.
But that's something that they did on their own. Maybe that's something that… that the SDK maintainers would find worthwhile and would my… would need help with. And probably also something that should be done org-wide, for our repos. Not sure if it needs to go into, like, the spec as such, or some supplementary addition to the spec, but maybe that's something that would be helpful.
Ted Young 00:21:52 Okay, great.
Armin (Dynatrace) 00:21:52 Just to give an example, there were a bunch of security vulnerabilities reported for the collector, where an authenticated receiver, or an authenticated user would send a lot of garbage to a receiver, and then the receiver would not be happy with that. And the model that the collector maintainers came up with is If a receiver supports authentication, then you're supposed to use that authentication as a best practice. And then if someone can bypass that authentication, it's bad in any case. But if it's a properly authenticated client and that one is acting up, someone who's expected to be a good actor, then that's a normal.
bug or a normal public feature to be to be fixed rather than a vulnerability with like Fast lint resolution.
Ted Young 00:22:53 Cool.
tnajaryan 00:22:57 Some were related for the advisories.
Someone from the TC, please remind me if I'm forgetting… I'm not remembering this correctly. We… I think we were talking about keeping the original TC member assigned to the advisory for the for the duration of the advisory. Did we enact on this? I'm forgetting.
we were.
Armin (Dynatrace) 00:23:17 Yeah, there was some PR that merged that one, because we figured that it doesn't make sense that Sunday evening we hand off in Hong Kong.
tnajaryan 00:23:25 Previously we were handing off. So we enacted that. You're saying, Armin, is that in effect now already? We're keeping the original assignee?
Armin (Dynatrace) 00:23:35 Yep, it is.
tnajaryan 00:23:36 Okay.
carlosalberto 00:23:37 I'm here.
tnajaryan 00:23:39 Okay, cool. That's good.
For people outside the TC, we were previously doing, like, we have weekly… on-call rotation, and previously we were handing off the advisories from one TC member to another.
based on that same rotation. We no longer do that, so that we keep the same person assigned to that one advisory, so that the context is not lost.
Ted Young 00:24:08 Yeah, and a good point there is if we feel like there isn't enough sustained work to have a security SIG, you know, the security SIG was basically created to help take work off of the TC's plate and maintainer's plate, but if we've reached a point where we feel like there isn't enough there, then it would probably be best to then shut down the Security SIG and just fold it back entirely into the TC.
I… I feel like… we could use help naturally. But Anyways, it's an ongoing conversation.
But I just wanted to bring it to the attention of maintainers, if you all have thoughts about this. Because I know something on the TC and on the GC we've been thinking about. Just want to let you all know about that.
tnajaryan 00:24:59 If Riley was here, he would tell you about a number of… a bunch of problems with security. I think it would be interesting to have this discussion continued next week when he's here.
Ted Young 00:25:08 Great. Sounds like a good idea.
carlosalberto 00:25:10 You can just write him, Ted, offline and have a pre-discussion and just come next week also, you know, to share that.
Ted Young 00:25:18 No.
Okay.
I think we can move on. It's just more bringing that to people's attention. We'll have a better discussion when when Riley's back.
carlosalberto 00:25:35 Yeah, but you have the next item, so please take over.
Ted Young 00:25:38 Okay, so related, just kind of like part of post-graduation, thinking about how we structure and manage projects.
again, bringing it to the attention here, not a lot of client-side maintainers on this call, but something we're seeing on the clients is they're maturing enough. We have clients in iOS, we have clients in Android.
clients in the browser. We're now looking at a SIG that's doing Dart and Flutter, which is kind of Cross, you know, like, cross mobile, cross browser platform.
And when you stack all of that up, there's… feeling like a need for like sort of a layer of management, right, and coordination across the different clients. I think part of that is driven by, you know, we have a technical committee and they're awesome, but it's very much heavily weighted on the server side. So when we look for things like sponsorship.
for Flutter.
And things like that. It is kind of a hard ask to make of the TC right now because, you know, the TC doesn't really have.
a lot of client-specific expertise.
So that's, like, a pretty burdensome ask, you know, I think, you know, to make for people on there. There are people in the client SIGs who, you know, because they've been around for a long time now, are kind of gaining enough experience that they could do cross-client, you know, organizing.
The three things we're kind of seeing the need for is, one, taking advantage of federated semantic conventions, right? So for… the semantic conventions for client-specific things to get owned by those SIGs, and for them to coordinate amongst each other about things that are specific to clients across all the different clients, but people on the server's side don't care about.
The other is there's still some remaining, like, spec issues that are very specific to things that clients need, but again, not super interesting to the server side, and it's always been a bit painful to kind of be… have that work be a little bit gatekeeped by people who mostly have server-side experience.
And again, with this Dart Flutter group gaining a lot of interest, that's specifically something where it's going to drive the client SIGs to have to really make some decisions about what are cross-client semantic conventions, for example, versus things that are specific to Android or iOS or the browser, because you're now going to have Both, existing within OpenTelemetry.
So, again, this is something we're talking about a lot in the different client SIGs, but I just wanted to raise it here as an example of a place where it seems like it would be helpful to have, you know.
a layer of management, as opposed to, like, a cross-client SIG, where it's just people from the different SIGs just… just talking to each other, but… but not necessarily feeling like anyone's in charge or has… has some agency.
And Tigrid, I see you got your hand.
tnajaryan 00:29:02 Yeah, hey, since I guess Josh stepped down, we now have a seat in the TC that we'll elect for, and one of the inputs for candidate selection is the expertise that the TC is missing currently. Like you said, we're missing the client side expertise, so it's gonna be one of the… dimensions we'll be looking for. So we hear you loud and clear. We'll see what we can do.
Ted Young 00:29:26 Awesome.
I think that will definitely help.
but it's also, I think, an example of, like, you know, having a seat… someone on the TC who has client-side experience will definitely be helpful, and then they can sponsor these SIGs, but, As the project grows and grows, I think there's maybe other areas where something like this might be happening. So again, this is just more of an FYI, just bringing it, you know, to the maintainers at large, that this is an example of a place where we feel like like.
you know, it's… we need a lot of expertise, but it's… a lot of it's somewhat concentrated around issues that a lot of other people in OpenTelemetry maybe don't care about. So, you know, finding a way to sort of grow the project to have these parallel tracks without the project becoming So disconnected from each other that the different parts, you know, the left hand doesn't know what the right hand is doing.
carlosalberto 00:30:31 I have a specific question, if you don't mind. So you mentioned some issues that SIGs may need, and I'm thinking about their source.
changes that you may need from the client's side.
what's your expectation on that front? Because my expectation would have been that somebody from that group comes and iterates on that, and probably somebody from the TC could sponsor, you know, understanding what you want to do. But probably it would be better for you to have somebody at the TC that could actually drive that, like.
Create the PR, try that.
More than actually just doing the review, right?
Ted Young 00:31:11 Right, like if it's just, if we're just sort of doing things like on an issue by issue basis or point by point basis, you know, the different maintainers from the different client SIGs are pretty good about being like, I wonder if this is a cross client.
issue. Like, like, semantic conventions are a good example of this, right? Like, there's plenty, like, database semantic conventions. You have, like, where do we want to have generic database semantic conventions versus SQL semantic conventions, versus Postgres semantic conventions. And there's a lot of nuance in figuring out how to do that. And clients, surprise, surprise, have quite a number of those things where they're similar in many ways, but the browser, for example, is pretty different from… from mobile environments in some significant ways. So, how do you figure out where these SIGs should be trying to present data and functionality that's similar to each other versus where are they different enough that that's just an ill-fitting shoe.
And.
Having some people, like, feel like, you know, it's… it's their responsibility to… to sort of help those SIGs sort that out, rather than just a flat structure of the different maintainers kind of collaborating with each other.
feels helpful to me, and what would kind of go hand-in-hand with that would be giving those people agency, right? Where if they do do the work of, like, digging into all of that and figuring those things out.
in the past, you know, we've had, like, these classic things with spec issues, where you sort all of this stuff out, and then you go to a broader community, and it feels like you have to kind of rehash the conversation from scratch. The people who have ultimate deciding authority suddenly shift.
And that can be frustrating sometimes.
So maybe it's just a matter of getting, you know, someone on the TC, but I think it's also just… Seems like a place where where more structure would would be helpful.
And that's, I think, just an example of the project growing in scope, you know, where we have like a big enough set of multiple SIGs all centered around something.
Where, to some degree, if they can cook on their own.
Things would move faster, would feel less frustrating, that kind of a thing.
Josh.
Josh Suereth 00:33:54 I do have some concerns on this, just based on, like, specifically for client-side, some of the discussions we had at Semantic Conventions, it was like, There were discussions where client-side was making decisions but not communicating that impacted semantic conventions.
And so, like, to some extent, I just want to say, like, I… I understand wanting to give people authority to move faster, but, like, you can't decide what Semantic Conventions is doing unless you decide it with the Semantic Convention maintainers. So, like, I… I don't know, to some extent, it, like… if we can find a way to isolate client-side from other ownership, great. But, like, if we're just saying, cool, you guys get to make decisions and do what you want, and the other maintainers have to suck it, that's… that doesn't work, right? And that's my fear here, like, are you doing the latter?
Ted Young 00:34:41 I don't, I don't think we want to do that. I think it's actually, to some degree, if.
if there's more of a coherent structure, I'm wondering if that also enables that group collective, you know, if there's… there's people who feel like they're trying to do that level of coordination, right? Like, figure out what cross-client stuff needs, and then also, how does this relate back to the server side? Like, will all of that function better, versus just kind of letting it all shake out?
Which is kind of what we're doing right now.
I feel like, to some degree, we're getting some of that, because all the SIGs are just sort of independently trying to move on, you know, and when… not, you know, when they should bring something up, you know, to the more general group or not, is… is… Is not something like being actively coordinated.
Josh Suereth 00:35:35 I got you, yeah. I'd be 100% a fan of someone actually coordinating that, making sure that happens, and then I'd also be a fan of, like, with SemConf, we were recommending, like, there's a lot of things where you just don't need that level of coordination yet, you know what I mean? Like, it's better to cook on your own, and that's one of the things we're trying to do with SEMCOV. So, like, I do think the dividing responsibility stuff makes a lot of sense. Just, I don't want it to be the case where it's like, okay, they have carte blanche to come in and define a bunch of requirements that everyone else has to react to.
Because that… that doesn't work in hotel, right? Like, it's better when we understand, okay, this is actually this other team's, I'm gonna work with them on it, as opposed to around them, you know?
Ted Young 00:36:16 It's finding… it's like finding that balance. I think another area that's… that's, again, like, very nascent, so it doesn't necessarily have this level of… of expertise built up would be like Gen. AI is an example, you know, of one I've touched base with. You know, Ludmilla's been doing a lot of work. There's been a more like Tc. Attention on on that group. So it's been, you know, it's been fine. But it's another example of like, you have a whole bunch of different players who are very interested in developing out Like, a big pile of instrumentation and things relating to a domain, That's, like, pretty different from… you know, some of the other domains, and so it's like that same balance, right? Of, like, we need to figure out a way for this group to, like, make a bunch of decisions on their own, but also make sure they're not just totally straying away from from… from what everyone else is doing. I… I think it's just… there just happens to be more TC and GC members directly involved in the GenAI SIG, than are involved in the client-side stuff.
Cool.
Again, no real resolution I'm looking for at this moment in bringing this conversation topic up. I just thought it would be good kind of FYI to bring back to this group while the different client SIGs sort of figure out who amongst them would be available and interested in performing that role.
Tyler 00:37:54 So Ted, I got a question for you. Like you're describing a very top down model, which is kind of like the opposite of what OTEL currently operates under.
So, I'm kind of, like, wondering, like, why isn't like, where are? Why aren't these client maintainers at this meeting and coordinating in this meeting.
Ted Young 00:38:14 Yeah, I think that's a good point, bringing more client maintainers into this call. I feel like maintainers kind of come and go from this call because I could see from a client maintainer perspective, maybe most of what we talk about over here isn't super interesting to them.
But I can bring that back to them.
But to your point about it being more of a top down model, I guess.
I… I don't think it… I don't know how much we want, like, a comp… it's about finding a balance, right? And I see it less about having a set of people who are gonna just make diktats to the different client SIGs about what they're supposed to do.
and more just, like, we're seeing that there's work needed, like, like, if you want to figure out some of these cross-client issues, like, like, that just involves work, right? Like, someone has to actually, like, do some work to surface the information that would help those SIGs make those decisions.
And without… without structure, it's just sort of falling on which maintainer feels like they just want to sort of grab the ball in that moment.
And take a hit in terms of their time and availability.
And it just feels, like, a little too loose, and it would work a little bit better if… you know, we clarified who who who had the time to do that, and and who is gonna gonna try to to take on some of that work.
So I don't know how much it is, like, a coordinating role, you know, versus like someone who's like in charge and and making diktats.
Does that make sense?
like… like, it just feels a little bit too loose over on the client side, like… like we're just letting things kind of shake out, and… and that… I'm starting to worry that… that we might… Be a little too uncoordinated on that side.
So a little bit of structure might, might help everyone understand like, like how to do it. And maybe it is isn't that we need another layer of management or something like that, but it does feel like we need like a bit of structure.
more than just SIGs.
Tyler 00:40:43 Yes.
To be honest, I don't know. I'm not like, I'm not I'm not saying you're wrong, I just don't, like, I don't understand, I think, the problem space, completely.
like, I'm a little confused, because, like, OTEL has always kind of been, like, what you're describing to me. Like, there's always been this problem, where, like, we've had, like, maintainers that will go off and do their own thing, and, like, that's collectively, by and large, I think maintainers in this project have come back to this specification and said, like, this needs to universally be defined for the rest of, like, the group, so that, like, OTEL is, you know, a cohesive project.
And so what I'm hearing from you is that, like, that's not actually happening in the client sync, like, there's no, like, maintainers there that are undertaking this responsibility, as, like, a part of their role?
And, it's like… Maybe not necessarily, like, malicious intent, it's more just, like, they don't know, or maybe they aren't experienced, or maybe they really, like, don't want Is that what you're saying?
Ted Young 00:41:47 I think it's more like, like, as the project grows, we've had, like, a spec.
That allows us to coordinate across a set of implementations, and we had a set of maintainers working together on that spec, and a spec meeting to do that. But that was all almost universally focused on the server side.
Domain?
And now the project's grown so that we have this server-side domain, but we also have GenAI, we also have clients, and one answer is, like, to some degree, we all have to coordinate across all of that stuff.
But to another degree, there's… there's stuff that… that's, like, super relevant to those different client SIGs, but it's, like… like, pretty boring for maybe maintainers who are not working on that to… to, like, sit through a meeting discussing that stuff.
Tyler 00:42:41 I mean, I think that's the problem It's like that, that mentality, right? Like, like, I imagine.
I imagine… It's maybe a little bit of, like, they are at this meeting because sitting through server-side stuff is pretty boring for them.
Right? And, like, if this meeting is supposed to be a specification for the OpenTelemetry space, like.
it's not, if that's the case. Like, it's for server-side OpenTelemetry, which isn't… isn't good. We shouldn't do that, right? Like, personally, like, I don't think that that's good. I think that they should feel welcome here to come talk about cross-cutting concerns on a client-side thing. I think that.
bring issues to the forefront for people that are all considered. Like, I think everyone on the call then becomes more of an expert on client-side issues, and, like, you start to see yeah, you start to see, like, this knowledge gap, so, like, I think we should try to make this meeting, maybe in this space, more welcoming to them, and so that we get that, I think is kind of where I would see that.
Ted Young 00:43:39 I think that's really good feedback. So, maybe this as an action item is, I can go back to the client SIGs, and you know how we've been doing presentations of Kind of report backs from different groups. Maybe one of the upcoming ones should be from the different client maintainers of like sort of what is the state of like client development and open telemetry.
You know, what are their needs? How are things sort of shaking out over there? Maybe that would be a good next step.
Tyler 00:44:08 Yeah, sounds great.
Ted Young 00:44:10 Yeah, and I see Lumila in the comments saying like.
that it's not necessarily… it isn't that this SIG is designed to be a server-sized SIG, it's just more, like, as the project grows, there's stuff we all care about, right? There's needs to be keeping track of what we're all doing, but it's like… The more and more context we have, the harder it becomes to do everything together all at once. So… Not that we should all go our separate ways, I'm just noting, like, we need to… to… to maybe put some active thought into what the right balance is here, rather than just Just let it shake out.
Liudmila Molkova 00:44:50 Yeah, what I mean is goes back to what Tyler said.
Like, we had a discussion about attribute limits. Guess what? Quiet perspective would be the most useful perspective, probably.
And it's unfortunate we don't have people in this call to contribute to this discussion.
Ted Young 00:45:09 That's great feedback.
Okay, that was, I feel like that was useful. I think we can move on.
carlosalberto 00:45:22 Yeah, actually I was going to say that because 10 minutes passed, but it was a great conversation.
We have the last item. I don't know, Alex, you here? I didn't see you. Prob.
Alex Boten 00:45:32 Nice. I am, I am here. Yeah.
carlosalberto 00:45:34 It's good.
Alex Boten 00:45:35 Hello, are you…
carlosalberto 00:45:36 Can you share your screen or I can just share my screen?
Alex Boten 00:45:38 No, you can… you can just share it. I… this was more of a general, like, introduction to this donation exists, if people are interested.
So, a little while ago, I spent some time investigating whether or not it would be possible to wrap a C++ SDK implementation in Python. This was specifically around two kind of performance concerns that some customers came to us with. One was around the memory footprint, which was, you know, kind of one aspect. The other one was around the global interpreter lock. That is always a problem with any of these kind of runtime languages that use a global interpreter lock.
And so this prototype, that I'm proposing to donate here is… like, one aspect of the donation proposal, but what I'm really looking for is whether or not people are interested in moving this kind of project forward, where maybe we have, like, a thin wrapper around a common SDK for different languages. Specifically, this wouldn't be to, like.
replace the existing SDKs, but this would be to give people who are looking for, like, maybe a specific, different… performance profile benefits, an option to do this. And yeah, that's really it. Sorry, it was kind of last minute. I got a message asking if I was interested in presenting this, and so I didn't prepare anything else for it, so…
Ted Young 00:47:23 This is awesome.
Tyler 00:47:24 By the way, the OB team would be super interested in this. It helps us integrate with SDKs a lot easier. Just a heads up.
Michele Mancioppi 00:47:34 And for my side, I… I actually would like to see it.
As many SDKs as possible, based on a… on a common core with effectively mostly language bindings and instrumentations on on… in the language-specific nature. For example, when I look at the state of inconsistency in implementations like declarative configurations. If we had only one of those implementations that matters, we would move so much faster as a project.
carlosalberto 00:48:10 Josh.
Josh Suereth 00:48:13 Yeah, just two things. One is, I know from talking to Aaron Abbott, There's, pushback on native libraries in Python.
So I would actually talk to the Python maintainers. I still think we should… like, I still think having native wrapped is a good thing. The… So, so, this is awesome. For context, I did the same shenanigans, but, with, with a Rust-backed implementation when I was doing the OTLPM map thing, just to see, like, what, what it looks like, and I, I think there's a lot of merit here with what you're doing.
the second concern I have, though, is I know from, like, the C++ ecosystem versus, like, the OpenTelemetry overall, I would pick, between, like, C++ and Rust, which one we think is going to be a healthier ecosystem, or have more maintainers as the backing store, because I honestly think, at this point, we might want to consider our backing on that side, because it's a little bit stronger, in my opinion, the current ecosystem and, like, making things faster and nicer and that sort of thing.
I do think that there's a… This integration with OB and stuff is awesome. There's a whole exploration that we should have here. So if you're like, is there interest, I would be interested in what you do here, what you define as the minimum SDK, how you provide that to other languages, et cetera. I also looked into doing this on Java even, by the way, in terms of how crazy it was.
That one's a bit harder.
to actually make any kind of performance dent, Python is super low-hanging fruit. You can beat the crap out of raw Python with native, because half the Python libraries that are important are native anyway, right? So, Yeah, anyway, I'm a big fan of this. I think it's a good mission. I'm just asking, like, two random questions I have in my head about, like, you know, what you think would be better for, like, OpenTelemetry overall.
Alex Boten 00:50:14 Yeah, I… you know, when you're talking about Rust versus C++, I… I ended up going with C++ here because the early prototype I was doing with library, like, native library usage from Python was… like the the libraries just weren't up to what the C plus plus libraries were up to so like the the python libraries themselves to do the the callback to native code weren't where I expected them to be, but I also only had a very small amount of time to do the the investigation there between the 2.
And… yeah, I mean, I would be open to going one way or the other, I don't really… I'm not tied to one, like, native language or another, or whatever, so… There's a lot of hands up.
Ted Young 00:51:02 Dad.
I'm just curious, you know, we have an API SDK separation in different languages, and this was always brought up as, like, a good example of something you could do with this, but I'm curious if there were any, like, gotchas that you ran into.
Where it didn't turn out to be as clean as you would have expected.
Alex Boten 00:51:24 Yeah, I mean, the big one was the context. This was called out many years ago when this idea was originally brought up, was the… the fact that in… at least in the Python implementation, the context is part of the API package, and so any kind of, sharing of spans or whatever is… It it.
needs to somehow translate, or be done in a way that's kind of like monkey patch, which is the way that I went with this prototype, is I ended up monkey patching the context API directly.
So that I wouldn't have to worry about, like, translating the object from one language to the other.
But otherwise, it was… it was pretty straightforward, I think.
I think the… yeah, I think the separation between the API and the AICK is really what drove this attempt in the first place, was that, you know, in theory, all the instrumentations should only rely on the APIs, and if that's true, then, you know, a lot of this stuff will work out of the box, and in my experiments it did, so that was… that was really good.
Daniel Dyla (Dynatrace) 00:52:30 Yeah, I just wanted to say, like, this is something I've been thinking about for a really long time in JS. I think JS, similar to Python, is another one where it's kind of low-hanging fruit from a performance perspective to re-implement some things in native code.
The main thing keeping me back from it.
Aside from just purely the time that it takes to implement stuff and not having cycles for it was always the browser.
Because, you know, things like this are just a lot harder in the browser, and then we get used in all kinds of weird runtimes and stuff like that, and… this… might be, in JS at least, you know, it's easier to target a single runtime like Node, but now that browser's splitting out, I think we would probably also You know, I might consider looking into something like this.
As well.
You know, in JS it might look like compiling to WebAssembly or something like that. I don't really know, but I just wanted to share my support for this as an idea and that I've been thinking about this for a really long time and I'm happy to see it moving.
Alex Boten 00:53:44 Yeah, as you were describing this, I was immediately thinking about WASM because of… there was… someone, I think Pablo and Evan, who ran a collector in the browser using Wasm, so there's… there's options for… for things… for creative ways to get… To get, like, a common… Common, I think… Yeah.
Daniel Dyla (Dynatrace) 00:54:03 I did some WASM experiments, and actually, I was surprised to find that the performance benefit of my experiments were not as drastic as I had hoped.
The JS runtimes have been optimized all to hell, for browsers, and stuff like that, but all, like, the object translations.
It costs… To translate between the runtime and native.
And those costs ended up being.
more than I initially estimated. It wasn't worse, but it wasn't, like, so much better that I was like, oh god, we gotta drop everything and implement this.
Alex Boten 00:54:46 No.
Yeah.
Daniel Dyla (Dynatrace) 00:54:47 To me, there's another benefit, though, which is that if you have a single implementation.
You fix the bugs once.
And you write the features once, and things like that.
Alex Boten 00:54:59 Yeah, I… I will say that I… I don't know that this would ever… replace native SDKs in all possible scenarios. I can imagine scenarios where, you know, someone might not want to incur the cost of downloading, like, a native extension to to their… I don't know, maybe their lambdas, or some other kind of, like, lightweight runtime environment, where maybe that's not… that's not acceptable, or whatever.
There you go.
Diego 00:55:33 Yeah, right, so… Actually.
That's, Something I was thinking that is almost a continuation of what you just said is that this project, I see lots of potential for really great things.
But at the same time, I feel like, there are… Two goals that, Are… maybe are overlapping here?
And I understand the enthusiasm everybody has regarding these 2 goals, whereas I see it like one. The 1st goal would be to Increase the performance.
for a particular language, which is, I think, what motivated you first to do this with Python.
The other second goal I see that I don't see necessarily dependent, I see actually them as two independent goals.
is to only have one implementation so that we get the benefits of, as it was just mentioned, like fixing box only once.
And and so on, right? I see them as, as different goals. So I just was thinking that Those two goals may not necessarily be… As you just mentioned, Alex.
Satisfied.
By one single implementation, because, One single implementation may be suboptimal for some languages.
I was thinking about the case with Python and entry points, which is something that I haven't yet figured out, or the consequences that it will be.
to have only one implementation here. But I guess the same thing can can happen to other languages. So I just I just wanted to clarify with With us, with everybody in this call, if we can see this project, it's actually, Two different projects that… are not opposed.
We could have both things. We could have one implementation for Python that is performant, and we could also have one universal implementation for other languages, depending on And they could provide different benefits.
I don't think they work against each other. Of course, it's more work to satisfy two goals.
But I think it's it's important to keep that in mind so that we can have a a clear… understanding on what we want to achieve with this this idea.
Alex Boten 00:58:36 Yeah, and I think I agree. I don't think the one implementation would, you know, a bunch of wrappers in different languages necessarily has to be at the same, at the, like.
It doesn't necessarily have to be the exact same project as the one that's, you know, trying to identify, like, a more performant Brute, But, I mean, you know, if we get both at the same time, great, if not, then that's okay, too.
I will say that we're almost at time here, but there was a question, from Josh talking about, can you speak about the Libotel idea? This was a comment from Aaron. I've not spent a lot of time looking at this. Josh, I don't know if you have.
If you have any… any thoughts you wanted to share on this, but…
jmacdonald 00:59:23 Can you hear me?
Alex Boten 00:59:25 Amount. Yep.
jmacdonald 00:59:27 Yeah, so I was just, I liked the idea that if there is a native wrapped SDK that the libotel concept becomes another form of OpenTelemetry instrumentation. If you're running a Rust codebase and you want some Python, you wouldn't want to bring in the C++ SDK, you would want the Rust version of libotel. So it starts to look like a low-level instrumentation point. Like, libotel is how you provide the OpenTelemetry API at the CABI level. That seems appealing to me. I just wanted to make sure that that was out there.
Alex Boten 01:00:05 Yeah, I agree. I think there's, you know, there's many different ways we can, we can go about this and I'm.
also open to whatever people prefer.
And there was a question here from Tigran asking about whether this would be maintained by the Python SIG. I guess this kind of depends on how we want to tackle this. Like, if we decide to go this lib hotel route with a common, like, ABI, then it's possible that it would be a separate SIG.
You know, it's, it's unclear to me there Josh.
Josh Suereth 01:00:36 Yeah, for context, when PHP instrumentation was added, it's also written in C++, the auto instrumentation. So the PHP SIG coordinates with the owners of this, but it's actually a new maintainership that's embedded in the SIG.
And we did get the C++ SIG to help sponsor it, because they are taking a hard dependency on it. So it's kind of like this weird three-way thing, where, like, you as the donator would obviously be a maintainer of this, right? And you need to make sure whatever you do here is, like.
approved with the other maintainers, and you kind of become, like, one of the Python things. That's… that's how we did it for PHP. I'm not saying that that's how that would work here, but, like, I would, if you want to talk to SIG owners and the owners of the C++ auto instrumentation components, you can see how that's working out for them and how they like it, because I think it's a model we've had for how we did this in the past, if it.
Bob Strecansky 01:01:32 I'm here, and yes, I'm happy to help talk through it if anybody has any questions about it.
carlosalberto 01:01:39 Well, it will have to be written offline for next call.
Bob Strecansky 01:01:43 Yeah, yeah.
carlosalberto 01:01:45 Thank you so much. Suddenly we are out of time, as you can see that. Yeah. See you next time. See you around.
