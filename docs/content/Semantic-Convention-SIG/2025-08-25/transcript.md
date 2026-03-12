SIG: Semantic Convention SIG
Date: 2025-08-25
Duration: 71 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:06:42 Hello! Hi, everyone.
Christophe Kamphaus 00:06:48 Hello?
Liudmila Molkova 00:07:02 Okay, let's give people 3 more minutes to join, and in the meantime, let me prepare… to present.
You know what, it seems I cannot share. My computer is not set up.
Where….
Trask Stalnaker 00:07:44 I can….
Liudmila Molkova 00:07:44 Sure. I can share. Yeah, thank you.
Trask Stalnaker 00:07:47 Yeah.
No problem.
Liudmila Molkova 00:07:55 I'm converting from Windows to Mac. I hate it so far, I'm sorry.
Trask Stalnaker 00:08:02 It's hard to change. Changes are hard.
Liudmila Molkova 00:08:05 Yeah.
Trask Stalnaker 00:08:52 We could start… Peeking at the triage board… … So, needs all approvals means it has already got the… SIG approval… and in this case, I think it already does have enough approvals if you want.
Did you want more?
Eyes on.
Liudmila Molkova 00:09:25 Yeah, I wanted somebody in the SIG to take more eyes on this, because it was, … it was an old one, and we've done some changes, so maybe if you could move it to a waiting, … Singapore….
Trask Stalnaker 00:09:40 Yeah.
Liudmila Molkova 00:09:41 Yeah.
Trask Stalnaker 00:09:41 Sure.
Liudmila Molkova 00:09:43 Thank you.
Trask Stalnaker 00:09:49 And… If Sam shows up, possibly we could… oh, looks like I hadn't seen that… … You and Sam, I saw we were having a lot of discussions….
Liudmila Molkova 00:10:07 I think our discussion is no longer about this particular PR content, but if someone's here, I would love to have, 5 minutes spent on it.
Okay, I'll add it to the agenda.
Trask Stalnaker 00:10:26 Okay.
Oh, yes, I see.
Quick scan through… I don't know how to tell if anything is blocked… Short of recently….
Liudmila Molkova 00:10:53 I have just blocked deployment type and deployment target.
Trask Stalnaker 00:10:57 Okay.
Liudmila Molkova 00:11:04 So my reasoning is it adds a significant … I feel it's a significant area on how to represent, different properties of the deployment.
And we don't have experts working on this.
like, defining something like deployment target entity, is a big enough change, and I think it should be at least researched and investigated and discussed with Kubernetes SIG and, CICD pipeline SIG, because it's relevant to both of them, but I think we need some group of subject matter experts who would actually, our experts who become experts by doing the research, that could, create a holistic view on how to improve the deployment, and lead it maybe to stability. Currently, it seems we're doing one of things that are not aligned with the existing deployment tools.
Josh Suereth 00:12:07 I absolutely agree with this, Ludmila, and I also wanted to add, there is that semantic tag proposal, where there's, like, 3 pieces to it. One of them is deployment, where they want deployment stable.
So, I think forming a group that will stabilize deployment is absolutely things… something we should do, and there's interest, so I don't think we should rush this or throw things in right now. I think we should actually think deep and hard, and get a group of experts who will say, like, here's how it's used, and here's what we need to do.
Christophe Kamphaus 00:12:39 actually in the CICD Phase 2.
We have listed, deployment context.
As part of it.
Liudmila Molkova 00:12:50 Oh, nice!
Josh Suereth 00:12:53 Then I say we wait for CICD, alright?
Liudmila Molkova 00:13:02 I'll update my comment and include the link to the CICD scope. Thank you, Chris.
Trask Stalnaker 00:13:10 So it looks like they may be just added in order here, so these are the most recent, … We can go back. I saw the discussions, … about WASM, … So this one… Oh, okay, so this one has approvals and a block, let's see… tricks….
Liudmila Molkova 00:13:50 I believe my feedback was addressed, but they didn't have a chance to take a look at it.
Trask Stalnaker 00:13:56 Okay.
No problem.
This is an interesting… Topic… … Bye.
Tend to agree that… We should wait till we decide on this.
And then there's no need to, like, Obsolete it, and then… Bring it back.
Liudmila Molkova 00:14:38 Should we add this to the agenda?
Trask Stalnaker 00:14:42 Yeah, let's.
Liudmila Molkova 00:14:44 Yeah, I like it.
Trask Stalnaker 00:14:46 Okay, thanks.
GenAI… I assume this just means blocked within the GenAI SIG group.
Liudmila Molkova 00:15:02 Yes.
Trask Stalnaker 00:15:20 … This one showed up in blocked, but it is… Not… blocked, unless I'm in the wrong column… no, okay.
So, should we move this….
Christophe Kamphaus 00:15:36 I thought it was in blocked status.
Trask Stalnaker 00:15:41 But I don't think it actually has a block.
Christophe Kamphaus 00:15:48 It was a discussion on the info metrics that made it blocked.
I created the separate PR to, just move on forward with the… Canary guidance on per… Per pipeline run metrics.
Trask Stalnaker 00:16:06 Okay, so it's… So this PR is blocked on this PR?
Christophe Kamphaus 00:16:14 No.
Trask Stalnaker 00:16:15 But this PR is fine.
Christophe Kamphaus 00:16:17 Yeah, I split that part of the PR off, that is not blocked.
ANSI blocked PR. There, we need the discussion on infometrics.
Trask Stalnaker 00:16:29 Oh, yes, yes, sorry. I, of course, remember that discussion now. Thanks.
I think we're about at… time bot.
Let's just see, since this is potentially interesting things to add to agenda if we are short on agenda.
… Potentially… This could use a brief.
Discussion of briefs.
Liudmila Molkova 00:17:16 I can add it to the agenda.
Trask Stalnaker 00:17:18 Cool.
Alright, let's go on to general topics.
Ludmilla.
Liudmila Molkova 00:17:34 Yeah.
… Give me a sec.
… Oh, Trasky are showing the RPC… struggle, ….
Josh Suereth 00:17:50 I think that's last week, by the way.
Liudmila Molkova 00:17:53 Oh, yeah.
Trask Stalnaker 00:17:54 Oh, did I flip? Oh, jeez, sorry.
Liudmila Molkova 00:17:56 No worries.
Trask Stalnaker 00:17:59 Okay, ….
Liudmila Molkova 00:18:01 Thank you for reminding me, I need to… we need to find the time.
Trask Stalnaker 00:18:05 Okay.
Great.
Liudmila Molkova 00:18:08 Okay, so this is a pull request from Gregor. He, adds some… Means to document declarative configuration and semantic conventions.
I mostly wanted to talk with other folks and see how we… envision it. So, from my point of view, we should have formal ways to say, okay, this attribute is opt-in, now this is the declarative, or not necessarily declarative. The configuration means on how to enable this opt-in attribute.
And things like this. … we don't have this YAML structure yet.
we need it for code generation, for validation, and for other things. But also we… don't have enough precedence, I feel, to start defining this general configuration story.
So… I… I actually don't mind having it, in the free form.
Since that's what we do for environment variables.
But it will… Become too messy too soon.
So… I kind of feel we need to have someone looking into this and having general idea of how configuration should be declared in semantic conventions.
And start… who would start to form patterns and start to propose.
things to… in YAML.
… And I don't want to block this PR.
Josh Suereth 00:20:00 Can I ask a question, Linone? Like, do you think this should be in semantic conventions, or do you think this should be in the configuration?
like, the declarative configuration and stuff that OpenTelectricity's building. Like, where… where does it belong?
Liudmila Molkova 00:20:15 That's a great question. We had a quick chat with Jack about it. Let's imagine it's in the declarative configuration.
Then, when we introduce an opt-in attribute.
I hope we could, at the same time, introduce a declarative configuration property for this.
And then the flow to go to declarative config.
then wait for the release, come back to semantic conventions. It's hard, and it won't work, so we will consistently have some, different sets of configurations defined there.
And here, in semantic conventions. So I think the way it could work is if we owned the instrumentation Section of the declarative config.
It seems Jack is supportive of it, in general.
So this is, the proposal I would have. We are the authority for the instrumentation configuration.
Josh Suereth 00:21:18 Yeah, as long as we're clear. Yeah, that's… that's… I… I'm fine with that direction.
It might make sense, like, does it make sense to ask the configuration SIG to come in here and help us do that?
Or… not.
Trask Stalnaker 00:21:35 So the… they specifically asked us to… declare the configuration options in SEMconv before they add it to their schema.
So they, they still own the schema, so it would still end up in their schema.
But they want us to define, like, have the specification for it.
in some continents.
Josh Suereth 00:22:05 I guess I'm… I understand your concerns with Milla, and I think we should pick a place where this lives, that makes sense, but I'm nervous if, like… What we did for SEMCOM was we… we took the specification and had it carve out a hole that SEMCOM fills, so that SEMCOM can work independently, fully. Because there's the thing that's like, hey, here's all the stuff that goes to SEMCOM.
to what you were just explaining, Trask, I think we need them to carve out a hole.
to say, here's where Semcov owns things, and then Semkov can just run.
Because otherwise, it's just gonna slow every… like, all of Ludmilla's fears would still be realized, right? Like, we'd be defining things first, sure, but then we might still have problems getting into the configuration schema, unless there's some kind of a, here is how SemConv will influence configuration.
If that already exists, that's great.
Let's… let's make use of it. But that… that's my concern.
Trask Stalnaker 00:23:08 Yeah, we can discuss that with, I think the… let me know the… Correct me if this… but my, understanding of our discussion with them was that they would still… they still want to have the configuration options in their schema?
Liudmila Molkova 00:23:33 … I don't think so, but that's… it seems we didn't discuss it enough, so maybe, I can bring it up on the spec… I'm not sure if Jack is back yet. So once Jack is back.
… I'll bring it down the spec call.
Trask Stalnaker 00:23:55 Yeah, I mean, we could bring it in the spec call, even before there's other… folks there.
Liudmila Molkova 00:24:02 ….
Trask Stalnaker 00:24:04 At least to kind of get a, check.
It makes sense not to have… I mean, like, yeah, I'm seeing what you're saying about this… this has kind of been a carve-out for semantic conventions. You would use Weaver to generate your type-safe configuration.
Liudmila Molkova 00:24:31 Or even the instrumentation code, right? So the… the enabled headers, well, in theory, the code could be generated to populate HTTP headers that are enabled.
Trask Stalnaker 00:24:49 Okay.
Yeah, let's… let's pursue that.
Liudmila Molkova 00:24:53 Yeah. I like it.
Josh Suereth 00:24:57 Yeah, I guess to echo the point.
I want to make sure Lydmilla's concerns are answered, and so… If we get a hard,
Trask Stalnaker 00:25:05 If we get a firm interface, I think that leads to the things we want.
And as far as, … exploring YAML structure for this.
I can provide that… I can ask Gregor if that's something he would be, interested in pursuing, because he's been doing it a ton of, declarative config work in the JavaSig. That's kind of where this… this… these are coming from.
… And so, I could ask him to, you know, try to propose some YAML structure and just get that discussion going.
Liudmila Molkova 00:25:42 Oh, wonderful. That would be great, thank you.
Trask Stalnaker 00:25:55 Alright, right on time.
Next topic, Michael.
Ayy.
Oh, I can't hear you.
Michael Safyan (Google) 00:26:12 Oh, sorry about that. Nice seeing you guys. So, I have a small pull request related to this gcp.apphub convention. I wasn't entirely sure whether it was sufficient to just update, like, the .md file, or whether… This also required, enumerating all of the cases in… the .yaml code as well. And if there might be a more elegant way than just copying and pasting and updating, to have app hub underscore destination instead of app hub for all of these.
But basically, the instrumentation code that we have, basically… so the AppHub attributes represent, like, the app that a particular service belongs to. And we have logic that can basically take that, transform the attributes, to represent the destination in cases where we have both edges.
Josh Suereth 00:27:10 So… You know, to add some context to this, I think Michael's running into a fun problem of… these are decoration-type attributes that apply to a span, but don't define the span.
So this wouldn't be a new span type, or a new event type, this would be a set of attributes that describe a signal.
If you're familiar with, like, in Google, we have VPC flow logs, like, so you can actually see events that say, this thing is communicating to that thing, right?
And so, we actually will annotate the AppHub application for you when you export these with this AppHub label.
Of, here's the thing it came from, and here's the thing it's going to.
… These are… so one would be the resource, and one would be a destination, like the… on the span, like a client span, right? They're not… we don't want to define a new span type, because these just augment spans.
what should we do here for these? And then it's actually the exact same set of attributes as we had for one thing, but with, like, a context associated with it. Does this sound familiar with the whole embed discussion that went on for a long time, and we… Wrapped around in circles, right? So, effectively, we actually have a system that does this, and we'd like to provide these labels to folks to consume in the meantime.
And what we've done is we just have underscore destination that we'd like to provide for that context here.
you know, we'd like to advertise this in SEMCOM, and I think there's… there's two pieces here, is like, what… what should we advertise the hotel community? And then secondarily, how does SEMCOMF want to solve that problem?
Trask Stalnaker 00:28:58 So, there's already… just catching up here, there's already App Hub, there's already GCP AppHub.
And what you want to do is add GCP AppHub destination, which would then have all the same attributes under it.
Oh, sorry, I'm.
Josh Suereth 00:29:22 Yeah, the difference is AppHub is attached to an entity.
And make sense as an entity, this application?
But the destination one would be, like, a… Augment of a span, not, like, the sole purpose of the span.
Trask Stalnaker 00:29:38 Right.
And so, are all the… Oops.
Liudmila Molkova 00:29:53 I think we have plenty of attributes like this, like the code attributes, or exception, huh?
Yeah, exception attributes that you can attach to almost anything.
The thing that I don't really understand, why don't we declare any attributes? We're declaring the namespace, and it does not It's not how we do this, can we actually declare them, even if it involves some copy-paste?
Michael Safyan (Google) 00:30:22 Yeah, I can add that to the PR. I just wasn't sure whether it made sense to do that or not.
Liudmila Molkova 00:30:28 It absolutely does. Like, if you declare something in Markdown, there is no means to validate it. If you declare it in YAML, then there are.
Michael Safyan (Google) 00:30:38 Done. Okay, so I'll add that to PR as my next action.
Josh Suereth 00:30:43 So, and to my question, should we be defining a span as well? Like, a new span type for these?
Liudmila Molkova 00:30:54 I think we need to… yeah, go ahead, Trust.
Trask Stalnaker 00:30:57 No, go ahead.
Liudmila Molkova 00:30:59 I think we need to document it somewhere, that there are certain Groups of attributes.
That can be stamped, stamped anywhere.
And I have a proposal in Weaver on how we can do this. Let's talk on Wednesday.
… maybe that's not the perfect proposal, but the problem is real, and I think we don't… we didn't declare special, like, even if it declare a spend, what would it… mean. It wouldn't cover the scenarios we wanted to cover, right?
Josh Suereth 00:31:35 Yep. Yeah, exactly. That was kind of my fear here. So, if I can reinterpret this for Michael, basically define them in YAML, and is it okay if we go with registry only, with no signal for those attributes, since they would be attached to a bunch of signals.
But we don't want to define, like, a specific signal yet, because we don't have one. It attaches to other signals that exist, right? Like, this would attach to an HTTP span, for example.
Liudmila Molkova 00:32:04 Yes, and we can document specifically this somewhere in the GCP convention, saying that this group of attributes can be anywhere.
Trask Stalnaker 00:32:14 Yeah, I think it's.
Josh Suereth 00:32:15 Or if you have a note. Yeah, go ahead.
Trask Stalnaker 00:32:17 Lydmila raised of, like, the code attributes, and we do have, various attributes that… and what we've said before is, like, all attributes are opt-in.
on spans.
It's just, we don't list them, like, if they're not listed there, they're still, like, you can use them. They do have the definitions.
But I like that idea of somehow being able to mark that these intentionally don't have a signal, since we are trying to make sure that things generally Are accompanied by a signal.
Christophe Kamphaus 00:33:10 Lutmila has a proposal you have for WIFA, can you link to it so we can take a look?
Liudmila Molkova 00:33:16 Yeah. Yeah, definitely give me a sec.
Josh Suereth 00:33:21 Also super excited about the proposal. I think this is… the more we find these gaps and close them, the better. So, thank you for working on that.
Liudmila Molkova 00:33:30 I wish it was exciting, it's not… it's boring.
Josh Suereth 00:33:34 Even better, if we can do it quickly.
Trask Stalnaker 00:33:37 This is the embedding.
We're talking about?
Liudmila Molkova 00:33:40 No, the suggestion I have is to have an attribute group that explicitly mentions if it's public.
By default, attributes group are… internal. And if you want to say that this group is visible, is doc… like, you would render a documentation for this group, or you would expose it when you import, like, in the… when you have multiple semantic conventions, and you import.
let's say OpenTelemetry conventions, you can import this group and refer to it somehow.
… I… I'm not super excited about this proposal in this context, but I think it's relevant.
Trask Stalnaker 00:34:28 Alright, let's go to the next… … Topic….
Michael Safyan (Google) 00:34:36 Cheers.
Trask Stalnaker 00:34:37 Peak Client and server spans.
Michael Safyan (Google) 00:34:40 So this one had a lot of discussion on it, with one reviewer, and it might need to be broken down into smaller pieces that are agreeable, but I think there were several, kind of, separate Discussions or topics that are worth discussing here?
So one was basically… basically prescriptive versus descriptive behavior. So this gcp.project underscore ID isn't really aligned with current hotel naming, because it's usually gcp.project.id for hotel naming. But this is unfortunately, like, a control attribute that exists in… like, the current, telemetry endpoint, and it's already been documented on GCP docs and what have you.
So I was wondering if it might be possible to capture in hotel semantic conventions just to create awareness of, like.
for downstream consumers to understand what this is. … There is maybe a possibility of engaging with that group to change what those control attributes are, but, … it was kind of one of these things where, like, the discuss… it's kind of already too late, I think.
And then there are a couple other attributes, … That, that had some conversation, and there was, the question of.
defining spans that kind of merge HTTP and gRPC together. … So, for… for Google's, API system, like.
The implementation and where instrumentation generally goes is in a place where the underlying protocol of gRPC or HTTP isn't necessarily known. There's, like, a very lightweight automatic translation layer that can translate it to either protocol.
And so this defines, spans that basically contain a mix of those attributes. So, for example, having both HTTP status and gRPC status, and there was some debate on that as well.
Josh Suereth 00:36:59 Real quick, some quick context. gcp.project underscore ID is produced by the resource detectors for GCP resources and open telemetry.
That was before we embarked on our semantic conventions journey from, like, 5 frickin' years ago. And it is possible for us to change that to project.id if we need to. We will probably need about 6 months of lead time to fix some of our systems, because they rely on that.
Like, with how we generate it, but it's, it's something we can do.
… Just to call that out. But the important thing of this, this is also a, like, Michael's targeting our client libraries, so, like, the Google Cloud client libraries are provided by Google.
These would be the semantic conventions we want those to abide by, so if you depend on one and it has hotel baked out of the box, this is what you get. And I think there's some interesting questions here. I'm gonna add another complication, Michael, sorry.
We have the cloud attributes, which the entity SIG feels are generally very awkward and somewhat of a failure, because they don't really… provide the thing that we want, and there's a lot of other conflicting things with that, like, the whole availability zone problem, where GCP looks a little bit different than everyone else, and they all break There, the difference between host and VM, and whether the host ID should be, like, a cloud ID, Where you put one versus the other, that kind of stuff. So, I think there's a, … There's a piece here I want to call out, which is we probably need to get together a team to do cloud resource attributes.
Michael is working on GCP conventions, specifically, and I think the general plan we had here was to just define GCP as is, and then if cloud comes into place, we'll figure out how to adapt or make things compatible.
… Just to call that out. So, the project ID thing we could change. I think resource name, server name, service, the fact that, like, our cloud client libraries hide, whether it's HTTP or gRPC, think of this as the layer on the cloud client libraries, right? This is the semantic convention for that.
Trask Stalnaker 00:39:17 would you want that to be, like, I'm thinking, like, a RPC… semantic convention. Would you want that to be encapsulated in RPC semantic conventions, where RPC semantic conventions could be agnostic, or pull in multiple different pieces? Or are you really… preferred.
… Just to target that, … GCP client library itself.
Michael Safyan (Google) 00:39:48 I mean, I suspect it's… probably makes more sense for it to be a GCP-specific thing, only because I think A lot of other systems.
probably don't do this for their multi-protocol. Like, I don't… I mean, if there are other cases where people are, creating a shim layer to accept both gRPC and HTTP, then sure, but I think that's more of a GCP-ism than anything else.
Josh Suereth 00:40:18 I'll call out the attributes that Michael's adding that are new.
are GCP-specific, so if we… if we have an RPC General SunConf.
these would be the GCP-specific things in it, the way, like, the database spans have sometimes database-specific attributes. I think we could go that way, actually, Michael. Like, if… if we look at… depending on how RPC and the discussion goes, and that's defined.
the key set of things that are in here, which are, like, things that look like HTTP clients, things that look like methods and stuff.
we might be able to go with an RPC convention there, but there will be GCP-specific attributes that need to get added. As long as we have that, that actually does seem reasonable, but mostly what Michael's adding here is the GCP-specific parts. So those would still be GCP-specific, of like, you know, we have a thing called a resource name.
Amazon has an arm. Do we want to share? Do we want not to?
we could… we could talk about that, but that's more of, like, a cloud-related problem, not necessarily an RPC-related problem, right? RPC frameworks in general aren't… Necessarily talking to resources the way we think about it, but service and method.
That absolutely is in line with RBC, and should align with, what you're building.
So yeah, the new attributes, I think, might be GCP-specific. The service and method ones I think we could align to the RPC conventions.
Michael Safyan (Google) 00:41:51 Yeah, I mean, I think I'll add here that although we definitely want to reuse the attributes from those conventions, and, like, we want to, like, logically inherit from them, this also does serve the helpful purpose of not only telling consumers what they can expect from GCP services.
But also providing, like, a central document for… the GCB teams that are implementing instrumentation for their server-side spans as well, in addition to the client-side spans, and so being able to tell them, yes, this is the combination of attributes from these different sections that you need to provide, I think.
Is also helpful with having it, like, centralized in this way.
Trask Stalnaker 00:42:30 So, let me show you what we do for that in, like, … database semantic conventions, because I think this is what Josh is kind of talking about… where we have very gen… we have general database semantic conventions, database spans, so potentially this could be, you know, we would have general RPC semantic conventions, but then underneath that.
We have, like, here is the… … which one am I looking for? SQL Server, and so it specifically calls out what it can add more attributes under… for SQL Server, and it can redefine… it can kind of… Add more context.
So that could be the GCP… client library underneath RPC, and you could still have that where it's all in one for… the GCP clients.
Michael Safyan (Google) 00:43:42 That makes sense, although in this pattern, I'm wondering if it makes sense for there to be, like, a GCP entry versus, like, an entry per GCP product in that category. Like… Maybe in RPC it makes sense, but like… under database, for example, I wouldn't expect GCP, I'd expect, like, Cloud SQL or something like that, or AlloyDB, or one of the, ….
Trask Stalnaker 00:44:07 Right, right.
So under RPC, I guess it depends on if you have… if RPC is… consistent, you know, across all the… like, if you can fit it all into one GCP kind of RPC convention, or if you need them broken out by product, that's okay also. But it doesn't have to follow this exact, like, by product. It can be by category.
If that category… categorization is meaningful.
We should probably… Move on any kind of… I don't know.
… Does it… Does that help you with moving forward at all?
I….
Michael Safyan (Google) 00:45:07 Can I just ask, maybe, if some of you could just code review it afterward, and dig into it in more detail, and then you can give me a specific recommendation of whether that alternative structure proposes what you guys want us… want us to move to, or not.
Trask Stalnaker 00:45:24 Yeah, and the RPC question may need to kind of… Wait for, … We're just kicking off… oh, not that, it's a pull request.
RPC semantic convention stability, Proposal.
… So I'm not quite sure how all of that… Would work, timing-wise.
Alright, for sake of time, let's move on, … Oh, yes.
I saw… Oh, what is this?
Some changelog linting issues. Oh, no.
Liudmila Molkova 00:46:10 I think I just, fixed them, … We'll probably need some automation, but the release, we've spent a fair amount of time fixing release workflow. It's me. I broke everything.
But, now it seems to be green, and, … We can finally release.
Trask Stalnaker 00:46:36 Cool.
I will, I will run the rest of the release. Thank you for fixing all of those.
Liudmila Molkova 00:46:45 You fixed the half, and it's been a decent half.
Trask Stalnaker 00:46:48 Teamwork. Teamwork. Yeah, yeah.
Alright, SQL Commenter….
Liudmila Molkova 00:46:55 Yeah, I think Sam is not here, but it might be interesting to… I'm curious on your thoughts, and maybe we should move this discussion to the spec.
So, I think the remaining, discussion is around propagator behavior.
And, … Whether the propagator is limited, to, like.
So, okay, so let me explain the core of the discussion.
… Normally, how we call propagator, let's say over HTTP, we give it a set of headers.
and it… as a carrier, and we expect propagator to actually inject things into the carrier.
… And normally, after a propagator runs.
We don't expect any instrumentation to do anything else.
But, it creates some, weirdness with SQL Commenter.
Because what you wanna do in an efficient manner.
is to… … Have, let's say, a map as a carrier?
But then you would, serialize this map into the SQL command.
And then Propagator does one part of the job, injecting into the map.
And then instrumentation needs to do something extra.
The sterilization part.
… I don't feel particularly strongly, and I don't… I'm not blocking this PR based on this, but they think it's super weird that, we use TextMag Propagator.
And then ask instrumentation to serialize it to string, and it's error-prone.
And it means that instrumentation needs to have a logic, like, okay, if propagator didn't do anything, if the carrier is empty, and … So, it's not what we usually ask instrumentations to do, and I would like us to… Sam and other folks working on this is to maybe figure out some way to… Embed all this logic into the propagator itself.
Josh Suereth 00:49:21 Are you suggesting, like, directly pull from context to make the string?
Liudmila Molkova 00:49:28 Maybe it should be a special SQL injector propagator.
Or some… some form of propagator that can efficiently work by, appending things to a ring.
Josh Suereth 00:49:45 Yeah, for context, we had a binary propagator in W3C and in OpenCensus.
And that literally was a different call. So there was, like, instead of a text map propagator, there was a specific propagator that would generate that format for you in that string.
And that's what we did for, like, the advanced binary thing, where it serialized into bits, and gave you the bits back.
I feel like your intuition's 100% correct here, and this probably deserves to be in the propagation part of the spec.
As a thing, right?
Trask Stalnaker 00:50:24 So I'm trying to think that, like, if you… had a smarter care. Like, if you had a You create your own carrier object.
Right? You could have that carrier contain the, you know, the original string query, and as the setters get called on that carrier, it updates the query Yes, then the instrumentation has to ask to get that object, the query text back from the carrier, and it's not truly the carrier.
In the sense that we think of.
… I don't know how that makes you feel.
Liudmila Molkova 00:51:10 So you still need to, once you're done, right, you need to tell Kira, okay, I'm done.
Trask Stalnaker 00:51:16 You called the getter, and, you know, lazily, it can… construct.
the query text.
Josh Suereth 00:51:23 But why are you using the carrier… sorry, why are you using the text map propagator at that point anyway? Like, why… why aren't you just… again, it… Why aren't you defining what your format string is, and then just directly pulling it from hotel context?
Trask Stalnaker 00:51:43 I didn't quite pull that.
Josh Suereth 00:51:44 warning from Zoom that something crashed, and I don't know what it is.
Trask Stalnaker 00:51:48 Everything seems fine.
Josh Suereth 00:51:50 Okay.
Trask Stalnaker 00:51:50 From our end.
I didn't quite follow the… your comment.
Josh Suereth 00:51:58 Yeah, so the way context propagation works, right, and the way the text map propagator works, we defined a format of key-value pairs.
for… that… that is W3C trace context. And so, text map propagator is if… if you have key-value pairs you write into, you use this thing to write those key-value pairs, and we use it for, like.
Messaging systems, because there's a key-value metadata thing you can throw into, right?
Or, if you need to propagate across something that doesn't have key-value pairs, you just invent a place that has key-value pairs and shove it in there.
This is different, this is… we want a string. So this is not a text map propagator. We're hijacking something designed for one thing and using it for something else, and it's weird, and I agree with Lyudmila, and in the past, when we wanted to do binary serialization of, here's a binary blob.
that is trace context, we defined a specific propagator. We didn't have a need to define one in OpenTelemetry, because everyone has moved to key-value pairs, even in the context where we had binary. Like, gRPC is actually using key-value pairs now.
Right? But I… I fully agree with Lyudmila, like, it… it just makes sense to have a propagator.
That's… that will serialize directly from context to SQL commenter format.
Right? So it takes a no-tel context and dumps a SQL commenter string as a thing that exists. That just… I don't… I don't know why we would… say, cool, invent a map, right? And then serialize W3C context into a map, and then we'll serialize that into a string afterwards. That can be an implementation detail, but from an instrumentation author, or from a user.
That just seems super inconvenient.
Trask Stalnaker 00:53:36 Oh, it is. We've got… I could pull up many examples in Java instrumentation where we do something funky like that.
Where we can't store it directly into the carrier, so we… we do pass in, like, a map, and then… but to your point, those are still generally key-value pairs.
But I could… I mean, you could argue that the SQL commenter, I mean, it's… its key-value pairs is just an encoding of key-value pairs.
Josh Suereth 00:54:10 But you can code key-value pairs within W3C Trace context.
Right? It's… so, like, even in trace parent, and trace state can have, like, key-value pairs within it. So, I'm encoding key-value pairs into trace state, but I'm coding it into two key-value pairs. It's about the carrier being a text map.
But your carrier is a raw string, and so if you were to, like, configure this in OTEL, we could have a string map propagator format that would be, like, the SQL commenter, or sorry, the string propagator format that would be SQL commenter, and we could have a text map one that would be W-2 trace context, right? Cool.
That's the thing, is like, I want to propagate data, and I want to propagate it as a string, I want to propagate it as a text map, I want to propagate it as a binary, and I need to configure something. It just feels like we have the wrong form factor in OTEL.
And I know from experience writing the propagators, back when I did instrumentation, which has been a while, I agree, it's been, like, 2 years since I really, like, did the text map thing in detail.
with all the Scala stuff back in the day. … it's not an easy interface to work with. It's pretty awkward. So I… I think we should be pushing for a string propagator, or something more specific.
four SQL comments are here. If I want to bundle everything into a single string.
And then we can have an instance of it for SQL Commenter that does the SQL Commenter packing and unpacking.
Trask Stalnaker 00:55:41 Yeah, so you're saying basically, I mean, whether it's string or byte or something is, like.
serialize… it's like, serialize it into a thing that then I will take away with me after the fact.
Makes sense.
Also, a lot more efficient than putting it into a map and then serializing it from the map.
Josh Suereth 00:56:07 Well, aren't HashMaps the most efficient data structure in the known.
Trask Stalnaker 00:56:11 Programming world?
All the time.
Josh Suereth 00:56:14 Yeah.
Anyway, yeah, sorry. So… Agree with Ludmila. Is that related to this PR, though? Does that block this PR? Does that change this PR?
Liudmila Molkova 00:56:24 It doesn't block the SPR, and it seems Sam removed the, sentence that implied this behavior. So I think the SPR is… fully unblocked by now. It's… it's still… perhaps I'm… I'm going to create an issue in the spec repo to discuss SQL commenter or string kind of propagator.
Further.
Trask Stalnaker 00:56:56 Cool, I will mark it ready for… to be merged, but I'll give you the last word, Ludmila.
Liudmila Molkova 00:57:04 Yeah, I agree, it's ready to be rushed. There's nothing controversial there anymore.
Trask Stalnaker 00:57:10 Okay, I will hit the button.
Liudmila Molkova 00:57:12 Yay!
Trask Stalnaker 00:57:19 Alright, revivingevent.name.
Liudmila Molkova 00:57:25 Yeah, so, … We used to have event.name attribute, to record event name.
We moved over to the event name top-level property, and for the absolute majority of cases, we don't need event name anymore.
There are two cases where it could still be useful.
First, let's say I'm using something like Log4J, or S-Log, or any login facade that is not up on telemetry API.
And I still want to provide event name.
So the login bridge can take event name from the attributes, and then use it as a top-level property to create proper OpenTelemetry native event.
The second is, let's say I'm exporting or converting OpenTelemetry a log record.
into something not up in telemetry, not on TLP.
then I need somewhere to put the event name.
Well, assume… assuming it has attributes of some sort, the structured metadata, then I would… Reuse event name.
There is a slight controversy here that, outlined by Robert, that, we usually, when we export to non-openTelemetry destinations, we add a prefix otel.
But… staying consistent with, let's say, a hotel scope name or hotel library name.
It doesn't feel like a good justification to have two attributes, one for into OpenTelemetry, and one for going out. So, the proposal is to just bring event name.
And document something for external systems to represent event name and up in telemetry.
Checking everything around your economy. Yeah.
Trask Stalnaker 00:59:36 Yeah, the only, worry that I have is, Kind of this… making it look like we've got two places.
Two officially places to put event name.
The event.name attribute Seems very easily confused for people, users, especially given that it used to be the way that we did things, that they will try to set that into attributes.
on… Loggers.
On our loggers, or just use that instead of the event name property?
That's kind of the only downside that I'm… the only hesitation I have.
Liudmila Molkova 01:00:26 Do you have a solution in mind on how we can minimize it?
Trask Stalnaker 01:00:30 No, I mean, I… I… I do support this overall.
And I think the only solution I have is documentation for that.
It's just the one worry in my head.
Liudmila Molkova 01:00:47 Yeah, that's… that's a good one.
Would you mind leaving a comment? Unless, like, just so your concern is captured?
Trask Stalnaker 01:01:22 Do we have… I mean, I kind of like the… oh, the other thought I had is, I mean, I… oh, I think I put in the comment, … Did I…? Yeah… I sort of like the idea of having attribute names to represent all the built-in fields.
Like, span.name… we've wanted a span.name something before, for, like, stamping onto metrics, for example.
So I… I think that's a good, maybe… Also, reason to do this.
Yeah, Josh.
Josh Suereth 01:02:08 That's actually a good reason to not put the OTel there. If, like, you're saying, hey, event.name is how you convert events into metrics.
Maybe.
Maybe not. But I, I do, I do like… I really like that idea of, like, let's have… Built-in things have… A semantic invention that you can use for when you translate back and forth.
So, I like metric.name, I like event.name.
Span.name, that sort of thing.
Trask Stalnaker 01:02:57 Yeah, I think that… that really sells it for me, Lyudmila, is that it's a… It fits into, sort of, this future vision.
So, yeah, I'd say let's… Ship it.
Liudmila Molkova 01:03:19 Once Robert.
Yeah. Epic, ….
Trask Stalnaker 01:03:23 Oh, he's back this week. Awesome.
I can finish that comment later.
… We've got 2 minutes left. Do you want to talk about this?
Goodmilla?
Liudmila Molkova 01:04:01 I am curious what, is there some angle we should discuss here that we didn't discuss before?
So last time, I think we, … talked about… … The fact that… okay, so we have enums, and in enums we have a value, which is, let's say, idle, all lowercase.
And then… Sometimes, most of the time, actually, enums don't have briefs.
Because they are self-descriptive, and essentially the attribute definition, is sufficient to understand what each individual, you know, member is. Sometimes it's not, and this is where the briefs, notes, and other things are very useful.
But in general, like, if you look into YAML, it has, … it doesn't seem beneficial to repeat the value in the brief in different casing. We could have Done all the markdown, niceness.
using Jinja filters.
And we don't need to… bloat the YAML structure with redundant information.
I left the comment, I blogged the PR, I believe James still thinks it's beneficial for the consistency, but I… I'm not sure.
If the ginja… Would solve his concern.
Trask Stalnaker 01:05:39 Okay. Yeah, that makes sense to me. I mean, at least as a first step, let's try the ginja.
And… Get nicer, improve the markdown, without… increasing the YAML, because, yeah, that… It's nice, I mean, I know it's supposed to be machine-readable, but it's also… humans read it a lot, too, so… There's some consideration there.
Josh Suereth 01:06:05 Also, I have a theory, which is… The less you have, the less the maintenance is.
So, if you ever have the option between verbosity and less.
You should go for less, generally, because you have less mistakes and less issues you have to maintain.
That's not always true, but generally it's true. So this is an example where Right, you know, if we don't think there's a value, let's not add all of that YAML.
Trask Stalnaker 01:06:34 Cool, we have hit our time.
Thank you, everyone.
Liudmila Molkova 01:06:39 Thank you.
Trask Stalnaker 01:06:40 See you in the repo.
