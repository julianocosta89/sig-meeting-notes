SIG: LLM Semantic Convention WG
Date: 2026-02-17
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/EVCXKpG02ctUdfKdh0AHMxAWyGVhBF8oAMCG6mNxpwc0umPNfilJoNU90Y0JnN2Y.oeBaLQG9tn4pO9R0
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:57 Hello. Hi, everyone.
Josh Bonczkowski 00:02:01 Hello!
Liudmila Molkova 00:02:04 Okay, so let's get started.
What do we have?
Our agenda is packed.
So… Please add your name to the attendees list.
Let's see, what do we have here?
By the way, if somebody, you feel free to populate your topics in advance, there are some people who've done it before.
R… I'm sorry, Kumar, I'm going to push you.
Down.
Because… It's been there. I think we didn't… Discuss… this…
And we don't have Minghoi to talk about it better, so we'll postpone it until… We can.
Okay, let's spend some time on the triage board, and feel free to… 2…
Add things to the agenda while we are triaging stuff.
Okay, we have some new issues,
Okay, semantic convention for Tokyo Level Attributes and events.
Oh, this is the server.
So maybe I'll do a new column, I'll call it…
And we'll move it… There?
Revelation… I think we talked about this.
Last time…
I think we decided that there could be a small, smaller pieces. This, this, PR can be breaking down into.
So I'm going to remove it from the new issues.
And… I think the whole thing makes sense, but we need a more granular proposal.
Reasonings… Pants.
Sergey Sergeev 00:05:33 Yeah, if we can get back to that ticket, so… I was trying to…
to make a proposal, but didn't get time. I think we can discuss some more generic, user-provided, association references.
You mean this? This? Yeah, yeah, yeah.
So, basically, what it does, it defines some test-specific or experimentation-specific properties, Which may be not,
Necessarily generalizable at all.
It may be… That we can just define association properties, basically some ways to… To keep user-provided, properties.
and to add them on Gen EA spends.
Liudmila Molkova 00:06:28 users can do it today, right? They can put any properties they want through the context and the processor.
Sergey Sergeev 00:06:38 So, it's… yeah, maybe…
it's more into Python instrumentation event, where we can define some helper methods to make it easier.
Liudmila Molkova 00:06:48 Hmm.
Sergey Sergeev 00:06:49 And to propagate it, if needed, to the child's plans.
Liudmila Molkova 00:06:55 I see.
So, like, something… I've lost our project board.
I think it's a good discussion to have. Let's spend just a few minutes on it.
so, something like, in Python, in Gen AI… Util's.
Sergey Sergeev 00:07:22 Yes, that association properties, and maybe with the flag, to propagate down to the child's pence.
Liudmila Molkova 00:07:31 So, like, we would write something like, with… .
Sergey Sergeev 00:07:35 Yeah.
Liudmila Molkova 00:07:35 I don't know, Jenny, I… .
Sergey Sergeev 00:07:39 With telemetry handler, start…
Liudmila Molkova 00:07:41 Oh… And put some arbitrary stuff here.
Sergey Sergeev 00:07:46 Yeah.
Liudmila Molkova 00:07:51 And…
What it would do is that it would put stuff in the context.
Sergey Sergeev 00:07:57 Saddles.
Liudmila Molkova 00:07:58 And anything emitted under this would, would be, would have this attributes, all the spend.
Sergey Sergeev 00:08:06 And to auction this template, on the first, GenA
a span and mark it as a root span. So, those platforms which can derive all the needed information just from the root generation can use it for… we can have a flag, basically, to propagate it down to the child spans.
Aaron Abbott 00:08:37 So, do we mean all child spends, just Gen AI spends, or, like, specific.
Sergey Sergeev 00:08:43 I think it's Gen EA spends, specifically, but, it's a good question. I think,
They will press, as I said, association properties.
Which I believe, I stamped down this… two over the child's plans.
Aaron Abbott 00:09:07 Yeah, I, added this one. So we did something in…
Google Gen AI for this, but it's… it's very… it's more narrow, and I know that there's also something in Java, there's, like, some code gen to generate specific context keys for spends you want to target.
So yeah, this sounds good, and it'd be great to have, like, a more general way to do it that works across instrumentations.
Sergey Sergeev 00:09:30 Yeah, sounds great. I will definitely work.
Liudmila Molkova 00:09:37 That's cool.
Okay, I… I love the idea. If…
Maybe it already works, but if not, it would be cool to have a prototype, and then it can move on.
I don't want to take more time to spend on triage, we have a packed agenda. If anybody wants to go ahead and introduce themselves, go for it, we would love to know what brings you here.
What you want to do here, what you're interested in, and feel also free to book any, additional time on this, agenda list. We are the first come, first serve. Sig, we will, would be happy to hear from you.
Does anybody want to go ahead and talk about themselves?
Kyle Hounslow 00:10:27 Yeah, I can go, first today. My name's Kyle Anslow, I'm from the OpenSearch Project in AWS. I've been kind of a fly on the wall in the past couple, but now… now that I've gotten deeper in development,
Awesome things to… to discuss. Yeah, so basically, like, open search dashboards, we're working in some, agent tracing, like, native support for visualizations and, you know, the tracing investigation workflows.
So naturally, came across this conventions and this SIG, so that's why I'm here today.
Liudmila Molkova 00:11:00 Nice. Great to see you.
Okay, anybody else?
Okay, then let's move on.
Do the agenda.
So… This is what we started talking about last time.
I…
I missed a part of the patency call, where we talked about it. I'm super sorry. Did we come up with anything?
Else beyond the, the… More tests and more better validation, automation around the validation.
Aaron Abbott 00:11:47 Yeah, so I took some notes in the Python… Signotes…
There was definitely a lot of interest in
in the, code review stuff, AI code review.
I think we just kind of need to follow up with Trask on that.
Yeah, definitely improving some of the tooling. There were some concrete suggestions, like improving
Type checking coverage, stuff like that.
I can paste the notes in here if that's helpful.
Liudmila Molkova 00:12:16 Oh, yeah, please. Sorry, I should have caught up, but yeah.
I didn't expect yesterday was a day off.
In the US.
Okay, so, the concrete…
steps. One of the things I was, thinking, we do have OTLs, but we don't have cross… Instrumentation.
Unitask helpers.
And if we had test tools, we could put the Weaver integration test there, but we could also put the test helpers.
And by reviewing tasks.
We could also check that, like, if they use the helpers, it's a forcing factor to stay compliant with everything else.
Aaron Abbott 00:13:13 Yep, totally agree. That would be… Really good.
Liudmila Molkova 00:13:25 Improved CI tooling.
This is just the cross, not just Gen AI, right?
Aaron Abbott 00:13:38 Yeah, yeah, there was a little bit of, like, event session about the, just stuff in general in the repo, and this was one of the things that
you know, like, sometimes it's hard to review PRs because there's a lot of generated boilerplate, which…
I… for me, that's not a high priority, like, I know you can ignore, for example, in,
I think there's a special .gitub file you can put to ignore generated files, or to have them automatically not show as expanded, so we can do stuff like that.
Liudmila Molkova 00:14:07 Yeah, and I think it's great. We should target improving overall repo rather than just doing things for GenAI, so, yeah.
more reviewers.
Yeah, so about the component owners, I, I, I did, Thing…
was, we have a problem with how the component owners are triggered, right? And today.
Everything in GenAI is assigned to a group of people.
And many of them are not responsive at the moment.
So, I think we're…
should be more strict around who component owners are, in the only sense that we should
check who is active, who is reviewing PRs.
And that the component ownership should come From it.
rather than from involvement in any other parts of the GenAI work we do, right? So,
I have a PR to update the component owners, and I talk to the people who
Been there and been unresponsive, give me a sec.
Okay, so, this is the current state. I think, some people, We're not responsive, and…
We definitely would like to see more component owners.
And… but… Only if you are ready to commit to review things, right?
Okay.
So, I'll keep following up on this. We will try to at least for this list to be Realistic.
Triage your role. Okay, can you help me understand?
Aaron Abbott 00:16:44 Yeah, this is… I think in OTEL, it's, like, pretty well defined, the triageer role. It's just something we haven't done in the Python sig yet.
you know, I guess any… anything is useful, help-wise, and the main difference here is that triagers get permissions to, I think, just modify issues, put stuff in the project board, etc, etc.
Liudmila Molkova 00:17:09 Right, and we would… Do we want to share the project board and triageers between semantic conventions and Python?
Aaron Abbott 00:17:22 I think it works well for me, personally.
What do you think?
Liudmila Molkova 00:17:29 Yeah.
It's just maybe,
the same role, but maybe same permissions, but different people would be interested in different things. How… do we… do we have people interested?
Oh, yeah, I see, so you're interested in up-in-the-air review, please, yeah.
Leave a comment, and, it would be highly appreciated.
some feedback, since they maintain a lot of groups for localization approvers. We… have…
A lot of groups and semantic conventions, as well.
And we essentially have a process where we have to… we have to use code owners mechanism. People need to get right access to the repo. The code ownership is applied to a specific area. It's the mechanism alternative to code owners. It does not
change much, it just gives the component owners the… the real green checkmark that counts towards review process.
I don't know whether it… I don't feel it will make a difference, but it can be helpful.
Yeah, and if somebody is interested in, enabling better
co-pilot reviews, or any AI reviews.
I think it would be… right?
Everyone is so quiet, is it,
Do people have comments about any of this?
Aaron Abbott 00:19:47 I think, Ankit, you left a comment in the chat. This was… this was more specifically for the Python instrumentation.
anksing 00:19:58 Yeah, I think, I worked in Thailand, but I think the last, 4 or 5 months, I have not, so I can get back in the game there, but, just, did a little bit of polishing. Otherwise, yeah.
Liudmila Molkova 00:20:15 So you actually don't need the permission to start reviewing things.
anksing 00:20:18 Oh yeah.
Liudmila Molkova 00:20:19 Once you get into a habit, it's the question of just to do…
Do the… do the reviews, and… Regardless of your checkmark.
And once… once you… you get the context around everything and provide good quad reviews, it would be a great
way to, get the formal status. So just don't wait for permission.
Surya Teja 00:20:45 Yeah, Lindmila, I have a question. I have been working with Mike Goldman from Honeycomb, who has been helping me move the PS and stuff. I asked him if he's interested in being a component owner for Anthropic, alongside with me and Ani.
So, can we… can I ask people who are really,
in the community that, if they're interested, can I add them also? Because they have been helping moving PRs and stuff, they have been reviewing also.
Liudmila Molkova 00:21:14 Oh yeah, so if they, like, I think we should have a rule that if people consistently demonstrated that they
been reviewing and contributing, one of them, reviewing this better, to the component, it's a low barrier to make somebody a component owner.
And I don't think we… do we have it documented in Python country? Like, what is the process of becoming the component owner, Aaron?
Aaron Abbott 00:21:44 That's a good question. I think… I think we have it in the contributing guide. Is there some boilerplate I can copy from a different repo, just in case?
Liudmila Molkova 00:21:55 There might be.
Hmm.
Anyway, so.
Let's hold up on this.
Aaron Abbott 00:22:23 Yeah.
Surya Teja 00:22:25 Cool. Thanks, guys.
I'll do that.
Sergey Sergeev 00:22:29 Thank you for I'm wondering if, there are some ways,
Basically, to… to… to do, maybe.
Not on call rotation, but something like triage rotation, when people just find…
somebody to review it, and get some commitment table, review it in day, in two days.
just brainstorming this idea, because I think with so many companies participating in it, workload changes.
And if you have, those fixed… All nearest reviewers.
I fear that it may be unpredictable how much time it will take, and hard for…
Somebody created a pull request.
Just to plan the work.
I don't have a solution, Jess. Asking.
this commission.
Liudmila Molkova 00:23:39 I think we have a decent amount of people in this group, and if we tried hard to review.
We're focused on the review in PR, so we could… provide some guarantees.
But the review is a hard process. It's harder to review code than to send a PR.
Aaron Abbott 00:24:02 Yep.
I think
we can do all this, but really having some automation for the, like, having good tests, having some automation is… I think that was one of the things that came up, was knowing if a PR follows semantic conventions is incredibly difficult.
Without some automation, so… Even if you have, you know, most…
Python-savvy reviewers or whatever, it's really still somebody has to go through, comb through and see if it's doing the right thing, both, like, semantically and structurally.
Sergey Sergeev 00:24:34 Yeah, in our district, they built a few of the demo applications, which
Which we run, basically, on a daily basis, to… to get the telemetry and etc, on top of integration tests and…
So, so they are kind of integration tests,
But also, we can probably stop everything, and,
just run it, on a permanent basis. We can definitely just a couple of apps.
Liudmila Molkova 00:25:10 Okay, we spent a decent amount of time on it, and I think we,
the two main areas is the automation, second one is having people participate more actively. I think they're not contradictory, they should coexist.
I will focus on this one.
And I think it would be awesome,
It would be awesome if, in addition to GenAI tools, we would have GenAI test tutorials that would be used consistently across all the libraries.
Okay.
Moving on, to the… Agenda…
Honey?
Do you want to present your topic?
Kyle Hounslow 00:26:21 I don't see Annie today.
I work…
alongside with him is Kyle from AWS. I think you might be on vacation, so you might want to bump his till the next,
Next meeting.
Liudmila Molkova 00:26:36 Okay. Oh, it looks like an action item from something in the past,
Maybe it was copied over in the wrong way.
Okay, Kyle.
Kyle Hounslow 00:26:51 Yes.
Liudmila Molkova 00:26:52 about this?
Kyle Hounslow 00:26:53 Yes, we'd love to, yeah.
if you wouldn't mind, you know, pulling up the issue, I can copy it into the chat, too, for other folks to take a look. So this concept… not entirely new, but it's something that I was required to do when trying to build
a unified dashboard view. I think the same problem… this is in open search dashboards, I think the same problem would be, like, we wanted to do something in Grafana.
Or anywhere else, to have… Consistent queries to be able to get these views.
And so, like, it's a bit of a moving target, all of these different libraries popping up, both in,
on the instrumentation side for the models themselves. Actually, I don't need to… I don't need to talk about how tough this is, to you folks. But basically.
There's… even if we were to instrument all the libraries properly, there's still…
Do you actually want to patch your deployments on those, if they're, like, in an outdated semantic convention, or they're…
you know, simply not following the convention. Like, some of your agents out there aren't.
So this is… this is a…
a processor at the collector level. And so, like, I had implemented one at this, we have something before ingest into OpenSearch called Data Prepper.
But that's, like, not so vendor agnostic in this community here. So I moved it out, same logic, out to the collector and tried it, and it works really great.
So I… it seemed… it seemed like a little bit… the feedback I was getting from the…
maintainer here, which was, like, really valid. I could see it was… might be kind of, like, a governance concern, is like, where does it… where does it end? Where does it end if we left… if we, let something like this in?
So, but I wanted to get…
Your folks' opinion on it, because you're closer to the problem.
Yeah, special receivers…
Aaron Abbott 00:28:50 Yeah.
I saw this, I was pretty excited, and
I think, you know, we live in the real world. It would be great if everybody used the GenAI semantic conventions, and it seems like a really nice stopgap kind of thing.
I… I'm not super involved in the collectors, you know, I'll obviously defer to them.
there,
But, like, what you mentioned about the code, you know, kind of working in production, you mentioned this is a reimplementation of something.
I think that's, pretty valuable feedback, because I…
I don't know, for example, like, Open Inference, how well it actually follows its own conventions across, like, Node, Python, all the different agent frameworks, etc.
So…
Could you mention again, like, how… how has it been tested? You said you had something similar running in,
Was it, like, internal, or something you could point out on open source?
Kyle Hounslow 00:29:43 Yeah, I'll have to push it to open source, because also data prepper's used for across, like, search in open search as well, so there's a large surface area there, not just observability. So I'll have to make that PR public.
So, basically, we have, like, a UI UX team, they're building out these beautiful views, and, you know, they… but you need to… you need some kind of anchor, at least 4 or 5 of these, attributes to be able to, you know, get some kind of overall view for your agent health.
And… and I found that, honestly, it is, like, about just 5 to 8 of them that are really fundamental to getting these views, and… and just every vendor has them, like, the model name and…
What else?
what else can we say? But the,
It's really simple logic. Honestly, it's just taking the attribute name and replacing it, and giving the option to be able to keep the old ones if you want to. But I tested it across this. This is, like, the…
surface area in which I tested.
Just kind of combinations of both OpenLL imagery and Open Inference, for Crew AI.
Minecraft.
Aaron Abbott 00:30:44 Yeah, yeah, super cool. So does it handle, like, prompt and response normalization, for example?
Kyle Hounslow 00:30:50 Yes. Yes. But that is… I think it's, like, opt-in?
In most of the libraries, too.
So it's not always there, but yeah.
Yeah, this is a good file to look at. It's, this is what it all boils down to. It's like, what do we interpret? And this could be opinionated, too, but I tried not to make any guesses as to what it could be.
From 1 to… I only mapped the obvious ones and left everything else at the beginning here, so…
Aaron Abbott 00:31:18 Yeah, cool, I can… I can, follow up on this. Maybe one more question was just,
I know some of these other
Some of these other ones, like Open Inference, they represent arrays as, like, flattened, flat… Handle that as well.
Kyle Hounslow 00:31:34 Right now, I'm still handling that part at that data prep, because it actually breaks in open search, because you need to have some kind of… you can't have, like, an object,
if you define it as a string or define it as an object, you can't have a nested object. It just doesn't work. So I handle it there, but I could try and pull out that logic here and see what it looks like. I just didn't want to…
Convolute so much at the beginning.
Aaron Abbott 00:31:56 Yeah, yeah, I'll let other people, you know, ask questions and whatnot, and I don't want to make you commit too much time, because ultimately it's… if it's Collector, it's kind of up to them, but it seems super cool to me, yeah.
Kyle Hounslow 00:32:08 Nice.
Liudmila Molkova 00:32:10 Ankit, I think you were next.
anksing 00:32:12 Yeah.
Kyle Hounslow 00:32:13 Yeah, one more, one more thing, is that, if anybody here wants to sponsor the… just the proposal there, it would carry some weight as well, if you do think it's cool, or you do think, do you have time to, you know, write a few comments?
That'd be helpful. Thanks.
anksing 00:32:28 Interesting, because, once, like, I think I remember,
other ACI, or some other artworks, like, so, we're working with, like,
instrumenting or, evaluating, like, Microsoft-specific agents, which are following JDAC convention. They were doing the reverse, where they were transferring, like, transmit, like, translating JDAC conventions to what they follow, which is open intent, and now here I'm seeing the opposite one, which I feel is, is, is, is,
It's a great thing at the office. Thank you.
And the full cycle from the end.
Kyle Hounslow 00:33:04 Yeah, I stumbled across that as well. Gave me a chuckle.
Sergey Sergeev 00:33:09 Yeah, I think it's a great idea, and basically what everybody seems to be doing on GDI side of the platform, so it looks like everybody is using OpenCinematic Galactic mappings to remap to internal schema.
From different, telemet flavors.
I'm wondering how it will fit with something like, FSP order, which we do on the Python side.
Because if somebody wants to…
Yeah, it's a trade-off, do you want to do it in utility and AI on the Python collector side, or OpenTelematic collector? I think both are, both are helpful, but,
Just wanted to brainstorm.
I'm looking, at Aaron. What do you think about Python with, collector, say?
Aaron Abbott 00:34:10 I kind of missed the question.
Sergey Sergeev 00:34:13 Yeah, so we have a spare cup order on the Python sites, which you can enable
to, to, to upload, basically, conversation messages, artifacts to every spec, destination. And right now, it's, on the Python side.
So, what's… what do we do?
Aaron Abbott 00:34:37 Yeah.
Sergey Sergeev 00:34:37 if this…
Aaron Abbott 00:34:41 You mean, like, can we do it in the collector?
Sergey Sergeev 00:34:43 Yeah, should… should we move it to collector as well, or…
Aaron Abbott 00:34:49 Yeah, it's a good question. I…
So there's also… this is maybe getting a little off-topic, but, there's an issue from Mingui on… from Alibaba also on changing the format slightly, and different requirements as people have used it, so…
I… I almost feel like we need to push more on bringing this to the spec, the whole blob upload issue.
I think we tried that before, and there was… there was, like, a lot of, like, why do you need this? What's this for?
But I feel like that would be…
Maybe a nicer way to build it into the collector directly, instead of trying to kind of round trip it through spans like we're doing right now. Roundtrip it through…
logs.
Liudmila Molkova 00:35:30 I think that this is a good point. The blob uploader…
You can… you might want it to be…
Synchronous, in a sense that you block until
upload happens, right? And this is the reason it… it…
could be in Python. It needs to be in Python this way.
Or if it's sensitive and you never want to stamp it on the telemetry.
It's so sensitive that you don't even trust the collector.
But other than that, it should be in the collector.
I think the… the bringing this… the spec, it's a long-term project. It… I… I think it's… it's a new signal, it will take…
anywhere from… Years to years.
So… And… Let's do it, but we should have a plan for the next future.
Sergey Sergeev 00:36:39 I think with AI coding things and everything else, once implemented anywhere, in GoNQ or whatever, we can easily maintain a copy in Python if needed, so…
I think the hardest part is to define those mappings, basically, and especially the message, messages format, in my opinion.
And all the flattening and etc. Once defined, I think it doesn't matter where it resides, we can have both.
Intuitive.
Liudmila Molkova 00:37:12 Kyle, do you know what kind of sponsorship is needed? I can check with collector folks, do you have any other details on this?
Kyle Hounslow 00:37:25 Yeah, I think it's mostly just that…
from this side, like, this perspective, I think from the Gen AI group would be… would carry some weight. I think it's really just…
Does anybody agree? Or is this person… working… Alone.
I wasn't quite sure about the sponsorship as well, and how much… how involved the sponsor is supposed to be here, but…
Liudmila Molkova 00:37:48 I think this is the component sponsorship. I can follow up. I'll follow up and I'll check.
I'll also leave a comment here, I think I agree with their concerns, but I think this is pretty special, it wouldn't…
We wouldn't need a similar story for other conventions, but there are similar cases.
Where we have a mapping between something external and hotel. They're a much of a less scale.
Kyle Hounslow 00:38:15 Yeah.
Liudmila Molkova 00:38:16 It might be useful to have a common approach for it.
Let me think a little bit, and I'll… I'll follow up on this.
Kyle Hounslow 00:38:26 Awesome, thank you.
Liudmila Molkova 00:38:48 Okay, thanks a lot, Kyle. Anything else on this before we move on?
Kyle Hounslow 00:38:54 Thank you.
Liudmila Molkova 00:38:56 Settings, okay, Ankit, the GenAI Open… I think it's OpenAI Operation API type now.
anksing 00:39:09 Yeah, so I think there was feedback on making this OpenAI specific, so I've updated the PR to include that, and then also updated the description.
So, yeah, please take a look and let me know if there are any more feedback. I'll be happy to address. Pretty straightforward, just an attribute specific to OpenAI to identify what kind of API you can use to application versus OpenAI, responses.
So, peace.
And, based on the offer, design, and…
giving me a checkmark, so I wouldn't need one more to kind of get this across my…
Liudmila Molkova 00:39:50 And I think it doesn't need a Gen AI app over the second one.
If anybody wants.
anksing 00:39:56 Hello, please.
Liudmila Molkova 00:39:57 go ahead, otherwise I can just… we can just advertise it in the General Semantic Conventions channel, and…
Anyone can approve.
Trust can take a look, if you're ready to take on more Gen AI reviews.
anksing 00:40:14 It's a pretty small number, I would say.
Liudmila Molkova 00:40:23 Okay, and Ankit, you're still on the Stage Hub to capture user information.
anksing 00:40:32 Yeah, this is basically how to, capture, like, the user who's make… doing this operation, actually is involved in the agent, and then…
say, for example, invoke agent span, right, or LNM inference span.
So, right now, like, I think I came across user attributes, however I wanted to check if that's the right way to do it, and I think that would probably cover humans, and I don't know if it's gonna cover, like, if agents are being used to actually aid all those operations, right?
And if there's a way to kind of capture those agent identity as well.
Liudmila Molkova 00:41:06 Let's think about how would we capture it.
Like, what is it that that we're going to capture? Where it would come from?
anksing 00:41:20 Yes,
I just can't work on that, because I know, like, a couple of, a number of…
at least the Python libraries that I've worked on, our SDKs.
They do capture, like, user context, and then they put it on, like, you know, the request that goes out, to the server side.
And, like, when you log those requests, it also captures them and can log it, like, for your console logs, or wherever you want to get your logs to. Can I capture user information on the screen setting.
invocation.
our operation bundle.
I can build up a smart prototype if that helps.
Liudmila Molkova 00:42:05 The, the other part.
anksing 00:42:07 For the, agent?
Liudmila Molkova 00:42:10 Wait a second.
anksing 00:42:11 It's too good.
Liudmila Molkova 00:42:12 For the user.
if it's… it's a central component that, let's say, pulls the user ID or something from the context, it does not have to be in GenAI.
Instrumentation.
anksing 00:42:25 Under…
Liudmila Molkova 00:42:26 It's probably a separate topic.
anksing 00:42:28 I see. I think, yeah, that totally makes sense. However, like, my reason for putting it here was, like, at this point, I was interested more putting them on the Gen AI operations.
Because I want to capture,
Possibly who is invoking it, be it user, agent, like a human user, or an agent, right?
pictures.
Liudmila Molkova 00:42:50 Yeah, you can still do it, it just doesn't have to be part of Gen AI instrumentation, and probably you should take a look at this thing we discussed.
This one.
Because… This would allow you to do… to do exactly
What you want, but without introducing any new concept.
anksing 00:43:14 So, actually, the thing that I was looking for more was…
Can we… is it possible, like, to say that, your user attributes can be added on a GenAI-specific operations, right? If we are, like, this is how… these are the attributes you can use to capture the user?
Liudmila Molkova 00:43:35 All the attributes are opt-in, like, all the attributes you see in semantic conventions are opt-in on any spans.
Think about them this way.
anksing 00:43:44 forced to get.
Liudmila Molkova 00:43:45 And then…
anksing 00:43:46 Anybody can use user ID.
Liudmila Molkova 00:43:48 But they could also add something else.
anksing 00:43:54 Is this so cable.
Okay.
Liudmila Molkova 00:44:12 Hey, anything else on this?
Aaron Abbott 00:44:17 Yeah, I… Yeah, I had a quick question. Would this be… would this fall in a similar camp as the session ID we were talking about that would be propagated through baggage?
Liudmila Molkova 00:44:32 Yes, session AD would be propagated as baggage, and we entertained the idea of
Gen AI Instrumentation, stamping it.
the use… the user ID cannot come through baggage, right?
It's sensitive.
Aaron Abbott 00:44:53 Yeah, I feel like… I feel like…
it's likely to come through baggage, though, right? Like…
If you have some kind of auth proxy or something like that in front of the agent, where the request is already authenticated. Or maybe, you know, it's probably already somewhere else in the request or handle outside of the telemetry.
So… I guess that's another possibility.
Liudmila Molkova 00:45:41 That's a possibility, yeah.
And this then wouldn't work, because if you… if you… if you want to propagate it everywhere.
Jankit?
anksing 00:45:52 So, the follow-up here is, if I understood this right, that, we need to figure out, like, how this information is…
Gonna be captured, and then passed along, whether it's baggage or some other village.
are…
Liudmila Molkova 00:46:08 Yeah, so, like, if you can build a prototype and show where this information comes from.
Which would help to understand it better.
I'm curious, aren't you… your…
it seems you're kind of following the session ID and user ID. Is it something you folks are also interested in?
Aaron Abbott 00:46:41 Yeah, I think… I think we're interested, it's…
like, I think… so ADK has this concept of user ID also, which is a little weird. I was a little surprised to see that.
the session ID, if I understand right, would be, like, the…
browser propagated session ID, like, it would be a run kind of thing, which is interesting, but I was kind of more interested in propagating the conversation ID, actually. Just trying to tie the threads together.
Sergey Sergeev 00:47:15 Yeah, it goes back to, that, association properties, basically.
just custom context, I think that user is supported by at least few providers as a separate entity, similar to conversation ideas, so we can try to define it.
Overall, but, A good start may be just to…
to provide some options, to stamp user-provided association properties, including user ID.
Liudmila Molkova 00:47:51 Yeah, so this could be very powerful.
Sergey Sergeev 00:47:55 That was called for a mess.
Because this is application context, we need to provide, probably helper methods, if not provided yet, if we can use the scope.
It's fine.
Yeah, it would work, from the applications.
Yeah, the only question, do you need to stamp it on all for a rude conversational message, because…
In most cases, it may make no sense to propagate that down in the transport.
Liudmila Molkova 00:48:43 Good, good, good question.
Once reflected.
Okay.
Let's move on, we just have just 12 minutes, let's try to…
I'll make sure we talk about things…
Yeah, so where did we stuck here?
Redeema, can you help us, understand how we can unblock it?
Ridhima Satam 00:49:37 Yeah, I think there was a concern from Aaron about how workflows can be used in ADK, and then, we discussed, and someone from, I think, ADKing also looked at it. Looks like the workflow agents they have cannot be wrapped into a… mapped into a…
workflow, because, like, it's already modeled as an agent and creating an invoke agent. So in those cases, we cannot use it, but otherwise, so last time I synced with Aaron, I think we can use it in the other agentic frameworks.
So, yeah, that's… that's all, I think, but if there are any other questions on this, or any issues you see…
Please let me know.
Sergey Sergeev 00:50:19 Yeah, go ahead.
Liudmila Molkova 00:50:22 No, no, no, go ahead.
Sergey Sergeev 00:50:24 just wanted to provide, some additional context. We brainstormed the demo last week, internally, so one of the reasons we brought, workflow may be
basically generalizable root-level span, because in some frameworks, like rank chain, Basically, he…
it's… it's helpful because, agent invocation, not necessarily the root level thing, and it's not necessarily the agent invocation at all. So it's basically a grouping
Which may include input and output, so it's kind of root level generally a conversational span.
So, what we realized, after reviewing Aaron's feedback, so in ADK, agent invocation is a perfectly fitting into that,
GenAA conversational route span definition. So, probably, all we need is just some additional attribute, which will say that it's GenAA conversational route.
and maybe a type in LTA, which will
Require input and output on the span.
And so is this plan… yeah.
This plan also will be a great place for
All the additional association properties were the scope.
Because in many cases, you want, basically, to…
To build some aggregate metrics and etc. on this level.
you probably, if you want to see something by user ID or by conversation ID,
It looks like, in most cases, you just need those properties from the root level.
Some backends may need that to be pushed on every channel span, but in general, I think, it's been, that we may need that, conversational route.
Not daily outside.
Yeah, there's also water.
Liudmila Molkova 00:52:39 Something like this.
You're saying that this is the start of the conversation?
Sergey Sergeev 00:52:44 Jenny, conversational route.
Liudmila Molkova 00:52:49 I'm enjoying…
Sergey Sergeev 00:52:49 route.
Liudmila Molkova 00:52:51 the genre, it's kind of ambiguous, right? You never know. You cannot say that there is no root on top of you.
Sergey Sergeev 00:53:00 In some cases, you can. Again, in some cases, frameworks explicitly set, this is… My roads.
And, of course, there are multiple ways. I mean…
infinitive ways to make it wrong, but we probably should,
suggest to the users how to do it, so again, if…
If you're using some frameworks, you can expect, that you will have that generate a conversation route set.
Or it may be.
again, in UTGNA, it may be…
additional API, basically, to start workflow and stop workflow.
Which…
will be that explicit grouping, so if you have in your application multiple frameworks, some custom, GenA, LOM calls, and still want to have that grouping for some reason.
You can explicitly start workflow and start stop workflow, which will ensure that you have that, conversational.
Liudmila Molkova 00:54:12 Yeah, I am… let's not waste time on the naming. I think root is problematic, but we probably can find a better name. I really like the idea of just having an attribute that would differentiate this band, because otherwise, this is just invoke agent with maybe a little bit different set of things you would put on it.
Sergey Sergeev 00:54:30 Yeah, Invoke, agent, maybe…
not applicable for some use cases. For example, you are not building an agent, so in this case, it can be very poor.
So, just having an attribute, just generic attribute, which will say.
GenAI root or something like that may be sufficient enough.
Aaron Abbott 00:54:59 I think my main feedback on this one was just, like, I don't think ADK would do the workflow span as is, but it might be useful to put whatever attribute we have there on agent spend so that it could fill that in.
But I also, you know, if ADK is pretty unique in this regard, a lot of other frameworks don't model everything as agent.
We don't have to do that.
Liudmila Molkova 00:55:26 So…
Ridhima Satam 00:55:28 Yeah, so for the conversation, the GenAI conversation attribute, do we want to add it on the same PR, or do you want a follow-up peer on that, like…
Hmm.
Right now, it has the workflow name, output and input messages.
Liudmila Molkova 00:55:47 It sounds like we don't need that span, right? Did I get it right? We want to replace it with an attribute, and we would put this attribute on
Something.
Sergey Sergeev 00:56:00 Yes, so I was thinking that we still may need the workflow span, invoke workflow, which is different from invoke agent, or from agent spend.
And take another… The request might be to introduce that conversational route, or whatever.
Mark Ceruto.
On both, workflow and, on agent spends.
Liudmila Molkova 00:56:48 Can we… Maybe we've done it before, I'm super sorry. Can… can we… Create the table of…
What are the SDKs?
What concepts they support, which would… have…
concept similar to workflow, which wouldn't.
And it… it doesn't need to be in the PR, it can… I mean, in the… in the files themselves, it could be in the dis… just in the description.
I… Just wanted to… sorry, sorry for putting Trask on spot.
I took liberty to merge this friend, because it was obvious.
And you see that there is an analysis of which Things have the concept.
And there is an analysis of existing patterns and semantic conventions.
I'm going to say that reviewing this PRS is trivial, like, you know what you're signing up for and what it's applicable.
Cheer.
So, if we could have some table that lists these things, and lists the concepts.
They… that exist, and…
Terminology used, and then it's trivial to say, okay, this makes sense across the board, or it's the specific framework that it would apply to?
Sergey Sergeev 00:58:26 It was an action, I think, on our side, to show at least a few
Frameworks which we've looked at, and what it will look like in those frameworks.
Liudmila Molkova 00:58:45 Okay,
So, it seems like we don't have time for anything else. I'm super sorry. So, Nakumar, I think you've done a lot of work. Can we… can I put it for the next meeting to be the first topic we discuss?
nagkumar 00:58:59 Yeah, sounds good.
Liudmila Molkova 00:59:01 Yeah, thank you, and sorry about this. So, there are… a bunch of PRs that Neat.
Review.
Surya Teja 00:59:14 Yeah, yeah, Lidmula, that's from me. The reason why I posted this here is because I will be open more… opening more PRs, because I have been trying to decrease the amount of,
code review as much as possible. So, after these three PRs are merged, 4 more, 6 more PRs are going to be open for OpenAI Response Instrumentation and Anthropic Messages Instrumentation. So, is there any strategy that I can work with, so that I can work with, the,
merge people to merge these, PRs after I get feedback? Because what's happening is someone else is coming back and saying that, can you… you reviewed the Anthropic PR, and someone else came back saying that, can you please reduce the lines of code so that
We can merge at P. And so it's… context is being lost. I'll be shortly.
Liudmila Molkova 01:00:06 Hmm.
Aaron Abbott 01:00:10 Was the 17,000 lines mostly just, like, the generated code, or did it have kind of everything in it at once?
Surya Teja 01:00:15 It only had the,
Cassid files were the bulk of that. This instrumentation covered both the stream function as well as the create function.
Aaron Abbott 01:00:28 Okay.
Surya Teja 01:00:29 So, I removed the stream function and, completely kept only the create function.
And now, if I need to open a few more PRs, it's going to bulk up the PR workload on maintainers.
Aaron Abbott 01:00:44 Yeah, I think… I think the feedback was…
like, usually multiple people try to review, so it was probably disturbing that, like, I,
Yeah, I'll, I'll respond on Slack to you, we can figure out a way forward.
Surya Teja 01:00:58 Yeah, so Aaron, can I message you on the side whenever I'm opening a PR and I get it reviewed from Ludmila or someone from the SIC team so that I can work with you and merge it? Because I don't know anyone else whom should I… I should work with for merging them.
Aaron Abbott 01:01:12 Yeah, sure.
Surya Teja 01:01:16 Bothering you.
Aaron Abbott 01:01:17 No, that's alright.
Surya Teja 01:01:18 Sorry.
Aaron Abbott 01:01:19 There's other maintainers too, but I think I might be the only person looking at Gen AI stuff at this point.
Surya Teja 01:01:24 Yeah, I mean, you helped me merge two more PRs, that's the reason why I wanted to reach out to you. Nothing else, but sorry for bothering you.
Aaron Abbott 01:01:30 That's alright, let's, let's chat offline.
Surya Teja 01:01:33 Yeah, sure, thanks, Eric. See you.
Aaron Abbott 01:01:35 Thanks, man.
Surya Teja 01:01:36 Excellent.
Aaron Abbott 01:01:36 Bill.
Liudmila Molkova 01:01:38 Yeah, thank you, and we are out of time.
RNAC… you're working on MCP, that's awesome.
Aaron Abbott 01:01:46 Yep, I can, leave an update in Slack or just chat about it next week.
Liudmila Molkova 01:01:51 Yeah, thanks a lot. Sorry for being late.
See you around!
Aaron Abbott 01:01:55 Later.
