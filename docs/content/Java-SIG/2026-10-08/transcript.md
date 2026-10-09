SIG: Java SIG
Date: 2026-10-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker (Microsoft Corporation) 00:03:26 Hello!
John Watson 00:03:57 Good morning.
Trask Stalnaker (Microsoft Corporation) 00:04:30 Add your topics to the agenda.
I know you got some, Jason.
Something for us.
Jason Plumb 00:04:45 Nothing that's not just full of snark and bile.
Trask Stalnaker (Microsoft Corporation) 00:04:56 Alright, I guess… Just quick update on V3, the last 2X release finally went out.
And, we've started Deleting massive amounts of code, which is… Amazing.
And… So, I don't know exactly when we will get… This… 3-0 out, Should… will be this month.
Our standard release date would be next Wednesday.
But I suspect we won't make that.
But I don't think we're that far out, maybe, like, a week.
Ha!
A week late.
Hopefully, at most.
Alright, let's go to… we've got SDK release tomorrow.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:06:02 Yeah, we got SDK released tomorrow.
And, yeah, this is kind of a discussion about anything that needs to or ought to go in for there.
I've identified two PRs that I think are worth talking about.
The first is that somebody opened an issue, and this is kind of news to me, but, so… there's a comment in our code somewhere about, you know, because we hand-roll our gRPC clients, for the OKHTTP sender, and there's a comment in our code that basically says, like, hey, the GRP response status code is always in the standard headers.
And this person came along in this issue that's linked here, 8843, and says, like, no, that's not actually the case. There's gRPC implementations where the status code is returned in trailer headers.
And, yeah, so it's… I validated it, and it's a bug in our implementation. But because the response code may come in standard headers or trailer headers, it actually changes our… it causes our implementation to have to change a bit, because to access trailer headers, you have to fully consume the response body.
And, yeah, so that's… that's what this implementation does here, and, in this PR, and, you know, I've gone back and forth with them a little bit. It was pretty crufty, the initial thing, but, I think it's… pretty close, and unless folks sort of, think otherwise, I'm going to try to tidy this up and get this in a state to merge before the release, because it would be a nice bug to fix.
John Watson 00:07:53 We can't handle this with the, the built-in Java HTTP client, right? Because it doesn't support trailers.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:08:02 Correct.
And for that reason, our JDK sender implementation does not support gRPC. It's only the HTTP protobuf.
John Watson 00:08:12 Okay, we don't even… we already don't support it. Okay, cool.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:08:14 Correct, yeah.
Trask Stalnaker (Microsoft Corporation) 00:08:23 Any, consequences to having to read the whole body?
First.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:08:31 Yes. Bodies can contain bodies contain bites.
And, yeah, like, so it's not free to consume those bodies, and we have limits in place to make sure that the body consumption isn't excessive, and… but that is something that we have to think about. So there's not a free lunch here.
Trask Stalnaker (Microsoft Corporation) 00:08:57 What is the… so we do have a limit.
Is that a…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:09:01 I.
Trask Stalnaker (Microsoft Corporation) 00:09:02 Is that an OTLP spec limit, or that's our own?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:09:06 It's an OTL.
Trask Stalnaker (Microsoft Corporation) 00:09:07 fault.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:09:08 It's an OTLP spec limit. And, you know, that was added somewhat recently in the last couple of months.
And, so we have a configurable limit on the request size.
That defaults to the OTLP specs default, and we have a static limit on the response size.
And the max… the response size is static, because we don't do anything with it today. So, there's no point in making it configurable. In the event that we do do something with it, then it all of a sudden becomes relevant to make it configurable.
But… So right now it's just a static hard-coded limit that's aligned with the spec.
John Watson 00:09:52 Do we know what sort of stuff?
Like, I mean, assuming… and this is, I know, a big caveat, but assuming non… like, something trying to do something bad to us. Do we know what normally ends up in the body? Like, is it normally just empty? Or is there normally just, like, nothing there when there's a… On the response?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:10:15 Yeah, it's normally… under normal circumstances, there's nothing there. And the… the only… Data that is optional in the response body message type is, like, this sort of, like, unstructured.
informational string that tells you, like, that allows a server to indicate that there was some sort of problem with the payload, and to say, like, what the problem was. But it's completely unstructured. It's like… it's essentially, I think, like an array of strings, if memory serves me correctly.
John Watson 00:10:49 And we don't do anything with that today to try to provide information on logs or anything, right?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:10:54 We don't. There's an open issue for it, but it's been open for several years.
John Watson 00:10:58 you Interesting. So we can… I don't know, I haven't looked at this PR at all, but we can just spin through the bytes and throw them away as we go, and then… And then look at the trailers, right? Seems, since we're already ignoring the content.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:11:18 That's right.
John Watson 00:11:19 Okay, cool.
Trask Stalnaker (Microsoft Corporation) 00:11:23 Cool, sounds like a good one. What, one more… oh, Big guy, big guy.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:11:31 Well, I'm not set on this, but I want to sort of tease this idea and see what people thinks.
see what people think. So, Josh Sures has this PR that's been open for a while to land an entity's prototype, and it's not the first iteration of this. Jason had, like, a previous iteration of this.
trying to add something, like an initial prototype for entities in Java. And Josh Surrett's PR was hung up at the spec level for a bit, because the spec was ambiguous about a few things. The merge mechanics, and the nature of when entities should be emitted, like, whether it's, like, an opt-in or opt-out feature, or something like that.
And those SPAC issues have been cleared up.
And, you know, in… after those spec issues have been cleared up, I have this PR open to update Josh Surrett's PR to solve a bunch of, like, sharp edges, and to make it conformant with the spec.
And, yeah, so Josh and I are going back and forth on that, and Josh is, like, pretty aligned with me, and we've been, like, talking in DMs that, like, hey, like, we're about ready to merge my PR into his PR. And then at that point, like, you know, we're kind of in this weird state, because, like.
like, it's Josh's PR, and I've reviewed it, but I've also contributed to it, and so, like, you know, do you all feel comfortable, sort of, you know, letting me underwrite that and, like, you know, merge it when I've also been a major person contributing to it?
That's kind of the question, and, like, you know, does the… do you care about me doing this, quickly? Because there's, like, you know, a release tomorrow. And, some context for… that might influence what you say is that, you know, when this PR is merged, nothing changes.
So.
So, entities, there's nothing that is producing entity-aware resources, so nothing happens day one. And for something to change, for you to start seeing, like, entities in your OTLP payloads, what would have to happen is you would have to start specifying this OTEL entities environment variable.
which allows you to encode entity information in a structured way as an environment variable.
Or, you know, what this PR unlocks is it unlocks the Java instrumentation resource detectors to start producing entity-aware resources. And so, if Java instrumentation were to start producing entity-aware resources, then… and you were using that version of Java instrumentation, then you would start seeing entities in your OTLP payloads.
But, you know, as noted here in the first bullet point, there is no opt-in or opt-out. Like, entities are serialized as soon as they are present. That is where the spec landed on this, and… You know, they're still experimental from an OTLP standpoint, so a consumer of these OTLP messages has to specifically look for this, like, the presence of this field, this new field, where entities are encoded, which is experimental and annotated as such. So, like, that's sort of the opt-in mechanism, is your OTLP receiver has to choose to start reading this entity information.
Got him.
John Watson 00:15:04 I'm… I'm fine, I'm fine with a relative fast track, but I would also say our other approvers should… Take a look.
Jason Plumb 00:15:19 It's true, we should.
I think that it's been such a long time coming that there isn't a lot of benefit in fast-tracking it.
But if you're inclined to, to move it forward, I also understand wanting to do that. Can you… can you talk through, not having looked at the PR at all, or not in months, can you talk through how, components that use the resource get aware of changes? Like, how… like, how does a tracer provider get an updated resource?
Is that part of the speech?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:15:54 Okay.
I'll just add two things that you said. So one, like, what's the benefit of fast tracking this? It's not huge, but there is some, because instrumentation can't start producing entity-aware resources until Core publishes a release that makes the APIs available.
Jason Plumb 00:16:10 Sure, is that a core need right now, though?
Is there anything…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:16:14 I coordinate an open telemetry.
Jason Plumb 00:16:17 No, I mean, like, has instrumentation been chomping for this?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:16:22 That's a subjective question. I think people have been chomping for entities for a a long time.
Jason Plumb 00:16:30 Yeah, okay.
Okay, so… I mean, so it's fine. So the second point.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:16:38 Second point, yeah, how do… how does Tracer Provider become aware of, like, an updated resource? So, this PR does not address the dynamic portion of resources and entities. Okay. And, but I have a separate PR up that, like, so one of the things that was landed as part of these spec PRs that resolve these ambiguity questions.
is the spec has now defined a component part of the SDK called the resource provider.
And resource provider is, like, the thing that resolves resource and entity detectors, and makes, like, a resolved resource accessible to the tracer provider, meter provider, logger provider.
So, I've modeled that out in a separate PR, and, you know, that would have a nice interaction with entities, but they can… those two PRs can actually go forward in parallel, and then be connected and wired up together in a subsequent follow-up. And even my PR that introduces this resource provider concept, it punts on the idea of dynamic entities, entities where the descriptive attributes are subject to change.
And… but it… it accommodates it. Like, architecturally, there's, like, a very obvious place to extend the APIs and, like, you know, and make the entities, you know, dynamic with some sort of callback functionality. But, you know, for… in the interest of keeping the PR digestible and small and atomic, or whatever. Like, I punted on that for a future one.
Jason Plumb 00:18:13 Cool. I think that's a smart approach.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:18:17 So, Okay.
Trask Stalnaker (Microsoft Corporation) 00:18:23 For me, from a merging perspective, Sam Taylor, two approvers, like yourself and Josh, have each contributed to it, and reviewed each other's code. I feel like that should… count.
Easily as good as… Somebody else submitting it, and one approver reviewing it.
So I'm…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:18:54 Sounds good.
Thanks for that feedback. I'm not sensing… I'm sensing, like, a little bit of questioning, but, like, not so much that I… I don't know. I'll exercise my judgment and just, like, you know, evaluate what the state is after Josh and I, you know, chat more today, and I'll make a go or no-go call.
I'm not going to merge something where there's still open questions, but if everything is sort of, like, neatly resolved, then… I'll merge.
Trask Stalnaker (Microsoft Corporation) 00:19:26 Yeah, yeah, if you get to that point, yeah, merge it. Let's get entities. Entities is… Each little step we can make will help your picture.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:19:42 That's right.
Jason Plumb 00:19:45 Yeah, no, you just got me thinking, like, I don't think there's been any talk yet of entities in Kotlin yet.
And it's something to think about.
Might might be easier to to start building it early than than not.
Trask Stalnaker (Microsoft Corporation) 00:19:59 Yeah, and we're definitely thinking about it in semantic conventions, repo… Just this week, Ludmilla has been… updating… On.
all of the entities to the Weaver V2 schema.
And kind of that has… Modeling in the… our original modeling of entities was pretty loose.
Like, say the Android entity like, so it's… just got… it's… a lot of them have been sort of almost bags of attributes. This one's closer, this one's almost. I'm not quite sure if that is identifying So…
Jason Plumb 00:20:54 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:20:57 Some of them are a little more obvious, even, like, and I'll let comment on this, like, for… like, we had originally defined a cloud entity But the only… it was kind of like a bag of attributes. There's a resource ID in it, but that's obviously not an identifying attribute for a cloud. That's an identifying attribute for a cloud resource.
So we've been a little loose. But we're starting to… in the semantic convention side, we're starting to tighten that up, because with the schema V2, the… It requires identifying attributes.
Alright, Any… anything else on entities?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:21:52 No?
Yeah.
Thank you.
Trask Stalnaker (Microsoft Corporation) 00:21:58 Cool. I threw this on just to wanted especially Laurie's thoughts on, I know I have, we've resisted, sort of, automating the… or not automated, but, like, change log, requiring change logs on PRs, in the past.
Because it's kind of annoying as a contributor to have to always put in a changelog entry, it can be released. We felt that way in this repo.
But I think my thinking has kind of changed a bit.
Given that AI is very used to and good at just always throwing in a change log entry, and that having them in the PRs If we… if we improve our code review guidelines for change log entries.
we can kind of enforce those as the PRs come in, and… hopefully… Yeah, it should simplify the release process then, and… Doing the town crier seems like the most popular option out there.
We're using that in the Gen AI repo. I know in OpenTelemetry, there's kind of a, that changelog gen, utility that, several of the repos use, but that's, like, a hand-baked OpenTelemetry one, which I'm… My personal preference would be something more standard, off the shelf, that AI Coding agents understand better already.
So this, basically adds You add a file, same as the changelog gen, you add a file for each PR. This is just a one-time, basically, taking our current change log entries and moving them over. Actually, I'll probably have to… currently, that's only the breaking changes. I'll have to actually backfill that a bit more.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:24:22 So what's in one of these files? So they're markdown. It's not YAML like changeloggen.
Just.
Trask Stalnaker (Microsoft Corporation) 00:24:29 just.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:24:30 Text description of the change?
Trask Stalnaker (Microsoft Corporation) 00:24:32 Yeah, so the label is encoded in the file name here.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:24:36 Got it.
Trask Stalnaker (Microsoft Corporation) 00:24:38 And so there are… let's… Change log… no.
Read me… here we go.
Nope.
Where are the labels described?
Guess it's just here… Freeform, but yeah, so the label… that's the label.
And then, when we generate… Oh, here we go, this is what I was looking for, the Town Crier Toml.
defines the… labels, and then these are our headings that it turns into. So it basically retrofits, then, along with this Jinja template.
Read, this will… Format it the same as our existing change log entries.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:25:47 So, A couple… couple questions. So, is the changelog markdown file, is that then, like.
updated, at… at the time of the PRs contributed? Are there gonna be, like, a bunch of, like, merge conflicts, or are the change log like, you know, files, do they accumulate over the course of, like, you know, daily life, and then the changelog.markdown file is only updated as part of the release?
Trask Stalnaker (Microsoft Corporation) 00:26:21 latter.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:26:21 The latter? Okay, so no sort of, like, merge conflicts to worry about there?
Trask Stalnaker (Microsoft Corporation) 00:26:26 Right.
And no step of sending a changelog PR before the release.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:26:36 Right.
And I guess, another question. So, one of the things that, I'm not sure how you handle this at this point, but that we do, that ends up in our changelog.markdown file, is this, like, categorization of, like, like, component. It's like a component categorization. At least we have that in core. Did you go away from that in instrumentation?
You still have that?
Trask Stalnaker (Microsoft Corporation) 00:26:59 I don't think we've ever had that in the instrumentation.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:27:05 Yeah, okay.
Yeah, so, I mean, I was just thinking of your category system.
Trask Stalnaker (Microsoft Corporation) 00:27:11 contribute.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:27:12 contrast.
Trask Stalnaker (Microsoft Corporation) 00:27:13 Yeah.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:27:14 Yeah, so, like, maybe there's… Maybe you could encode multiple bits of information into the file names, like, the… The class of change, whether it's a fix or a breaking change or whatever, and then also, like, the component that it relates to.
Trask Stalnaker (Microsoft Corporation) 00:27:33 Yeah, I don't know much about Town Crier other than kind of the default usage here. It's pretty popular Python, it's pretty popular, probably. I would think you could customize it more.
Jason Plumb 00:27:50 So, do you think… Go ahead.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:27:53 Do do you need to have Python locally, if you are a contributor now, or is this just like the contributors just need to generate the markdown files and all the validation in in in Python runtime is just available in the build?
Trask Stalnaker (Microsoft Corporation) 00:28:06 Yeah, you only need Python for generating… for the release process.
Cool. Like, so we're not even… there's nothing really to validate, I think, since it's just, markdown.
And, you can…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:28:22 Amanda, it exists, right?
Trask Stalnaker (Microsoft Corporation) 00:28:26 Yeah, I'm actually not even, I chose not to enforce validate… enforce it, and where you have to do the skip changelog label for stuff.
Because I find that a little annoying. Instead, my thought is just to enforce it via Copilot review instructions.
And so, Copilot will… The review will flag if it's missing.
And… or if it doesn't follow format.
Jason Plumb 00:29:00 So there's going to be a new check on PRs that make sure that these changelog files exist. Is that… No?
Trask Stalnaker (Microsoft Corporation) 00:29:07 Not a… it'll be a Copilot review instruction. So, Copilot review will flag if it's missing, and if it has… if it has user behavior changes.
And it's missing. Or if it's a braking change and it's not flagged, it's not marked as braking.
Jason Plumb 00:29:28 Got it. So if it was, like, a typo in a comment, it wouldn't… the PR wouldn't be blocked by a missing changelog entry. And that determination is made by Copilot as to whether or not it's breaking, or deprecation, or whatever, the three statuses. Okay.
Trask Stalnaker (Microsoft Corporation) 00:29:43 Yep.
Jason Plumb 00:29:46 Okay, and then if… so let's say I am… let's say a contributor is making a breaking change.
Would… and then Copilot's like, hey, you need a changelog entry, and here's how you do it.
Presumably, the author then has to go and create that file and add it to their PR, if they didn't in the first place. And aren't they just going to copy the text of the description of the PR and paste it into this file? Like, that seems like what people are gonna do. And then it's redundant information.
Trask Stalnaker (Microsoft Corporation) 00:30:15 If they do that, so I… I… I want to, improve the code review guidelines for those changelog entries.
Meaning?
Jason Plumb 00:30:28 Okay.
Trask Stalnaker (Microsoft Corporation) 00:30:28 I want them, you know, like, we'll have things about, it should be concise, it should be in this tense, it should be, like, basic, like.
I've noticed AI generates has been generating bad change log entries in our repo, and so I need to tweak those to make them good, but yeah, that's…
Jason Plumb 00:30:52 Yeah, one thought there was, like, if you could also automate that, like, if the co-pilot determines that it's a break and change, can it just, like, summarize… like, it probably can't add a file to your PR, but it could at least, like, give you the thing to paste into the file.
Just, just, I'm just trying to reduce the amount of, like, yeah, contributor cognitive burden.
Trask Stalnaker (Microsoft Corporation) 00:31:15 So, anyone who's… do… sending it via AI, like, and I'm assuming most people are using AI to generate PRs to this repo.
the… it should… AI is pretty… determined to add changelog entries to PRs, from what I've.
Jason Plumb 00:31:33 Yes, it is.
Trask Stalnaker (Microsoft Corporation) 00:31:36 I'm not really too worried about it for, like, that's partly why I don't think it… Poses much of a burden anymore on contributors.
We just need to direct AI to generate the changelog entries in the way that we want them.
Gregor Zeitlinger 00:32:04 And, we have been using this mechanism in other OTEL repositories for a very long time, so people are already used to that.
Even if it was not Town Crier, but this custom tool.
Where you had to do it all of the time.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:32:32 Well, I've been thinking about.
Trask Stalnaker (Microsoft Corporation) 00:32:33 Yeah.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:32:34 Trask? I'm probably gonna pick up, pick up the torch and try this on for the core repository as well, unless anyone feels strongly against it.
So…
Trask Stalnaker (Microsoft Corporation) 00:32:47 Cool. Jason, to your point, I have… I have played around with… so AI is… writes horrible PR descriptions.
Also… Very long, often.
John Watson 00:33:02 I was going to say, it writes a lot of words. There's a lot of words. Yeah.
Jason Plumb 00:33:06 It's like one of the ways that you can smell an AI-generated PR.
Trask Stalnaker (Microsoft Corporation) 00:33:10 So, I have a… I have a little local instruction for writing PR descriptions.
And I've actually, when I see in this repo, when I see a PR come in with one of those massive PR descriptions, I actually overwrite their PR description. I have my AI overwrite their PR description by basically doing what you're saying, is look at the PR.
it… you can automatically generate a PR description, but follow these, like, you know… ideas and don't make it huge. Don't list every single test that you ran against it. It really loves to do that. And it's completely useless information.
Jason Plumb 00:33:56 We have.
Trask Stalnaker (Microsoft Corporation) 00:33:57 MCI, we could see that it's, you know, green or failing.
Jason Plumb 00:34:01 Yeah.
It's fun when it adds the markdown files with that information too.
I've seen those a bunch.
Trask Stalnaker (Microsoft Corporation) 00:34:09 Oh, yeah, we were having that problem, Laurie flagged it on a… Bunch of my PRs, were… the mig… it added migration notes into the READMEs.
I'm like, no, the migration notes, that's… the change log entry is…
Jason Plumb 00:34:30 my.
Trask Stalnaker (Microsoft Corporation) 00:34:31 migration notes. We don't need to document, you know, There's a bunch of, yeah… Bunch of tweaks we need to keep making.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:34:41 I get a laugh every time I get a 300 word PR description for like a Java doc update. That's like a one word change.
Trask Stalnaker (Microsoft Corporation) 00:34:55 Cool. Laurie, I didn't hear anything from you.
Hoping… Wondering what… if you have thoughts about this, preferences, any… anything you'd like me to… Tweak here. Change.
Lauri Tulmin 00:35:15 Yeah, I was hoping that the current AI is good enough.
Trask Stalnaker (Microsoft Corporation) 00:35:22 For generating the change log.
Lauri Tulmin 00:35:24 Yeah.
Adding the changelog entries feels kind of annoying, but… I guess we have to try it.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:35:37 I mean, it doesn't… it doesn't strike me as dramatically different to require it at PR time, or to encourage it at PR time, than it does to have your own agent, perform that function against all the PRs.
that were part of the diff since the last release, but, like, is it, like, a one-time action instead of, like, an action that's performed each time that a PR is submitted? So, like, in some ways, the approach that we currently do, we're… whoever's doing the release has to manually generate the changelog. It allows more standardization, because whoever's generating that changelog can control the prompt for every single changelog entry.
Trask Stalnaker (Microsoft Corporation) 00:36:24 So, that is what we've been doing here for a few releases.
We've got a workflow here that runs, and… it does, use Copilot to basically generate those changelog entries for everything, and classifies everything as enhancement or not.
Bug fix, breaking change, etc.
I still end up spending.
Quite a bit of time, on those… And… I mean, the last release… And this upcoming release are probably exceptional, though, just because of the number of deprecations and breaking changes we're making in preparation for 3-0.
So one thought was, by having these in… Under source control would kind of let me draft them.
as we go a little bit more. Maybe another op… an option would be that might You know, I mean, it would be not requiring them at all, but allowing them.
And then I could backfill.
Those change log entries… From time to time.
We're at…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:37:58 I mean, that's what you're doing with this, right? Because you said that you don't have, oh, I guess you did say that Copilot was going to enforce the presence, just not like build automation. So the presence is still enforced, but it's just like LLM instead of.
Trask Stalnaker (Microsoft Corporation) 00:38:12 Forced. Yeah, yeah.
But, I mean, it could make that optional.
I could tell Copilot review instructions that it's… optional, and if it is included, to use XYZ format, but not to flag if it's not there.
And then I could run that.
From time to time.
I like that. I mean, because… With the PRs I send, especially with these breaking changes and deprecations, I like to… I like… I'd like to… I usually do change log entry them.
While… because it kind of ties it.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:38:59 I know what you're saying. Like, there's there's there's multiple views of how you wanna present the information in the PR. There's the PR title, which is, like, 10 words or less and isn't enough detail for a change log.
There's the PR description, which is, like, pretty verbose sometimes, and again, like, not appropriate for a changelog. And then there's, like, the changelog entry, which is, like, somewhere in between. And, like, it's nice to craft that somewhere-in-between message that's going to be consumable by end users.
Like at the time that you're doing the work instead of like at release time trying to like remember the context.
Trask Stalnaker (Microsoft Corporation) 00:39:35 Yeah, I like that idea. I think I'll do that.
Of basically not making… making it… totally optional.
But if it is there, then I can add… Like, sort of what it should look like.
And then, at least for my PRs and breaking changes and deprecate the things that I'm sending, I can tailor those.
And then… I can… Probably even change this draft release notes to basically be, like, backfill those.
It's nice to have them under source control, gives me something to review, and… Check as we're leading up to a release.
And sometimes I backfill, like, backfilling the actual changelog file itself is just… It's an option, and I think we've done that in the past before, but… I don't know, AI is so determined to update that changelog entry, the changelog file.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:40:55 I wonder if, like, you're talking about backfilling in bulk, I'm like, you know, make it optional, but the backfilling process could be at, like, the PR level, so, like, some sort of automation where If a PR doesn't have a change log entry.
You know, when you're ready to merge it, you… like, a change log entry is generated automatically using, like, whatever prompt you come up with, and it's merged. It's, like, it's committed to that PR and then merged as a… as an atomic unit.
Lauri Tulmin 00:41:25 You mean something that AI submits PR on top of PR that has the changelog?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:41:31 Just, like, no, a commit that's… that contains the changelog entry that's pushed to the commits… to the PR's branch. Not a new PR, because, like, as maintainers, the default is that we can push commits to PR branches.
And so we can basically leverage that feature to, like, you know, update their branch.
Trask Stalnaker (Microsoft Corporation) 00:41:55 Yeah, that might work. Updating, checking out… Branches is… is a common security flag.
The pull request target thing.
But in this case, you don't actually need to run anything in there, and you don't even really need to… You just need to get the PR diff.
Yeah, I think… I think that would be.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:42:29 You can get the PR diff from.
And the value weight that… Right, right, right. And not have to actually execute any code that's in that diff, just compute the changelog entry from that.
Trask Stalnaker (Microsoft Corporation) 00:43:11 Alright.
That's great.
Gregor Zeitlinger 00:43:14 The tools who automate that part, so generate release notes based on the diffs.
using AI, if… If you want to have that one instead.
Trask Stalnaker (Microsoft Corporation) 00:43:27 Yeah, that's what we've been doing, essentially.
But it's… It still requires… I mean, I'm not super happy with I generally end up spending a decent amount of time still massaging that.
Gregor Zeitlinger 00:43:48 Okay.
Trask Stalnaker (Microsoft Corporation) 00:43:50 And so what I'm kind of hoping is to spend that time incrementally as the PRs go in and make the release process Just a one click, then.
Because currently, I don't trust the… it's not a one-click, because I don't trust the AI, change log entries.
I mean, they're… they're fine, they're not, like, wrong, they're just… not up to the standard I would like our changelog to have.
Alright, hey, Gregor!
Moving around inside of Grafana.
Gregor Zeitlinger 00:44:44 Yeah, exactly. Was looking for a bit of a new challenge. Still OTEL, but More on the eBPF side of things.
Just for your information.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:45:00 Hope you have your Linux machine ready.
Gregor Zeitlinger 00:45:04 Okay.
It's already churning away!
Trask Stalnaker (Microsoft Corporation) 00:45:11 Alright, anything else to discuss today?
Yeah, Pranav.
Pranav Sharma (Google LLC) 00:45:24 Hey, I think I was just a few minutes late to the meeting. The very first topic was about the V3 instrumentation. I was just wondering, you know. If there's any update on when it's gonna be out?
Trask Stalnaker (Microsoft Corporation) 00:45:37 Yeah, so the final 2X… Release, the final minor release went out What's that?
Last week.
Pranav Sharma (Google LLC) 00:45:49 5 days ago?
Trask Stalnaker (Microsoft Corporation) 00:45:51 Yeah.
So the next release from Maine will be 3.0.
And so that will… Be, this month.
Probably my guess right now is, the… 21st.
Pranav Sharma (Google LLC) 00:46:15 I see. Sounds good. And do we plan to release, make any releases from contrib anytime soon? I think the last one was two months ago, I guess.
Gregor Zeitlinger 00:46:31 We have to, because, There are some changes that are needed to be.
compatible with 3.0 with the things that are being removed.
Trask Stalnaker (Microsoft Corporation) 00:46:49 Is it… in… Anything that is… anything need to make it in… Or is it ready for release now?
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:47:02 3135 needs to go in. I was just waiting on a code owner to approve it.
Trask Stalnaker (Microsoft Corporation) 00:47:09 3135, this one.
Jason…
Jason Plumb 00:47:19 I can take a look at that one.
Trask Stalnaker (Microsoft Corporation) 00:47:24 Cool, that's… that's it, Jay.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:47:27 I think so, yeah. I think I already merged the one Gregor was talking about.
Gregor Zeitlinger 00:47:33 Yep, that is in.
Trask Stalnaker (Microsoft Corporation) 00:47:37 And we got the instrumentation update.
Already.
2 32.
Yeah.
Alright, yeah, sounds like a plan.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:47:59 Hey, Jay, just, vincentnestler: Just a small point on that, like, waiting for, a code owner. So, Sylvain's a code owner of that as well, right?
Jason Plumb 00:48:11 Yes.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:48:13 I wonder… I wonder if we, like, so… Do we need… if a code owner is, you know, contributing a change to a component in Contrib.
do we need another code owner to approve before it's merged, or is any approval from a general maintainer or approver sufficient for that? And, like, the problem I'm getting at is, like, many of the components don't have a lot of code owners. Some of them have one code owner, and many have, like.
one or two, and so if many have one or two, then requiring another approval from another co-owner means you get an approval from this specific person, the only other co-owner that exists, or none at all.
Jason Plumb 00:48:58 I think the answer technically is no, I think it doesn't, it's not required, like, the button's green right now.
Right? But… I also understand maybe wanting to vet something with a component owner, if it's important enough, or if it's… If, like, a maintainer doesn't know that area very well, and is like, oh yeah, it'd be nice. Like, there's some stuff in here that I… I have no clue about, where I'm like, I need help from the AWS folks to review this one, because I think it's doing the right thing, but I don't really know.
So, in those cases, it's nice to have, but is it required? No, right? The maintainers have final say.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:49:32 So I have a proposal, but I want to see if it aligns with what Trask is going to say.
Jason Plumb 00:49:36 Okay.
Trask Stalnaker (Microsoft Corporation) 00:49:38 Yeah, my thought is, I like to… Push for the other, another code owner approval, because I like to make sure that those code owners are involved.
Like, I don't want them… I feel like that is the way to keep them involved, is to make sure that they are… looking at PRs, And if they're not, you know.
Then they shouldn't be code owners, and if we don't have more than one code owner, we should retire the, the component.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:50:22 I think we should formalize that somewhere in the Control repository. Components need two code owners, and if they don't, if they drop below this, then we consider them for retirement. And these are the responsibilities of a code owner.
Like, we've all said things to that effect, but I don't think it's written down anywhere.
And the thing that I was gonna say, which I think relates to… I think it… I think it melds with what you're saying, Trask, but, it was gonna be about lazy consensus. So whenever… whenever I'm, like, working in the spec repo that has, like, a lot of people that have approval rights, but the strict criteria is you need, like, two approvals or something like that. Like, if I've met the strict criteria.
I like express my intent and I attach a date to it.
like, hey, for anybody else that's interested to review, like, this has enough approvals to go forward. I'm going to merge this on this date if there's not, like, if other people, like, don't comment before then. And that date is always, like, a week in advance or something like that. So that could be a way to… do what Trask said, and encourage the other code owners to participate, but not, like, open-ended and indefinitely.
So, something like that.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:51:36 On a similar, there's another PR that's open for one of the AWS components, and I've been I've been pinging the code owners for a while, the last one, the cloud account ID. I'm tempted to just merge it. I think Laurie already reviewed it. I was yeah, I was trying to give them an opportunity.
To, weigh in, but maybe because it's been so long, we just…
Trask Stalnaker (Microsoft Corporation) 00:52:07 Yeah, I mean, you know, We definitely have… The maintainers, have interest in some of these components, for sure.
Some of these are pulled into the Java agent.
And… Some are used by our companies.
outside of that. So, I… I think for maintainers to basically be like, I have an interest in this, I'm kind of representing a code owner is fine.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:52:43 Cool, okay, yeah, that makes sense to me. And yeah, I was gonna… if nobody else had a chance to take a look at the JMX one, I was gonna merge it before the next release regardless, but I just figured, since I knew Jason, and I thought he might want to look at it, but… It's pretty straightforward. It's not that…
Jason Plumb 00:52:59 Yeah.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:52:59 It's gonna change, so…
Jason Plumb 00:53:02 Cool. I'll look at it.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:53:06 Yeah, I didn't realize I didn't do a release last month, that's my bad. I'm not sure if I'll have the opportunity to do it this week. I'm probably gonna end up Going to the hospital with my wife at some point today.
So… If somebody else could, maybe pick that up.
Trask Stalnaker (Microsoft Corporation) 00:53:24 Congrats.
Jason Plumb 00:53:26 And then you're out, right? Are you taking time off?
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:53:28 Yeah, I'll be out for about 8 weeks, and then I'm gonna come back for a month and a half, and then I'm gonna go out.
For about a month. So I'll be in and out. But yeah, I may may continue to.
poke around, but… We'll see.
Trask Stalnaker (Microsoft Corporation) 00:53:47 Any, any volunteers for contrib release?
Duty?
While Jay is out.
Eeny, meeny, miny, moe.
Flip 2 coins, 1 and 4.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:54:08 I, I'll tell you what, I'll… I'm gonna kick it off now. I think I still have another couple hours before we… we take off, so if… if I don't finish it in time, I'll post in the… in the channel, but I'll see if I can… I can do this last one.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:54:22 I still wanna delete.
Trask Stalnaker (Microsoft Corporation) 00:54:23 where.
Lauri Tulmin 00:54:25 If nobody does it, I can try it tomorrow.
I'm not sure, like, for their… Whether it required some approval from someone.
John Watson 00:54:38 But on the topic of retiring components, I think there's a component somewhere in Contrib that I'm the sole owner of, that I think we can absolutely close.
and get… and deprecate and get rid of. I don't… I'm not involved anymore in whatever… whatever it is. Yeah, the client… the Prometheus client bridge, like, I'm not using it. I was the only… I only put it in here because I was using it, and I'm not anymore, so I think we can kill this… kill that component.
Jason Plumb 00:55:08 And then send it.
Gregor Zeitlinger 00:55:09 News car?
John Watson 00:55:12 It was basically allowing the… The Java SDK… to use the Prometheus… like, use a Prometheus server… I don't remember the details. As I said, I haven't used it in a long time. I don't care about it. I'm the only person, I think, who ever cared about it, so I think we can kill it.
Jason Plumb 00:55:36 He hasn't had any meaningful commits in three years.
John Watson 00:55:39 No, no, exactly. Like, I'm not doing anything with it, I'm not using it. I mean, I think it works… But I don't think there's any reason to keep it around.
Unless there's somebody who's actually using it.
In which case… they can own it, but there's no reason to keep it around, because I don't care anymore.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:56:01 Let's formalize the policy. We gotta have policies that create the incentives for what we want.
Trask Stalnaker (Microsoft Corporation) 00:56:15 Let's see, so we've got Prometheus Client Bridge.
Runtime attach.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:56:25 No op API.
Trask Stalnaker (Microsoft Corporation) 00:56:37 This one has…
John Watson 00:56:38 Jack, what is that NOAA API?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:56:41 I just had to go look. It's an implementation of the no-op API that doesn't even include context propagation.
John Watson 00:56:50 So it's, like, really… it's, like, real no-op.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:56:54 Exactly.
Trask Stalnaker (Microsoft Corporation) 00:56:55 I think Anurag had created that, based on some… Performance testing, load testing, or something.
A long time ago.
Alright, well, that's a good start.
Let's say we will retire these… at end of October…
John Watson 00:57:41 Probably tag current maintainers of those components, although Jack and I are here, so… I think I don't remember who it was… John Basuti on the runtime attach?
Trask Stalnaker (Microsoft Corporation) 00:57:52 Yeah…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:57:57 What about… there's one more in there, Traska, the micrometer provider one, that was the… Halo 4 dude.
Jason Plumb 00:58:05 Like this won't notify him though, will it?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:58:09 Well, if we tag them, it will.
Trask Stalnaker (Microsoft Corporation) 00:58:11 I'll tag him, yeah.
Jason Plumb 00:58:13 Does that actually send a notification?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:58:16 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:58:24 And there was still one more GFR events.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:58:42 Do you know the JFR events one has had contributions in the past couple months?
I don't know if that changes our view on it, but…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:58:51 Here's the question. So we're reaching out to these individuals.
that are the code… the component owners. Let's play this out. They reach back out and they say, hey, I still want to maintain this, but there's only one of them.
Like, do we, do we require two component owners? And if so, like… like, what do we do if the one component owner who's left still thinks this is important? Or do we say, like, hey, go solicit somebody else to be a component owner with you?
Trask Stalnaker (Microsoft Corporation) 00:59:32 Yeah, let's, Interesting, because… Is this the one that… What was he? Was… What's the history of this one?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:59:55 From CORE, moved out.
Trask Stalnaker (Microsoft Corporation) 00:59:57 Core, oh… What does it do?
Jack Berg (Raintank, Inc. – Grafana Labs) 01:00:03 I think it converts… JFR events to spans? Or the other way around, it converts spans to JFR events.
Trask Stalnaker (Microsoft Corporation) 01:00:15 Create HDFR events… oh, okay, okay.
Hmm.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:00:26 Sort of like an exporter, the export spans as JFR events.
Lauri Tulmin 01:00:32 I think we actually can't, like, put too much emphasis on having the component donors.
Because, like, I don't know, the AWS components have, like, the component owners, but those two dudes, like, never show up, and they're completely useless.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:00:47 Well, that's why you have to couple the component owners. You have to say, like, how many component owners are required, and what are… what's the expectation of a component owner? Like, and so, like, if you have an expectation that says you review PRs related to your component, and you get tagged, and you don't respond for 2 weeks, then you get removed as a component owner.
The component drops through below the threshold, and then you delete it.
Like, that's like, that's the sequence.
Lauri Tulmin 01:01:13 Well, the problem with AWS components is that we actually need them.
Jason Plumb 01:01:16 Everybody uses it.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:01:19 Well, that's the thing, then. So, if it drops below the component owner threshold, then a maintainer or somebody else has to volunteer to step up as a component owner. It creates the right incentive structure.
If nobody's opposed, like, I can write that policy and at least, like, open a PR about it.
Trask Stalnaker (Microsoft Corporation) 01:01:47 Yeah, let's do that. I'm not gonna open this issue, let's… let's establish policy first, and then we'll apply that.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:01:59 That's good.
Trask Stalnaker (Microsoft Corporation) 01:02:03 And we're out of time!
Good topic.
See y'all.
Pranav Sharma (Google LLC) 01:02:10 Yeah.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 01:02:11 I.
Pranav Sharma (Google LLC) 01:02:12 Right.
