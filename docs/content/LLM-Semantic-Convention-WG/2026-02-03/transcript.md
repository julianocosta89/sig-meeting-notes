SIG: LLM Semantic Convention WG
Date: 2026-02-03
Duration: 123 minutes
Zoom Recording URL: https://zoom.us/rec/share/e92TaOq5xFMbRxlPQ4tqw4OSoOZBJff7LU4Th5NfvevSVaeiP31lPJfmCZyNejd2.tlQj_7dNn5q2wXzQ
============================================================

## Zoom Recording Transcript

John McBride 00:04:38 Hey, everybody.
Looks like, Aaron and a few people will be late, so…
We can either sit around and wait longer, or get started.
neil yashinsky 00:04:52 Hey, John. I vote for either. Inspired by the dogs in the background, I'm kind of a fan of lying around and waiting, honestly.
John McBride 00:05:03 That's all they do all day. It's great.
neil yashinsky 00:05:06 But also, I would like to, suggest, like, they serve as role models, in a sense. Like, they get to be… we get to observe them and take inspiration by them.
John McBride 00:05:16 Yeah, there you go.
neil yashinsky 00:05:16 Not work per se, but, you know, value indirectly, or something?
John McBride 00:05:25 Okay, we'll give it a few minutes, there's not really any…
Too many, action items, so come and see who else shows up.
shuwpan 00:05:38 While we are waiting, Neil, I'm just watching the, what VLM, like, the Alibaba people doing for the VLM. I saw that you were sort of in there as well, so I'm just wondering, is there any collaboration happening, or we're just kind of waiting?
neil yashinsky 00:05:55 Oh, great question! I was wondering about that very same thing today, I mean.
shuwpan 00:05:58 Yeah.
neil yashinsky 00:05:58 So, I've been, I've been, like, I had, I had two parts of my project that were poorly separated. One's the specification, and one's the, the, you know, if you will, the reference implementation, technical.
shuwpan 00:06:13 Bye!
neil yashinsky 00:06:14 And I only really got it… it's not fully separated, but it's, like, 90% separated out. And so I was just a little bit shy, because, I don't know, my… my…
Well, for… I'm a human, you're a human, you understand why people get shy, but yeah, so I think now we're just… I think I'm ready to really start pointing people to the repo, not because it's amazing and,
you know, relevatory or, you know, insightful yet? Perhaps it is, but just as a…
you know, another source code, or what have you, a framework, I guess both at how to solve problems like the ones that we're talking about. And so, I feel like I'll probably learn a lot more from the Alibaba team than they will from me, but, you know, I… stranger things have happened.
shuwpan 00:07:02 Yeah, so… did you talk to them, or you just had the repo, haven't talked to them yet?
neil yashinsky 00:07:09 I would say we… we… like, on the first session in particular, I mean, I think you saw the notes, so I would say our collaboration hasn't gone beyond what was really documented in the notes.
shuwpan 00:07:18 Oh, I see.
neil yashinsky 00:07:19 But I… but I do feel like the stage was set, if you will, for more…
shuwpan 00:07:23 Oh, I see.
Alright, yeah, just let me know if, like, you people, like, hang out together and maybe ping me?
neil yashinsky 00:07:31 Oh, 100%! I'll ping you. In fact, if you're interested, I can put on some time together later in the week, and we can just, like, throw some time out for anyone in the SIGS or whatever to come and drop by and talk a little bit more.
shuwpan 00:07:44 Yeah, sounds good. Thanks.
neil yashinsky 00:07:46 Yes, great, and can you just ping me in the chat, so I have your email address, and I'll also find you on Slack, too, so we can connect there as well.
shuwpan 00:07:53 Sure.
John McBride 00:08:30 Alright, well, I'll kick us off. Let's, get started. I don't know, without the…
people leading most of the efforts, I think some new people here. Feel free to shout out if you're new, or, anything interesting you're working on. Otherwise, we could start with this first security spec.
Right here.
nagkumar 00:08:57 Yeah, cool. I can start off the security spec. So, I brought up this last week as well, so, there have been a few changes, from last week, just one wherein
the target types, I think I still have to push that up. Target types was, enum, now I'm changing it to, like, a non, not a freeform string. So, you can target, let's say, MCP, or A2A, or anything.
else that would come in into the future and not limited to just these. So that's a change. But yeah, other than that, a reminder for everyone to review it. Let me know what you all think about it. Feel free to comment on it with more changes if you want.
That's… that's pretty much it. Thank you.
neil yashinsky 00:09:53 Thank you, College.
Nabkumar, if I'm pronouncing that right. I'm really excited about this. I think this is, really everything I love about, like, this SIG, and why I'm here. So, yeah, I'll be happy to, you know, offer a few more,
Feedback later.
John McBride 00:10:11 Is there, PR?
nagkumar 00:10:13 Yes, I can drop a link in the chat.
John McBride 00:10:16 Okay, perfect.
It's probably… probably easier than your, your branch, right?
Cool. Let's see what we got, next, Anthropic Streaming and Async Instrumentation.
Surya, you wanna speak to that?
Surya Teja 00:10:36 Yeah, sure, sure. So, this, these are the two PRs which add instrumentation around, Anthropic's Python SDK.
So, the, first one is about the streaming SDK that is being instrumented, and the second one is around the async methods that are being instrumented. So, pretty much, it's…
Capturing all the… Attributes that we have in semantic conventions, and trying to put them together.
Nothing new in this one. I just need some eyes on this to push it, and then I can,
Work on releasing a new… Version from the… OpenTelemetry team site for, anthropic SDK.
John McBride 00:11:33 Very nice.
What did you say was worth, calling out? It was… it was some new…
Mostly just in the Python SDK stuff.
Surya Teja 00:11:45 Yeah, it's mostly a Python SDK, so if these two PRs are reviewed and merged, we are going to have some visible instrumentation around the AnthrofX SDK with open telemetry semantics, so right now, OpenLelementary is only the one which is capturing those.
So…
John McBride 00:12:05 We worked on.
Surya Teja 00:12:08 getting, using the name along with them, so if these two are merged, the next thing is really cutting a release and releasing it in PyPi so that people can use this.
John McBride 00:12:20 Nice.
Okie dokie, great.
Anything else there? Or just call to action to review?
Surya Teja 00:12:36 The call to action is just a review, nothing else.
John McBride 00:12:40 Okay.
Cool.
Surya Teja 00:12:41 So, let me throw this around.
Currently, I only have one person who is going to review the Anthropics SDK, if there are any bug fixes or anything. So the last time when I broached this idea, no one came forward, but since we have a huge crowd over here, is anyone else interested in taking the responsibility around
reviewing PRs that are coming towards the anthropic instrumentation, I can add them as the… add them to the list of reviewers, and we can share the responsibility.
neil yashinsky 00:13:14 So you're probably not familiar with the, American television show, Welcome Back, Cotter, so I'll spare everyone, but, yeah, I would love to, so feel free to, you know.
Surya Teja 00:13:26 Yeah.
neil yashinsky 00:13:26 Connect.
Surya Teja 00:13:27 Sure.
neil yashinsky 00:13:28 However best.
Thanks.
John McBride 00:13:41 Great.
Aaron Abbott 00:13:42 Hey everyone, sorry, sorry I was a bit late.
Thanks for…
John McBride 00:13:45 air.
Aaron Abbott 00:13:46 John, you can keep going by all means, please.
John McBride 00:13:49 Sure.
Yeah, we've just been going through a few things,
I don't have great context on some of this, so if, Aaron, feel free to jump in. Next item was mine. We recently open-sourced a proxy, that's going to eventually emit
client spans for AI agents, for OTEL, but my main question was.
what are the state of the Go SDKs, or if anyone in this group is maintaining those? Because they seemed a little… a little rough.
Aaron Abbott 00:14:24 Cool. When you say Go SDKs.
Do you mean, yeah, what do you mean in particular?
John McBride 00:14:31 When I looked… There was…
Yeah, OpenTelemetry Go, but it didn't seem like there was…
I don't know, maybe I was fumbling around and not… not getting what I needed, but… Aaron, feel free to point me in the right direction.
Aaron Abbott 00:14:49 Oh, no, I mean, that looks like the right thing. I think it should be in a really good state, actually.
John McBride 00:14:55 Okay, okay.
Aaron Abbott 00:14:56 They might not have logging GA'd, but for trace and everything, trace and metrics, it should be
It should be great. Was there any specific, issues you faced?
John McBride 00:15:06 Just on some of the newer stuff, like some of the tool calling stuff, I think maybe it was the logging pieces that…
And some of it is, too, just, like, figuring out how we'll integrate, so…
Yeah, but is there… I guess another general question, I guess this kind of goes into some of the Python SDK stuff, too. Do those… do those SDKs have separate working groups, or are those generally more in OTEL, segmented by…
Yeah. Purpose, okay.
Aaron Abbott 00:15:34 Yeah, so there's…
there's kind of, like, semantic dimension working groups like this one, or SIGs, depending. I'm not even sure what this one is at this point, but…
For pretty much every language, there should be a SIG.
Excuse me. Let me share you the repo, and there's…
there's a community calendar, which you can add to your Google Calendar, or you can just view it online, I believe, and that should have
all the schedules, so I think… so the Python seg, for example, is on Thursdays at noon Eastern.
John McBride 00:16:06 Okay.
Aaron Abbott 00:16:07 And yeah, you're… everybody's welcome to join just like this one. I encourage you to go… go to those if you have specific questions.
John McBride 00:16:14 Yeah. Yeah, I appreciate that. It's always… it's always fun navigating these landscapes of, working groups and stuff, but yeah, that should… that should unblock me.
Aaron Abbott 00:16:23 Okay, cool, and yeah, thanks for… thanks for sharing. This is pretty cool, I think…
It's great to see people adopting the conventions, I assume… I assume that's what you're doing.
John McBride 00:16:35 Yep.
Aaron Abbott 00:16:36 Yeah, I'll take a look, dude.
John McBride 00:16:40 Cool. Next item… Ongoing PR Imple implementing session ID in Gen AI utils.
Pavan 00:16:51 Yeah, so I think we have been working with Splunk, essentially, to
implement session ID based on, like, the feedback that we received from Ludmilla in the last call. The, you know, repo that you see is probably, you know, like, a clone of the OpenTelemetry Python contrib, but, you know, the one that Splunk actually actively maintains.
And what we do there is, like, probably provide various different ways in, you know,
figuring out how the session ID, so to speak, can be set, how can it be, like, propagated between, like, you know, the agent or the trace boundaries, so to speak. And yeah, I think, based on the feedback that we received on this, like, draft PR,
We would be, like, probably, happy to, also, like, make some improvements in, sort of, bringing in, like, the different
agent-to-agent protocols, you know, like, for example, A2A, specifically in showing how the session ID could
be propagated through the baggage API? And, you know, how could it be set in the metadata so that, you know, the agents can seamlessly just communicate to one another, but at the same time.
You know, have, like, a session umbrella that sort of tracks the multi-turn conversations, user sessions, and, like, different workflows,
for that.
user interaction. So…
I think we would be, looking for some, feedback and or a review on that PR, so, please feel free to just
Take a look and see if that is…
Now, what you had in mind as well.
John McBride 00:18:54 This is, this is very interesting. When I was last playing around with Gastown, the way that did it is it would…
just put it in a SQLite database, those, like, cross-agent sessions, and it was pretty janky. So that… that would be an amazing unlock.
Anything else on this? Go ahead.
Aaron Abbott 00:19:20 Yeah, yeah, Pavin, is there anything blocking opening, like, a PR to the actual contriburb rep repo?
Pavan 00:19:27 I think, we are basically having, like, a bunch of the different Gen AI, you know, utils,
Components that probably hasn't been…
fully pushed upstream, if I'm not wrong. I know, like, several Splunk folks are actually on this call who can probably give some more context, but, the… some of the handlers, some of the various Gen AI types that, you know, like, we have been working on.
has been on the Splunk clone of the contrib, but, you know, I can probably double-check and see if they have all been pushed upstream, and if so, I think we can just open a PR within there. I mean, in upstream itself, so…
Aaron Abbott 00:20:16 Okay, because if I understand right, there was… is this, like, a prototype, or is it,
Is… is there instrumentation, like, updates to the… to the GenAI utils?
Pavan 00:20:28 There is some updates to the GenAI utils, but, like, what we are planning to, like, sort of show is how easily this could probably be, utilized by the instrumentation SDKs.
and, you know, like, how some of the existing instrumentations out there actually use it today. So, I think in that PR, you will probably see, like, quite a lot of that, so…
Aaron Abbott 00:20:55 Okay, gotcha.
Yeah, I would suggest just, like, if the PR is really large, you can kind of open it as a draft in the repo, it's easier to get eyes on it.
But also, if we're, you know, looking to merge stuff, if we can split the PRs up into smaller chunks, would be really good.
Pavan 00:21:13 But I think… did you want to, like, do a demo or anything? Anything in particular you wanted to show?
I… I know Sergey probably helped quite a lot, in that PR,
I had some issues with, you know, like, just setting that up, but maybe I can aim for a, like, quick demo and a walkthrough in the next session, you know,
If that's okay.
Aaron Abbott 00:21:42 Yeah, yeah, please, I think that would be really helpful.
Pavan 00:21:45 Chuck.
Yeah, thanks, Vidhima. I think some of the, new, like, GenAI, you know, semantic conventions themselves that, Splunk is probably pushing with, like, the workflow and the agent invocation types are probably yet to be
Pushed upstream. So, some of the session concepts that we are building is probably, you know,
Building on top of that, so…
John McBride 00:22:30 Nice. Great work.
Yeah.
neil yashinsky 00:22:35 John or B, that was, Pavan, right? That's, we… it's actually a great segue, if we have a moment or two for me to, describe. I think you asked, even for folks who are new to the team, to maybe give a quick intro or whatever on what they're working on.
So…
John McBride 00:22:50 Yeah, I think there was one more someone added for… Please, please.
neil yashinsky 00:22:54 to go, except the very, very end.
John McBride 00:22:56 Sure, sure. Ankit, is this a PR request?
anksing 00:23:02 Yeah, yeah, thanks, Sean. So… Yeah, if you could open that, or…
Oh, I can check this, that's not the terrible.
So, just a quick context, so…
John McBride 00:23:22 You got some background noise as well, FYI.
anksing 00:23:26 I'll just stay busy. Get ready for school and other things.
So, Just a quick context. This is about, like,
Right now, in Genesis semantic convention, there is no good way to know whether you use responsive API for, like, a chat completion operation, or… or, like.
Or, use the Card Completion API or response API.
So, I wanted to, introduce, like, another attribute, which can help identify that, and this is based on some of the feedback I got in the PR, where I tried to use the operation name as responses, but there was feedback on
Even the responses API is kind of a chat completion API, just a different version of it, or a chat API, but a different version of it.
So, for those reasons, I am,
Suggesting to have a new property called genii.api.type.
And… which can be added, to identify whether it's response is set completion, or, like, old completions APIs.
Or any… That completion or inference plan.
Any… any feedback, or any… specific questions on that.
Aaron Abbott 00:24:47 Yeah, yeah, I get the need,
I feel like we discussed this at some point.
Specifically, we were talking about, like, how OpenAI API is usually implement… is implemented by a lot of vendors for inference. So, like, you can call, you know, Gemini or a lot of proxy servers with the OpenAI API.
So I think it's useful if we can… if we can agree on a name. I'm in favor of this, but…
I don't wanna… I don't have any initial impressions on the… on the name. I mean, it makes… it makes sense to me, but I'm not,
I think Lydmilla would be… Better at the,
being, like, an automatic winter on the name, because I'm not 100% sure, but I support the idea, for sure.
anksing 00:25:31 Got it, okay. Yeah, I think, yeah, I wanted to validate on, on idea here. Yeah, for naming, even I'm not a… I'm not very great at naming things, so I'm gonna leave that to, like, folks who have much more experience. So, yeah, but agree.
Yeah, okay, I'm gonna then tag, Lumen, I think she had some feedback as well, about the same thing, so, let's see.
Aaron Abbott 00:25:55 Awesome. Thank you.
Tao Chen 00:25:58 I have a question on Kit.
anksing 00:26:00 Oh, sure, please go ahead.
Tao Chen 00:26:01 Yeah, how is this different than the operation name?
anksing 00:26:05 So…
Tao Chen 00:26:10 Can we reuse the operation name?
Oh, okay, that was the original.
attempt.
Okay, Steven is also… okay.
Aaron Abbott 00:26:37 I don't know.
Tao Chen 00:26:38 C.
Aaron Abbott 00:26:39 I feel like we've already kind of broken this with the generate content operation, because that's… that's literally the RPC method for calling Gemini.
And it's… it's not really, in essence, very different from…
the OpenAI APIs is just, you know.
Maybe, maybe there's some small nuances, but, yeah, I can…
I think… I still think I'm in favor of the direction of having a separate attribute, but I don't… I can't say this makes 100% sense to me.
Tao Chen 00:27:12 Okay, yeah, I agree.
Okay, I have to pump text now.
Thank you so much.
anksing 00:27:16 Cool, awesome. Thank you.
John McBride 00:27:19 Does some of this get more confusing, too, where, like, V1 chat completion APIs can emit different MIME types? Like, I've seen…
like, Olama kind of gets weird with this, with local inference, where they can…
bring back, like, images on some of those APIs, and maybe that's not the target use case, but…
It's not always a chat, I guess is what I'm trying to say.
Aaron Abbott 00:27:43 Yeah, yeah, that's a good point. I think that is… that is one thing that the Generate Content API does do a little bit differently, I think, but…
Yeah, I feel like… Logically, honestly, I think of all these, I think of generate content.
The deprecated one, it's…
John McBride 00:28:02 Oh, I see.
Aaron Abbott 00:28:03 completion chat, like, in my head, they're all just inference. I don't really…
John McBride 00:28:06 Yeah.
Aaron Abbott 00:28:07 find a lot of value with having, the specific name, but having the RPC, like, method specifically seems really useful.
John McBride 00:28:16 Yeah.
Okay, sounds like the, yeah, it sounds like the action is to review… Yeah, request for review.
Kind of figure out the direction.
Okay.
Surya, looks like you had an item as well.
Surya Teja 00:28:56 Yeah, so the PR that I posted is from,
Minghui. He actually is adding some content capture stuff in Telemetry Handler, and it's already approved, so if someone can help
merging that PR, it will be helpful for adding the content capture stuff, on the Anthropic side, instrumentation side, too.
John McBride 00:29:37 Cool.
Aaron Abbott 00:29:51 Yeah, I think.
I think you pinged me to review this one, too. I…
I'm struggling to keep up with, in case people didn't notice, I'm struggling to keep up with all the reviews. So, like you mentioned a little bit earlier, yeah, if folks can help out on reviews, even if you're not, you know, green checkmark or, you know, code owners, it would be super helpful.
Surya Teja 00:30:11 Yeah, I'm sorry for troubling you, Aaron, on that one.
Aaron Abbott 00:30:16 No, it's okay.
John McBride 00:30:29 Well, I think that was it as far as PR asks. Neil, I know you had a demo you were interested in giving.
neil yashinsky 00:30:35 Boy, demo, I hadn't even pondered that word yet, but yeah, I mean, I wanted to…
a few minutes. Good kind of scary. No, thanks. So, what I've noticed in a few years in doing applications, and especially most recently.
Helping people keep the big ones up and running is there's this really big gap that exists between, like.
the project management tools that we use to create applications, and the observability tools that we use to monitor them, and this was most painful, and I think in some ways most relevant.
when you have to add observability, you know, to a new application, and at the moment, and please correct me if I'm wrong, because I'm still learning so much every day, I don't think there's a lot of ways to programmatically derive your observability needs, for lack of a better word, from your code.
Are, like, you know.
be able to extrapolate the… some of the key business context, like what was built, and who, you know, who was the requirements, you know, approved by, etc. So you can do things like set up notification policies when micro, you know, services…
go down, it's easy to tell where the stakeholders are in the business side of things. And so…
I started, really, with a way to basically do onboarding of applications, into observability tools, and it just kept
kind of… I kept coming back to this idea that there… this semantic layer was really missing between them, and so inspired by OpenTelemetry, I decided to… to just define one, what the heck, why not? See what happens. And so context score is the specification, I would say, like,
you know, a sibling, maybe, even, if I could be so grandiose, of OpenTelemetry, in that OpenTelemetry creates this great framework for how people understand applications, and it basically just tries to extrapolate that back.
As far as naturally possible, so that…
you don't have to… you can keep the two things together in a queryable fashion, and I think that's kind of the… one of the useful things is, be it either queries or dashboards, we have a lot of application observability
Tools in our toolkit, and they're readily available.
And they'll actually even benefit from kind of embedding these two things together. So I don't want to take up a lot of time, but I'm happy to answer more questions and continue on if people… if that makes sense. Oh, and the one thing that, sorry, that Pavan mentioned that naturally arose out of this and out of my work is that, like, keeping track of what agents are doing, how they're doing it and stuff.
became, in this era, the complementary need, right, for keeping… if you think it's hard to keep track of what people are doing, then boy, once you got, you know…
Dozens, hundreds, whatnot of agents out there, then, like, keeping track of what they're doing becomes, you know, both for people and humans, kind of reflected the same challenges.
And so that's why I'm like, oh, time series databases, get rid of a lot of markdown files, because those have, like, context challenges.
And the other thing was, like, the agents kept not knowing what infrastructure already existed, and so they would… they would create parallel versions unnecessarily. And so, I don't know how much of that will be readily available. I think that's a very common pattern that people will find.
So, yeah, so context core is the specification, and then I'm currently working on, like, how that works. I mean, there are implementation details in the repo,
But… but I hope… I thought it was a little bit, I don't know, confusing to have OpenTelemetry be both a specification and OpenTelemetry be, like, a sample implementation or something like that, just semantically, it seemed better to have their, like, two names.
What do you think?
Sound interesting?
John McBride 00:34:32 This is, this is actually something I was thinking about over the weekend with, you know, everybody going crazy about OpenClaw.
or whatever it's called now, because…
neil yashinsky 00:34:41 Yes.
John McBride 00:34:41 I mean, it's something I've wanted in, like, IDPs to provide.
neil yashinsky 00:34:45 Yes!
John McBride 00:34:45 when a JOT gets signed to have some metadata that's, like, who's the owner, like, or even if it's just, like, is bot, or something. But, I mean, I don't think OAuth supports anything like that, I mean, besides just the metadata inside of there. So it sounds like you're trying to tackle, you know, the idea that
there's an owner, or some service that… or some agentic thing has, like, an owner.
neil yashinsky 00:35:08 The, the, the project, yes. So, yeah, I mean, in some ways, this is, is an open cloud for work, and it's got integrated role-based access control as well.
So, like, you know, one of the things that I think came out about OpenClaude, and all of a sudden there was, like, this social network of agents, like, intercommunicating, and, like, there was very little to no guardrails. Who was it that had the guardrails project? I thought was so great. Nagmar, I think, right, had these guardrails up, and it's just like, oh, yeah, like, how are you communicating when you're… when one of your agents attempts to cross
That's the bollard or whatever, and, like, keeping track of that's probably a really important thing.
So yeah, I'm very eager to… like, I said, I think this, in many ways, like, it's a natural complement to open telemetry, and I have no interest in, like, defining proprietary anything, actually. The opposite, I think. We've got too… you know, a lot of them, that's what I love about OpenTelemetry, is we can create… we just… we just need to decide on the right naming conventions, if you will.
And so, yeah, I've got, basically, I think, just about all the OpenTelemetry standards covered, either here in Context Core directly or the application, and then, as well, the A2A, protocols and semantics, or what have you.
the GenA… Gen 2 AI, as well.
Aaron Abbott 00:36:26 Cool. I had a question, and it was mostly…
Yeah, in terms of, like, this SIG, you know, we mostly, we mostly work on
convent… like, conventions for GenAI,
stuff, right? Yes. I was wondering if you could share, like, I don't know, either learnings, or maybe the relationship, like, have you adopted hotel Gen AI semantic conventions? Yes. Do you have any feedback on it?
Like, new conventions, or just feedback in general on instrumentation and all that.
neil yashinsky 00:36:55 I think both, and that's what's exciting for me about the collaboration here is, is I think, like,
there's a lot of… you know, it's just the virtuous relationship of collaboration, and so I've been inspired by so much of what's already happening, and I really think that, like, the novelty is not in what I created. I don't think there's a lot of novelty there, it's more like, finally, just…
connecting these already existing, practically connecting things. And so, yeah, like, one of the useful things is the OTEL Blueprint Group.
like, I'm gonna naturally be really a great proto-candidate for that, because I'm trying to basically be a template for that work. And so, yeah, and back to your question, I think, Aaron, specifically about, like.
the Gentu AI specifications and providing feedback. I'd be happy to do that. I'm… I'm… I have had a lot of interactions in using them, and I, you know, I just described, I think, a few of them, were more like.
We're more like the,
the pain points that you will, you know, the conventions and whatnot will be solving through implementation, and so I think I'm, like.
Oh, maybe halfway ready to do that, in that, you know, before I can tell you about, like, the usefulness, and I can… I know they are, but I can't articulate them quite accurately enough to be, you know, useful and worthy of the folks on the call's time yet. But soon, I think, actually. Very, very… relatively soon?
Okay.
Aaron Abbott 00:38:25 Yeah, cool, I'm looking forward to that. I, I…
Yeah, like, you know, we've been pretty focused on stuff that's really in the weeds, so it's cool to see it together, stuff like…
How do we define a vendor-neutral format for inference across vendors, right?
neil yashinsky 00:38:41 Right.
Aaron Abbott 00:38:42 And then, you know, the… this is much more high-level, and we have, you know.
multi-agent, semantic convention working group and stuff like that, so,
Feedback, yep.
neil yashinsky 00:38:53 Excellent, awesome, thanks so much for the, for the questions and the opportunity, John, to chat about it.
Anyone else have a question? I guess, since we are… we're done, I guess.
Anirudha Jadhav 00:39:06 I just wanted to introduce and quickly, sort of maybe next time we can participate more, but from introduction standpoint, hi everyone, my name is Ani.
I'm a senior engine manager at Amazon. My team primarily works in OpenSearch. OpenSearch, it was in, like, Elasticsearch, Kibana, and now OpenSearch. It's a Linux Foundation project.
And my team primarily works in open source for observability. I think lately we've been working primarily on agent observability, agent semantics, and evaluations. I see some of my team members join, I think we'll have more members participate actively, helping out PRs and…
The goal for us is primarily going to be helping agent observability.
I think for that, a lot of things actively were getting worked on, and very mature. Some things in dev stages, so we'll have questions, and I think we can go through over there. From the other part, evals, I think evals is much more, like, un… like, it's there, but not as mature, and as talked about, so I had a question, and anything we can catch up next time, too.
Boop.
I'll pause over here. Any questions on… until now?
neil yashinsky 00:40:15 No, but thanks for the intro, exciting. I think, you, you really have some great,
descriptions of common concerns, I feel like. I'm still too new to the group to know myself, if I'm, like, biased or whatnot, or if these are the types of perfect things, but I do feel like, like, especially when you talk about, like, evaluation and whatnot, observability is, like.
I want to make sure I'm in the right place, but I sure hope this is in the right place, or it wouldn't be the first time I was more confused, yeah.
Anirudha Jadhav 00:40:41 So, from a observability standpoint, our primary objective would be to build, like… we have an open source tracing platform, open source logging platform, we support Prometheus metrics, and how do we weave the agent investigation and debating workflows in it? And from an eval standpoint, I saw the eval…
sort of, spec. And the eval spec currently covers eval as a telemetry out.
So, I think the question, and I wanted to ask the team, like, is there been interest in eval, kind of, requests in?
kind of interface in for eval. I know the evaluators and the next part of it is instrumenting. The output of an evaluation is what people are more interested in, but the eval in is also such a fragmented space, because if you're using an agent, you choose a framework A, like Strands, then go framework B, framework C. Everybody has their own evaluators and their own things.
And everything's exactly the same. They have an LLM journey, they have Type A, Type B, Type C, but the standardization between agents, or if you move between agents, the request in is…
kind of missing standardization, and that's where I wanted to get some feedback from the team, like, how do you guys feel about the in part of eval? And the out part, I did see the eval, like, gen AI evaluation.result.
I think there are some pieces that we can eval, like, add over there and improve and have discussions, but I'll pause and get feedback on the in part of eval, which may be not an implementation, but as an interface.
Helps.
Sergey Sergeev 00:42:09 Yeah, it will be really cool to see if you can describe, basically, what's,
your platform provides, in general, Agent Core and Bedrock. Overall, I think, provide quite a rich functionality, so if you can connect, basically that input request to your evaluator service, if you have it.
and basically, connected to a result. It will be cool also, for one distro, for OpenTelemetry, for GenAIV, implement, instrumentation site evaluator and other framework, and etc. And,
what we do, we also provide some metrics on the evaluator itself, basically cost, usage, and so on. Tokens used for that evaluation, and I think…
It will be very… Word, Vivian, yes.
Anirudha Jadhav 00:43:05 We're going more towards is, like, can this evaluator
or the evaluator SDK itself be part of an open source, like, in hotel framework, because then it has a common framework, and if others want to adopt it, they can adopt the interface and do something similar, and there are so many benchmarks coming up, and all these benchmarks do something, but I don't know how to align them, and I don't know if they make the same sense, and I can compare apples to apples at this point.
So, I think that's where the evaluation in… was the question, and if it makes sense, I'll put a formal proposal and we can discuss it.
Sergey Sergeev 00:43:36 Yeah, it will be very cool. And second, you have, session propagation, implemented.
Anirudha Jadhav 00:43:42 Yes, USA. Yes, yes.
Sergey Sergeev 00:43:44 I think it's worth standardizing, so we have a current proposal for the session from Paban. Unfortunately, I missed that discussion, but if you could
review and add your thoughts on this proposal, it will be super. Makes sense.
Anirudha Jadhav 00:44:02 That's it from me. Any questions, thoughts? Go ahead. Aaron, you had a hand raised.
Aaron Abbott 00:44:07 Yeah, yeah, welcome,
It's always nice to have new folks. I, I was… yeah, in terms of, like, the inputs,
I was wondering, like, isn't that kind of everything? Like, what do we need besides
pretty much all the conventions we have. Like, we have schemas for, kind of, what we expect portions of a trace to look like.
You know, we have prompts and responses and all that, like,
Was there something more directed that you were looking for?
Anirudha Jadhav 00:44:36 So, for example, if you are supposed to evaluate an agent, the evaluation libraries today lie in the proprietary land of multiple vendors, including non-vendors like Strands and other open-source APIs.
Everybody provides their own evaluators. So the goal I was trying to see was, if you are evaluating an agent.
are probably moving between agent frameworks. What is the standardized mechanism for you to compare? None exists today. What exists today is a trace. So you can output and emit a trace, and the output and emitting of a trace only gives you the signals out, but it still doesn't standardize, like, what are you evaluating against? It gives you half the story.
That's where I was going.
Aaron Abbott 00:45:22 Interesting. Okay. I, I kind of…
My… I'm not a traditional, like, AIML person, so I'm… you know, I might have a naive view on this, but I was thinking, you know, the input would more or less be, like, open telemetry protocol format, like, you know, the data,
Anirudha Jadhav 00:45:38 So, currently, there are SDKs, like Arise has its own SDK, BrainTrust, Phoenix, LangFuse, Strands, every library has their own SDKs, and all these SDKs are different, and there is no standardization in how people should evaluate. The output, they're trying to standardize now because of the GenAI evaluation.result. It's still not there.
Most of them don't have it. Some of them are starting to have it.
But then if you standardize the output, maybe everybody is just asked to standardize the output, but then you can't switch and compare against anyways. And my question was, would that input format also make sense to be a standard? So the input-output comparison helps creating benchmarks that can align themselves.
Sergey Sergeev 00:46:18 Yeah, I can provide a few ideas on what was the thinking on the side for this, and we have a basic support right now in the upstream open telemet, so what we're doing right now, we're trying to build a little bit, build up the story in our district, just serving our customers and validating some of our assumptions.
And next, we will try to propose more concrete things to upstream, and we have all the infrastructure, like Otil Gen AI, where we define types.
Basically for all the telemetry, agent, workflow…
inference, and so on. And those types should be the same for different frameworks, and this is the core idea, and this is the semantic conversion idea, so we defined.
Anirudha Jadhav 00:47:09 different types, and those can be evaluated. For agent, you can.
Sergey Sergeev 00:47:14 run those evaluations. Maybe just a little bit developing this way, so we can try to define evaluator itself, maybe a system prompt.
Anirudha Jadhav 00:47:27 Yes.
Sergey Sergeev 00:47:28 Maybe, what types it… can evaluate.
And what are the requirements? Something like input messages, output messages, and so on. And we did a little bit of that in Spoangedista, and I think we will be, now when it proves a little bit, with time, that it's working on our side, so we will be ready to propose
more specific.
examples to upstream, but if you can.
Anirudha Jadhav 00:48:00 Yeah.
Sergey Sergeev 00:48:00 basically…
Anirudha Jadhav 00:48:01 We're in a similar boat. We're in a similar boat. We haven't built and gone that far, but the question I ask myself is, like, why are we building one more SDK? Why are we building one more evaluator? Like, it should just be a standard. Everybody's building one now without sanitization, so, plus one.
Sergey Sergeev 00:48:16 Yeah, it's very hard to generalize things until you prove it quickly.
on your customer base, and I think the OpenTelematy community intentionally is a little bit more protective, so, you won't… Makes sense.
To find what is generic, and which makes sense to everybody across every framework.
Anirudha Jadhav 00:48:41 Okay, thanks, makes sense, Chris.
I'll, open an issue up for the discussion, and we can see how it goes ahead then.
But happy to help out, and thanks, everyone. Happy to be here.
Aaron Abbott 00:48:55 So…
Alright.
I think that was the end, right?
Sergey Sergeev 00:49:07 I see a few questions from, Neil, in the chat.
neil yashinsky 00:49:14 Oh, maybe just, like, contemporary chats or whatever. The discussion, I don't think I had anything that was, like.
I mean, I think I was just kind of… because I, I, was good seeing the, the, the details, that was just provided by,
Sorry, I'm gonna have to refer the names. Enruta, is that right?
Anirudha Jadhav 00:49:34 I go by Ani, I go by Ani, Annie.
neil yashinsky 00:49:36 Annie, thank you, yes, thank you so much. Yeah, and obviously, I'm so new to the idea of, like, evaluating, you know, agents and agent evaluations that I was just offering, like.
the perspective, dare I say, of, like, you know, there's the eval of the… let's call them the… the deliverables, the… what are they called, the artifacts themselves? And they… they had their own criteria, evaluation, or rubric, or whatever. And then I would also wonder about the secondary evaluation is really, like.
in the context of why the requester requested this thing. You know, if it's a… if it's an agent to find inventory, like, how… does the inventory that it finds actually get sold, or whatever, you know? Is it solving the business problem behind this?
Which I thought was really a great question to have. So thanks, just thanks, really, more, like, to, to, to pointing me this way.
But thanks for, I think that was Sergey making sure my questions were answered, appreciate that. Yes?
Good stuff, Annie.
Sergey Sergeev 00:50:53 Yeah, we… we have, 10 more minutes, I… I was wondering if,
Yeah, I… it's my fault I could not join the first half of the meeting because of conflict. I'm wondering if I can provide any additional information about the session.
And how it is, basically implemented,
on the Splunk, distro site,
neil yashinsky 00:51:23 Cool, yeah, that'd be cool.
Sergey Sergeev 00:51:25 And, asking Quan, because Aaron had, a few questions,
Basically, I wanted to ask, will it make sense if I, walk over, what's happening on the Splunk distra side to, will it be better if I just, make that change, try to make this change in, the upstream distra?
And to view… And we will make the change in the proposal, I just wanted to check with Aaron.
Since he… yeah, when… when he get… when he get a chance.
Aaron Abbott 00:52:11 Sorry, I kind of missed the question.
Sergey Sergeev 00:52:13 Yeah, yeah, yeah, sorry, I missed the session discussion. I was wondering if it will be helpful to provide a little bit more details in what we do in the Splunk upstream, or if it will be more helpful for you if we just go ahead and make that change and pull request in the upstream.
Aaron Abbott 00:52:33 Yeah, I mean, would love to learn more, but if you want to,
I think we kind of talked about sending a pull request, and then maybe there might be some issues in terms of rebasing the changes or having a really big PR, so…
it's kind of up to your discretion, you know, like, feel free to open a draft PR with something kind of large, but it would be helpful to get context if you wanted to walk through something.
Sergey Sergeev 00:52:59 Yeah, and just in general, the discussion may be related not necessarily about the session, but about some of the attributes propagation, text propagation, down to the child's expense.
I wanted to quickly sync up on it. So, originally, we had a discussion, for LM
Where inference, spans, And basically, propagating to that span,
Parents, agent name, or workflow name, and session ID.
So, the whole idea is that a few instrumentation libraries doing that, like TraceWoop, for example, and so on, and the key idea that you push down those attributes down to the child spans.
So you can, create, additional dimensions on a metric, for example.
Token usage or duration, so you can really filter by agent, workflow, Or,
You can, for example, on the spend level, do something for the session level.
And, wanted to check,
just the feedback from the group. Right now, I don't think we'd do it, and
We don't have those attributes on.
Lom metrics for duration and.
Aaron Abbott 00:54:39 Yeah.
Sergey Sergeev 00:54:39 token usage.
Aaron Abbott 00:54:41 Yeah, so I, I mean, I think we kind of agreed on the high-level approach, and I think for, I'm assuming we're using baggage, right?
Sergey Sergeev 00:54:50 So, the baggage is basically… and it will be up to particular instrumentation to use it or not.
Aaron Abbott 00:55:00 Yeah, I think we had, like, pretty good agreement for, like, the tracing side. It makes sense.
I would say, like, maybe we could do metrics iteratively? My biggest concern would be cardinality, right? Like.
Sergey Sergeev 00:55:14 You have…
Aaron Abbott 00:55:15 thousands of sessions.
Yes.
Sergey Sergeev 00:55:17 Session, session makes sense, on trace level, and maybe optionally on,
On the metric level, if the backend supports high cardinality metrics, but agent name and workflow name, may be low cardinality in generic use case.
We may even set, by default, Because in the end, customers want, to know
what, what tokens used by an agent, by workflow?
They do want to know token usage,
And overall, more detailed trace level.
Operation by user or session.
But it doesn't fit the metic.
But, yeah, I'm wondering if there is a chance to consider, basically, agent name and workflow name.
on, the LM inference, metic as an optional attribute.
Aaron Abbott 00:56:27 Yeah, yeah, I think those make sense to me.
So I guess… Is there already an issue for those? I mean, I think…
Definitely agent name makes sense.
Sergey Sergeev 00:56:40 Yeah, I was completely on different topics, and out of time to participate in those meetings, so, I'm just trying to restart my brain on where we are in
as a community, thinking about those issues. For session, we can make a specific example in AppStream, and I think we can do it for cross-RPC propagation.
the baggage and basically, support, in instrumentation library, like MCP client, we'll put it
Into the baggage.
Into the headers, and this is where we will extract it.
And, propagate, to…
to those plans, I did that, POC for… I did that implementation for MC, it's not using baggage, it's using, protocol-level MCP.
But, I think, the concept, just wanted to double-check, is it, okay to consider it,
To be auto-propagated by all the instrumentation?
Aaron Abbott 00:57:54 Yeah, I mean, I think… I think it makes sense to me. We definitely… we discussed, like, the last couple of weeks, some of the concerns there, and how it's, like, uncharted territory a little bit for OpenTelemetry, especially adding, like, baggage automatically out of the box.
But I think, honestly, if we could do, like, a demo next time, that would be super helpful to kind of visualize everything that's happening here.
And then, yeah, like, the metric labels that you suggested, if you want to open an issue for those, they definitely make sense to me.
But yeah, if your fork is, like, pretty far from…
from what we have in Contrib, if we could add stuff piecemeal, I think…
Sergey Sergeev 00:58:34 Yeah, yeah, I… it's… it's pretty far, but,
There are concepts we can just rebuild easily, especially the AI coordinates.
It should be a Dumo. And, one more concept, so again, back to, what's implemented in, trace hoop, and I think it's…
Generalizable. So, there is a method, one.
the instrumentation library to just… to set and propagate arbitrary attributes, for example, user ID and etc. And since we have Utilogen AI, we can make this method as well.
So it can… it can be more than just a session.
And yeah… Got reactions to this.
Aaron Abbott 00:59:33 Yeah, I mean, I think… I think this is what baggage was always intended for, but, I mean, obviously the… the security aspect is the thing that pops up first, like, yeah. Especially with the kind of implicit nature of instrumentation, if… if you have something in the baggage, you don't mean to propagate it somewhere, you just gotta be careful, but I think… I think there's plenty of people.
Sergey Sergeev 00:59:53 Doing this in…
Aaron Abbott 00:59:54 you know, in real life, I think…
I'd love to hear more from,
I think AWS has some recommendation to use baggage to propagate the conversation or session ID or whatever, so I'd love to hear if…
I don't know if your team any, but, do you have any feedback on how that's working for customers, security concerns and stuff?
Sergey Sergeev 01:00:13 Yeah, the last I seen, it's done manually, basically. It's an example. Put it to the baggage, get it out of the baggage on the coin, but do you want to set it up in instrumentation? Maybe disabled by default on the server side?
instrumentation.
But optionally enable, if you just set some environment variable, your server will, try to extract those attributes from the baggage.
And propagated, on all child splines.
I think, yeah, I would try to make a proposal.
That'd be great. Yeah, time.
neil yashinsky 01:00:58 Love to see it.
Aaron Abbott 01:01:01 Alright, thank you everyone, really appreciate it.
See y'all next week.
neil yashinsky 01:01:07 Thanks, bye.
shuwpan 01:01:09 Bye.
