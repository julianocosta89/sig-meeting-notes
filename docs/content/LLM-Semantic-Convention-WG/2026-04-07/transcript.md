SIG: LLM Semantic Convention WG
Date: 2026-04-07
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:58 Hello, hi folks, how are you?
Minghui Zhang 00:02:07 Oh, hello, Mila.
Liudmila Molkova 00:02:09 Hello!
Minghui Zhang 00:02:10 you.
Liudmila Molkova 00:02:11 I am good, how are you?
Okay, let's see…
Minghui Zhang 00:02:18 Mute, I'm doing well.
Will Truska come here?
Liudmila Molkova 00:02:25 Yeah, let me ask if he… if he's coming.
Okay, I pinged him… I pinged him, let's see if he's coming.
Oh, let's see… Okay, we have a lot of things.
In the agenda.
Minghui Zhang 00:03:50 So I have left… I have left a multi… topic here.
Liudmila Molkova 00:04:00 Yeah, it's okay.
What is your time zone, or which time zone we're recording this in? Anyway… I'll just leave the Pacific.
Minghui Zhang 00:04:17 I would change the… I would change it to someone.
Liudmila Molkova 00:04:22 Okay.
the… Awesome, thanks.
Okay, I hope… that Trask will come, if he will, we'll talk about conformance testing.
So… This seems to… Be the topics you've added?
Minghui Zhang 00:05:16 Yeah, but we… maybe we couldn't, discuss them more. So, Let's, let's push… let's try to push it, and, if, if some issues, could… cannot be discussed today, it, it will be fun.
Liudmila Molkova 00:05:39 Okay.
So let's just take a quick look. Like, what is the, like, the top, the top thing you want to discuss?
Minghui Zhang 00:05:50 No, let's… let's go with the agenda.
Liudmila Molkova 00:05:55 Okay, so, like, what would be the first priority for you?
Minghui Zhang 00:06:00 Mmm… No, sorry, I, I, I, let me… catch up this issue, I didn't notice it.
Liudmila Molkova 00:06:14 Which one?
Minghui Zhang 00:06:16 maybe the second one, so the… Let's start with the second one. Yes? This one?
Liudmila Molkova 00:06:27 Yeah, did you address tasks, comment?
If you did, then…
Minghui Zhang 00:06:47 So I resolve all the comments.
No.
Liudmila Molkova 00:06:54 Let me take a quick look… I don't think… -Oh, Russ didn't approve, but let's see.
So I have to definition… awesome!
Another example… I have… Notebook… Go to YAML… Go definitions… Right.
Follow… Required may provide.
And… The only substantial comment.
Minghui Zhang 00:07:55 U.S.
Liudmila Molkova 00:08:00 You might need to regenerate it, it seems something get merged.
Minghui Zhang 00:08:05 Okay.
Let me fix it.
Liudmila Molkova 00:08:15 Twice this one?
Verse 6, 10.
Aye.
I mean, it looks good. I don't think we need to wait for Trask's approval, just make sure to address it, and I'll merge it.
Minghui Zhang 00:08:48 Okay, I will fix the, conflict.
Soon, so…
Liudmila Molkova 00:08:55 Yeah.
Minghui Zhang 00:08:56 once I finish it, I will, ping you, and let's push you to… As soon as possible.
Liudmila Molkova 00:09:04 I said, yeah.
Minghui Zhang 00:09:05 The sun broke.
Liudmila Molkova 00:09:10 Go ahead.
Minghui Zhang 00:09:11 I know this, this PR, blogs, this, yeah, this, this work.
Liudmila Molkova 00:09:20 I mean, the moment you do this, this PR when getting blocked, it's actually awesome that you had a PR that specifically helps here. It would be cool if you can review it as well.
Minghui Zhang 00:09:36 Yeah, I will review it.
By the way, could you, could you address the issue that I didn't be noticed, when someone changed their… when someone… when someone changes the, codes in OpenTelemetry due to Gene AI, because I… I can't, receive the… the notice, or… I'm not… I'm not one in the reviewers, so I… I didn't know who, who provide a new PR.
Liudmila Molkova 00:10:20 Yeah, so you don't get any notification, because turns out that I think GitHub changed it. You cannot even assign things to you, Because you're not… you don't have right permissions on this repo, so, we are… What we're going to do, one way or another.
We'll need a, component or code owners, and you would be part of the, group that works on GenAI, and it will have right access to this reappo, or the new repo.
So, like, let's, we're trying to figure out how the newer repo story would look like, and let's, let's resolve it.
Done.
But you are not triggered just because you don't have right access to the repo. And we don't have, like, a good model for someone to become… to get right access without becoming an approver as well.
But, wait, so, can't I… I can't… I mean, I can… Add some people here, just not… Not you.
No, wait, my theory doesn't hold.
So these people are not approvers, but I can add them.
Minghui Zhang 00:11:43 Maybe they have, they have left some comments in this PR, so you could, than this PR to them.
Liudmila Molkova 00:11:56 Yeah, can you just leave a comment?
Yeah. Or.
Minghui Zhang 00:12:02 Okay, I will, I will leave it. But it didn't resolve the issue that I can't, I can't receive the notification, from the new PR. Maybe… maybe I need to be… I need to become, a re-approver.
Liudmila Molkova 00:12:25 But it, it would be weird, but, yeah.
Let's see… Let's just take some random pure.
Let's see who can I assign. Okay, these are the order.
me and somebody else can I assign?
Okay, yeah.
So you don't know, whether you… Need to review anything in this report?
Minghui Zhang 00:13:09 no, yeah. Up to now, I… I will… I will, catch up the… issues and PRs that, that's changed, in the last week, every month, every Monday. So, I will, once I… I noticed the new PR, or something changed, I will review it, but maybe something missed.
Liudmila Molkova 00:13:41 Yeah, of course, yeah, and you don't need to review everything, but maybe I can… what I can do on my side, I… I have… I checked the notification, GitHub notifications, and if I see that, there is something… that needs your attention, I can just mention you. So let's see, component owners… You are on… What's your Gen AI, and only your Tilgene AI.
Minghui Zhang 00:14:12 But I didn't see… I didn't… I think it didn't work now.
Liudmila Molkova 00:14:18 Yeah, it doesn't work for you, because you're not… you don't have the right access to the repo.
So, as I do my triage, I can just mention you, let's say… This is Jenny Yai.
to sphere… It's not… it's not a requirement to look, it's just a notification for you, that that's it.
Minghui Zhang 00:14:45 Okay, thank you.
Liudmila Molkova 00:14:46 I will… I will do my best on this, and there is, there is a few, I would love to.
Selfishly get your review on… Mine.
Minghui Zhang 00:15:02 No, no, it works for, for us.
Liudmila Molkova 00:15:12 And, this helps you… Get more visible in this repo.
and be a contributor, and it's the path to becoming an approver, as you review PR source and changes and everything together.
Minghui Zhang 00:15:30 Okay, okay, thank you.
I will do my best.
Liudmila Molkova 00:15:34 Yeah, thanks.
Cool.
Minghui Zhang 00:15:40 Okay, so… Hmm… The third one is about the, confirmance test.
that I will talk with, Chask, but I have received, his, reply, so let's skip this, this issue. I will send a PR in his, repository.
Liudmila Molkova 00:16:05 Nice, nice. See, you already discovered it all! Nice.
Minghui Zhang 00:16:11 Yeah, this is an awesome repository that we really needed.
Liudmila Molkova 00:16:19 That's nice.
Cool.
Man… The skills fun.
Minghui Zhang 00:16:28 So this is a very, very big, proposal, and let's, let's skip the, foreigner, let's, let's, let's skip the pro… provide, scenes, and, go, yes, go, go there.
Here is, so, so this, this issue is, provided by our… by my colleague. So I have discussed with him, intern… internal… internally, and, we have, new.
implement about this comment… semantic conventions. So, here is the proposal, the new proposal. You could just see my… A look at my, comment.
There is the first comment.
Liudmila Molkova 00:18:00 So, okay, this one.
This is the proposal.
Minghui Zhang 00:18:04 Okay, yes. So, we didn't want to, define a new span, with a kind… with an operation name, like invoke skill or load skill. We only want to add some, necessary attributes into the, the existing span named the, executed tour. So, we… we just capture the, skill metadata in this, in the… in the tour span.
So that's… that's our new, proposal.
Liudmila Molkova 00:18:50 Cool, so then, essentially, instead of creating a new span, when you have information about skills inside a tool execution, you would stamp the skills there.
Yeah.
Would there be… and it sounds, it sounds totally cool, is there any difference between skill name and Tool name, like, there are multiple tools per SKU, right?
And the same as the description.
Minghui Zhang 00:19:23 Hmm… So, a tour, maybe a commenter, like, his name… his name may be, Read, read file or low skill, but the skill name is a specific skill.
like, browser use or browser visible. So, it depends, it depends on the skills name, and the skills name and the source name is… is not, is not when seen.
Liudmila Molkova 00:19:59 Yeah.
How would… True.
Know that it's being executed in the scope of the skill.
Minghui Zhang 00:20:17 In my opinion, the skill will be loaded… will be loaded in, for, execution. So, It's, yin… Yin's this, In this case, the tour… the tour execution is, refers… referred to the, refer to the specific skill, so we should, I think we should identify this behavior.
Liudmila Molkova 00:20:59 Yeah, I mean, just from a practical standpoint, let's say I'm the MCP instrumentation, would I know?
Or, like, where would this come from? Like, let me probably ask a different question.
What is this?
Who will do this? Which instrumentation?
Minghui Zhang 00:21:23 I think, maybe, like, we should do this in the instrumentations or agent framework, like Lynchron, or some Lama Index, or some errors, instrumentations, because their skills, the, the, the, the skills is, designed by those, agent framework, so we should do that in these instrumentations.
Liudmila Molkova 00:21:58 Yeah, so, what we've been doing lately… Let me find it.
R.
So, since there are so many different libraries and so many different, ways to do things, I tried to create some analysis of, like, what What can we instrument, which libraries?
And what are the… what is the terminology used? I think for skills, it's pretty consistent, but it would be good to understand, like, what are we targeting, who would emit it, and whether it's feasible to instrument it.
Minghui Zhang 00:22:46 Okay, so, maybe I should add a list like this, right?
Liudmila Molkova 00:22:53 Yeah.
And I think Trask has a cool thing in his, conformance.
thing that's… And… skills, minimum support request… Oh, under GitHub, of course.
Okay, so this, I think, is a different one, the prototyping skill.
Oh, here's the task, I started talking about your skills, and here you are.
Minghui Zhang 00:24:03 Hey, hello, Trask.
Liudmila Molkova 00:24:09 is…
Trask Stalnaker 00:24:13 Hey, Minghui! Hey, Hashin!
Hello, Gatlin Miller!
Liudmila Molkova 00:24:19 Your camera is off, but…
Trask Stalnaker 00:24:21 My camera's broken.
Sorry, I need to reboot. Apparently, probably.
Liudmila Molkova 00:24:28 Yeah.
So, we've been talking about, the, the issue that, the inquiry brought up to add.
Skills details to the toolkall.
And I've been trying to guide, And through the… your skill that you added for the prototyping?
Baby, you can talk about this.
the research part. If you want to share, feel free to take over.
Trask Stalnaker 00:25:00 Yeah, definitely.
I will share… I think it's… making… I think you have to unshare for some reason first.
Liudmila Molkova 00:25:18 Yep.
Trask Stalnaker 00:25:19 Thanks.
Alright… Hi, Tiffany, by the way.
Liudmila Molkova 00:25:33 Sorry for calling y'all.
Tiffany Jernigan 00:25:36 I see you see me lurking.
I was planning on joining this earlier, and then I lost track of time.
Trask Stalnaker 00:25:45 Same.
I just made it, like, 3 minutes ago.
And apologies for my camera, I'll just stop the video so that it will, I… so you won't be able to see me talking with my hands, but that won't stop me.
So, yeah, I saw Minghui, I saw you had opened this, this is you, right? I always forget, Cirilla, yes.
Yeah. And… So yeah, definitely we can work in here. I'm… hoping to move this to the OpenTelemetry org in the next week or so.
But we can definitely get started. I've been… I've been going through pull requests, per… Initially I was pushing to main for a while and clobbering stuff, but I've been going through pull requests myself for a couple of weeks here, so, it should be, you should be able to 7 PRs.
So, one of my goals… well, first, let me show you… what it produces… So let's take something like inference bands, where there's lots of instrumentations.
So it'll take the library.
let's say Google, and then there's… Some native instrumentation it has, and it'll… Show which attributes it emits.
Maybe this should float or something, so you can still see those, attribute names.
Instrumentation, whether it's open inference, or open LLMetry, or hotel contribution that we have.
Native is built into the… piece, the library itself, and then I have, what I'm calling prototype, instrumentation, which is… Basically, manual instrumentation.
And it's… kind of use… I find it useful… To demonstrate what is capturable.
So, for example, I don't know, I haven't really looked too carefully, but… oh yeah, GenAI tool definitions.
I added recently… And so… you know, it is capturable for Google, but, oh, actually, maybe I might just not be testing, oops.
Happened.
I may not be… Running the… the tests… Might not cover… Tool definitions in that case.
So… Yeah, so… and then the… so there's a couple… there's… I think there's two main points to… two main purposes of this repository. One is just conformance, and for that, I'm kind of planning to strip out probably these prototypes, Because the goal is just to highlight which instrumentations out there are conforming to OpenTelemetry semantic conventions, with the goal of… we want to kind of pressure people into… into supporting OpenTelemetry semantic conventions.
Because there's a lot of problems, right? Users are running into a lot of problems right now, because of the fragmentation of the space.
And so, if everybody can emit the semantic inventions, that would be amazing.
The other goal of this repo is, for prototyping semantic convention PRs.
So let's take… Something like… your, tool definitions PR.
So I took that, Yesterday, and… I actually have a… Skill here, for building a prototype from a semantic invention PR.
And so, I fed the… your PR into that skill, and… more or less, it came out with this PR.
Once I then realized I was never capturing tool definitions to begin with. But this is where it helps to have the prototypes already.
In the repo.
Because it makes it easy to then see… Oh, okay, for .NET, you know, this was what it looked like when we were following source schema, and now this is what it looks like when we're following the proposed standard schema.
And… Then we can… There's another skill for… Evaluating a prototype.
Which will sort of evaluate that it's actually getting these values, because when it first… when I first ask it to, like, prototype it, it'll just, like, hardcode the things into here.
And so it's… Not as obvious that it's something that's really coming capturable in reality.
And so, sort of, that's where these… the skills and evaluating them helps.
And so, I was trying to get this ready before, our meeting to, well, I think it's ready, but, I was gonna post it to your PR, and I'm also gonna post probably, just… After this meeting, I'll post I think I'm pretty much done with the prototypes for… I had posted this one to the PR already, the SEMCOM PR, but now I have one more.
prototype here for the reasoning token semantic convention PR.
Liudmila Molkova 00:32:52 Did I dream it? But I think you had a skill for writing semantic conventions pure. But, like, for doing the research.
Trask Stalnaker 00:33:03 Not for the writing the semantic invention itself.
It was a… it was… what I had shared with you before was, in this repo, it was, I had previously called it a conformance skill.
But I changed it into a prototyping and evaluating prototype.
Liudmila Molkova 00:33:30 Oh, capturability study.
Trask Stalnaker 00:33:33 Oh, yes, yes.
Liudmila Molkova 00:33:39 Is it now part of the prototype?
Trask Stalnaker 00:33:41 Yeah, so the… well, capturability studies now evaluate prototypes, more or less.
That's what that was, and then Prototype will actually… you can feed it a semantic convention PR, and it will… Apply those best practices while it builds the prototype to begin with.
So that hopefully Evaluate Prototype will say it's good.
Liudmila Molkova 00:34:10 Yeah, we've been talk… oh, sorry, go ahead.
Minghui Zhang 00:34:13 No, sorry. So, maybe we… once… once we, send a proposal or an issue in the semantic conventions, we need to, send a PR here.
with these skills and, generate a prototype, right?
Trask Stalnaker 00:34:34 Yeah.
And so that will kind of help to make the semantic convention PRs more concrete.
Yes.
Minghui Zhang 00:34:45 Definitely.
Trask Stalnaker 00:34:46 Which… is an area that I have struggled with as a newcomer into this area.
So, yeah.
Minghui Zhang 00:34:58 Awesome. I will… I will try to, give you some prototypes.
in another issue that I have, sent.
Trask Stalnaker 00:35:13 Cool.
Huxing Zhang 00:35:15 Hello, hello, trust. Can you hear me?
Trask Stalnaker 00:35:17 Hey, Hoshin.
Huxing Zhang 00:35:18 we…
Trask Stalnaker 00:35:20 Yeah.
Huxing Zhang 00:35:21 Yeah, yeah, my Zoom setting is something wrong with that, and so I can't… I've figured out, once I open my camera, my zoom will… make me log out. I think there's something wrong with it, so I… Oh, no. So I turned off my camera, so I will… yeah. I have a quick question about your, prototype, so, so, your prototype skills means that, your, you will automatically use AI to implement that semantic convention with your, the existing instrumentation in OTO REPL? Is that, is that true, or…
Trask Stalnaker 00:36:02 No, so that would be a step… past this.
Which would also be great. I hope that we can… I haven't focused yet on the hotel, the Contrib instrumentation yet.
I think, Ludmila and I have been chatting and have some… Thoughts that were… Trying to bake up into a real plan.
But for now, this is just focused on… Improving the semantic invention.
PR work.
Huxing Zhang 00:36:47 So my question is, how, how, how does the… The prototype code come from?
Trask Stalnaker 00:36:56 So the prototype, it's, it's actually just a manual instrumentation prototype.
Huxing Zhang 00:37:03 Oh.
Trask Stalnaker 00:37:04 If that makes sense. So let's… let's go and look at one of them.
Huxing Zhang 00:37:09 So you… basically, you will fork, the target that you want to implement, and add some code to that ripple.
Trask Stalnaker 00:37:21 No, so it's not a native, prototype. It's literally… let's see, let me show you what it looks like.
so… this… This is a prototype for, OpenAI.
Huxing Zhang 00:37:39 Okay.
Trask Stalnaker 00:37:39 And so what it does is it makes, if I can find inside of all the telemetry.
Here it's creating… The… Chat completion, getting the response back.
And all of this is, right, the manual instrumentation of start span, set the attributes, end span, set the attributes.
Huxing Zhang 00:38:11 So the OpenAI code has been forked in your Ripple?
Trask Stalnaker 00:38:15 No. This is just, like, think of a user who's using OpenAI.
Huxing Zhang 00:38:22 Oh, okay. There.
Trask Stalnaker 00:38:24 Purely manual instrumentation.
Huxing Zhang 00:38:27 Actually, you… sounds like you write the test code. You depend on OpenAI, and you add some manual instrumentation.
Trask Stalnaker 00:38:38 Exactly.
Huxing Zhang 00:38:38 Okay.
Liudmila Molkova 00:38:40 But you add it with an assumption that it, like, it's essentially a wrapper around this underlying call on line 31, and it only knows what you… what that call knows, plus maybe some… some things they can point.
Trask Stalnaker 00:38:56 Right, so there's some things that are acceptable to hardcode.
But other things have to be, like, you have to be able to trace Here, that, oh, okay, this is coming from the real thing that's fed into the… The OpenAI chat.
Huxing Zhang 00:39:17 Okay. What I'm thinking is, I… when we are trying to propose some new semantic convention, we… we can bring our implementation. Basically, we… we, Maybe, or we also have already implemented that in our practice, so we can bring our implementation to that semantic convention.
And for you, for the review… other reviewers that… To have a better understanding of how we are doing.
Trask Stalnaker 00:39:53 So the thing that's useful, I think, about the manual instrumentation Is that it's sort of easy to read.
Huxing Zhang 00:40:03 Oh, okay, alright.
I know.
Trask Stalnaker 00:40:06 Yeah, you don't have to… you're not talking about all the, you know, monkey patching and other things, abstractions, just… yeah.
Liudmila Molkova 00:40:17 Also, I think the common question and concern that, okay, this applies to link chain, does it apply to anything else?
And I think this skill allows you to prototype for multiple things at once, right? And it would be a good litmus test to say, okay, it does not apply to Crew EA in the same way it applies to link chain.
Trask Stalnaker 00:40:41 Right, and then you can, from the prototype, from the build… You can actually… you can download, it attaches the dashboard.
locally, so you can open that up and view what, which new boxes will be checked. Although, probably we could do a better job of displaying that, or even… the… prototype evaluation skill. Actually, it prints out a pretty decent… I was thinking of almost, like, having this hook into the PR and dump its output into the prototype, because it actually outputs a fairly decent summary.
Huxing Zhang 00:41:34 Okay, I'm just wondering if there's some case that, Manual instrumentation couldn't… To, be… in order… in order to get some… data, maybe, I don't… there's some limitations.
The manual instrumentation could not get the… Actual… data. I think… I don't… I'm not quite sure right now, but I'm just wondering if there's some case.
Trask Stalnaker 00:42:05 engine.
Liudmila Molkova 00:42:06 There… there… I'm sorry, go ahead.
Trask Stalnaker 00:42:08 Oh, no, please.
Liudmila Molkova 00:42:10 Yeah, so there could be cases, like, what we started talking with Zinghoi before you joined Trusk, that, That we want to stamp skill information on the tool execution.
And in theory, with auto-instrumentation, you can inject the skill information into context, and let's pull this information from the context. The same story, maybe, with users and sessions.
I think this is a good thing to know. It doesn't mean that the semantic conventions PR is rejected, but it's good to know that there is some special treatment that's needed for some properties.
Huxing Zhang 00:42:53 Yeah.
And I…
Trask Stalnaker 00:42:55 I think it would be okay in a prototype to… Cause, you know, to add something extra, like, that's, you know, okay, I need to read from the file system and look at what skills are there, or I need to… Even hard-coding something, or at least adding a comment explaining that this would be capturable via Some kind of auto instrumentation.
Liudmila Molkova 00:43:33 But I think it also helps us with the review process, because in a lot of cases, I think what you also feel the pain with is that Nobody has enough context to provide useful feedback on the… issues or PRs, but when you provide the analysis and some prototypes, it's much easier to review.
It also shows that you've done the research, and you analyzed a couple of different libraries, and here is the mapping.
It's been tremendously helpful lately, thanks to Trask's effort.
Minghui Zhang 00:44:08 Yes, thanks to Chask.
Huxing Zhang 00:44:13 Cool. Thanks.
Trask Stalnaker 00:44:20 Yeah, Well, I'm planning to share… In tomorrow's… just kind of what we went over in tomorrow's Gen AI SIG.
meeting… And I'm… I'm planning to start publishing these prototypes to the Semantic Convention PRs.
So yeah, definitely, would love any, you know, any… any thoughts or PRs, whether it's prototypes, or adding new instrumentations, or looking over any of the existing instrumentations that maybe you're particularly familiar with, because You know, 95% of this repo was vibe-coded.
And so, you know, definitely domain expertise is, is… Wanted.
Minghui Zhang 00:45:23 And I will definitely web code and… Stop y'all here.
Trask Stalnaker 00:45:30 Awesome.
Huxing Zhang 00:45:33 Yeah, actually, I think Ming Hui had proposed to add the one of them, our repo, is called Long Suite. We have, many instrumentation there. Maybe we can… some of them can be… could be referenced in your, conformance, test.
Trask Stalnaker 00:45:51 Yeah.
Minghui Zhang 00:45:52 I will send FTR to, resolve this, issue. I will, add the items into the, Into, into the compre… Into the list, into the metadata.
Huxing Zhang 00:46:09 You know.
Trask Stalnaker 00:46:10 Yeah.
Huxing Zhang 00:46:10 I want to make some explanations to this repository, because you know that the Python repo, there's the PR get, gets merged quite slowly, so we… add some implementations in our repos. We, we, actually, we want to, put, contribute them to… into OTEL as… quick, as soon as possible, but, you know, once there… there's a more easier way for us to contribute, we can, yes, make these instrumentation to put in there. So this is, like, a temporal… temporal… temporary… storage?
Trask Stalnaker 00:46:53 Sure.
Huxing Zhang 00:46:53 We call it an incubator. Incubator, incubation.
Thank you.
Trask Stalnaker 00:47:00 Great, yeah, and stay tuned, hopefully, in the next couple weeks, we'll have some better… plans as far as what we can do from the OpenTelemetry side to speed up the, the Python, GenAI instrumentation.
Liudmila Molkova 00:47:24 Yeah, by the way, Would we… would you consider… contributing the Java, because I think there is no pull on, like, it seems… the Java instrumentation repo is quite fast and nice and has a lot of tooling. Like, what would it take to contribute this one?
Huxing Zhang 00:47:47 Yeah, sure, we can do that. I think Steve is working on some sort of Gen AI stuff.
Already.
And, yeah, we can definitely do that.
Liudmila Molkova 00:47:59 Nice. And for Go, the story is interesting, but yeah, I don't think we have a strategy for Go. You would be probably the first library.
And, the Go Country has some… Policy around, instrumentations.
But… we will need to figure it out.
Huxing Zhang 00:48:20 Yeah, actually, we have the Go compile time instrumentation set there, and then there's the Ripple. We can contribute to that.
Not necessarily also a possible way for us to do.
Trask Stalnaker 00:48:37 Yeah, and anything, Minkley or, Steve can do in the Java repo now around Gen AI, I know I was not very useful in that space in prior PRs.
But now that I have some, some baseline, I'm definitely interested in reviewing and helping any Gen AI Java PRs get through.
Huxing Zhang 00:49:08 Okay.
Minghui Zhang 00:49:09 Okay.
Liudmila Molkova 00:49:15 Nice.
So we have 10 minutes left, and Minghu, you have a lot of other things on the agenda. Do you want to talk about them?
Minghui Zhang 00:49:25 Let me see, sorry, I think, Maybe we, we could, we could have a discussion about the, 1, 2, 3, 4, 5, the, the, the fifths.
When?
And let's skip the second… the sixth and seventh… So, What I want to… what I want to propose is that we want to, We want to, propagate the agent contest in the, existing, metrics, so we can identify what an agent, actually called… like, ARM, or tours, or other, other, scenes. So, we could, we could, analyze the metrics with, we, we could group the metrics with, agent.
We could define the… what the… what the agents do.
what a specific agent do?
So, let's add the… attribute, like a gene AI agent ID to these metrics.
Liudmila Molkova 00:51:01 You're… okay, so to… by metrics, you mean the… this metric?
Minghui Zhang 00:51:06 Yeah.
Liudmila Molkova 00:51:07 the token, token count. Yeah, so the agent name, probably, or agent ID, or maybe both.
Probably in the name, because ID is high cardinality. Yeah, I think that this is trivial, and we should do it, I also stumbled upon it.
Maybe the version.
Minghui Zhang 00:51:30 Yes, but I think it may be, need more, documents about that, because we should, We should define, behavior to propagate the, context, in the agent, because agents, we, we… We emit the, invoke agent span, but once the span, ends, or once we, throw, child span, we will lose the agent ID and agent name, so we should, inject that… we should propagate the metadata into, with, with Contest, so that we can, so that we can identify the metrics.
Liudmila Molkova 00:52:25 So, wait a sec, so there is the invoke agent span, right? Let's say, I don't know, agent one. Then there is an inference pan here.
Minghui Zhang 00:52:36 Yeah?
Liudmila Molkova 00:52:39 You want to stamp the agent ID here.
Do you want to propagate when you make… when you're saying propagate, Do you mean… Record something here, and stamp it on this pen.
Minghui Zhang 00:52:58 Yeah, I think so.
Maybe not in spam, but, in metrics, we need that.
Liudmila Molkova 00:53:10 And in metrics, because… you would… Want to know… why would you have it on the inference, let's say, duration? Maybe I understand about the tokens, but… Why would you want it here?
Minghui Zhang 00:53:32 So, in some cases, we want to know, we have, we have multiple agents, so we want to know, each agent, each agent, spend, how many tokens? We want to know the, the core… how many times to RAM or some air scenes. We want to analyze, the metrics with, In the, we want to add the dimensions.
Of agent to this, matrix, so that we could, identify, some specific agent.
What they are doing.
Trask Stalnaker 00:54:30 To equate it to, like, even HTTP land, that would be, say, taking HTTP route.
and propagating that down to your database metrics, so that you could see your top queries by HTTP route.
Minghui Zhang 00:54:50 Yes, definitely.
Trask Stalnaker 00:54:51 cost per… by HTTP route.
Liudmila Molkova 00:55:02 I ran it.
This is…
Trask Stalnaker 00:55:05 I think that's the context, scope, attributes, sort of.
Liudmila Molkova 00:55:08 Yeah.
Yeah.
I'm… I keep thinking whether it should be, like, an application decision, or… an instrumentation decision.
because… Some… in many cases, people would, from, like, from duration perspective, like, how much time that agent takes.
like, if you stamp it on the agent ID on the underlying LLM calls.
Wow, how… it would be hard to use.
Minghui Zhang 00:55:50 So why not, inject them into the hotel contest, where it works?
Liudmila Molkova 00:55:58 It works, but you would, Create some duplication that's not… not always necessary.
And technically, we can find means to make it work, but whether, like, should the instrumentation invoke agent instrumentation, should… should it do it by default?
Minghui Zhang 00:56:24 Maybe it could be optional, but… I think… Hmm.
Trask Stalnaker 00:56:34 I've heard the same, of… even on just spans. I mean, I know spans are… should be easy to join.
Up to the parent and get the agent ID.
But… I've still heard people wanting to… stamp the agent ID all the way down, basically onto everything, because they… they want to… Easily be able to… aggregate over… The agent is the primary thing they care about.
Minghui Zhang 00:57:15 Yes.
Trask Stalnaker 00:57:18 But I don't think we have a good… really precedence… in semantic conventions or open telemetry for… doing that.
At least by default.
Liudmila Molkova 00:57:34 Yeah.
Minghui Zhang 00:57:38 I've…
Trask Stalnaker 00:57:39 Kind of intrigued by the context-scoped attributes.
proposal as… Potentially something that could… unlock, like, semantic conventions.
Could make certain attributes optionally… I haven't quite… Fuck.
Liudmila Molkova 00:58:07 No, else it reminds me. It reminds me entities and session ID.
Because you would have a few agents.
An adjunct is an entity.
And you would create a tracer that's specific to that entity, and it will get the entity through resource… through entities, through the source attributes.
Trask Stalnaker 00:58:28 That's interesting.
Liudmila Molkova 00:58:35 But then, you would need… okay, this is more complicated, because this is one layer talking to another layer.
They need to share the same tracer.
Minghui Zhang 00:58:48 Yes.
So, so it will, it will work, well when we just, resolve this, issue in… and auto instrumentations, but when we have multiple twisters, it will be complex.
Liudmila Molkova 00:59:16 Yeah.
So I think that the context called… it's the proposal being discussed, well, it's resurrection, it seems.
It's the second life of this proposal, I… I… Don't know when and how it will be merged, but it's definitely not in the… in any of the implementations.
So far.
But we don't really need generic attributes to make it work for GenAI.
It could be cross-communication.
Across instrumentation communication.
Minghui Zhang 00:59:58 So, hmm… So, what should I do if I want to push this, Pushing this issue forward.
Liudmila Molkova 01:00:10 I think the good plan would be to prioritize the things that you want to work on.
And just, like, when you send… keep sending proposals to semantic conventions, we just never do them, because they are difficult.
It's not easy. And then, if you prioritize a specific issue, and let's just work on it through, and then let's move on to the next one.
How do you feel about this?
Minghui Zhang 01:00:37 This one will…
Trask Stalnaker 01:00:38 Honestly, it's gonna be challenging. I'm not sure if we have… I would probably, if you have a specific need for it.
I would probably think more about What… not semantic conventions, but what can we, like, can we add… flags in the instrumentation, would that be acceptable to people, or is there something you can do in a span processor, to copy span attributes down. I know that that's something that I've done before, is have a span processor that automatically copies like, the agent ID down to its child spans.
And… It's a little challenging to get it onto metrics. OpenTelem… Java has that capability through an incubating API, but other languages don't have metric processors yet that really allow that.
But that… that's a proposal, actually, that I think There is some weight behind right now in the spec.
So, probably you'll need to get creative if you are trying to solve this.
You know, in the next couple of months.
Minghui Zhang 01:02:08 Yeah, so, okay, I will, I will be involved in the… in the PR, in the discussion of the PR, of the OpenTelemetry specific… specification, and, I will provide more, comments or, points.
Under the PR first. And, second, I will… try to, show, implementations in the long suite person agent, which is named, Open, Long Suite UTO Geni, the fork of the OpenTometer 1. Open Animetry 1, so I will… Ed is a… agent IDs or session IDs in the… I will try to show an implementation here, and let's discuss it once the Specification… Get merged, or, get some… Get some chinsed.
Liudmila Molkova 01:03:26 Yeah.
Minghui Zhang 01:03:28 push it forward. Sorry, go ahead.
Liudmila Molkova 01:03:33 We are, over time, it would be cool if you read the, the, this ADAP.
In the specification, because there is discussion there on whether instrumentation should be… even setting context scoped attributes. And, like, having your opinion recorded there would be useful.
Minghui Zhang 01:03:55 Yes.
Okay, thank you.
Trask Stalnaker 01:04:00 Yeah, good to see you.
Liudmila Molkova 01:04:02 Yeah.
Minghui Zhang 01:04:03 Good to see you.
Trask Stalnaker 01:04:04 Bye.
Liudmila Molkova 01:04:04 Thank you. Bye-bye. Bye.
Minghui Zhang 01:04:06 Bye, Ben.
