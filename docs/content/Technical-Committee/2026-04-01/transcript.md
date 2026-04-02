SIG: Technical Committee
Date: 2026-04-01
Duration: 65 minutes
Zoom Recording URL: https://zoom.us/rec/share/VX8KeL5S4bIJLdvbmMNiF3H_mOpU-zZk6rWfL9R7ODyn4m00U5mcZasb6KRa9yBf.gYwM3mcTlBTbkxmO
============================================================

## Zoom Recording Transcript

David Ashpole (dashpole) 00:00:39 Hey, Tegan.
Tigran Najaryan 00:00:45 Hello, how are you?
David Ashpole (dashpole) 00:00:48 I'm doing well.
Had a fun morning. We finally released Version 2 of the Open Metrics.
standard.
Tigran Najaryan 00:01:12 It's true.
And Prometheus is implementing that, right?
David Ashpole (dashpole) 00:01:16 Yes.
Tigran Najaryan 00:01:22 But that's also… that's a wire format, right? It describes, like, the metrics on the wire, how they're supposed to work.
David Ashpole (dashpole) 00:01:28 Yep.
Tigran Najaryan 00:01:34 Hey, Army.
David Ashpole (dashpole) 00:01:35 Okay.
jmacdonald 00:03:27 Hello.
David Ashpole (dashpole) 00:03:28 Hey, Josh.
Tigran Najaryan 00:03:30 Hello.
Jack Berg 00:03:38 Hi, everyone.
Sorry I'm late. I'm not in the meeting today, so I'm gonna pull up the notes, and we can get into the triage section.
Right, just because we don't need… Quorum, to get started on this, let's go ahead, starting with the TC inbox.
Nothing in there.
Community inbox.
Nothing in there… Unassigned open spec PRs… And who are we filtering out? We're filtering out… Otups.
authored by TC members, drafts, and, you know, trivial things like updating spec compliance matrix.
There's this one by Bach P.
David, David, David… Robert.
Tigran Najaryan 00:04:51 You can assign the system define to me, if you want.
Jack Berg 00:04:55 Okay.
This is an OTEP, this is a draft.
David, David, David.
OTEP, OTEP, okay, so that's all, because we're into 3 weeks ago at that point, so this is the only other unassigned issue.
Decouple the responsibilities of environment variable propagation. This one's already… has a bunch of approvals, so I suppose, I can take it, but it's not going to require much, I don't think.
David Ashpole (dashpole) 00:05:36 Does this just need the merge button hit?
Jack Berg 00:05:38 Yeah, why don't we just do that?
Let's see, it's got a changelog entry, yep.
And it's 2 weeks old, so there's been plenty of time to comment on this.
And we're done with that part, then.
OTAP backlog.
Does anyone remember which OTEP we looked at last?
David Ashpole (dashpole) 00:06:12 I remember Josh Surith talking a lot, so I think it was one of the entity's ones.
Jack Berg 00:06:18 Telemetry policy…
jmacdonald 00:06:20 Last time we went through these, we ended at the stability requirement, and I went and approved it, and asked Austin to do some more stuff, I think. It was at the bottom of the page last time.
Jack Berg 00:06:29 Stable by default.
jmacdonald 00:06:31 Yeah.
Jack Berg 00:06:32 Right.
Do we… do we need to follow up with that, or should we jump to the next one?
jmacdonald 00:06:40 I mean, I can go look at what he… if he's done anything since, I can try. I'll follow that one.
Jack Berg 00:06:47 Looks like Robert has a bunch of comments.
There's a bunch of additional comments. I don't see any additional commits.
jmacdonald 00:07:03 Okay, yeah, agree. He, yes.
Yeah, further discussion… Oh my god, so much conversation.
Jack Berg 00:07:14 Well, when you tackle a huge scope, that's gonna happen.
jmacdonald 00:07:19 Yeah, there's a lot to read here.
Liudmila Molkova 00:07:21 I believe the conversations are around… How much press… how much solution you should be in the hot tub, or should it be just directional?
Jack Berg 00:07:38 Well… Let's follow up with those comments, and let's go on to this next OTEP. This is the Schema V2.
Dude, Mela?
Liudmila Molkova 00:07:49 Yeah, so for this one, it's pretty much already with the one caveat, it's still… there is an action item on me to do a prototype for maybe Java instrumentation, not for all conventions, but for some of the… a couple of different conventions.
specific to Java, and show end-to-end how to… host them somewhere in the Java instrumentation recall. I would like… I'm working on the prototype, I would, want Trask's approval on this one.
Jack Berg 00:08:22 Trask, I assume, is supportive of this idea overall, correct? Or have you worked with him at all on this?
Liudmila Molkova 00:08:30 He's supportive.
You know, it's needed, but I… we wanted to have some specific prototype to… for him to understand the details.
Jack Berg 00:08:42 Okay.
Do you think it's useful for others to review this, ahead of that prototype, or do you…
Liudmila Molkova 00:08:51 Absolutely, yes.
Jack Berg 00:08:52 Okay.
Liudmila Molkova 00:08:54 One thing we probably will change, and I know Tigran, you're approved, but I wanted to check with you as well.
So, the file format 110 we have today, and we are changing it to 2.0.
Zero.
This… Yeah, this one. Yeah. So… Should we reconsider how we do versioning for the same reasons we do it for SKU, for configuration, and drop the patch?
So we would rather call it file format manifest slash 2.0, because we also have resolved schema Resolved 2.0.
So, it would not be somewhere, but for the, like, the language.
syntax, the somewhere doesn't work. Great.
Tigran Najaryan 00:09:48 I don't think we ever used the patch number as well, right? So we only had 1100 and 110, I think, as far as I remember, those two versions. And I don't think we ever defined what it would mean to have a patch number changing there.
So, I… I don't mind what you're suggesting.
That matches what we… We did assign a meaning to the minor number and to a major number in the schema OTAP. We did not assign any meaning to the patch number, so we may as well say that we get rid of it.
Liudmila Molkova 00:10:21 Yeah.
Jack Berg 00:10:22 That's the reasoning in declarative config, why we got rid of the… patch, because it's only… there's no feature changes that are allowed to happen in a patch version, and so including it in this file, at least in declarative config, that the user has to author, all it does is create the impression of that it's impactful when it… when it has no impact. There is nothing that can… that it can, that it can change.
Tigran Najaryan 00:10:51 Yeah, yeah, I'm fine. Works for me.
Liudmila Molkova 00:10:54 Awesome. Thank you.
Jack Berg 00:11:00 Okay, I'm gonna go take, I have an action item to go review this offline, Lyudmila, so it's good to see an approval from Tigrin and from… from Josh, so, I'll go look at this now.
Liudmila Molkova 00:11:10 Thank you, appreciate it.
Jack Berg 00:11:16 Any other thoughts on this before we move on to the next OTEP?
Okay, we're gonna do this for 4 more minutes, to the 15-minute mark for triage, and then we'll get into the agenda, by the way. So, Is Josh Surreth here?
I don't see it.
jmacdonald 00:11:40 I said he'd be out this week.
Jack Berg 00:11:42 That's right. So the, you know, the next one is a draft, and that's his, so we can ignore that. The next one after that is context-scoped attributes from Carlos. We talked about this in the spec meeting yesterday. Do we want to have any more discussion about this today?
jmacdonald 00:12:00 I'm still reading it.
Jack Berg 00:12:01 Okay.
I think that one, honestly, is not something we need to spend time on from a triaging standpoint. I view this triage exercise as, like, trying to get these things unstuck, and that one is very much… being engaged with actively, so…
Carlos Alberto Cortez 00:12:20 Yeah, that's correct.
Jack Berg 00:12:25 Continuing up the list, we have a new one, Agent Telemetry Semantic Conventions. This is the next OTEP, which is… Not a draft, and that we haven't looked at.
Liudmila Molkova 00:12:41 We, we did, so… Is this… is just misplaced PR. We have pretty much everything that this person suggests, and it should not be in specification. Why would it be?
Jack Berg 00:12:57 So, can we politely close it?
Liudmila Molkova 00:13:00 Yeah.
Do you want me to close it again?
Tigran Najaryan 00:13:03 Is this… is this AI agent, by the way? Not the… not the telemetry agent, right?
so unfortunate that the, I guess, we now have the term agent Azure replied, I guess, by the AI world.
Liudmila Molkova 00:13:19 Yeah, so this is the observability for AI agents.
But I hope it's not the agent who created the PR. It doesn't look like that.
jmacdonald 00:13:27 Yeah, I've started using Collector more often now, just because I can't use Agent the way we used to.
Tigran Najaryan 00:13:32 Yeah, we're stuck with the word agent in no pump, because it's in the protocol name now, so there isn't much we can do there.
Anyway, sorry for the sidebar.
Jack Berg 00:13:45 So, it seems like this author, though, is… aligned with the feedback from this, and so hopefully they're okay with… with closing this and moving this. Did you get that impression, Ludmel?
Liudmila Molkova 00:13:58 Yeah, I think so. I will leave a comment that if there is anything missing, they should go work with us in semantic conventions.
Jack Berg 00:14:05 Okay, great.
That somehow, incredibly, takes us to the end of the OTEPs. We have worked through all of them, so I guess we're down to the bottom again next time. With that, let's move into the agenda for today.
So, Riley, you have the first topic.
Reiley 00:14:28 Yeah, just to recap for folks who forgot or wasn't in the previous discussion. So, So there's a discussion about adding some features to the Node.js runtime about OpenTelemetry APIs, and the question is.
do we consider OpenTelemetry APIs as a good addition to language runtimes, or we think the general guidance and direction is OpenTelemetry community should just build that without working with the runtime team, and I remember we discussed this, like, twice in the TC meeting, and the general consensus is, as TC members, we believe in the future, we want to see all the language runtimes have the OpenTelemetry API built in, if possible, because there are a lot of benefits.
And… and to help to communicate that, direction, we agreed that it's a good idea to invite some folks from Microsoft .NET Runtime Team to explain their journey, like, how NET ended up having the OpenTelemetry API as part of the runtime, and what's the struggle and the balance, like, they've learned in the past? Like, one example is, we talked about spend in OpenTelemetry, but .NET already have a a type called SPAN that's used by something totally differently, then what should they do? They need to call it something else, like activity. So, like, there's history, they won't start, like, 100% clean. So I… I reached out to the .NET architects, and they agreed. Like, they're saying, we're willing to work with OpenTelemetry folks to write down this, like, blog post, share our learnings.
like, who should I work with? So, I'm getting back here and see, can I get another TC member? Like, of course, I'll help there, because I have connection on both sides, but I… I need someone else who's not Microsoft to make sure, like, it's more neutral.
So, so Josh won't, won't be… won't be my candidate. I'm asking who else would want to work on that?
Carlos Alberto Cortez 00:16:30 Since I am, you know, the TC, person representing… the person representing the TC at the JavaScript sync, I can do that as a… if you need additional hands.
Reiley 00:16:43 Okay, then, Carlos, I would think in this way. I'll kick this off, I'll start some skeleton, like, I'll say, this is what we want to do in the blog post, I'll start a Google Doc.
then, like, you and I should review the skeleton first, and agree on that. Then I'll ask .NET folks to help fill in their part, and once we have the initial draft, I will bring that back to the TC discussion.
And the goal is, like, once we agree, we'll send a blog post, and with all the TCs supporting the direction.
Sounds good.
Carlos Alberto Cortez 00:17:18 Yeah.
Tigran Najaryan 00:17:19 Yeah, and I wouldn't worry too much about, I guess, the fact that you're from Microsoft and you're working on this. It's the right thing to do.
I would say, think of yourself as more of a person who is close to .NET people, and has the, I guess, the most knowledge on the topic, and who's the right person to work on it.
Reiley 00:17:41 Yeah, I know, I'm well aware that I'm wearing multiple hats here. It's just, like, I want to get someone who come, like, more with a fresh opinion, making sure, like, we don't have this bias.
Jack Berg 00:17:56 We…
Tigran Najaryan 00:17:56 Yeah.
Jack Berg 00:17:58 I will say.
Tigran Najaryan 00:17:58 Yeah, I guess…
Jack Berg 00:17:59 We don't have any prior art to, like, this type of transition from, like, you know, because .NET started with the OpenTelemetry API, in the runtime when the .NET OpenTelemetry project was kicked off. It's not like it was added later. And so there's, like, some additional complexity with, like, migrating the JavaScript community from using the OTel JavaScript API to one that's built into Node.
I think a lot of the learnings and the tensions that the .NET team can still share… that can share will still be applicable, but there's going to be new complexities as well.
Reiley 00:18:32 Yeah, yeah, it's ultimately, yeah.
Tigran Najaryan 00:18:36 And it may be worth also to work with Dan Dyla, because he had some good thoughts on the topic, right? And he also commented on the PR there.
Reiley 00:18:45 Yeah.
Okay, I… I think I'm all set here. Thank you.
Jack Berg 00:18:51 Okay.
Next topic, Tigrin.
Tigran Najaryan 00:18:56 Yes, we have a product proposal there. I do not think we responded to that.
So… And there's an expectation that we have to… make a decision as a TC.
whether we have a TC member who wants to take this, whether we think we should take it.
So, essentially, give a response to the GC.
I think we discussed this a few weeks ago. I do not remember if we made any decisions.
Jack Berg 00:19:29 So, I love to comment here, so I think there's two things we need to do. We need to decide the sponsorship level, and then assign a sponsor. You know.
You know, assuming that we accept this scope as, like, a valuable thing to do. So maybe there's three things. Do we or do we not want to do this? What's the sponsorship level? Who is the sponsor?
I think we can't get away with an escalating sponsor on this one. I left a comment to this effect here, and so we're looking at guiding or leading.
that's… that addresses one of the questions. The other question of, like, whether or not we should do this, I think that we should do this.
Like, I… The only question in my mind is, like, do we have the bandwidth to do this right now? Do we have the community interest to do this right now? But it's useful… it's a useful thing to do, and we would benefit.
Liudmila Molkova 00:20:32 Is my understanding correct, that it's essentially the release work stream?
From this tablebydefault.up.
Jack Berg 00:20:42 I think it's different, this is about, coming up with something like this.
An apt install OpenTelemetry command.
And embedded in this are all sorts of decisions that are… that intersect with stable by default, because you have to make decisions about, like, what does it mean to install open telemetry? Which components should be installed? Should there be a stability threshold that gates inclusion?
And so that's where those things intersect, but, like, the… what this… what this is trying to do at its core is try to come up with a cohesive definition of what it means to install open telemetry, so that we can go from, like, this, This… this box of discrete tools, which, if you're sort of, like, an expert, you can assemble in the right way and monitor your system, to, like, we have a simple install flow, which is opinionated, and which works for most people.
Liudmila Molkova 00:21:48 Okay, thank you.
It sounds like, though, that the intersection with stability is relatively high.
Jack Berg 00:21:59 I wouldn't disagree with that one.
Tigran Najaryan 00:22:09 If this is the… if this is the new project and you seek.
I mean, they will be responsible for making sure that experience is consistent, what you're asking about, what it means to install OpenTelemetry. I don't necessarily think we need a PC member to make those calls.
We… we do not… We don't necessarily have any… important historical knowledge here that needs to be carried over in this decision making. As far as I can tell, I may be wrong on this.
because of that, I tend to agree with you that we can get away with having just escalating.
Jack Berg 00:22:46 Oh, I said we can't get away with escalating.
Tigran Najaryan 00:22:48 You're saying we cannot?
Jack Berg 00:22:50 Cannot.
Tigran Najaryan 00:22:50 I'm not sure, I… okay, so then… I'm not sure I understand why we cannot in that case.
Jack Berg 00:22:58 See what I said… Acting as a point where we take various components in the ecosystem and stitch them together into an opinionated set of defaults. There's going to be questions about which components are included, the threshold for included.
Tigran Najaryan 00:23:15 No, I get it. I get it, Jack, but I'm saying they can make the calls, this Sikh can make the call, right? Because they are working across they can make that call. Why do you think we will have some knowledge. Typically, it's… why you want to bring the TC members, because some sort of historical knowledge is being involved there, that we do not think that new people necessarily have, which is important for this particular project. For this area, I don't think we do have that sort of knowledge there, right? So it's a matter of Doing a good engineering and making the right decisions there.
If the people are… solid engineers there, why do we think they can't make those calls? Is there a reason?
Jack Berg 00:24:02 So, I think it's the, so, where TC members have been required in the past has been, like, if a SIG needs to make changes to the specification. And I don't think there's going to be many changes to the specification.
Tigran Najaryan 00:24:16 Yes.
Jack Berg 00:24:17 it doesn'.
Tigran Najaryan 00:24:17 It does.
Jack Berg 00:24:18 It doesn't, like, meet that criteria. But what it does is it glues together lots of components that need opinions formed about, like, what the sensible defaults are. Like, so, like, what happens if you, like, want to install OBI and, you know, auto instrumentations? Like, which do you install and when and why, by default?
And, like, this is the project that is going to be sort of the, like, if it's successful, it's going to be the front door for open telemetry, the thing that most people pick up and use. And so, like, there's a reputational impact to us getting this right.
Tigran Najaryan 00:24:56 Okay, that's a big difference. What you're saying is this is too important for us to ignore, that's what I'm hearing.
Jack Berg 00:25:02 Yeah, sure.
Tigran Najaryan 00:25:02 Because otherwise, I would still say, okay, it's their job, whoever is leading this seek, to make sure that they go and talk to the OBI people, if they are including OBI in the instrument, in the, whatever, the system package.
But you're saying even a decision to include or not to include is an important one here to make, and them not having the full picture of what exists in OpenTelemetry On its own can be a problem, because they will forget to include some piece that needs to be there.
Jack Berg 00:25:40 Yes.
Tigran Najaryan 00:25:40 That's what I'm hearing.
Liudmila Molkova 00:25:42 And it sounds like whoever works on the SIG will need to work with every other SIG to find out the shape of… the included components. Yeah. And this is a lot of communication.
Jack Berg 00:25:59 Like, one thing, just to make that, like, tangible, Lyudmila, is… so, the Java agent right now has this process where it has major releases every once in a while, and it bundles lots of breaking changes into those major releases so that users can consume them in, you know, sort of like a structured way. Like, there's going to be breaking changes, but we want to bundle them together, so you don't… aren't exposed to them over and over again.
Like, I think that all the SIGs should do that with their auto instrumentation solutions. They don't do that today. I think somebody from the TC should, somebody with an important, an important voice in the community should sort of drive that issue across all of the language SIGs, and sort of decree that all of the language SIGs should adopt this philosophy.
And so, like, if it's not somebody from the TC saying that, I think they will struggle.
Liudmila Molkova 00:26:59 Yeah, to add to this, we have a previous example of operator doing something similar, and they have very old versions and an unclear update strategy.
Jack Berg 00:27:11 Yeah, the operator got burned by trying to become a sort of pseudo-gatekeeper of, like, what versions of all the auto instrumentations get used together.
And… and it… it… I think there's… they're sort of trying to unwind that, and go back and, you know, switch their philosophy from, like, we're going to determine what versions of all the auto instrumentations work nicely together, and sort of do… be QA on that, to we are going to, like, you know, have the user make the decision of which versions of the Java agent, which versions of Python, which versions of Go, or whatever they want to use together.
and why.
So, like, yeah, I think that's, like, in my mind, a sort of cautionary tale. Like, the operator is the version of this packaging SIG, but for Kubernetes environments, and I think it could have benefited from TC involvement.
Liudmila Molkova 00:28:09 Yes.
David Ashpole (dashpole) 00:28:14 Yeah, I would also say, like.
the boundaries weren't well-defined at the beginning. Like, they ended up being responsible for a lot of The build steps and stuff for the actual agents that they were distributing.
Which… You could argue, like, would have maybe been better served by having the individual languages build the artifacts and them just being kind of… distributors of those and managers of them on Kubernetes.
Jack Berg 00:28:41 Like, if the packaging SIG existed, David, the operator would consume the packages and use those to bundle up the auto-instrumentations into images.
And they wouldn't have to make that decision themselves. And maybe the packaging SIG should, force the respective language SIGs to be the ones forming those opinionated and publishing those packages. Something like that.
Or there at least has to be, like, a relationship, a horizontal relationship between them that's, like, formal.
David Ashpole (dashpole) 00:29:11 Yeah, or even that the packaging SIG just… Kind of, like, for some conv… How people come and contribute and manage their own semantic conventions, but, like.
you know, Josh isn't going and updating the JVM conventions, and making sure that they're… like, it… It exists as a central place for people to go.
And make changes to their artifacts, but they're not the ones that have to chase down the latest.
Java release or something. So, like, they would need someone, some volunteer from the Java SIG to come and actually go push the changes as part of their release process, or something like that.
Jack Berg 00:29:51 Yeah, and the Java SIG feels like a sense of obligation to go and have its conventions codified and semantic conventions, so I want that same, like, obligation to hold true here. I want, like, the Python sig to go and, you know.
be an approver, or own some part of the operator or the packaging repo that relates to the Python, you know, packaging.
David Ashpole (dashpole) 00:30:16 I agree.
Liudmila Molkova 00:30:20 So, would it be too much? So, I'm just reading through this table by default, and there is the work streams, redistributions, and component definitions.
Let me paste the link.
Would it be, crazy?
to… Make this packaging effort, part… Essentially, of this work stream. Or, like, from the technical perspective, it seems like they are not the same, but the packaging SIG would depend on this specific effort.
Should it be the same effort? Should it be the same SICK, or do we need two different… Seeks for this.
Jack Berg 00:31:02 We could call the packaging SIG the, like, technical embodiment of stable by default. Like, you know.
Liudmila Molkova 00:31:11 And this, this works Terms 3, yeah, this one.
Jack Berg 00:31:13 Exactly. So, you know, distribution and component definition. So, like, distribution are the packages, and so, like, the packaging SIG becomes the gatekeepers of stable by default, and, you know.
Draws the line about which components are included in the distributions and not, based on their centralized definition of stable by default.
Liudmila Molkova 00:31:38 But then it means the expansions of their school, because it seems they target Linux distributions for now, but this is essentially a distribution.
Jack Berg 00:31:50 Yeah, right. So, like, the collector, for example, already independently publishes images, and those images are used in places like Kubernetes, outside of, like, Linux, right? And so we'd want those… that same, you know, definition to apply to those… those images as well.
Liudmila Molkova 00:32:06 Yeah.
David Ashpole (dashpole) 00:32:14 I do feel like that, like, stable by default stuff should end up in the spec.
And under our purview?
And not… and, like, they can be enforcers for their artifacts that they build, but that… those decisions should be, like, probably made by the TC.
Jack Berg 00:32:34 I think that because, like, the spec is the place where we write things down that affect more than one repo. Like, policy, and especially policy related to more than one repo, and the stable by default is more than one repo, so yeah, I agree.
Liudmila Molkova 00:33:03 So it sounds like at least the prerequisite for this work, for the packaging sake, is something that CC should own. Well, together with GC.
This is our responsibility to make the packaging… well, the distribution story, release story.
Right.
And it can happen maybe within the SIG, or, like, a broader project, but this SIG cannot happen without that effort.
Jack Berg 00:33:34 I agree.
So the question is, do we have anybody on the TC that has the interest and time to drive something like this?
And if not, like, what do we need to finish?
In order to do… In order to open up, like, attention to work on something like this.
Tigran Najaryan 00:33:58 There's a question I wanted to ask. What do we want to stop doing so that we can do this?
Jack Berg 00:34:03 Doing her finish, right? Yeah.
jmacdonald 00:34:08 And I've been thinking about the stable by default, like, OTAP the whole time, like, because there's a… I mean, I've seen some of the feedback now, and it's like, there's a lot of benchmarking implied, and a stability work implied there, too, and I'm not sure what we give up. It also occurs to me that like, I… I've always felt this way about OTEL, which is, like, we… each vendor and, you know, sends some people to do what they specifically want, and, like, the whole community moves, like, haphazardly, slowly, in some unclear direction. This has always been this way. I don't know what to do about it, but it feels like… shouldn't we, like… wouldn't it be great if we had a way to, like, marshal all the maintainers from all the vendors and, like, point them in the same direction? I don't know how to do that.
Jack Berg 00:34:55 I think Ted and the GC is… is trying to think about things like that, like, more having a, there's an idea that was being tossed around about having an annual or biannual. The schedule doesn't really matter, but having a required meeting between maintainers of language SIGs and the TC and or GC to make sure that there's alignment on that SIGS goals and how they relate to the project's overall goals.
And so, like, it's not exactly a stick, you know, carrots and sticks, but, you know, it's at least a chance to, like, formally have a conversation about, about how the goal… about where the SIG is going, and how that relates to the broader community efforts.
Liudmila Molkova 00:35:42 If I had a magic wand and sent all the maintainers to work on something.
I would imagine, in most cases, we would send them to work on first declarative config.
And then, future parity and stabilizing.
everything possible.
Jack Berg 00:36:02 My magic wand is actually, In finishing the key domains of semantic conventions, and going and embodying those semantic conventions, and all the instrumentation.
If we had, like, if we had stable and consistent, embodiment of the, of, you know, the key semantic conventions across all languages, that would be… that would be a very good story.
And it would also free up a bunch of attention to work on other things. Like, that has plagued us for, like, years. It's just the consistency and quality of instrumentation.
David Ashpole (dashpole) 00:36:41 I thought you were gonna say Prometheus, but, you know.
But I couldn't.
jmacdonald 00:36:45 Maybe we should all do our magic wands. I have a problem with, essentially, the reliability. Like, you turn your SDK on, and it starts sending data, and then some of it starts dropping, and some of it starts… like, I don't know how to get reliable delivery for low cost out of the box.
And, you know, it comes down to not having a concurrency support in the SDK often, but just sort of, like, not having a general plan for, like, how do we get above 1,000 spans per second, or what do we do when the logs happen too much, or whatever, like… like, load has been my problem.
Guess we all have different ones.
Tigran Najaryan 00:37:24 Okay. What I'm hearing is no one wants to… take leadership on this one, at least no one in this call.
Jack Berg 00:37:33 So… I don't want to do it right now. Like, I think that this is an important thing to do, but I just got done working on declarative config for, like, 3 years, and, like, I want to work on some, like, smaller problems that have plagued people for a long time and have gone under, They've, you know, they've been ignored, largely. So, just like the kind of run-of-the-mill spec issues that, you know, don't have a project around them, but have lots of upvotes and are popular for users.
Those get… those don't get as much attention as they deserve. And I also think it's important to stabilize this, like, this, the key parts of Prometheus. We've been working on that for so long, and it's, like, it seems like it's a blocker for Collector 1.0.
Right? So, you know, I think a lot gets unlocked if we can start to… if we can finish things, and that's kind of where my head's at, is like, let's not get into a new thing, even if it's important, before we finish the prior things. And, you know, Prometheus is high on my list of finishing.
Liudmila Molkova 00:38:38 It sounds like… Oh, sorry, go ahead.
Reiley 00:38:43 Oh, very simple, I agree with Jack.
Liudmila Molkova 00:38:48 it sounds like… This tries to package things Together, but these things are not stable yet, or not good enough yet, and it's the second… Step after, we focus on some other areas.
But if we're… Don't… do… the… stable by default.
Then this is a risk to gradiation, and it may be important for some, not less important for others, but it's… it sounds like the… Most important thing for overall… for the project.
Jack Berg 00:39:32 What if we did something like this? What if we say, like.
like, we… I don't think we've done this yet, where we've tried to say explicitly to a proposal, yes, but not now.
And, like, what if the not now, part of that comes with a goal on when we actually want to do that? So it's not just, like, open-ended. It's like, yes, we want to do this, we're busy with these things at the moment, we'd like to pick this up in the second half of 2026.
Tigran Najaryan 00:40:03 So that's looking at…
Jack Berg 00:40:04 Put ourselves accountable.
Tigran Najaryan 00:40:06 Yeah, I was just looking at the number of proposals, Jack. When you're saying, yes, we want to do this, I'm not so sure anymore.
Why isn't there 50 outputs for this project proposal?
Why only? Why only… So few, huh?
Who cares? Maybe nobody cares.
Can anyone ask that question?
David Ashpole (dashpole) 00:40:29 upvote it.
I don't know if people actually use the upvote button that much.
Reiley 00:40:35 But even if the upvote, I think if the proposal here is, let's just bundle a set of unstable things together and make it more unstable. Like, from TC, we're going to say, no, we need to focus on making sure we have the stable components first.
This won't happen. If you want to explore some experimental thing, fine.
Right, so there are two things. One is, if there's less volt, we probably even don't want to spend the time here discussing about it. But if there's enough interest, we still hold the bar for stability and reliability.
David Ashpole (dashpole) 00:41:10 My thought was that I'd almost like to, like, mark this blocked on stable by default.
I feel like once we have a clear policy of how that would work. It's actually not… it wouldn't be crazy for me, I kind of agree with Tigran's point of view, that it wouldn't be crazy to have this being escalating, if it had good technical leadership otherwise.
And we have the right policies in place.
Reiley 00:41:38 Agreed.
Liudmila Molkova 00:41:42 The next question would be, do we do table by default?
They think that this is the key question. Like, if it is stable by default, this becomes trivial. If we don't, then this is impossible.
Reiley 00:41:59 We should. I always think there are two things we should do by default. Secure by default, stable by default. We're not doing a great job there, and we should.
Liudmila Molkova 00:42:12 But then, if we should, then how do we find the stable by default work?
This needs TC attention.
Reiley 00:42:19 Yeah.
And also, like, for this PR, we can say.
You're blocked by stable by default, so if you have energy here, it's common how unstable by default.
Liudmila Molkova 00:42:33 They block not on their energy, but on our energy.
Reiley 00:42:39 No, but we need to set a clear direction for the community that we care about stability and security, and we don't want to go spread this thing and give people, like, 100 things, and 99 of them are unstable.
Right, so this is something I think the GCs start to see the problem, and they want us to solve that problem, and seems like TC is also aligned on that.
Liudmila Molkova 00:43:03 Who would own from this group? Who would own this work stream?
3. Whoever would own it should probably be the representative of the packaging sync if both comes through.
But yeah, it sounds like it makes sense to block that effort unstable by default, but, like, yeah. But then, we should have answer for other stable by default.
When we do this.
Reiley 00:43:38 Yeah.
Jack Berg 00:43:39 So, what… just so we can, like… because I think somebody's going to need to leave a comment on this… this PR to that effect, that this is blocked by stable by default, and I'm just trying to think about what the reasoning would look like. Like.
What I'm hearing is that if we solve the stable by default work, that we think that we could continue with this packaging work with just an escalating level of sponsorship, and it would be okay.
And so, in a way, does that mean that you could also unblock this by a TC volunteering at guiding or leading sponsorship level? Like, is it one or the other? Solve stable by default plus escalating? Or, like, you know, make… not necessarily solve stable by default, not abandon it, but, like, have a TC member at a higher level of sponsorship.
David Ashpole (dashpole) 00:44:28 I guess the first thing I would expect the group to do is establish a policy that resembles stable by default.
I feel like the things that… What actually happened would be the same regardless.
Jack Berg 00:44:46 Okay, so… I'm gonna… I wanna call time on this soon.
Dick's done.
Tigran Najaryan 00:44:54 I don't think we necessarily have to reply publicly to that issue. Maybe we go and talk to the GC, or maybe tell the GC what our thinking on this is before we do the public response.
Jack Berg 00:45:08 Yeah, this meeting is recorded, so, you know, the conversation is public, but I agree, we don't necessarily have to.
Tigran Najaryan 00:45:15 I'm not saying to hide it, I'm saying let's go and consult with the GC before, I guess, we have an official response, together with the GC, ideally.
Jack Berg 00:45:26 Fair enough. Should we… should we try to get on the GC's agenda for next week, or do it asynchronously?
Tigran Najaryan 00:45:32 Let's start asynchronously, and if we have a call next week, let's also make sure it's on the agenda.
if… So, we have a reasoning that we believe there's a dependency or overlap with the, I guess, stable by default.
let's see what the GC thinks on that, right?
And if they agree, then… probably this means we postpone it, or whatever, right? I think we have to have that discussion.
Jack Berg 00:46:16 Okay, so that's… that's a much easier, action item, just, like, start a conversation with the GC in the GCTC channel. Does anybody want to volunteer for that?
David Ashpole (dashpole) 00:46:33 I can take a stab, if nobody else wants to.
Jack Berg 00:46:43 I'll chime in, David, after that, and try to add some of the context that we were talking about today.
David Ashpole (dashpole) 00:46:50 Okay.
Jack Berg 00:46:54 All right, then I think we can move on from this, unless anybody has any final thoughts.
So, the topic that I have is about this uptick in security advisories.
And I guess before we get into it.
I think that we can have this conversation publicly and recorded, as long as we're not, you know, as long as I don't pull up links to specific advisories.
If everybody agrees, then let's continue with that, and just try to be careful.
Okay, so I'm seeing some nodding, we're good. So, as some of you probably have noticed when you've done your TC on call, there's a decent number of security advisories, and it sort of shifts It sort of shifts what it means to be on call for the TC.
Because there's more load. And for me, when I'm responding to these things, the first thing that's going through my mind is, like, am I doing the right thing? Like.
what… should we have a standard operating procedure for how we kind of work through these, or at least have some things in common with each other, so that we kind of, present the TC voice in a somewhat consistent way. I'm thinking about things like you know, when do we accept an advisory versus request a CVE? You know, that could be… and maybe it'll always be pretty subjective, but maybe we could add some criteria, or at least, like, a notes document that helps us apply a common set of principles to that.
scoring. Like, so right now, I think we put a lot of, responsibility on the reporter to score the thing, and, like, at what point should we intervene? At what point should, like, the maintainers intervene and, like, offer their own opinions?
And that kind of goes into this last thing, which is, like, what is actually the responsibility, this set of responsibilities for the maintainers versus TC? Like.
what I… what I want to do as often as possible is I want to… like, bring in the maintainers and, and get them to run this thing, and decide when to accept it, decide when to accept a request as CVE. But, you know, practically speaking, I don't think that all the maintainers have a ton of experience with this.
Right? So, like, they probably need guidance as well, so… or at least, like, a cheat sheet on what to do and when.
So those are kind of some of the things that's going through my head. Open it up for conversation.
Tigran Najaryan 00:49:42 Yeah, I think that's a… it's a very good idea. Maybe you have a one-page Description of the process, of the expectations, of exactly the questions you're asking. When do you accept the advisory? Does it contain enough details to be considered something that is worth looking into?
I saw advisories that are open with virtually nothing in the description. I've seen… I found something there. What is it that's something?
And at some point, so you… I think it's the TC's responsibility to ask the person who is reporting the advisory to supply enough details before engaging the maintainers. There is a few steps that probably we should be following, and once you engage the maintainers, how do you guide them and help them? And there's also one more bit, the follow-up. I often go back to the old ones, the ones that are open for a while, and I don't see any communication there, and I try to make reminders.
to maintainers, primarily, if they already are engaged, to see if they are making progress there. It would really help if we have this written down somewhere, it doesn't have to be a very long document, it's probably, like, one page should be… should be enough.
But I agree with you.
Reiley 00:50:55 Fair.
So we already have it, and of course, it's never going to be perfect, but we're improving based on the feedback.
Tigran Najaryan 00:51:03 Nice, we have it. Okay, I didn't know we had that. Okay.
Reiley 00:51:05 And that's a problem, so I think the security sake, it's understaffed, and we don't have good visibility in the TCI. I brought a couple PRs, I… I don't have enough review, and I decided, okay, I'm going to wait until this is becoming a bigger problem, then, like, people will pay attention to it.
So, Tigran, there's one small thing I disagree with you. I… I don't want TC to get stuck in the middle for every single SIG.
Tigran Najaryan 00:51:32 I agree with you, that's… yeah, I was not suggesting that. I was just saying.
Before you accept it, you kind of set sort of a… little… there is a bar before acceptance, right? Once that is done, you definitely want to make sure you connect the reporter with the maintainers, and they work together. But as a TC member, I also feel some responsibility to make sure I go back and check to make sure that progress is being made, right? I don't necessarily… want to be involved in the actual resolution, and fixing stuff and all of that, but if I see that the maintainers forgot To work on that.
Reiley 00:52:11 Yeah.
Tigran Najaryan 00:52:12 It's fine, I can go and remind them, right?
Reiley 00:52:14 In a nutshell, in a nutshell, as TC members, we're accountable, but we should delegate as much as possible.
Tigran Najaryan 00:52:20 Absolutely, yes. But if they don't do the job, I will remind them. That's all I'm saying.
Reiley 00:52:25 If they don't do the job, we should first give them a nice reminder, because we're accountable. Like, we need to hold people accountable, and we need to understand not everyone is ready, right? So sometimes people make mistakes. So remind people.
And then we need to observe if this is a constant pattern, and people are not taking the feedback. If they don't take the feedback, then we should get back to the GC and have a serious discussion saying, this SIG has the maintainers, and they don't know how to do their job.
We should either replace the maintainers or dismiss the SIG, because we cannot keep the basic bar here.
Tigran Najaryan 00:52:59 I agree, I haven't had a case like that myself, but if that happens, I agree with you.
Reiley 00:53:05 Yeah, I've seen that a lot.
And another thing is, there are people who don't feel comfortable of creating GitHub, like, security advisories directly, or maybe they don't even have a GitHub account, they don't want to do it. So, for those issues, we allow people to send email to the security sig.
I'm… I'm getting about, like, 2 emails per week.
Like, there's some folks saying, I have this thing, then I cannot create an advisory, or I don't have GitHub account, but I just want to let you know. So, I'm handling that with two other security-sake folks. I don't expect anyone to reach out to the TC directly for any security issue.
They should either, using that email alias, go to the SIG security, or they should just directly file the advisory on OpenTelemetry repositories.
And if any TC member has the bandwidth and interest in security, they should also join Seek Security, so that's my goal.
can we… can we look at the… the meeting notes, Jackie, you have? So, I, I do have a lot of, like, experience and… and opinions there. So, first is treated as the same way. So, my position is everything under open telemetry, as long as it's there.
should be treated.
At the same bar.
If you have a feature branch or something else that you don't release, like, it's just, like, some playground, fine, but your official branch should keep the same bar.
Jack Berg 00:54:37 Right.
Tigran Najaryan 00:54:38 So, I guess.
there may be some exceptions to that, let's say, examples, right?
Reiley 00:54:44 No.
Tigran Najaryan 00:54:45 Dude.
It doesn't…
Reiley 00:54:47 also lead security. If they don't take care of security, these are going to be summed up in the organizational level security problem. And also, examples are a great way to demonstrate what's the best practice. So I disagree that we give any exception. And once you give exception.
Other projects will come and say, we just made a donation, this… historical issue, so… so for security, I… I want to hold a bar, like, wearing my security sick hat.
I think if you have some example, you don't want to meet the security bar, fine. Don't go to OpenTelemetry Community. Put that somewhere, it can still be open source.
Tigran Najaryan 00:55:27 I'm not sure I agree with that, Riley. Sometimes the purpose of the example is to teach something.
When you implement all the Proper error handling around that, that often is necessary.
for security reasons.
There is too much noise, and… too little signal in some of the cases. I don't know if I necessarily agree with the assertion you're making there.
Reiley 00:55:56 Sorry, I'm confused. I think the security here we're talking about is very specific to the supply chain security, so if the example is taking a dependency on an outdated version of OpenSSL, I would expect people to go and update that.
Of course, like, when it comes to the design, should the example demonstrate all the security, like anti-DDOS? Not necessarily. That part, I agree.
Tigran Najaryan 00:56:22 So, I'm saying, let's say there's an example of how to parse a particular protocol, let's say OTLP, right? Let's assume Protobuff didn't have let's say parsers, and you had to implement it manually. I would imagine I could have an example somewhere which shows how you parse it.
Without error handling, because it's so much easier to show how it works. If you add error handling in the mix, it's 10 times more code and less understandable.
And if I had a security scanner, that security scanner would say, this is unsafe, you're not handling the errors, this is going… this is a security disaster.
For me, it would be acceptable, because I'm trying to explain and teach something. This is not the code that you're supposed to run anywhere. The purpose of it is different.
Reiley 00:57:15 So either…
Tigran Najaryan 00:57:17 possession you're making, I'm not sure I'm totally buying that, right?
Reiley 00:57:22 for different things.
Here, we're talking about security advisories, so I expect that whatever example in the repo, you still respond to the advisory, and you can dismiss the advisory saying, I'm just an example, not in production, and I have clear comment in the example saying, this is this example, don't use it in production. So I'm going to dismiss the advisory, but I don't want you to ignore the advisories.
Tigran Najaryan 00:57:46 Okay, I'm not sure what's the difference between dismissing and ignoring. Like, of course, we're not going to say nothing, no response, right? We'll tell…
Reiley 00:57:54 If you're the repo owner of an open telemetry organization-owned repo, and people file security advisories there.
You should respond to the dividers instead of ignoring that.
Tigran Najaryan 00:58:05 Yeah, I think that goes without saying, yes, I agree, sure, of course, you don't ignore it in the sense that you have to respond somehow. The response can be, no, we're not fixing it.
Reiley 00:58:14 You can dismiss it.
Tigran Najaryan 00:58:15 Yeah, yeah.
Reiley 00:58:16 And that's aligned even with production one. You can dismiss it by saying, this is just used in a test case for the negatives, like, we're using this vulnerable package to test this corner case. I have to take dependency on this vulnerable thing, because that's by design.
Fine, you dismiss that, but you cannot just ignore it.
Tigran Najaryan 00:58:34 That I agree, but I think that goes without saying with any communication you're having with or within OpenTelemetry. And it's an official communication, you have to respond to it. Agree.
Reiley 00:58:45 Yeah, so this is about the process, like, this is why I'm saying contribute report and core reports are the same, they follow the same process, no exception.
Jack Berg 00:58:56 So, I agree with that. So, just kind of wrapping us up, we have one minute left. I already added this to the agenda for next week, so we don't have to finish this conversation today. I think it's worth continuing to talk about. But, like, two things kind of stuck out. One is, Riley, I didn't know about this document. I imagine most maintainers don't, too. Like, what we can do to start to, socialize its existence and improvements to it to get more attention to the PRs.
and things, is start to include a link to it as, like, our standard practice when these advisories are open. So when we loop in maintainers, also loop in a link to this doc so they can know what their expectations are.
That's one thing. That'll just build awareness and hopefully get some more attention, for the things that you're interested in. The other thing is, on Contrib, I felt the same way as you. I think Contrib should be, like, at the same bar as everything else, but I also want there to be, like, an effective back pressure mechanism. So, like, if most of the advisories right now are coming from Contrib, and one Contrib repo in particular.
And the one contrib repo, the collector contribib, just has, like, this massive, massive surface area. So, like, you know, somehow we have to reflect the fact that if you want a repository, a contribrib repository with massive surface area, you have to be able to staff that from, like, a security perspective, and continue to reliably respond to things on the cadence that you're expected. If not.
You have to find a way to trim down that contrib repository, so it can't just be unbounded.
Reiley 01:00:21 Yeah, exactly.
Jack Berg 01:00:23 Okay. I want to be sensitive of people's time. Let's pick this up next week. Thanks for the discussion.
Reiley 01:00:30 It's alright.
Jack Berg 01:00:31 But…
Armin (Dynatrace) 01:00:32 See you.
Carlos Alberto Cortez 01:00:33 Yup.
