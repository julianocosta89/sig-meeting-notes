SIG: LLM Semantic Convention WG
Date: 2025-10-07
Duration: 50 minutes
============================================================

## Zoom Recording Transcript

**Aaron Abbott** 02:59 Hey everyone, how's it going?
**Sergey Sergeev** 03:04 Aaron.
**Aaron Abbott** 03:06 Cheers.
So, looks like, Lumil's not gonna join, but… That's alright, let's give it a few more minutes, and… Please add your names and any topics to the agendas, please.
Sorry, agenda, please.
Alright, maybe let's just, go ahead and get started then. Can folk see my screen?
**Michael He** 05:06 Oh, yeah.
**Aaron Abbott** 05:08 Okay, let's start with the… Backlog.
This one's not new, but I think we talked about it a couple weeks ago, So, someone was trying to get in touch with Danny, right?
Was it you, Sergey?
**Sergey Sergeev** 05:34 Hmm, yeah, I could not find… Even people in ABM cannot find.
**Aaron Abbott** 05:41 Telecontacts.
**Sergey Sergeev** 05:43 Okay.
Again, it's more or less aligned with how we see genre types, what's being defined.
so, Microsoft Team has more… Smaller items for each.
**Aaron Abbott** 06:02 BM.
Okay, I think we went over all these already. I'm not sure why they're still in new issues, because they… I guess… I guess we have to move them, but I'll wait and check with Ludmilla, maybe. But, Yeah, trees.
**Sergey Sergeev** 06:20 That was my question, probably, we need to… To review…
**Aaron Abbott** 06:27 This issue is A.
**Sergey Sergeev** 06:28 I think a lot of work being done.
It's done outside of, this project, so… Maybe we just need to do a better job.
Failing those issues, and working on them, or updating them.
**Aaron Abbott** 06:45 Yep.
This one looks like it wasn't triaged yet. This is about skill, but I think it was probably part of the same… This is regarding A to A.
I don't think Wanya's here, but I… I don't have much to say to this, it seems… You know, pretty straightforward.
I guess I can ask if you'd like to take that.
Okay.
Yeah, that seems pretty straightforward, I don't think.
It's controversial, but… This one I filed. This, this would be a follow-up to, 2754, which I also have later in the agenda, which is the, adding the attachment types.
We don't need to talk about it too much now. I think we kind of discussed it at length last time, but, PDFs, documents, they're just not… scoped in the current PR, so this was kind of a follow-up.
Yes, I'll put enhancement.
And, yeah, this is something I'd work on after this.
Let's just move it to… To do.
I don't know how this niche triage label works. Semantic convention… oh, I see, I see. Maybe if I just remove it… Oops.
Oh, hopefully that was the right way to do it.
Okay, what else?
This is one I filed in the Python repo, yeah.
It's basically just regarding, like.
A lot of… so the tool calls we have in our schema right now are any.
So when we convert them to… JSON, either in… Snapping them in attributes, spin attributes until we have the complex attribute support.
For doing the uploader thing.
In both cases, the tool call results, like function tool calls can return, you know, objects that don't get JSON encoded.
So basically the task here would be to just… In the absence of anything better, we could either drop the key-value pair, or we could… use, String or something like that to encode it, so… I'll… I'm already working on this, I'll see a comment.
**Alex Hall** 09:54 I don't think you should need Pydantic as an optional dependency in any situation. I think that if you get a Pydantic.
model, you should be able to just call the method on it.
**Aaron Abbott** 10:04 Yep.
Agreed.
Actually, Alex, So it seems like… the Pydantic does have, like, serialization code that spits out a string, but we wouldn't be able to use that with, like, the standard JSON, dumps function, right? We'd have to do, like.
convert model dump to dict, and then just let the… JSON module will handle the rest, right?
**Alex Hall** 10:31 I think you can either use… go straight to a string or other bytes, Or you can go to… like, Python dicks and stuff, which… Again, it's configurable that they either are or aren't JSON dumpable.
So you can say model dump mode equals JSON or mode equals Python.
**Aaron Abbott** 10:54 Yeah.
**Alex Hall** 10:55 But I think we're getting sidetracked.
**Aaron Abbott** 10:57 Yeah, yeah, we can talk about it later, but I agree, yeah, it would not need to be… we could just check if the model dump exists and call it.
Okay, session ID.
I feel like we've definitely talked about this one.
**Sergey Sergeev** 11:20 Yeah, bottom line is here.
**Pavan** 11:22 Yeah, I think there was a PR for this, but not an issue. And maybe everything sort of was supposed to be tracked via issue, so I just created it, and then… linked to PR. I know there's some sort of…
**Aaron Abbott** 11:37 action items, and…
**Pavan** 11:38 You know, feedback, et cetera, that, Was already given, but, yeah.
It's, work in progress.
**Aaron Abbott** 11:50 I guess I do this. I don't know, we'll see.
Oh yeah, that's no problem, I just marked it in progress.
Thank you.
Okay, safety ratings… I'm a little confused why some of these are showing up now.
Oh, I see, because there was a comment.
Alright, I will make sure I'm doing the right thing with the triage after the call.
So, maybe I'll just go through this later. I'll read that doc, because I'm actually not super familiar with it, but yeah, this is… this is something that I think we discussed. We'd probably want to add it to, like, our part types, so… Yeah.
This one is similar.
Yeah, just moved in need triage.
Okay, that's all from the project board, I intro new members.
Do we have anyone new on the call who wants to say hello? It's totally optional.
Not sure if I see any new names.
Oh. Hey, Marcelo.
**Marcelo Trylesinski** 13:06 Hey, man, how are you doing?
**Aaron Abbott** 13:08 Good to see you here.
**Marcelo Trylesinski** 13:10 Yeah, just passing by.
**Aaron Abbott** 13:15 Okay.
Cool, do you want to give an intro or anything, or just keep moving along?
**Marcelo Trylesinski** 13:20 Sorry, what do I need to do? I'm not familiar with this.
**Aaron Abbott** 13:23 Oh, it's totally optional, and you could, you know…
**Marcelo Trylesinski** 13:26 I'm Marcelo. I work with Alex.
I'm working on AI Gateway as well now, so… just… Listening stuff here.
Is that it, the kind of the stuff you're expecting?
**Aaron Abbott** 13:41 Yeah, yeah, that's great. Glad to see you.
**Marcelo Trylesinski** 13:44 Okay, cool.
**Aaron Abbott** 13:46 Cool. Anyone else wanna say hello? Anyone new?
Alright.
Okay, cool. We'll go on to the next section, which is open PRs.
This first one is still open, it's from Drew.
Yeah.
This is OpenAI embedding instrumentation, Okay. I think this one just needs review.
Looks like Ricardo is reviewing already, so I will… Yeah, also just for anyone on the call, like, it's super appreciated if you… if you want to review, in addition to just, like, semantic convention PRs, some of the actual instrumentation efforts in Python, like.
Even if you don't have green checkmark over there, it's super helpful, and gets you on the way.
to being an improver in the Python SIG, but, just also some signal from, like.
AI experts, people who know stuff about this and are involved in the conventions would be super helpful. So, yeah, anyone's welcome to review these PRs.
You know, like, do the checkbox and everything, checkmark, yeah, but I'll ask Ricardo to take another look.
Cool, next one is for me… oh, sorry, not for me. This one is from Keith.
Looks like Dylan… Left you a review, earn approval.
That's great. Did you want to say anything about this, Keith? Just asking for more…
**Keith Decker** 15:45 Looking for more approvals. Looks like I need to do a main update as well, but…
**Aaron Abbott** 15:55 Okay, sounds good. Was there anything, outstanding, like, questions-wise, or just waiting for approval?
**Keith Decker** 16:04 From you, there was a comment about some of the testing, I couldn't get… the actual comment you had to work, it would not capture spans with that way, other than that.
I think Collins and I took this offline for this.
Sorry, Pablo and I took this offline to talk about… Immutable stuff.
I guess I'll update that comment about that.
**Aaron Abbott** 16:30 Okay. Cool, do you want me to… I can just update right now.
**Keith Decker** 16:33 Yeah, that works.
**Aaron Abbott** 16:35 Okay, cool. Yeah, I definitely owe you a review. Apologize for that. Try to… try to take a look today, or just merge with Dylan's approval, probably.
But yeah.
Cool.
Sorry, I don't know why I marked this one out. This is the one I wanted to talk about.
Okay, this is the one for me.
Yeah, thank you for the back and forth, Alex. I saw your last comment.
was regarding, yeah, URI and file part.
Instead of having, like, the one-off embedded in here.
I'm happy to do this, I just… Could you share, like, a little more about the motivation? Is it just to kind of keep things consistent, make it easier to use in Python, something like that?
**Alex Hall** 17:29 Yeah, I think it's weird that… Yes, blot parts are separated from these two parts.
By one method, and then these two parts are separated by a different method.
It seems confusing, actually.
I don't see any reason.
**Aaron Abbott** 17:46 Okay.
Yeah, I… I guess… I guess the… the goal was to just kind of… address Marcello's comment, which was more directed at just, oh, they should be mutually exclusive, I do see what you mean. I guess my only concern is it's a little confusing.
Since they both represent, like, remote reference files, to have one that's called URI and one that's called File 1, like, the files API, for example, in OpenAI, or Anthropic, or whatever, is kind of like a… it just gives opaque IDs back, but it's not like a general-purpose file storage. It's more just like a… Upload this piece of context for reference later sort of thing.
But…
**Alex Hall** 18:33 It could even be file ID.
Like, the type could be file ID.
**Aaron Abbott** 18:40 Yeah.
**Alex Hall** 18:44 It could just… fall back to the generic part, like, I don't even know if… Or what a convention achieves here.
**Aaron Abbott** 18:54 Something like this.
**Alex Hall** 18:57 No, no, no, no, I think the URI part should still be URI part, like, if there's a URI, Yeah.
Whether or not it comes from something called a file, whatever that means.
**Aaron Abbott** 19:11 Okay, yeah, just to be clear, like, the URI might not be a public URI, right?
**Alex Hall** 19:20 Right, but it will be a URL either way.
**Aaron Abbott** 19:23 yes, true, true.
But I know, like, some… so, for example, like, Gemini, you can call with a public URI. You can also call it with, like, gsutil URIs.
And… it knows how to handle those schemes, but in a sense, the gsutil one is kind of like the file ID, except that there's just, like, a well-known format for specifying the URI with the GS scheme.
**Alex Hall** 19:55 Another minor thing is that the PR still doesn't mention what to do in the case of… a data URI, if it's, like… if we think that it's best to convert it to… A blog part, maybe you should say so.
If either is fine, maybe you should say that.
**Aaron Abbott** 20:17 Okay.
**Alex Hall** 20:20 But that would be one more way in which you can have a UI pass that is very much not an uploaded file.
**Aaron Abbott** 20:26 Okay.
So just to be clear, like, if the… if the text in the parts is a little more clear, you don't really care which way we go. I mean, I would definitely prefer to put the bytes in line.
**Alex Hall** 20:41 Yeah, I mean, my first concern is just that… I'm not sure what I'm supposed to do when… if I was to instruct this.
**Aaron Abbott** 20:53 Okay.
No, I see what you're saying. So would you prefer… yeah, I could put down here, like, in the URI, I could put, like.
**Alex Hall** 21:04 I think I agree with you that a blog part makes more sense.
Yep.
**Aaron Abbott** 21:20 Okay, cool.
That's really helpful.
Maybe we don't need to mention anything about the data URIs here, then. We'll just mention it down here.
Okay, cool. I will address those follow-ups.
Anybody else have thoughts on this one before we move on?
Alright.
Cool. Then we're on the regular agenda items. Sergey, you're up.
**Sergey Sergeev** 22:04 Yep.
**Aaron Abbott** 22:05 documentation roadmap.
**Sergey Sergeev** 22:06 Just in general, it looks like, we don't have. At some point, I think Lyudmila did this table of instrumentations, By popularity, just by vote from this group, what's most needed, and etc.
probably we need, to create, just GitHub.
Github issues for each instrumentation, and just to track what's needed for each.
Instrumentation. We have a lot of people who want to contribute.
Does this work?
It would be helpful if we could adjust GitHub issues.
**Aaron Abbott** 22:53 Okay, you're talking about the spreadsheet we had before, right?
**Sergey Sergeev** 22:56 Yeah, yeah, yeah.
**Aaron Abbott** 22:58 Do you… do you happen to have a link to that? I can't find it right now.
**Sergey Sergeev** 23:01 No.
**Aaron Abbott** 23:02 Yeah.
**Sergey Sergeev** 23:03 Test.
And, in general, it feels like we have a lot of work happening in pull requests, not everything tagged in… GitHub issues, we can probably… if it's okay, I can probably go over it, before the next call.
And propose some of the items to be filed.
**Aaron Abbott** 23:28 Yeah, yeah, definitely. That would be helpful.
I would say… Like, you're not planning to make, like, an issue for every, possible, like, open elementary instrumentation, right?
**Sergey Sergeev** 23:43 Yeah, depending on how it goes, Biff, if we can… Basically… Transfer those donated by TraceWhoop.
But it gets into my next topic, so how do we do it?
**Aaron Abbott** 23:59 Okay, maybe just… Regarding…
**Sergey Sergeev** 24:04 Just for the frameworks, by framework, probably, we can.
Put some of those issues and prioritize it.
**Aaron Abbott** 24:23 Okay. Yeah, sounds good. I would… I would just be a little cautious about you know, overwhelming us with the issue tracker, but otherwise, it sounds… sounds great. It's good to have stuff tracked. If you want to do, like, a root issue with, like, a… Checklist or something like that, it might be.
If you want to have, like, absolutely everything from the spreadsheet, I think that would make sense.
**Sergey Sergeev** 24:46 Sounds good.
**Aaron Abbott** 24:49 Okay.
**Sergey Sergeev** 24:52 Yeah, I can't share for the next step.
**Aaron Abbott** 24:54 Yeah, yeah, please.
**Sergey Sergeev** 25:06 Again.
So, in general, It's just an evolution of the design for 2018, and I was trying to wrap my head how to best share with the community what we're doing, why we're doing, and how to represent it with the minimal cognitive overhead.
And just write down some of, the scenarios we want to track with the CTOGEN AI function.
And basically, we want to support, V12 is instrumentation, development, and in-house framework instrumentation, so when somebody, for example, built their own AI agent framework, and they want still to use, telemedicine and semantic conventions, so again, this is, coming out of, GenA… out of, UTL GenA, which already, which we already have, so, something like, data types, for AOM on vacation, or agent on vacation, and handler to submit it, can help those third-party.
instrument… third-party framework developers. But in general, we want, that utility to support standard SMIT convention telemetry. They want to switch, content from span attributes to events, basically controlled by environment variables. So, built-in evaluators, I understand it's a bigger topic, we just want to make it pluggable in the form of some callback. I believe we discussed some pluggable callbacks.
just overall, so that's the approach I took in this, development branch.
And again, guagabol.
I have third-party packages, so specifically, .6 and 7 for this group, so, If we want to switch it to the current trace loop telemetry forever.
And, make it pluggable, so if you install a package which… Basically, yes.
produce this telemetry. It should be easy to do, and this is how we can migrate, TraceWhoop existing instrumentations, and basically to support, some backward compatibility for the time it takes, to switch back-end implementation on TraceWhoop.
to fully follow semantic convention. And, to add, some third-party providers, like Splunk, for example, to produce some of the telematy in the format we need for backend purposes and etc.
And, again, it's, that development branch, where I tried, to build, those things, but also I wanted just to go over high-level structure.
And you can ignore evaluators, it can be just an external package callback, which integrates using callbacks.
But, the key is just… The files.
Ian.
OpenCLM at the UT with you, Dev.
UTHNA, where we have, Specifically, we have, specifically the JNA types.
the handlers… And, additionally, they already have, A broad hook which implements some of the functionality which shows and demonstrates how we can Add some extra… Functionality to all of the instrumentation libraries at once.
But emitters also built some infrastructure to basically… to, add pluggable Emitters for specific, telemeted type.
And again, I tried to extract some very high-level information, about, interfaces, we introduce an APIs. And, Some of the high-level ideas about, How, a consumer of this, utility library can control, behavior.
Oh, wait. Yeah, go ahead, Taryn.
**Aaron Abbott** 30:05 Yeah, yeah. So, I think we've discussed this a little, like, a couple times, and Kind of refined the approach a bit.
I'm still… like, I also had to leave the Python thing a bit early, so I'm not sure where the discussion was.
But I kind of want to make sure we're on the same page with the, With, like, the requirements, that kind of informs the decision and the level of complexity we need.
So, so yeah, like, specifically, I was wondering… Like, it would be good to have I know… I don't think Nira's here, but it would be great to have somebody from TraceLoop kind of chime in.
**Sergey Sergeev** 30:45 Yeah, yeah, yeah, how we do it. Yeah, unfortunately, Nir is, on vacation, so he's, seriously, he promised to.
**Aaron Abbott** 30:56 Review it, as soon as he can.
**Sergey Sergeev** 30:59 But I didn't hear yet from him.
Again, I think it's absolutely the goal to make sure that the converge on semantic convention Very quickly. But.
**Aaron Abbott** 31:14 From…
**Sergey Sergeev** 31:17 just realistically, I think it always will be some gap between semantic conventions, new stuff people introducing, etc, or some custom, Customer requirements of the backend, so… Most of the telemeters should fall within the convention, but again, it should be possible to tweak it a little bit.
Without, hardcoding to… Actual telemetry produced, especially if you have some of the foyers.
**Aaron Abbott** 31:49 Yeah. Is that telemet.
Yeah.
**Sergey Sergeev** 31:51 At this point, I shouldn't.
**Aaron Abbott** 31:53 I'm, like, a little nervous about, you know, I don't think this is well-charted.
territory and open telemetry, just generally speaking. Yeah.
**Sergey Sergeev** 32:01 Yeah, that's why I'm thinking about just introducing some basic functionality again. The way we do it now, just for semantic convention telemetry, it should be very straightforward. You just have it, As we do… Currently in that, utility.
package… The biggest difference is just to add some extensibility built-ins, so specifically some generic old work, so… The way I was thinking about it, just to introduce the completion callback, so when you, finish creating… finish, reporting, one of, the GenAI data types, just to edit, Basically, to make a call to some completion callback, and that completion callback can follow standard emitter interface.
Let me find, the gripper.
**Aaron Abbott** 33:11 if we have, like, a… just, like, a super generic… like, I like the generic.
mechanism, right? Do we still need to introduce, like, emitters and even, like, subtypes of emitters?
**Sergey Sergeev** 33:22 Some types of emitters, we don't have. We need to introduce some life cycle, so basically, you cannot, You cannot create, spans. You can create metrics or events.
before you created Span, without the span context. So, we need to call, basically… we need to have, basically, some telemetry-focused emitters. It's… But it's a very simple interface, it's nothing complicated. So, again, everything should support something like a base, Gen EA type.
which is the base type for all of the rest of the types, like, oh, I'm on vacation, and etc.
So, the interface will be very simple, and each emitter, third-party emitter, can do whatever.
It wants with the telemetry, so the simplest option is just to replace the semantic convention in the middle.
Viv.
TraceWoop Compatible in Italy, for example.
And use utility functions to set most of the attributes to semantic conventions.
**Aaron Abbott** 34:34 That's.
**Sergey Sergeev** 34:36 an easy… Not where he is.
hierarchical, dependency… Cost-dependency approach.
So all the functionality needed is basically to have a way to compose different emitters for span metic and content events, and the use cases, four specifically are traceful background compatibility and Splunk, custom, evaluation result emitter.
I also heard, from, Amazon team… oh, Amazon… sorry, from Microsoft team that, they may need some custom telemetry for a specific use case.
So, again, the key goal is to separate instrumentation from telemetry, so we should not maintain all… Of the instrumentation parts, just for the sake.
of slightly customizing utility, so… and again, we want to converge on thematic convention in the end, but, Not O… The backends will be able to do it.
Or want to do it.
I think, just focusing on semantic convention again, but just to provide this completion callback, Po, evaluators.
And some way to put your emitter into this life cycle, I think, can be simplified significantly, so… it's, if you… yeah, I will appreciate if you can review just this document, and provide some feedback, and again, that branch, we have it, working here.
Again, more stuff needs to be improved. For example, Metic.
provider should control. If you set Medic provider, it should control if you emit metrics or not.
And so on. It shouldn't be controlled by environment variable.
But overall, what works in this branch, so basically, we have a different packages.
And until you install this package, you don't get this functionality. Until you install this package, you basically get a semantic dimension telemet.
And you can control, just the environment variable if you want to have, conversation, if you want to have content messages on a span attribute, or if you want to have them in events for in semantic convention.
That's fully controlled just by, this package, OpenTelemnity RTM AI.
Again, it's a development folder.
But if you want, for example, to bring your own emitters, or if you… Want to plug in some evaluators.
V. Ken.
Just make it extensible and completely remove.
from the scope of this utility. So, all evaluators need is, a very simple, callback DPA.
So, completion callback on completion… You just send the invitation, and this is a non-working call.
**Aaron Abbott** 38:25 Sergey, how can we… it looks like this is, like, in a branch or something, how can we give a review on this?
**Sergey Sergeev** 38:33 Yeah, it's, so I think I can just move it to a Google Doc.
And we can comment again before we even jump to the court and et cetera.
The concepts, and, I just wanted to emphasize that, The use case is, seems, real.
I think, and I heard again from… Microsoft, and, I, I will be curious about, what the rest of, AI-focused observability.
companies.
like, Pydensic, thinking about this approach, we would be helpful.
for you, Alex, for example, to have that, instrumentation, why by separated from telemetry, so you can… are you fully satisfied with semantic conventions, or do you have some gap between semantic conventions and what you use?
**Alex Hall** 39:41 We definitely add things other than… That's in semantic conventions. One example of what Would be useful to everyone would be, costs.
actual… Yep.
monetary values.
And I can imagine that being a generic thing that gets plugged into… Virginia utils.
**Sergey Sergeev** 40:00 Yeah, it's, again, even to demonstrate to communities that it's helpful, it might take some time. For example, we are thinking about the same, like, cost and, agent, specific, medics, N2.
metrics for duration and token usage. And the best way to demonstrate it, you can just create a package which is easily installable and brings that functionality, which is not yet semantic convention.
But at least you can deliver it to the customers, to your customers.
And, VCAN… argue about it's helpful for a broader group. We can make it semantic convention.
I think it's, just… Fuse that gap between what we have in semantic convention, and what people actually use it. And it may be just your use case.
And nobody else may need it, but it's not a reason for you to maintain all the instrumentation of embers.
Again, that's the whole motivation.
I'll move it to the Google Doc and share in the channel.
And I will appreciate your feedback. And by the way, we're here in Cisco's Puanc, so we really appreciate your reviews and etc. We are trying to be more helpful to the community as well by… Starting to review your pull requests and etc, but… It's… it takes some time. They will get better.
**Aaron Abbott** 41:49 Okay. Yeah, I think putting it in a Google Doc, like I know we had a previous iteration, that sounds great.
I would definitely like to see more of, like, a requirements section. I think that would be, like, not just because I… not because I want to be dubious of the project, but, like, I want to make sure that we're capturing the right stuff, and, you know, like, from Google's side, Podentic's side, I imagine some of the goals are a bit different.
I, I also, like.
we… we… we do want the conventions to be adoptable by everyone. I think that's, like, a… a big part of what we did in the last 6 months to a year, like, we went back to the drawing board on some of the prompt response logging from feedback from, like, from Pydantic, from Arise. We came up with something that I hope works a little better, and I hope some… that everybody could adopt, because… You know, like, if the conventions aren't adoptable, then they're not… They're not great, right?
So… Okay, thank you so much for the effort here, Sergey. I'm looking forward to the doc.
**Sergey Sergeev** 42:54 Yeah, I appreciate your reviews.
**Aaron Abbott** 42:59 Okay.
Great.
Okay, we have one more agenda item.
Michael, you're on?
**Michael He** 43:12 Yeah, hey. I think, this was discussed briefly in the last meeting, where, currently the spec for invoke agent spans just support the client kind, so… Kind of wanted to just, like, loosen the wording to… also maybe support, internal and service mankind, so… yeah, I raised the PR, just, wanted to bring it to the group in case, there's any feedback on, like, the wording or anything. Yeah.
**Aaron Abbott** 43:38 Yes, thank you so much, I was looking for this, so thank you for bringing it up.
**Michael He** 43:42 Yeah, I think that, yeah, there's some comments, so I'll try to get to those today as well, along with any feedback that comes in.
**Aaron Abbott** 43:50 Okay. Yeah, I think… I think Guangya is… was the original author of… the convention, so I'm glad to see the review here.
Yeah, I'll try to take a look, too, and… Anybody else who's around, please take a look.
**Michael He** 44:06 Alright, sounds great. Thank you.
**Aaron Abbott** 44:08 Yeah, thank you.
Okay, great.
We made it to the end of the agenda.
Unless anybody has last-minute things, I think we get, like, 15 minutes back, so…
**Sergey Sergeev** 44:28 Just a quick question, so we have already… I think, a woman vacation, type in.
OT function in OTH and AI, so probably we need to switch.
length chain.
Again, drafts into it.
And to… Michael, I think you have that, pull request about, WangGraph.
Isabel.
**Michael He** 44:56 Yep.
**Sergey Sergeev** 44:58 Can we set up a session just to… to see what we would take to switch it to using also generate a library?
So we need agent invocation type defined, and setting.
**Michael He** 45:12 Okay, yeah, yeah, that makes sense.
Yeah, we can set up a meeting. I can, probably ping you, offline.
**Sergey Sergeev** 45:20 Okay. Sounds good.
**Aaron Abbott** 45:25 Okay.
Great, well, thanks for joining, everyone. See you all next week.
**Michael He** 45:31 Thank you.
**Marcelo Trylesinski** 45:34 You… can you…
**Aaron Abbott** 45:35 Later.
