SIG: Go Compile Time Instrumentation SIG
Date: 2026-07-16
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Xabier Martínez 00:03:00 Hello?
Let's wait a couple more minutes.
And if not, we can start.
Azhar Momin 00:03:12 Hello.
Xabier Martínez 00:03:15 Hello, hello.
Let me create a new entry on the meeting notes for today.
I'm going to pingali our rice.
Okay, let's start then. Kemal is going to join some minutes late.
Leave our guys, not sure if… Hi, Minori Jan, are you in?
And… The the 1st point was about the defining next steps for the big one.
However, as it's not Kemal here, maybe you can start with your… Rfc. Presentation.
As Kemal already have context about it.
Kathar, do you want to present it?
Azhar Momin 00:07:06 Oh.
I'm actually joining from my phone, so… I accidentally spilled some water on my laptop, so if you can go ahead, I'd appreciate that.
Xabier Martínez 00:07:21 But, like, I don't have context about it.
Azhar Momin 00:07:27 I think we can go with, or maybe we should wait for the amount then.
Xabier Martínez 00:07:34 Okay, let's wait for Kamal and and discuss the next steps.
Once he joins.
Kemal Akkoyun 00:12:04 Hello.
Azhar Momin 00:12:10 Hello, hello.
Kemal Akkoyun 00:12:10 Are we still here? Okay.
Xabier Martínez 00:12:12 We're here, Kamal. Hello.
Kemal Akkoyun 00:12:14 Sorry about that.
Xabier Martínez 00:12:17 No problem. We're waiting you.
I think Alibaba guys are not joining today.
Kemal Akkoyun 00:12:23 Okay. And then let's start it.
You should have started without me.
Oh.
Okay.
Cool, let's go!
Xabier Martínez 00:12:36 Yeah, there are 2 points today. The 1st one is to talk about next steps.
After this new V1 release, and the other is a new RFC from Nassar.
They are more or less related.
Let's just start with my point. We're waiting you because your puff here, it's quite interesting.
So I was thinking that now that we have a solid core of AutoCIM, and the next big move is to try to okay.
Take out.
all the instrumentation packages that we have. Try to move it to another repository.
It's also related with the RFC, I haven't gone through it.
But I see it's related with the AutoC registry and just consume from there. So maybe we can just define in a new repository those instrumentation packages and AutoC just consume AutoC registry.
So I think that's the big move from my point of view. But I'm not sure if you also have other ideas apart from this like, should we focus mainly on this one or apart from other issues that there could be. But do you have any other big milestone or big move apart from this.
Kemal Akkoyun 00:14:05 I think this is a good one, because this is also… tied to what Azar is working on.
So, we should definitely… create this repo and then like i don't know what to call it maybe just to maybe follow the convention go compile type contrib or something or like instrumentation i don't know the deal like we can decide we can have a poll on slack on what to put it in there but we definitely should move them out Because Azar is also working on an RFC to a registry-based approach, and then we don't need to actually keep them in the same repo, and then we can… Open this country, people, to the outside contributors, any vendors.
like, anyone wants to add something, and we can then assign owners, as the other SIGs and repos does, and then they can maintain that, and then it will be different from the tool maintainers.
versus the instrumentation maintainers could be more democratic, what I'm saying.
And yeah, but also with the registry approach, like.
This will be more flexible, right? Any repo can be registered to the OpenTelemetry registry.
Of course, we need some, like, guardrails against, like, what to accept.
What not to accept.
for the registry, because we need to make sure that there are no malicious intent, right? This will be distributed anyways. So, yeah, I think that's a good, good next step.
And.
And the Azars, like RFC, is another good step.
And I guess what else? Like… you can add, like the registry. Rfc.
is a good step for them. Let's say it's like next steps, right?
Xabier Martínez 00:16:01 Yeah, I just saw yesterday, there was a request like a pull request. Merch related with waiver. Yeah, I pronounced.
I think it's also interesting to maintain our same compatibility with OpenTelemetry, ensuring that But I'm not sure if… All our instrumentation should be aligned, like.
We are, like, the project was just at one… One example from… related with HTTP.
Yeah. So I think it's interesting to make this a standard and force this behavior to all the stakeholders.
Kemal Akkoyun 00:16:50 Weaver is about like enforcing the semantic conventions, right? Checking if everything is right or whatnot. So we should be compatible with the semantic conventions for sure.
Yeah.
Xabier Martínez 00:17:04 But we should force this approach somehow.
Kemal Akkoyun 00:17:08 We should force semantic conventions, for sure, because that's the way to go. Weaver is the best tool right now, so yeah, it should be.
Xabier Martínez 00:17:19 Okay.
And another concern that they have is.
That right now, we don't have too many… instrumentation packages.
So for the end user could not be too attractive right now, like use it. I mean, if they need to implement something, if they are like a big company, for example, and they can put resources, could be. But for a mid, medium, small company, it's hard just to start using it because.
we don't have too much too many instrumentation libraries. I I think there is the Alibaba long suite milestone.
Adding the compatibility of Launch Suite with Hotel C.
But until then, I don't see, like… easy to gain traction for this project. Like.
for an end user, it's really attractive to have lots of libraries. So I have my service and I get all metrics and spans by default.
But right now, they are, like.
really few of them. So, for example, for tracing.
it could be not so beneficial, because the traces in the end, they are going to end. Like, maybe it's not possible to get the full workflow, for example, or all the… Visibility that you expect from this kind of tool.
Kemal Akkoyun 00:18:48 Yeah, integrations are always the game, as you said. This is what we also mentioned in the announcement blog post as well.
And the next stages will be all about adding more instrumentations. There is no question to that. And we will ask our friends from Alibaba to maybe speed up that work.
Right? So that, like, that's, like, they're nearly there, right? We support all of the features that the old long-suit injector have, so, like, it's just changing some… configuration for them, and now that we are V1, like, we should just, like, basically ask them to, Like, speed up that work, right?
So I'm all in with adding more instrumentations, like the registry RFC is also about that, creating the country prepo, which also, if anyone wants to take the lead on creating the country prepo, we can add an action item for that.
I think we need to talk to some.
admins from Open Telemetry, so that, like, Right? Create a country, people. Who wants to take this?
Some admin work.
Azhar Momin 00:20:09 Oh.
I mean, I had a slightly different proposal. Instead of having our own country before.
There is already OpenTelemetry Go contract repo, which contains some instrumentation. So, we can follow the approach similar to DD Trace Go, which has their instrumentations, and they also have an orchestration.yaml file, which is the way for automatically instrumenting the manual instrumentation. And then.
We can try to move our instrumentations to the go-control graph, but first we'll have to at your orchestra, orchestra feature parity for that, because currently we use full code for that, so we'll have to do that for a single YAML file. We are… I think we're missing some features on that. So I think we can focus on that as well.
Kemal Akkoyun 00:21:01 This is what we discuss about this. I'm like, to be honest, I'm okay with that. I want to take more democratized approach, right? Keep the long suite instrumentation in their repo and use the registry. And in the same manner, we can use the GoCon trip as well.
But the question is, we don't maintain the Go contrib repo, right? This is a discussion that we need to take with the Go SDK people. We need to ask them, can we use this repo to add our instrumentation, the modules? This will be a layer of Go code, plus some YAML files, but basically.
If they agree, we can… Maintain, sub-directory, and in that sub-directory, we can provide a lot of instrumentations, right? The default one that we… want to have. But it's a conversation with another city, right? They own that.
I'm okay to, like, start that discussion as well. The only problem is, like, when they meet is Thursday, like, 8pm or my time, whatnot, like, that SIG meeting is really, like, doesn't fit my, to my schedule.
And, like, that's why, like I'm sure, like, any Europeans feel the same, like, it's outside working hours, whatnot, so it's hard to get that discussion, but we can use Slack as well. So, how I see this is, like, Having our own repo is easier.
But using GoControl is ideal, but it's slower. So we can also think about that.
Oh.
like… Start a discussion.
Core SDK Sync.
to put… I'm also taking an action item note to put our instrumentations.
In country people.
Also, in their country, people, they say that, like, they don't want to provide a lot of instrumentations, and they only provide a handful of Promoted ones. Which we will have more… More instrumentation, basically, for compiler administration. But it's like, that's the thing, like, having that discussion.
That doesn't hurt. So depending on the discussion.
Xabier Martínez 00:23:27 Yeah, how I see it is that We should put, and it's more or less what we have read the last time, for long suite Compatibility. And my idea was that once we have it.
try to donate those instrumentations to OpenTelemetry, so we just can migrate it to our own repository.
of OpenTelemetry, and once we have it, and we have our own instrumentation, just try to move it to OconTrig, for example.
So we know it's working, it's stable, and we can just move it to that. But before that, let's try to make the launch with compatibility and try to See if they can donate those instrument… that instrumentation.
Kemal Akkoyun 00:24:15 I'm not sure about that donation. It doesn't necessarily need to be donated, right? The licenses are compatible. And Alibaba is already maintaining that. Maybe we should just leave them where they are, because the registry is basically democratizing that. And then, like… because, like, donation and taking that into OpenTelemetry means a lot of responsibility. Someone needs to maintain those, right? And I don't want to just, like, sign under that, like, okay, we're going to take over all these instrumentations, and we maintain that, right? I think it's a commitment.
If, like, unless, like, as long as Alibaba actually maintained those instrumentations, They should… live in their repos. That's my two cents on that. If they are not maintaining, if something happens in the future and we need those instrumentation for the tool, then license allows, we can just, like, fork or copy and move them to the contrib repo and take the responsibility.
But I don't think we need to just, like, have an OpenTelemetry brand on them from day one.
Xabier Martínez 00:25:23 Yes, but for me, it's a bit strange to tell all the users, hey, you have this OpenTelemetry repo, but if you want to use it.
You need to also use the instrumentation libraries made by Alibaba.
Because if you just use the current OpenTelemetry OTLC instrumentation, it's not going to be enough. So it's a bit strange, that concept, that it's a hard couple right now with Alibaba.
Kemal Akkoyun 00:25:55 Yeah, I'm like, yeah, it's just like definitely.
that's a… that's… that community perspective, but we need to see this… this in action. I never seen that, like, Alibaba, they're already, like, more than okay to contribute this back to… To the upstream. I guess, like, let's take one problem at a time, right? Let's first focus on, like, where to put those.
let's start that discussion, and then, depending on the discussion, we can create the repo, and then we can ask Alibaba, like, what they want to prefer. They're not in the room, so it's, like, hard for us to just, like, make a comment in their name. So, next meeting, we can maybe have a dedicated Discussion item about that, but until that.
Let's have this discussion. Who wants to start this discussion with the other SIG, whether we can use their GoCountry people?
Xabier Martínez 00:26:54 I I can start it no problem, and I can also create the action like the next, the point for the next meeting.
to talk about this also, but we are quite aligned. Let's focus on our long-street compatibility and discuss which are the next moves after that.
Kemal Akkoyun 00:27:13 Okay, sounds cool to me. Thanks for taking care of that. And yeah, I think let's just start from… I don't know the… there, maybe… Slack channel?
Xabier Martínez 00:27:28 Yes, for the discussion, we are going to start the… the scope will be to move Or current, instrumentation that we have. Yes.
Kemal Akkoyun 00:27:41 Yeah, we can say that, like, we can even… we can propose to create an RFC for them, right? We just want a space.
And in that space, we will add Go modules, several Go modules.
And then they will be in the registry, and these will be about, like, instrumentation, and you can say that, like, as a SIG, we're gonna maintain, we can be the code owners in this repo.
And if, like, I think we should be ready for the questions, like, why are you not creating your own repo? Like, we don't want to fragment.
the repos, right? Like, it's more discoverable.
And then, yeah, we can take it away from them. If they say yes, that's amazing. I think that's the best outcome. Yeah, so… Let's have that discussion, and we can maybe ask them if… we can also offer them to meet online.
But we should tell them, like, that their SIG meeting slot doesn't work for us, if they can meet earlier, right?
I'm checking, like, this is Thursday.
And it starts at 7 p.m, so 7 p.m.
Xabier Martínez 00:28:49 No problem. I will start the discussions and.
Try to do a meeting or whatever. I will talk with them and see how we manage this.
Kemal Akkoyun 00:28:57 Okay.
Awesome. If they say, attend today's SIG meeting to discuss, we can push some boundaries. Not today, I can't make it today's Core SIG discussion. I want to really be in the room.
Maybe next week. Next week, it actually starts at 6 PM.
Maybe we can say that, like, okay, I don't know if this is alternating or whatnot. Oh, it's alternating. Awesome. So it's 6 p.m. one week, 7 p.m. the other week. So, yeah, like, we can sit, like, we can meet next week. I can try to be attempt that.
Xabier Martínez 00:29:33 Okay.
So…
Kemal Akkoyun 00:29:34 Awesome.
So, for one, like, other items for the next steps?
As part of LFX, with… Azar, we're going to tackle the registry problem, and then we will add some linters, which is like… Veeva does some of the stuff, but we want to create a linter, a checker, and then a schema for JSON schema, so that tooling, if you're writing these things by hand.
You can use this JSON schema for our rules, and you would have, like, LSP linter support, right? We will invest some, like, tooling around instrumentation for if community, like, develop these, right? So these will be handled as part of the LFX.
So that's also the next steps. We will do a lot of marketing. The announcement post should be merged any minute now. They told me yesterday there is a schedule.
And there was a post like two days ago, yesterday, and maybe they will announce it either today or tomorrow. And then I ask you to spread the word.
whatnot, so… And the last piece is dogfooding. Dogfooding means we are right now, converting all of the Orchestrion, instrumentations and the files to the HLC.
And then, we plan to have a downstream wrapper around Hotel C. We will keep the Orchestrian repo, just for, like, adding our configuration on top, right? This will be a super thin wrapper layer.
And as part of this process.
I expect us to find a lot of weak points, like some, like, bugs, whatnot, like, we will be using this in production, and there will be a lot of fixes for the upcoming, quarter.
So, those are the next steps, and probably… This could be same for Alibaba, when they are converting the long suit instrumentation. So, yeah.
Yeah.
Xabier Martínez 00:31:55 I'm just… LFX, project.
I see it okay with the implementation, but I think that the design and approval of the design should be out of it, because it's like the… biggest milestone that we have. So we all should work on having that.
Which one?
In the LFX project.
Kemal Akkoyun 00:32:20 Mmh.
Xabier Martínez 00:32:20 I've mentioned about the registry and all that. I think that the implementation is okay, but the design.
Kemal Akkoyun 00:32:27 Design is in the RFC and that's the next topic. But Azar is working on an RFC and RFC is open for comments right now.
So yeah, I'm jumping ahead for Azar, but like that was the idea. That's why we focused on creating the RFC. So all of the maintainers can align on the design, what to do, what not to do. And then when we have the agreement, we will start working on it.
Xabier Martínez 00:32:58 Yes, let's create an ADR in the end, with all these, and that's all, like, that's like the input for the LFX project, for example.
Kemal Akkoyun 00:33:10 Yeah, yeah. Like, NFX is just, like, this IT Azar is a, like, a maintainer now.
So he's just like it's this three months. He's the LFX mentee. But he's a he's doing a great job, for everyone. So the RFC, we will align on the RFC. We can convert that to the ADR and do the implementation. But like, yes, RFC is open.
Check it out.
We should also, like, announce that on the Slack, and ask for, like, comments, but let's put a deadline to that, because, like, we start We're working on it immediately, so maybe, like, sometime next week, we can put a, like, a review deadline until they, yeah, we collect all the comments.
Xabier Martínez 00:33:57 Great.
Totally aligned with that. Just a quick.
point before the Rfc. And discussion or presentation regarding the Lfx project.
a… Oh yeah, I wasn't checking there.
Kemal Akkoyun 00:34:16 No worries.
Xabier Martínez 00:34:17 Regarding the LFX project, I was thinking on the other proposals also about Making instrumentation more configurable.
Kemal Akkoyun 00:34:29 Mmhm.
Xabier Martínez 00:34:30 And, messaging, SENCOMF, standardization.
So, should we define before publishing the LFX proposals, like, agree on which are going to be the proposals for this project, because they are like different ideas.
And should we do all of them or not? How we are going to tackle this?
Kemal Akkoyun 00:34:57 So… I participated several of Lfx projects at this point.
what we did with the last one, we created an umbrella issue, because there were a lot of ambiguity, right? So, we can start with that. We can create an issue, and dump the ideas in there, but then We can align, on, like, how are we going to describe the project?
before we submit the issue.
But I think, like, regardless of what SIG wants.
This is a time sink for the mentors, so mentors should decide. So in this case, that's you.
So, whatever you would like to work on, right? This is because this is your time, your passion, and, like, you will be having a mentee to work on that as well. So, like, that should be something that definitely you would like to work on.
Xabier Martínez 00:35:57 Okay, great. I will create an issue just to open the discussion and have it documented.
And after that, if we all are okay with that, I will create the proposal.
Okay, yeah, that's great for the issue.
Kemal Akkoyun 00:36:15 Now, as far as I understand, we have three mentors, right? You, Azar, and maybe… A hobby?
Xabier Martínez 00:36:24 I like it.
Kemal Akkoyun 00:36:26 Yeah, so… If it's the case, we can actually have two projects and two mentors each, and one can participate in both of them.
Xabier Martínez 00:36:38 Mmh.
Kemal Akkoyun 00:36:39 So that's also okay. Like we can have two projects. That's it depends on like.
Yeah, the application of the mentees, right? If the CNCF accepts to have like two projects from us, because we are part of OpenTelemetry, we are coming from the SIG, even though we are a big project, I'm sure there is a budget for each project.
So, I don't know about that detail. We can propose, for sure, and depending on what is accepted.
It's a move.
Xabier Martínez 00:37:14 Okay.
Sounds good to me.
Should we move with the RFC?
Kemal Akkoyun 00:37:20 Yeah?
Bye.
Azar, do you want to say a couple of words on this?
Azhar Momin 00:37:27 And, I will be happy if you can start with it. I don't know.
Kemal Akkoyun 00:37:40 Yeah, I think, why can't I suggest now?
For me, that's.
Xabier Martínez 00:37:50 Put there a deadline if you want.
Kemal Akkoyun 00:37:52 Yeah, I want to put that, but I can't edit now.
Xabier Martínez 00:37:55 Oh.
Kemal Akkoyun 00:37:56 I think some views suggesting us.
I'll have to go ahead and do it. Okay. So, Lazar, do you want to go through it? Or, like, shall I do it? Like, how do you want to do this? Just go ahead and, like, maybe give a summary of the RFC.
Azhar Momin 00:38:15 So, this RFC would, allow OTLC to… so right now, OTLC has a embedded set of rules, which it can use to instrument applications, and all the instrumentations live inside a single repository.
we currently cannot have multiple repositories or third-party repositories that can be automatically picked up by OTLC, that would allow OTLC to instrument the applications, or If there, if we want to add new instrumentations, we have to release a new version of OTLC. We cannot do it, like, if, we can, add instrumentations, and at the same time, an older version of OTLC can pick it up automatically. Right now, we have to, publish a new release for that, so… our solution to this problem is to use OpenTelemetry Registry, which already contains the instrumentations, the metadata regarding the instrumentations, and we can add a small Additional amount of metadata, which authors can then use, and… authors, we can automatically pick new instrumentations directly from the OpenTelemetry registry.
Oops.
Switchboard summary.
Kemal Akkoyun 00:39:38 Do you have any questions?
Xabier Martínez 00:39:42 This will be like by default, no? You can import manually defining the path of the instrumentation package.
Or just say, I want… All the instrumentation from the OTLC.
At all.
Kemal Akkoyun 00:39:58 This is…
Xabier Martínez 00:39:59 Excellent.
Kemal Akkoyun 00:40:00 This will happen in the pinning process. So there is like two ways to pin. One is auto pin, which you just like say auto C build.
And then, like, from the registry, we will try to, like, we will resolve all the dependencies that you have, and from the dependencies, we will find the matching instrumentation.
There is a priority resolution, which means, like, it's already documented in here, which means, like, here, like, we will… check which instrumentation comes before, like, basically whatever comes from OTLC will be prioritized, and then the third-party ones, whatnot.
If you want to have more control, this is auto pinning, right? And we will resolve that, we will inject that, you will have that. But if you want to have more control, there is the manual pinning flow. And you say hotel pin C, then you will have the option to check these are the candidates, we will parse your dependencies from your dependencies, these are the instrumentations that you find in the registry, which one do you want?
pick. You will pick them, and we will create the hotelc.tool.go file for you, and you need to check that out, and next time you run the hotelc, we will respect your preferences. So that's the second way to do this.
And the third one is, like, you can always overwrite this file, right?
It could be a web link.
It could be a local JSON, right? And this is the same idea with the GoMod proxy.
With the comma separated, you can have, like, multiple of them, and we will discover, depending on that, the configuring, like, this environment variable.
Xabier Martínez 00:41:55 Oh.
Kemal Akkoyun 00:41:55 And again, all of these instrumentation is going to be a Go module. That's the critical bit. And we will mostly rely on Go module proxies, security things, and Go versioning, Go module versioning, resolution, whatnot.
In the end, they're just, like, call emo.
Xabier Martínez 00:42:20 I see it. Okay, at first sight, I need to review it. Indeed, but it sounds good in the end. It's a way just to populate the file automatically with the registry instrumentation.
Kemal Akkoyun 00:42:34 Yeah, it's just an index to tell OTel-C where to look for these instrumentations instead of embedding to the binary, having a huge binary. And also, I think the most critical bit is not about the binary size and whatnot, but we don't want to… keep releasing a new version of the tool whenever instrumentation change, right? You don't want to do that. So, if you want to add any instrumentation, if it's already compatible with the Hotel C, and then it will just, like, you will just create that module, and put it somewhere, and put that in the registry, and that's it. And you can update or upgrade the, Registry is independent.
of, hotel C.
I think the biggest problem we could have, And probably evil.
Discovered this along the way is.
Probably the minimum required go version.
Between these modules, because we, like, if we keep upgrading Hotel C, And use new features, let's say, and then the modules can be outdated or whatnot. But we'll see. Maybe it won't happen.
But it's, like, because now Autelsey will be an external tool, right? It's not going to inject itself, and maybe it will just, like, work.
Depending on how we arrange the dependencies. That's why this contraprepo is important because there shouldn't be a direct hard dependency between hotel C or any of the instrumentations, between tool and any of the instrumentations.
Xabier Martínez 00:44:27 So this opened the doors to take out the instrumentation for Note LC.
Kemal Akkoyun 00:44:32 Yes.
Xabier Martínez 00:44:33 Mmh.
Kemal Akkoyun 00:44:33 That's the idea.
Xabier Martínez 00:44:37 Sounds good. What else, for example, the long suite instrumentation, is it going to be added to the OTLC register, to the Open Telemetry Registry?
Kemal Akkoyun 00:44:48 Yeah, this is what we agreed in couple of… Weeks ago, if nothing changes, you can just go to register it, like, you just gonna open it.
PR and like basically show where the all long suit like instrumentation lives, right? This is basically these entries, right? Instead of this repo is like our repo, instead of this will be Alibaba long suit repo and the dependency again will be the gene whatnot.
And, yeah. And, like, your earlier question, with this, if we decide, okay, long-shoot instrumentations in the registry, but now we want to have Something else for Jim.
And we, if we put that in the goal country, depending on our priority resolution, which will favor the official instrumentation anyways, we will propose, like, the official one instead of, like, the long suit one. For example, there is already a Gojin one in our repo, right? This will be prioritized over what came from the long suit.
Xabier Martínez 00:45:55 Yeah, that's great. I was thinking about that problem, but it's already solved in the RFC.
Kemal Akkoyun 00:46:01 Check that in detail. Sorry, Azar, I just talked a lot about your RFC. Now I feel bad about it.
Azhar Momin 00:46:10 No, I really appreciate that.
Kemal Akkoyun 00:46:14 This is all created by Azar, by the way. So I'm just talking about it. I really like the diagrams. It makes it really clear.
what they expect.
Xabier Martínez 00:46:28 No more comments from my side. I will go through it.
Kemal Akkoyun 00:46:32 There are some open questions.
feel free to propose some solutions. One of the tips is, like, what happens if the registry.opentelemetry.io is not reachable? We are thinking to embed a JSON file, by the time we cut the release from the registry.io.
Right? That was my proposal, and it's just kind of a snapshot. If it's not, like, reachable, we will warn them, like, we are not using the latest version of the registry.
But do something from them, but… This could help, yeah.
And the custom registry is also, like, the local agency, internal registry, so if the user wants to have their own instrumentation in their private repos.
It is just, like, it's, like, giving hotel.register.json locally, and then, maybe setting the goal proxy, because I assume that, like, if you provide private instrumentation, they will be living in the private repo anyways, so private Go proxy with private local C registry JSON, you can have your own Private, instrumentations. And what else? He will just, like, support those.
Xabier Martínez 00:47:55 Yeah, I think.
One of the main problems would be to.
Also divide all these, like, it's a huge task, so dividing on… On smaller tasks, because they are, like, nice to have features also.
Problem, so we need to, like.
Define the roadmap for achieving all this.
Kemal Akkoyun 00:48:18 For this, My team implementation shouldn't take that much. To be honest.
Like, even with all these, like, the details.
maybe I'm familiar with the RFC, and that's why I'm thinking like that, but, like, have a look, have a look at this.
Xabier Martínez 00:48:34 Oh, wait, wait, I will also return.
Kemal Akkoyun 00:48:36 Yeah, this is, this is like, considering Azar's, like.
historical performance, it shouldn't take more than two weeks to implement this and, like, merge it to the OTLC.
Of course, we will have, like.
it won't be in a huge single PR, maybe. We will have, like, iterations on the… and several PRs to make it, like, easier to review.
But it shouldn't take that much, to be honest.
As far as I know, correct me, Azar, we already also handled the registry part. So the JSON file is already there. We propose some improvements on the JSON file, like version whatnot. It will be a PR, for example, to the upstream registry, OpenTelemetry.
And then the rest is all in OTLC.
Xabier Martínez 00:49:28 You commented before about the LFX project.
I thought it was going to be to implement this, or…
Kemal Akkoyun 00:49:38 This is the part of the LFX now.
Xabier Martínez 00:49:42 But for the current one, not the.
Kemal Akkoyun 00:49:44 For the current one. No, no, this is not good. This is Azar's work.
Xabier Martínez 00:49:48 Okay, okay.
Kemal Akkoyun 00:49:49 We just crossed the halfway point, or next week is the halfway point of our LFX, and we still have six weeks to go.
at least 6 weeks. Right, Azar?
Azhar Momin 00:50:03 I think yes.
Kemal Akkoyun 00:50:05 So we have plenty of time to implement this.
Przemek Delewski 00:50:11 Hi, guys. One silly question. What is Lfx.
Kemal Akkoyun 00:50:16 Okay, yes. Hey, welcome back, by the way.
So, LFX… Okay, what is wrong with my keyboard? I think it's a keyboard problem now. So… Github… yeah… and effects.
So… LFX is a mentorship program from CNCF.
The projects as part of CNCF, they can offer mentors and mentorship.
And then the mentees apply. There's a whole process and a website. There are a lot of criterias. And then you create this.
Where is it?
Programs. And in these programs, like there are like LFX, AltReachy and Summer of Code, but we are mostly focused on LFX. Where are the programs? Each. Okay.
Przemek Delewski 00:51:19 Okay.
Kemal Akkoyun 00:51:20 Yeah.
Przemek Delewski 00:51:21 Understand. So this is mentoring program. I was thinking that it is just some kind of project.
Kemal Akkoyun 00:51:28 No, no. Yeah, we refer to the LFX project. I understand now, as part of mentorship program, we have some projects. Azhar in the meeting, he's our mentee, selected mentee. We started working together at the beginning of June or like 8th of June or something.
And it will be over the summer. This is, to Q… 3 term, and we are also thinking, To apply for another term, which is the next… next quarter.
Przemek Delewski 00:52:00 Okay, thank you.
Kemal Akkoyun 00:52:02 Our community grows when you are out of things. Because of the LFX mentorship, we have a lot of contributors, which that's why we really appreciate this program now. So we want to have more.
Yeah, more of these, basically.
Okay.
Any more questions?
I think, Azar, we should add a deadline here. Can I add it now? Okay.
Third line… And we should also have a table of approvers here, right?
We can add a table.
And… Basically, I would say, like, maintainer handles, and the timestamp.
Or, like, status, like, approved or not.
So, we can approve… Alright.
You can have a table like that.
And then, like, we can sign, and if we have enough approvals on the Rfc. We can move on to the implementation phase.
Azhar Momin 00:53:29 Yes.
I think one of the biggest, questions right now is, regarding the security. Like, how do we verify the… file came from the official. I have left an open question at the bottom, so I would appreciate any help from anyone, because I am not, much involved with the security, so I don't know much about it.
I don't think so.
Single signature would be enough for it, or should we have some other complex mechanism for the security of it?
Kemal Akkoyun 00:54:02 Yes, that's the open question. I think that bit needs some research, but I think we need a signing mechanism. That's the easiest way to do.
The register like the open telemetry registry. I/O, whenever we generate that file, we should Sign it with the same shared key in the registry, and we should also, like, validate this In the runtime, like, in the build time with OTLC, If this is signed by… The known source.
But this should also, like, this should only be valid for the default registry, right? The public one.
Because we cannot just, like, share the same facilities for the custom ones, whatnot.
Azhar Momin 00:54:55 Thank you.
Kemal Akkoyun 00:54:56 That's my… Uneducated.
Proposal. I'm not a… cryptography expert. So this requires some like research.
Xabier Martínez 00:55:14 Let's just review it while going through the Rfc.
Yeah, yeah. To the next point.
Kemal Akkoyun 00:55:20 Yeah, also, like, if we go down to, like, the shared secret key approach, we need to do some, like, admin work to discover, like, is there a… secret store available for OpenTelemetry, right? Which one are we going to use? Is there, like, a VAN password type of thing, or, like, I don't know, vault, whatnot? Like, what is available as a secret store? Because this will be shared in between two repos.
Probably it will be stored in the GitHub.
CI secrets, but, like, whenever we would like to change, there needs to be a source of truth. Or we can use Git signing, whatnot. This is also, like, Git encrypt, where you use, like, the maintainers use their public PGP keys to put some secrets, this is also a way. But anyway, it's like… This could be… yeah, that, like… I think we should add a whole security section, to be honest, to… The RFC?
Here, and… we should discuss these something. We need to propose something here.
It's not a thing that we should take lightly, all that I'm saying.
Because, like, this is… we need to be responsible, like, if people just use this tool in their, like, CI pipelines, and their Docker files, whatnot, we are manipulating code, and if someone tempers the registry and decides to just, like, add some malicious Go modules to inject the code, we are, like, allowing them. So the security aspect is, like, super critical, especially for the public one.
But if they want to use their custom registry, we should… we cannot Yeah, we shouldn't sweat about it, right?
But, or, like, as an additional step, we can also make this parametric, you can define, okay, this is my, like.
signing key, whatnot, for my custom registry, then we can respect that. Anyways, like, it depends a lot on the implementation, and I think this is the weakest point of the RFC, and we need to add a section for that.
While the other maintainers review this, maybe, Azar, you can work on the security aspect.
Cool.
Any more topics?
Yeah, like… Again?
Announcement blog post is ready.
If you wanna.
Have another look at this. This is your last chance.
Because it's going to be out very soon.
You can comment.
Where is it?
Is it merged?
Oh, here we go.
I'm putting you here. And after that, this is merch, please spread the word.
Right.
Do some noise in your social media accounts, whatnot, about the announcement blog post.
Yes, I think Azar and… Xavier, you already reviewed that. Yeah.
Severin also reviewed that.
So… When we get an approval from the docs approver or maintainers, they will also merge that.
Then we can… They're officially out. They are already official.
But still, like, I don't think nobody's, like, discovers.
Discovered our tool, and also, like, as… been discussed here. We need more instrumentations to make this like more usable from the get go, and we should focus on adding them like Yeah, I think the fastest way is the long-field ones converted to the OTLC-compatible way and added to the registry. That's the fastest way, and we implement the registry as the Azars way, and then… It'd be good to go.
If you don't know, we made a mistake of not including a PR for V1, and we have… we have a wall of shame here, so we need to retract the V1 release, and we have V1.0.1.
I think, yeah.
Azhar Momin 01:00:08 Okay.
Xabier Martínez 01:00:12 These things happen, no problem.
Kemal Akkoyun 01:00:14 No problem at all. It's not about the blame, but it was so funny because I was kind of half expecting something like this to happen. And I was okay. Like this went smoothly and then boom, oh, we forgot something.
Xabier Martínez 01:00:27 It was the most…
Kemal Akkoyun 01:00:28 Yes.
So… But it's like, it should work, with the latest tech, whatnot. Like, we retracted in the GoMod file. The GoMod just has the system, so with GoInstall or GoBuild, like, GoGet, if you wanna, pull V1, it won't be, available in the goal proxy. It will say, like, I use V1.1.
But it should only happen if someone is, like, deliberately at the 1.000, like, if they want to, like, deliberately pull that version. Otherwise, like, any automation going to be the latest release.
It's not… Congrats, everyone. Like, we should celebrate. Maybe we should have started with that, right? This is, like, nearly two years of work in this thing that, like.
Right? When did we started?
Przemek Delewski 01:01:27 Yeah, it's about two years, I think.
Kemal Akkoyun 01:01:29 Yeah, like January 2025. Not exactly two years, but one and a half years, let's say.
Przemek Delewski 01:01:38 Yeah, yeah.
Kemal Akkoyun 01:01:38 I think the discussion started, like, two years ago, but, like, the repo, whatnot, it's, like, one and a half years, so… It's a long way.
Xabier Martínez 01:01:49 Yes, and it's getting traction.
During the last month, so that's good.
Kemal Akkoyun 01:01:54 Yes, we are doing a lot of work. I think this is the pressure of V1, and I hope this will continue as is. But I think it will continue. I mean, we're going to use this on production. We're going to talk about it. I hope we will have a lot of contributors, whatnot.
We are planning blog posts, to compare this tool with the manual instrumentation, or VIE BPF-based instrumentation, and this… We will be giving talks. I will be talking about this in GopherCon UK. We already submitted for KubeCon NA.
Or did we? Yeah, we did submit something, I think. We will also submit another one. There is also, like, this GoLab conference in Italy in November. I also have a talk, and I will be talking about OPLC, so… They are spreading the word. Do the same. Let's see.
Xabier Martínez 01:02:54 Great.
Also, we are running out of time, just comment that next week, Regarding long suit, maybe we can talk about that, deadlines expectation now that it's happening with us.
So just to make that word that it would be good to talk about this next next week and see.
which is the expectations here, and you have some kind of deadline. Not… not necessary to talk right now, as we are running out of time, but just to comment that it will be… it will be interesting.
Kemal Akkoyun 01:03:35 Yes.
I'm putting in some action items I'm maybe putting here next.
Yes.
But if you, if you already have an idea, Haben, like, feel free to comment.
Haibin Zhang 01:03:50 I have no comment. I… last week, the, cohesion were… To, next week, I will have a, PR, and, to this.
Kemal Akkoyun 01:04:07 Okay.
Okay.
Okay.
All right, that's it. I guess we can stop sharing and call the meeting.
Any last-minute talks?
Xabier Martínez 01:04:28 No, thank you all for the contributions and congrats with the this new milestone.
Kemal Akkoyun 01:04:35 Yes, same. Thanks everyone for making this happen. This was great.
Xabier Martínez 01:04:42 Thank you, guys.
Kemal Akkoyun 01:04:44 Yeah, bye.
Przemek Delewski 01:04:45 Bye.
Azhar Momin 01:04:46 Bye bye.
Haibin Zhang 01:04:47 Bye.
Azhar Momin 01:04:48 Goodbye.
