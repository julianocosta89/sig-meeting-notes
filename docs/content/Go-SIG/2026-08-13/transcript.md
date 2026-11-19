SIG: GO SIG
Date: 2026-08-13
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 01:34 Hey, y'all.
**Puneet Singh** 01:37 Hello?
**David Ashpole (Google LLC)** 01:39 Hey, Tyler.
**Tyler Yahn (Splunk)** 01:42 How's it going?
**David Ashpole (Google LLC)** 01:45 Doing well.
**Tyler Yahn (Splunk)** 01:46 Nice.
Dave, is that room actually, like, red or orange, or is it just your camera?
**David Ashpole (Google LLC)** 01:54 It is… It's very orange.
**Tyler Yahn (Splunk)** 01:57 Oh, okay, it is, alright, yeah.
**Michael Blum** 01:58 Super orange.
**Tyler Yahn (Splunk)** 02:00 Very orange, yeah. You look like you're at, like, midnight somewhere.
**David Ashpole (Google LLC)** 02:06 Oh, cause, like, like, the lights are…
**Tyler Yahn (Splunk)** 02:08 Yeah, it's just, like, it just… yeah.
Make the light… well, I don't know.
That's how it goes.
I was gonna say, we don't have too much on the agenda currently.
But yeah, if you haven't yet, please go ahead and add your names to the attendees list.
And, Puneet, I see you're adding… Yeah, I was actually wondering about this one, Some items, and if others have items, go ahead and add them, and then we can get started here in just a second.
Cool.
Alright, yeah, so, start us off, welcome everyone. I don't have too much, but I did want to point out that the KubeCon UCFP is open. It closes, October 12th.
So, before KubeCon, North America, which is kind of funny, I think, but, it's just the way it is.
So yeah, if you have… Talks or, things you didn't wanna… submit to the KubeCon North America, just because you didn't want to come to the US, like, I think it'd be great if we can get some more talks over, there. Also, Barcelona is where it's at this year, in November, sounds amazing, so I'm really trying to go to this one. Yeah.
Compared to… Other places and other venues. So, yeah, should be good.
Cool, alright, next up, Puneet, you wanted to talk about gRPC status overrides.
**Puneet Singh** 03:59 Yahn so, I think David posted a detailed follow-up on this one.
And I think the… just to recap from the last time, previously we discussed the options, and I added another option to override the mapping, which is combining the global override with the method level.
Overwrite, but… You asked, I think, David, to do a follow-up and see if the whole… Setup alone makes sense, or we need to do any additional things.
I think what David, the overview that David provided, I think it makes sense in a way that We are introducing, API change, but it is not quite covering what user might want to do with the span status, which is, like, setting up… setting it up by themselves.
So, I'm not sure if I'm, you know, like, this is my take on this, that it did… the introducing a method does… or option does a job, but it just does a limited bit.
So… David.
**David Ashpole (Google LLC)** 05:08 Yeah, I would describe it as being two separate issues. One is that when we set… a status?
the user has no way to unset it. Like, that's not something that the API provides. So, once we set it, like, it's kind of final.
And if we're wrong, then… Like, oh well, I guess.
And then the second question is.
If… if a status is unset, is there any way for the user to influence that? Like, to set it themselves based on their own custom callbacks, or handling of the responses, right? And so, I think, Right, so those are the two pieces of it.
And I think… Option 3 from the original list.
Is a great way to… be for the user to be able to control, like, to be able to stop the instrumentation from setting it, right? So that, like, it kind of leaves it open to the user.
And then… then the question for me is, like, What's the best… Like, way for us to provide… what's the best thing we can hand to users and say, like, oh, if you want to go custom… do some custom, like, logic for how to set this. Where does that get inserted?
And I think the previously proposed one was… there were a few ones. There was… There was a per-method non-error code mapping, so it would essentially be, like, sort of a function on the… Method, so you could have a code per method.
Or we could have a fully custom callback, which is just a function.
I did… in my investigation, I did look at on ending, but Honestly.
it works fine. I think the issue is, like, a processor.
feels like a heavyweight way to add, like, an instrumentation-specific hook. Like, if I just want to update The span status for a single method within a single endpoint in my application.
Like, handling every single span feels like.
maybe a bit heavy-handed. It works just fine.
If I were a user, I would actually… Be more inclined to write a custom stats handler that wraps the OTEL gRPC one, and does custom handling there, just because it's more targeted.
But I think there is maybe room for us to add.
a callback if we want to. I don't think it's necessarily required, and I have… I have one suggested that I think is, like.
Pretty well scoped.
As kind of the sweet spot between Between, like… sorry, I lost my train of thought. The sweet spot between Write a custom stats handler, which you can already do today, and… just choose which… Which, Which would… and the thing that we're proposing in option 3, which is just… these are the… these are the non-error codes.
And that's… so, like, something in between that could potentially be useful, but I'm not actually convinced that… I don't know how common the use case is, basically, but I think that we could add something if we want to make that more convenient.
**Puneet Singh** 08:37 So, doing tree kind of just does that enough.
Like, you know, that use…
**David Ashpole (Google LLC)** 08:45 I think 3 by itself unblocks people, and anything else we do on top of that is more like.
Allowing them to avoid having to write a custom stats handler.
In order to implement, like, their fully customized logic that they want.
**Puneet Singh** 09:05 Right, I think this also answers my another question, is that, if we have a mechanism to set the span status, then why not just drop the entire… all the options and, you know, let the user know that this This way exists to set the span status, but that is the step 3, or the option 3, doing the minimum stuff if the user needs it, actually.
**David Ashpole (Google LLC)** 09:27 Yep.
**Puneet Singh** 09:28 And only setting the status when they need it. So in that respect, yeah, I mean, it makes sense, the overall approach.
Yeah.
I think for the associated PR, which is already progressing with option 3, we only need to add directions for… to introduce this as an additional documentation, how to set the span status.
This will… I think this approach is specific to gRPC, box for gRPC.
Mmm, jump.
I think, yeah, that's… that's more or less for the… for the respective PR.
**Tyler Yahn (Splunk)** 10:20 Cool.
**David Ashpole (Google LLC)** 10:21 Let me take some notes.
**Tyler Yahn (Splunk)** 10:23 Okay, so it sounds like we kind of have a path forward on this, right?
**Puneet Singh** 10:29 Yep.
**Tyler Yahn (Splunk)** 10:31 Okay. Yep. Yeah. Alright, that sounds good.
Well, if that's the case, we can go and move on.
To the next item.
So next up, Mike, you wanted to talk about the Hotel Explorer?
Going module?
**Michael Blum** 10:48 Yeah. So, I've been working with Jay and some other people now in the, CompileTime GO instrumentation project that just went GA.
Recently, and we have a number of discussion threads that all kind of end up in the same spot, where it's OTELC, the compile time stuff, and then the stuff I've been working on with the GO Contrib and GO Core to basically exercise the bottom one that we would think is the upstream version that I'm aware of.
of basically creating Weaver instrumentation YAMLs of the OTELGO libraries so that they can be consumed by the OTEL Explorer site. And I'm wondering what the… we've… how do I explain it? The… other teams, like the Java SIG and the JavaScript SIG have been… creating metadata yAMls and instrumentation YAMLs specific to their repositories, and we're wondering what that would look like if GO were to adopt a similar thing, where we would either have… I think what, like, the OTLC people are doing is they are making exemplar, like, tools projects in GO, and using those to exercise the code and generate these Weaver reports. But that's specific to the compile time instrumentation.
project in SIG, and I don't know if that would fly with GO Contrib as it exists today. The reason I bring it up is, like, building out the… taking this PR here in front of us as an example, this just exercises, like, the HTTP exporter, but it doesn't go into, like, all the other different modules that are in the contribib. This is, like, just one.
And so I think we're looking for some direction on, like.
where this stuff should live. Like, right now we have… you know, we have the OTEL Explorer kind of pulling in these repositories remotely, downloading them, and then walking the repository tree with, like, AST, basically, and exercising the code, and then, like, step two is we, like, create these Weaver instrumentation.
reports, but ideally, we want that living upstream. But before we go off and build all that, I'm trying to get a sense of… what would that even look like? Because I don't… anyway.
I could stop talking.
**David Ashpole (Google LLC)** 13:15 It's… is there a good, like, issue or something for me to… I'm not quite… like.
**Michael Blum** 13:22 I saw this.
**David Ashpole (Google LLC)** 13:23 Big demo on it, and I thought it was really cool, and I won it.
**Michael Blum** 13:27 Yeah, so that parent issue in the Google Doc there is where I would start, And then this was me just, like, jumping through… kind of what this might look like, and this is what I found the Weaver reports and stuff like that. And then the conversation picks up in that, OTLC, The adding compile time instrumentation.
It's kind of step two, yeah, that one.
And anyway, like, there's a lot of… Words being said, but it's kind of unclear… ignore that… unfortunately, there's a lot of, like, drive-by people just, like, drove by with LLMs and just, like, barfed a bunch of text into here that… it's kind of unfortunate, kind of muddies the conversation here.
But, like, Jay's the maintainer, we used to work together.
And then, it… it seems like the… the GO ecosystem… the compile time team is, like, has some tech that already Could do this.
And I guess I'm just here carrying a torch, going, hey, it looks like OTL… it looks like the compile time instrumentation hotel C thing could just do this.
But… like, per the release notes from compile time, their whole thing was, we expect you to instrument your apps with both compile time and manual instrumentation from, like, GO Contrib.
And so my argument was, like, we probably want to make sure we're encompassing all three repos here, not just building it for one.
Pretty fun.
**David Ashpole (Google LLC)** 15:13 So, so the ask is… Should OTelGoContrib have metadata.yaml files?
**Michael Blum** 15:19 Yeah, at the… long… long story short, by some… by whatever mechanism, should GO Contrib have the metadata files, where would they live, and how would we go about generating them? The… I… so the existing… Explorer code is very much on purpose written in GO with the intent that it might get consumed by… There we go, System Explorer… Pull requests… Should've had this up, I have too many links up.
The opening… Part of it is this thing here.
**Tyler Yahn (Splunk)** 16:03 Mike, do you want to share your screen?
**Michael Blum** 16:05 Oh, sure, yeah.
They changed the color of the share button, and it's been tripping me out for the better part of a week now.
So this was the initial… Implementation.
And it was very much pointed at GO… at the whole idea of This is the extraction part of GO Contrib. Here, I can drop off.
docs… That's not going very well. No, is it? No, it is not.
**David Ashpole (Google LLC)** 16:45 the metadata YAML format, is that, like, what…
**Michael Blum** 16:50 This is, like, the… Or is this, like…
**David Ashpole (Google LLC)** 16:52 Like, each repo has their own metadata YAML format.
Or is this Weaver's better?
**Michael Blum** 16:57 It's a bit of a trick question. I believe JavaScript is on Weaver. The Java one is half Weaver, half not, because they didn't know about Weaver while they're… like, the Java agent… is what led this whole project. Like, the website, if you go to, like, Explorer Hotel, the only thing on there is. They're… they have plans to move to Weaver itself, but they're not there yet, and the… from a timing standpoint, now that we have the JavaScript one, and I think someone else is working on .NET, I can't speak to it, we've kind of been telling each other, make… put… get on the Weaver standard, whatever your docu… however you derive that document.
is kind of up to you.
But the idea was that we would have… the Weaver stamp… this Weaver doc be what all the different code… which… what each language was going to start omitting.
That has gotten into an interesting… Where did my link go?
I have way too many links.
What am I trying to say?
we're trying to avoid the problem of trying to one-shot this, like, here's the standard, all the other languages, like, observe the Weaver standard, when we don't really have a clear example to point to of, like, how do you get that into the upstream repositories?
If that makes sense.
**David Ashpole (Google LLC)** 18:30 is, like, just… there is a standard metadata YAML format.
Correct or no?
**Michael Blum** 18:35 Yeah. There is a standard that we are driving towards, which is the Weaver, which is this… Which is the Weaver docs that we've pulled out. But yeah, we are going off of the Weaver spec.
And that project is what's supposed to be And here's a… I think this is a tighter example.
I think this is ideally what we're… this is what we're going for.
is exactly what OTELC is doing. And the question is, like.
it feels like the obvious answer is to port this stuff into GO Contrib.
**David Ashpole (Google LLC)** 19:20 This is, like, the… Is this the schema for semantic conventions?
Or is this a different schema?
**Michael Blum** 19:29 This is what.
**David Ashpole (Google LLC)** 19:29 like… Bench.
**Michael Blum** 19:35 I bel… the way I've thought about it is that it uses SEMConf To do the attributes and everything.
**David Ashpole (Google LLC)** 19:45 I see, I see, okay. So this is, like, a layer on top of the.
**Michael Blum** 19:48 Yeah, exactly. It's using, like, semconf as a reference for it, and that's what also, I think, kind of dovetails with this work here of… making sure that GO Contrib stuff is even on SemConf to begin with.
Which I think is another… that's, like, another layer to this, is, like, you generate the Weaver report, and is it even all on… using semantic invention?
it, from… as far as I know from this issue.
it's not… we're not there yet. I'm not actually sure… this thing's been around for a long time. I'm not sure how valid this… Still is.
Like, how much work there's left to do on this part.
**David Ashpole (Google LLC)** 20:38 Yeah, I don't have context, and I think Damien's been out for a bit.
**Michael Blum** 20:42 Yeah, but anyway, that's why I'm here. It's like, there's a fair bit of work to do, and I didn't want to, like, have us all, like, we built a thing, please accept our thing into upstream, and y'all look at me like, what is this? Why?
Anyway…
**Tyler Yahn (Splunk)** 20:57 Well, I mean, so I think, like, the… Telemetry schemas is important to start implementing.
For our instrumentation. Like, that's a big part of, I think, OTEL, and, like, any sort of instrumentation should be exporting what semantic conventions they comply with, and any sort of, like, deviations need to be included in their own registry.
I think it sounds like, from what I'm hearing, like, that is a consumable part of this, where then you could take that and then… Build off of it into this, like, format that you're looking for?
So, I mean, I think that sounds good.
I think there's just a lack of, like, bureaucratic organization on this, so, like, an issue describing, like, the problem set, like, the solution, what's going on.
And that integration seems like a good place to get people, like, in sync.
**Michael Blum** 21:42 Yeah, I think that conversation is happening on this issue here.
The very end of it… I think is the succinct part.
Where OTELC here already has its own registry, and they tried to go to the existing OTEL registry they were trying to migrate away from.
And so… But to your other point about there being, like, an overarching, like, bureaucracy here, that's why we brought up the whole, like, here's the reg… here's the watcher and registry system we're trying to build out for GO Contrib.
And trying to match… basically take… what they've already got going here with Hotel C.
And seeing if the two can be merged together.
**Tyler Yahn (Splunk)** 22:31 Yeah, I think that's the missing part, is what I'm hearing. Like, OTLC, this is great, But it, like, if we want to do this in the contribib rep repo, like, we need an issue in the contrib repo describing, like, the overarching problem, the overarching design, like, solutions and goals, and then, like.
you know, what's needed, and get the work broken down there, because, like, even if it's not, like, the correct work, if it's speculative, like, it helps people understand, like, what you're asking. Because I think right now, like, it seems good in theory, But I'm like… vague on a lot of notions, so it's kind of hard to understand, like, what's the ask from OTL Contrib, I guess, right now?
**Michael Blum** 23:11 I think just that there… that is a good idea, and that if the work is put down to, like… like… so the reason it's being built in this standalone repo is so that we can kind of move around and figure out what is… what it's supposed to look like, without jockeying PRs up to what is now 3 different upstream Repositories, is a large driving factor of kind of why it's being done on the side.
**Tyler Yahn (Splunk)** 23:35 Yeah, I mean, that seems reasonable as well. Like, I would definitely keep doing that until you have a plan.
**Michael Blum** 23:41 But yeah, okay, so I'll make a GO Contrib one and try to synthesize what we're going after here. I just wanted to get, like, I think a vibe check of, is this even in the right direction before we go off and sink a bunch of effort into it, I guess was my…
**Tyler Yahn (Splunk)** 23:55 I mean, I think it is, as long as it also includes, like, telemetry schema registry stuff. Right. Like, if, like, these are overlapping, that's great, but I wouldn't want to, like, do just, like, this manifest to support this, like, Instrumentation Explorer without, like, also supporting a telemetry schema registry.
**Michael Blum** 24:12 Right. That is the goal here. I think what's unclear is that the… just the timing of this, like, Weaver came in, and also this migration away from the hotel registry that exists today.
And there doesn't really seem.
**Tyler Yahn (Splunk)** 24:26 Yeah.
**Michael Blum** 24:27 As of, like, what that's supposed to look like. Exactly.
**Tyler Yahn (Splunk)** 24:29 That's another question, because it sounds like this is really based on this federation idea of semantic conventions. Yeah. Which is not ironed out.
**Michael Blum** 24:36 Right, that… the RNI is the problem here. There's just, like, there's, like, 3 or 4 different variables we're all trying to solve for here, like, at once. And so, as you can well imagine, it's just… it's very unclear and kind of hand-wavy.
Unfortunately, right?
**David Ashpole (Google LLC)** 24:51 Yeah.
**Michael Blum** 24:57 But yeah, I can take that.
**Tyler Yahn (Splunk)** 24:58 So, I posted a link also in the docs to this thing that Trask came up with for the Gen AI, now it looks like HTTP Explorer.
semantic convention thing. How does this relate to that?
**Michael Blum** 25:10 Hmm, amazing.
**David Ashpole (Google LLC)** 25:11 Is this not that? I thought this was…
**Michael Blum** 25:14 One sec, so… because Trask and Jay work together.
This also looks really…
**Tyler Yahn (Splunk)** 25:22 Yeah, so, like, this thing was shared in this, specification.
**David Ashpole (Google LLC)** 25:26 even… GO is even listed on here. Well, not in the GenAI, but on the HTTP one.
**Michael Blum** 25:31 Yeah.
**Tyler Yahn (Splunk)** 25:32 Oh.
**David Ashpole (Google LLC)** 25:35 We got lots of green checks, so… We can go home now.
**Michael Blum** 25:39 Yay!
**Tyler Yahn (Splunk)** 25:43 I mean…
**Michael Blum** 25:44 this is news to me, which is just, I think, a further illustration of this problem. There, like, there's a lot of different… permit.
**David Ashpole (Google LLC)** 25:52 This is what I thought you were talking about. Oh.
**Michael Blum** 25:55 I'm just like, let me give you the site that I referenced.
**David Ashpole (Google LLC)** 26:00 Trask just gave this, like, cool demo at the Spec SIG two days ago.
**Michael Blum** 26:04 I'll talk to Jay about it. I'm sure he… I'm sure he knows about it. It's this site… Well, I should have led with that.
It's this link here.
**David Ashpole (Google LLC)** 26:17 Like, I'm pretty excited by the idea of, like, a pre-submit that can check whether You know, the correct Stuff for each semantic invention metric is actually being collected somehow.
**Michael Blum** 26:30 Right.
I… I'm very excited about it from a, being able to do it across different… the third-party part, I think, is arguably the most exciting, when it comes to, like, how do you instrument the AWS SDK, or what have you.
that part fills me with joy. What is daunting, though, I think, is, like, figuring out how to have this thing continuously.
going through the backlog of, like, you know, GO Contrib is not exactly small, and there's a lot of… modules, and, like, exercising every little facet of it to arrive at a Weaver report that's… here's every attribute.
on… of SimConf.
Like, that, that's, that's the hard part.
But anyway, this thing here is… what Jay's been.
**Tyler Yahn (Splunk)** 27:17 You wanna share your screen again?
**Michael Blum** 27:21 But, This is what Jay's working… been working on. And right now it has the collector and the Java agent.
**David Ashpole (Google LLC)** 27:32 Yeah, they demoed… they demoed this as well on Tuesday, and said that there was a plan to merge the two.
**Michael Blum** 27:38 Oh, that's good. I'm glad they're not separate. I was like, because they work together pretty closely, so I was like, it'd be kind of weird if they were just, like, these were completely separate efforts.
But yeah, I think that it… so that'd be an int… so I guess this… This is another interesting… edge to this, I guess.
oh, yeah, Jay's about… Jay is a maintainer of this… okay, that makes way more sense to me. I didn't know about this effort. I only knew about… the Explorer project.
So yeah, I guess there's now a fifth variable in play of this, in addition to the metadata files in the respective upstream.
Repos.
**David Ashpole (Google LLC)** 28:25 Is this work happening under the purview of the Semantic Convention SIG, or what's the SIG look like?
**Michael Blum** 28:31 SIG.
**David Ashpole (Google LLC)** 28:32 Under which SIG?
**Michael Blum** 28:34 communications.
**David Ashpole (Google LLC)** 28:35 Communications, okay.
**Michael Blum** 28:39 I… I don't know why, but… No, I…
**David Ashpole (Google LLC)** 28:42 It's more like… I feel like this needs, like… agreement and vision and stuff.
**Michael Blum** 28:49 Yeah. It does.
**David Ashpole (Google LLC)** 28:51 But… Yeah.
**Tyler Yahn (Splunk)** 28:52 Yeah, like, I definitely agree with that. Like, maybe there's also, like, Cause it's, it's also, like.
one of the more cross-cutting concerns in the, like, hotel space out there, and I don't think it has any visibility in a cross-cutting concern way.
**Michael Blum** 29:08 It's so cross-cutting that I'm having conversations with, like, 3 other SIGs.
**Tyler Yahn (Splunk)** 29:12 Yeah.
**Michael Blum** 29:13 in… kind of in… kind of in these, like, GitHub comments is where this is all happening. Like, I don't… I haven't been at any other SIG meetings except this one. Well, it comes, like, twice, but…
**Tyler Yahn (Splunk)** 29:23 Yeah, I think the maintainers slash the specification meeting probably needs to have more content on this, to be honest.
But, yeah, I don't… to David's point, like, there needs to be some sort of, like, point person in that meeting to talk about this more often.
**Michael Blum** 29:39 Right, it does feel like we're kind of catering from the back here. I think what we were hoping, or at least the thought that I've seen in chat has so far been, if we build it, and we iterate on it, and we present something that looks so good, everyone's gonna be like, oh, we want to adopt this because they've thought of all the corners and everything, but I think there's so many… different edges to this, like, I don't know if it's actually possible.
**Tyler Yahn (Splunk)** 30:05 Yeah, I think that, like, just, being a part of OTEL for… I don't know, 6 years now, like, get feedback early, is all I could say.
**Michael Blum** 30:15 Right.
Okay, to that end, I guess I'll make a GO Contrib issue, write out, to the best of my knowledge, where this is. I'll sync up with J2 and see what Jay and Trask are up to, because there's something… it feels like there's a really obvious thread to all this, it's just hard to find, because, well, I'm not on that side of it.
**Tyler Yahn (Splunk)** 30:41 Yeah, no, I mean, I think it, again, like, the spec SIG also has, like, these, like.
deep dives into project working groups or things like that, like, this would be another good thing. Kind of happened organically last Tuesday, with, like, yeah, Trask kind of displaying what, David said, but, like.
Yeah, I think, again, like, just showing people, I think, and it's happened before, I feel like I've seen this multiple times now, but yeah, just, like, that continuous, like, integration, I think, would be really helpful.
Like you said, like, opening that is should be really helpful, understanding what the ask is, getting maybe a prototype, getting maybe a smaller interpretation library onboarded here, like, that seems all relevant and things that we can do.
**David Ashpole (Google LLC)** 31:18 And also, if we can just get, like, Trask or Lydon Miller or someone to say, like, yes, you should do this, this is the direction things are heading…
**Michael Blum** 31:25 helpful.
**David Ashpole (Google LLC)** 31:25 It'd be helpful for us.
**Michael Blum** 31:26 Yeah.
**David Ashpole (Google LLC)** 31:27 Yeah.
**Michael Blum** 31:28 Yeah, I'll ask Jay, because they, I think, work together pretty regularly. Yeah, that makes sense. I think we have some instrumentation set up, and we've been trying to, like, make this… break this out into, like, small, incremental changes, but it actually makes it quite difficult to be like, okay, here's a demoable state.
you know, here's the 5 stacked PRs that arrive at this, like, demonstration, which… Yeah. Anyway.
**Tyler Yahn (Splunk)** 31:53 Absolutely.
**Michael Blum** 31:54 Yeah, cool. I'll go down that road then. Thanks for the feedback, it's helpful.
**Tyler Yahn (Splunk)** 31:59 Cool, alright.
Sounds good. Alright, next up, David, do you want to talk about exemplars and timestamps? Yeah, yeah.
**David Ashpole (Google LLC)** 32:16 I realized also, while I was looking at this, that We… we're sort of compliant… we're mostly compliant with the specification around, like.
the collection timestamp. I'm sure we discussed this, like, 3 years ago when it stabilized, but I've definitely forgotten.
But right now, we get a different timestamp for each instrument.
During collect, like, collect happens for an instrument, and then we grab the timestamp.
Apparently, a lot of the other language SIGs actually use the same timestamp.
For collection, as the end time across instruments.
And there's, like, some… like, collector processors and stuff that expect the timestamps to line up if you want to do math. Like, divide A by B.
Yeah. On things. But I don't really want to change that here. I think… I had some more time. Initially, I thought that these were more related, but I actually think we can mostly ignore the… So there's, there's two issues. One is that, even… Who?
If we're doing concurrent collections with And measurements at the same time. There's always going to be this window between when we take the timestamp.
And… When we swap, do the hot swap and wait thing, right? So, like… There's always gonna be, like, a small, teeny tiny chance that A measurement will… And an exemplar will happen.
Just before the start timestamp, or no, just after the end time stamp. And this, this is for delta and cumulatives, both.
So that, that unfortunately, I think, is just always going to exist if we, But for Delta, at least, it's really, really tiny, right? Like, we literally take the timestamp and then immediately… Like, do the hot swap and wait thing.
For cumulatives, it's obviously larger, because Like, we can, you know, you can have 10,000 time series on an instrument.
And by the time it gets to… the last one, and actually collects its exemplars. It's, like, a lot more likely that something will have come in then.
I actually… I added one more proposal at the end. So there's two main proposals that I think actually fix the big cumulative issue.
And I don't think, like… I don't really think the small delta issue is relevant, or… unless we want to revisit doing concurrent measurement and collection.
Entirely.
But I think I added option 4 for us to think about.
It basically… right now, we take the timestamp at the beginning of collection, for cumulatives.
But if we just move taking the timestamp to the end.
Then we'll make sure that the end time is always after the exemplar time, and it doesn't really have any other side effects other than moving the timestamp back.
It does mean that if you look at the values They will be ever so slightly… like, if you took a rate over the whole interval.
It would be an ever-so-slight Undercount.
Of the actual number of measurements, because some of the measurements that occurred during that time window have swapped and gone to the, like, next interval, basically, while we're collecting. So it'll, like.
By the teeny-tiniest amount, we'll be undercounting the number of, like, measurements that happened, but we'll make sure that everything that did happen, or sorry, will make sure that all the things that are included in the aggregation happened between start and end. And to me, that feels like a more correct interpretation of the start and end time.
But… We can't really do that for Delta, is the funny thing.
I suppose it's… it's not… It's not funny, but deltas, we will still want to have at the beginning of the interval, because we need to keep it as close to the The swap hot and wait piece.
To make sure that the measurements and exemplars Go into the same bucket.
Like, that the timestamp swap basically happens right when that hot swap I don't know if that's… if you're following that or not.
**Tyler Yahn (Splunk)** 37:01 Yeah, I am. Yeah, yeah. Okay.
**David Ashpole (Google LLC)** 37:03 So we would have different behavior for delta and cumulative, in terms of when we could take the timestamp, but it would solve the problem of you looking at your metric and being like, huh, this one is, like, 2 milliseconds, 3 milliseconds after my end time, like, what happened here?
**Tyler Yahn (Splunk)** 37:20 Right, yeah, yeah, yeah.
**David Ashpole (Google LLC)** 37:22 I did prototype.
**Tyler Yahn (Splunk)** 37:23 What about the idea that, like, the… I don't know, like, it's obviously a large refactor, but, like, what if, like, the exemplars and, like, the metric storage shared the same, like, backends? Not really, like, backends, like, the same sort of, like.
storage object, and, like, those would be concurrently, like, not concurrently, but, like, coupled in the switch. Like, the hot swap… essentially, when you do a hot swap change, you're not only changing the backing for the data, but you're also changing the backing for the exemplars in, like, that same atomic action?
**David Ashpole (Google LLC)** 37:54 Yep, yep, so if you scroll up to option 2… That's what I prototyped here. So this is the double-buffered So basically, right now, we have…
**Tyler Yahn (Splunk)** 38:04 Hmm.
**David Ashpole (Google LLC)** 38:05 For every histogram point, We actually have 3 of them, right, that we're keeping in memory.
One is… One is the hot histogram point, where new measurements are going in. One is the cold histogram point that we can use for collection. And then there's actually a third, which is the cumulative, histogram point. So, you end up Taking the cold, merging it into the cumulative at the end of collection every time.
And so… the merge operation is the tricky bit, right? Because right now, reservoirs are… they're just what they are. They're… they're like an opaque thing that we don't really… like, sometimes it may return one res… one exemplar, sometimes it might return 50, And you don't… you have to delegate the merge algorithm back to the reservoir to say, hey, do you know how to merge yourself into another one? So for histograms, for example, like, we need to… like, we know they're both fixed size, and we know that we, like, index 5 always needs to merge into index 5, even if… If the reservoir only has one exemplar, but it's in index 5, and the other one has one exemplar in index 6, like.
they don't override each other, right? They, like… Merge together in their proper indices.
It's like, we would need… we would need to implement that, like.
delegation back to the reservoir, and so we would be adding new API surface to the reservoir that would be optional, and we would implement it for our reservoirs.
But, like, custom reservoirs would have this problem until they… They implemented it.
**Tyler Yahn (Splunk)** 39:48 Yeah, yeah.
**David Ashpole (Google LLC)** 39:49 And so, we also keep the, like.
We basically have to, as well, implement both paths, then, in the histogram, where we have one path where If it is a mergable reservoir, we can do this.
Double buffered plus cumulative approach.
And then if it isn't, emergable reservoir, we have a single Reservoir that just has the, like, collection problem.
That we're describing here.
And the only other… like… when I implemented it, this is kind of obvious from just the design of it, but you end up with 3 full reservoirs worth of Like, memory space, and the reservoirs tend to be the… the dominant,
**Tyler Yahn (Splunk)** 40:36 Yeah.
**David Ashpole (Google LLC)** 40:36 Like, factory member usage injury.
**Tyler Yahn (Splunk)** 40:38 Yeah.
**David Ashpole (Google LLC)** 40:38 So it does triple memory usage, roughly, for cumulative histograms.
**Tyler Yahn (Splunk)** 40:49 Does other languages solve this?
**David Ashpole (Google LLC)** 40:52 I can check.
**Tyler Yahn (Splunk)** 40:58 I kind of feel like Java's doing this idea, this double buffering thing, but…
**David Ashpole (Google LLC)** 41:03 They might be, I can…
**Tyler Yahn (Splunk)** 41:06 But I remember also looking at their, like, API for the exemplars way back in the day, and I don't remember seeing a merge functionality like you're describing.
So… Okay.
Did you have a recommendation on these?
**David Ashpole (Google LLC)** 41:24 My… I mean, the easy option is option 4.
Which I like the more… from a practical standpoint.
I think best serves our users.
I think it's mostly whether you Can buy that this is… It is still within the metricreader.collect.
Function call time.
**Tyler Yahn (Splunk)** 41:52 But it's just…
**David Ashpole (Google LLC)** 41:53 Towards the end now, instead of… Like, invoked kind of implies, like.
Invoked makes it sound instantaneous, but it kind of implies, like, the beginning of the invoke, right? Like, so that…
**Tyler Yahn (Splunk)** 42:04 Yeah.
You know, I don't want to specify.
**David Ashpole (Google LLC)** 42:07 I don't want to not be compliant with the specification.
But…
**Tyler Yahn (Splunk)** 42:14 Yeah, I just… but, like, again, like, I think… you said it accurately. It sounds like invoked is, like, this instantaneous, like… action, but it isn't at all.
Okay. Did you need a, an answer in this meeting? Because I don't have one. I'd have to think about this one.
**David Ashpole (Google LLC)** 42:40 No, it's fine. I wanted to make sure that we had time for discussion, if you had thoughts or requests of me.
I will go look up Or… ask Gemini to go look up, what the other languages do.
Yeah.
**Tyler Yahn (Splunk)** 42:55 Yes.
**David Ashpole (Google LLC)** 42:56 And, we can… Especially if other languages are, taking the fourth approach, I feel like.
That would be my… that would… I… We've had a lot of, like, regressions in terms of memory usage.
That users have flagged over the… course of the metrics SDK, so I'm… I'm a little bit nervous about blowback for… You know, having member usage jump.
**Tyler Yahn (Splunk)** 43:25 Yeah, I see what you're saying.
**David Ashpole (Google LLC)** 43:26 Big time, if we go with the other option.
**Tyler Yahn (Splunk)** 43:29 Yeah, and like, if you do this analysis and you come to find out that, like.
all other SDKs have the same problem, then, like, I'm not as concerned.
We should probably… bring it to the specification, but, like, I don't know, like… Ideally, I'm hoping what you find in your survey is, like.
There's just, like, one golden child who actually has solved this, and, like, we're just not thinking about the right solution here, but,
**David Ashpole (Google LLC)** 43:59 That would be nice.
Hopefully that's well.
**Tyler Yahn (Splunk)** 44:02 Yeah, it's gonna be Erling, I guarantee it.
**David Ashpole (Google LLC)** 44:07 Swift.
**Tyler Yahn (Splunk)** 44:08 Yeah, yeah, right, yeah.
But, yeah, like, okay.
Yeah, I think… I think that would help frame a little bit, but also just, like, I don't know, I need to… I need to think about this one a little bit more as well.
**David Ashpole (Google LLC)** 44:25 Originally, I actually thought we might be able to do the… Merging… Yeah, originally I thought we might be able to, like, just explicitly handle… Fixed.
the two reservoir implementations we have in Tree.
By doing just type assertions on them. Yeah. But, not enough is… is public, so we can't actually… like, we have to… it would be nice if we could at least… do it without the API change, so that if we change our minds later, it's…
**Tyler Yahn (Splunk)** 44:59 Okay.
**David Ashpole (Google LLC)** 44:59 We end up with a weird function hanging out.
On our reservoirs.
**Tyler Yahn (Splunk)** 45:05 Yeah, I see what you're saying.
Yeah, okay.
**David Ashpole (Google LLC)** 45:10 Unfortunately, that wasn't possible.
**Tyler Yahn (Splunk)** 45:13 Yeah, okay.
I'll, I'll, I'll give it some thought.
And if you do get that survey, I'm guessing you will, or Gemini will, if you want to just post it, I'd be interested to see those results, obviously. So, that sounds good.
Okay, alright.
With that then, I think we're at the end of the agenda.
Any other topics folks wanted to talk about?
Projects, things they're working on.
If not, yeah, we can end the meeting, here. It's good seeing you all, good talking with y'all. I will see y'all in a week's time.
**Michael Blum** 45:53 Thanks for having me.
**Tyler Yahn (Splunk)** 45:54 Yeah.
**David Ashpole (Google LLC)** 45:55 Thanks for joining, Mike.
Bye.
