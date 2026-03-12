SIG: Android SIG
Date: 2026-02-03
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

Jason Plumb 00:03:37 Good morning.
We will give folks a few more minutes to trickle in, if they do.
DavidGrath 00:03:51 Good morning.
Jason Plumb 00:03:54 Ayy.
Cesar Munoz 00:04:24 Good morning.
Often.
Hanson Ho 00:04:28 Hello?
Jason Plumb 00:04:29 Hello.
Cesar Munoz 00:04:31 I think it should be… I think it should be possible in English to say good day, you know? It's like… It applies to, you know, whatever time zone, no?
Hanson Ho 00:04:42 Yeah, it's a good day, just like you said.
Jason Plumb 00:04:45 You can say good day, it just sounds fancy. It just sounds… it sounds kinda… English.
Got it. It sounds kind of British.
Cesar Munoz 00:04:54 I see.
Hanson Ho 00:04:56 Or sarcastic. Good day!
Jason Plumb 00:04:59 Yeah.
Cesar Munoz 00:05:01 Okay, I guess I'll stick to it.
Good morning, afternoon.
Jason Plumb 00:05:08 Morning somewhere.
Alright, well, it looks like a pretty light turnout so far today. I only had one item to bring up, Because Severin from the GC reached out last week, or maybe the week before, and said.
Hey, it's a new year, I'm ready to maybe revisit this idea of having this account get created.
And not necessarily tied to one person. So… This was floated, I think, back in maybe November, maybe even earlier, and we have this… we have this tracking issue here.
On Android, let's see… oh, all the way back in May, whatever.
But this was, I opened this, to see if we wanted to do this with it not being just tied to me, right? And… So, Severin has, looks like he's got some cycles and wants to follow through with this, so… Oh, look at this. I ha- I don't think I've even seen that.
Yeah, so we need to work together to make that happen. Does anybody have cycles to do this with him? Because I'm honestly stretched a little bit thin right now.
And I could probably snooze it for another week or two, but I, you know, if somebody has time and… is able, that's why I put it on here.
Cesar Munoz 00:06:39 I'm not familiar with that process.
Let me see the link.
Hanson Ho 00:06:48 I can do it.
it's not a lot of anything active, right? It's basically… hey, work with Severin to make sure this created account and things are…
Jason Plumb 00:07:02 Yes. Yeah.
That's great. If for some reason, he insists on there being a maintainer, that is a possibility, I just don't know yet.
We can… we can work with him on that, though. He's super… he's super reasonable. And then the next steps after that are actually wiring up the thing into… our build system, probably. Like, there has to be something about our library that knows how to be tracked, right?
So there's some additional code or build work that has to happen after we have an account.
But it's probably pretty minor. I've never done it.
I hope it's pretty minor.
Jamie Lynch 00:07:46 I think very…
Hanson Ho 00:07:47 arrow.
Jamie Lynch 00:07:48 I think it involves, like, adding something to the artifact these days, so I think they've changed it a bit since we did it at Home Embrace.
Jason Plumb 00:07:55 Okay.
Hanson Ho 00:07:57 Sure, there are instructions, yeah, something that tracks it and tags it, I doubt it's anything… Fingers crossed.
Famous last words, I suppose.
If it needs a maintainer, I will loop you in, Jason, for the rubber stamp.
Jason Plumb 00:08:13 Yeah, that sounds lovely. That would be tremendously helpful. Thank you so much.
Cesar Munoz 00:08:18 Thanks, Hazel.
Jason Plumb 00:08:21 Alright, what else do folks want to talk about? What's been going on in here?
Github Actions were pretty exciting yesterday, if you noticed that.
Did you see this? Like, they had, They had a bad day yesterday at GitHub.
It wasn't just…
Cesar Munoz 00:08:44 I still want, but I…
Jason Plumb 00:08:46 Yeah.
Cesar Munoz 00:08:46 Okay, so it wasn't anything on our… yeah. Okay, so that's good.
Jason Plumb 00:08:50 No, it was all over the place.
Alright, this person submitted, PR. They asked to be assigned it, and I assigned them that. They've contributed a few things before.
And they dropped this pretty large PR, but they're currently fighting with themselves over this stuff, so I don't know.
Hanson Ho 00:09:13 This is the AI guy.
Jason Plumb 00:09:15 Yeah, yeah. So I haven't given this really much review, because he's got 100 comments from Copilot already, and I figure that's enough.
So maybe if that chills out, then I'll look at it, but… 16 comments.
Yeah.
I think this one was good. No, it wasn't this one. The other one got merch already.
The fragment of the fragment one. Yeah, this can… I think this is good to go.
Yeah.
Hanson Ho 00:09:43 So, just by reading the title of the PR, isn't it just what we were talking about, like, making gRPC a first class?
Configurable, on the… the… the easy-to-configure API.
Jason Plumb 00:09:58 It is.
Cesar Munoz 00:09:59 Yes.
Hanson Ho 00:10:00 Why is that gonna take a thousand lines?
Jason Plumb 00:10:03 Well, I would hope it doesn't.
But…
Cesar Munoz 00:10:09 I kind of saw a bit of it. It's kind of strange, because it's like, some lines are… deleted comments, or things like that, you know, and I'm not sure why that was a change. Right.
Jason Plumb 00:10:22 Yeah, so Copilot brought that up a lot in its comments, right? It's saying, You don't have documentations, like… I don't know, there's… yeah.
But as far as, like, why it's 1300 lines, you know, I'm not… I'm not sure.
I haven't reviewed it yet.
Hanson Ho 00:10:44 Okay, I…
Jason Plumb 00:10:46 Hi, Manuel.
Hanson Ho 00:10:50 Hey, Manuel.
Manoel 00:10:53 Can you hear me?
Cesar Munoz 00:10:54 Yes. Yeah. Oh, okay, now it's really neat.
Manoel 00:10:58 Hello, long time to see.
Jason Plumb 00:11:00 I know, stranger.
Hanson Ho 00:11:01 Happy New Year! Every year!
Cesar Munoz 00:11:04 Fair.
Manoel 00:11:05 It's been very rare.
Yeah, sorry about being away for so long. I was in South America for quite a while, and lots of conflicts due to time zones.
We're just not joined, but have to be back.
Jason Plumb 00:11:19 Life gets busy, we all know that for sure, yeah. Good to have you back. Yeah.
Cool, yeah, I mean, we should take a look at this. There may… it may be pretty straightforward, but I am also surprised at the number of lines of code, and just… just reviewing, like, dropping into the PR, like, seeing all of this, like, first thing.
this co-pilot stuff. This… I'll be honest, and just because we have a light agenda, I'll be very casual and admit that, like, when I first saw this, I was like, okay.
Copilot jumped in and started reviewing, because I started looking here, like, this is where my eyes were, and then I was like, oh, due to automatic review settings. I was like, what? Okay, so… I'm like, something has turned on Copilot automatic reviews for PRs.
So I went hunting, trying to find that setting, and couldn't find it anywhere, and I'm just like… I think he just requested it. I think, like, it's co-authored, so I think he… I think he wrote this, using Copilot, and then I think you just kind of automatically get reviews when you do that, but…
Cesar Munoz 00:12:26 I'm not very experienced. Looks like it. Yeah.
Yeah, I'm also… I've seen a couple of PRs that have co-pilot reviews and others that don't within the same repo, so it must be that You know, the creators or somebody requests for it.
Jason Plumb 00:12:43 Yeah. But I have no idea, I have no idea.
Manoel 00:12:46 I think there is also an organization setting or a repository setting that you can either, hey, I don't want that at all, I think it's also possible.
Jason Plumb 00:12:55 Right, which is what I was hunting for, so… now OpenTelemetry is a big enough and organized enough org that we don't get full repo settings anymore. They are applied through Terraform in the admin repo, which I think is a private repo that not everyone can see.
So it's OpenTelemetry slash admin… And within there are all the Terraform settings for recreating the repo. Like, if a maintainer went rogue, or somebody decided to try and delete or destroy a repo, which I don't even think you can do anymore.
Yeah, all that stuff is gone. But if somebody did something very destructive somehow, then at least we have the Terraform to, like, recreate the repo with all of its settings, because that's really tedious, right? We used to keep it in a Markdown file, which was just, like, a description of all of the buttons that we clicked.
Which is great, but, like, it's not really automatable, so… The admin stuff is pretty nice.
Manoel 00:13:52 Yeah. In this case, the PR creator invited Copilot as a reviewer. Maybe it was even automatically, because they were using Copilot.
Jason Plumb 00:14:00 Yeah, yeah, that's what I think it was, but, like, it took me longer than it should have to sort of make that realization, looking at this back and forth. But once I… yeah, after a while, and then I tried to do this thing, this view session, where I think… This is supposed to maybe let you see what they were prompting with?
Or, like, how this interaction worked, but no, it's 404.
That was a bummer. I was like, oh, that's kind of cool that you could maybe check that out, but… I don't know why they put this button here that I'm not allowed to click.
Manoel 00:14:27 They wonder…
Jason Plumb 00:14:28 Yeah.
Manoel 00:14:29 I wonder when this, you know, reviewers' bots are going to, you know, ideally to each other, you know? One tells one thing, the other one tells another thing, and then it's… Right.
Jason Plumb 00:14:39 Yeah, yeah.
Hanson Ho 00:14:40 I feel like the bot review should be done before we even look at it.
Manoel 00:14:46 Yes.
Hanson Ho 00:14:46 At this point, there's… There's no point pointing out stuff if the bot's gonna do it.
Jason Plumb 00:14:53 That is the… Yes, yeah.
Manoel 00:14:56 You should have excused.
to your… Coding agents to do the review beforehand, so…
Hanson Ho 00:15:03 It should be a draft… it should be a draft PR, it shouldn't be open for human review until you've resolved it with your… with your… with your agent.
Manoel 00:15:11 The thing is that most coding agents today rely on PRs for code reviews. You cannot even make a comment before there is a PR, right?
So, there is now, like, different IDs that you can do the comments locally, so the bots could pick them up and fix them before you actually open the PR. So, the reviewing process is changing.
Jason Plumb 00:15:33 It may be better for us, right? For open source people, hopefully it gets better.
Manoel 00:15:38 Yep.
Cesar Munoz 00:15:40 Hopefully.
Jason Plumb 00:15:41 There is something Go ahead.
Cesar Munoz 00:15:43 I still kind of struggle a little.
To fully trust, AIs, you know?
Jason Plumb 00:15:50 Well, you…
Cesar Munoz 00:15:50 Yeah, I guess it's great, but then it's like, I don't think we will ever… Well, at least not right now.
Probably not this year, you know.
be confident enough to say that if it's approved by Copilot, then, you know, it's good to get merged. So that's why it's kind of like, well, it's great, but… I don't know, for me, it's not there yet.
Hanson Ho 00:16:13 if it saves me having to review .090% of very common things, that's actually a win, but I don't need to see that process. Like, when they have AI review it, they should put it in draft. I hope AI can work with the draft PR, and then when it's done, you know, put it to full review, or somehow have another mechanism to indicate that, hey, even though this is kind of up.
don't look at it until I'm done playing with the AI.
A change like that.
Cesar Munoz 00:16:42 Sounds good.
Hanson Ho 00:16:42 thousand lines that are… that's ridiculous.
We don't need that much documentation.
And certainly don't need that much code.
Cesar Munoz 00:16:54 Now that you mention it, Is it pos- it should be possible, I guess, to, limit the amount of lines changed in a PR.
And it's automatic? Totally cool.
Jason Plumb 00:17:08 No.
Hanson Ho 00:17:09 sometimes it's useful, like, when you make, like, a syntactic, like, a renaming change, you know, I think we could use, you know, common sense to be like, these are trivial changes versus, you know.
these are… these are not… like, I hope we don't have to use tooling to… to… to kind of force us to break stuff down.
Manoel 00:17:28 I think it would be better if it would be, you know, like, for example, AI identifies that you're fixing two different things, and that should be split up in different PRs, rather than number of lines or something.
Jason Plumb 00:17:40 Or, like, hey, chatbot, what's a good, like, how might I make this PR smaller? Like, that's even the kind of… things. I… I… we… it looks like we don't have a tracking issue.
for the PR template, remember we had discussed putting in a PR template that just has, like, two checkboxes? Like, did you primarily use AI to generate, like, most of this content? Which I think… I think elsewhere in OpenTelemetry, they standardize on the wording, LLM.
And my PR did get merged into the community repo, so I don't know, you probably weren't tracking that, but in case you were, this thing… Well, it's already on the second page, sorry.
Maybe it's on the third page. There it is. This one.
Yeah, so this, this finally did get merged, but It's… it's just guidance, like, it has nothing, like, really that actionable, it's just, like… It's trying to encourage contributors to be forthcoming.
with their usage of LLM and AI tools.
So, you know, so it's a whopping 10 lines here, but, the idea was just, like.
you should, you know, if you contribute content, you should freely disclose it, and then, you know, there was a lot of back and forth on this. But anyway, we, I think, around the time that I authored this, and we had some big PRs land.
We wanted to do… a PR template, or something that, like, when someone submits a PR, there's two checkboxes that say, did you primarily use PR? Is this mostly written by AI? And if so, have you taken the time to, like, thoroughly review and understand what this code does?
Manoel 00:19:28 What's your… what's your prompt?
How many prompts have you used?
Jason Plumb 00:19:32 Or maybe… I don't want to see all that.
Cesar Munoz 00:19:38 Maybe they just manually tested it, or… yeah, anything.
To make sure it works.
Jason Plumb 00:19:43 Yeah, and then, you know, just some sort of indication for reviewers to be not so burdened by it.
Sounds good. Okay, so one thing I did learn, and maybe you didn't know about this either, because I didn't, but, you know, like, as Copilot is going through doing stuff on a PR, like, if a contributor requests that, there are also some guidelines that you can put in this Markdown file, so this is in .github, you can make something called Copilot instructions, and this is in Java Contrib.
And I'm just using this as a reference, because I knew it was here. But you can sort of give Copilot, like, some hints about how to review, like… Prioritize the style guide.
Look critically at public APIs, performance, threat safety, memory management, right?
So these are kind of, like, there's a way to sort of give it, like, the guiding eye of scrutiny as it's doing reviews.
Right.
Cesar Munoz 00:20:43 I didn't know.
Manoel 00:20:43 I'm curious.
Cesar Munoz 00:20:44 critical.
Manoel 00:20:45 I'm not sure if Copilot also respect the agent's MD spec?
Jason Plumb 00:20:50 Because this is not…
Jamie Lynch 00:20:52 Yeah.
Manoel 00:20:53 Because this one is only for Copilot, right? And people would use different agents, so if I have, like, an agent's MD on the Ripple, then any QD agents that respect the spec would work.
Jason Plumb 00:21:05 That's true, yeah. I think we've seen mostly Copilot, but I think there were some other… Usages, I'm sure.
I think just because it's Copilot, and because it's GitHub, like, the integration is tighter, and so… But there are also instructions about, like, what to put in this file, right? So… I didn't finish reading this, but I was like, oh, it's cool that they have some guidance, you know, about, like, what you can throw in there and how to kind of structure it.
Anyway, that was interesting.
Manoel 00:21:35 Yeah. Yep.
Cesar Munoz 00:21:36 That's for the info.
Jason Plumb 00:21:38 Yeah, we could consider doing that, because, I mean, I don't know how much this person, appreciates these comments, but the first thing I saw was, like, it was just repeating itself. It's like, you're missing documentation, you deleted documentation, this should really have a Java doc. It's like, it's kind of doing the same kind of thing, and I'm like.
I wanted to turn that off, or maybe see if it was a good idea to turn that off, and how would you even go about doing that, and I think you can, using that mechanism, or at least tell it to chill out, like, deprioritize Commenting about comments, you know?
Something like that.
Cesar Munoz 00:22:13 Well, probably about what Hanson was mentioning, maybe if… There's a policy where these kind of beers have to the drafts first.
So that we wouldn't get notified Until, you know, all the co-pilot stuff is done.
I don't know if that's possible, but, you know.
Jason Plumb 00:22:31 Yeah.
I also don't know if that's possible, it's a good idea.
Cesar Munoz 00:22:37 You're on mute, Hanson.
Hanson Ho 00:22:41 I just don't want to say any co-pilot review comments outstanding before I take a look.
Jason Plumb 00:22:47 They're closing.
Hanson Ho 00:22:47 But… yeah.
Jason Plumb 00:22:49 Yeah.
Hanson Ho 00:22:51 Like, if you want to use this tool and just be super verbose, go ahead, I don't want to see it.
Jason Plumb 00:22:56 Yeah.
Let's just make a note around this.
Jamie Lynch 00:23:02 I'm pretty sure it is possible to get Cobalt to review draft PRs. I've done that a couple of times.
And then you can just resolve the comments.
That feels like a… Just a workflow we just need to document.
Manoel 00:23:40 This could be even, checklist in the PR template, I did.
address, or compile in comments or something, just as a, okay, I remember about that, I have to fix that.
in my own repository, usually I have a checklist, and one of the items is, I did review my own code, because lots of people don't do… I mean, they do while developing things, but… Then they forget a lot of prints, a lot of, you know… other stuff there.
And then there's always someone that just go and delete the whole template, and Right? Like, nothing very useful.
That's it.
Jason Plumb 00:24:21 That's what I do. That's what I do. I'll admit it, I do that.
It depends on the project. Like, if it's a big project, you know, that I've never contributed before, I definitely don't do that, but…
Manoel 00:24:32 Yeah.
Jason Plumb 00:24:32 Yeah.
Manoel 00:24:33 Context is important.
Jason Plumb 00:24:35 Yep.
Cesar Munoz 00:24:37 Let me see if I can take a look at this, these action items.
Jason Plumb 00:24:45 Yeah, so I think, like, you might be able to use Contrib. So, Trask is often using Contrib as, like, a testing grounds, approving grounds for this stuff, so maybe… Can I… how do you contribute from here?
There's a way to do a PR, do you have to do branches?
Manoel 00:25:03 Oh, if you go on the file, if it's a single file, you can just edit, you can have the permission on the repo, and then it creates a branch automatically.
So, if you just click on a file, for example.
And next day, on the right, yeah, the date button.
But that only works if it's a single file, right? And then when you change something, the commit change is going to be enabled, and then, it requests, like…
Jason Plumb 00:25:27 Yeah, there's no… there's no template here, but I… I thought… Oh, this is the commit message and not the PR message.
Manoel 00:25:35 Except.
Jason Plumb 00:25:35 Okay, so let's do that.
Manoel 00:25:37 the PR title sometimes is auto-generated by Copilot as well.
Jason Plumb 00:25:41 Yeah, yeah, so here we go. So this is the template.
And there's nothing in here mentioning AI. But, okay, so now you got me thinking.
Manoel 00:25:52 The template you can also see on the repo, so if you go under the.
Jason Plumb 00:25:55 Yeah, yeah, yeah.
Manoel 00:25:56 folder.
Jason Plumb 00:25:57 Yeah, yeah.
Manoel 00:25:58 Also there, somewhere.
Jason Plumb 00:25:59 I don't want that, okay.
Manoel 00:26:01 Pull request templates MD.
Down there, west, but too.
Jason Plumb 00:26:06 I'm almost awake. I'm waking up.
So this one doesn't have it, but I swear that one of them did.
Cesar Munoz 00:26:17 But based on what you mentioned earlier, Jason, that there is a… Copilot, guidelines.
Jason Plumb 00:26:25 Yeah, yeah.
Cesar Munoz 00:26:25 Probably doesn't matter what the template reads, right?
Because the guideline… the compiler should read that.
Set of guides.
blinds.
Jason Plumb 00:26:36 True, yeah, I think the PR template is more of a signal to us, right?
Like, it's a signal to reviewers to know that this is… like, has some AI-generated code in it, or is mostly AI-generated code, and so… I think that can change the way in which you review something.
Manoel 00:26:58 Yeah, I need to, though.
Jason Plumb 00:27:01 And also, it kind of, like… I don't think it justifies, and this is maybe a contentious point, but I don't think it justifies massive PRs, but at least it helps explain them. Like, you know… you know why something's so big. Like, it's really verbose because… Like, I don't think it's justified always, but like… It kind of makes sense. You end up with these big PRs.
So Trask has an example in here somewhere about a template.
Oh, it looks like he was just linking to a different one. I thought we had adopted it in one repo, but it looks like maybe not.
That's alright. So, he's looking to the Renovate Bot one.
And theirs looks like this.
Yeah, so something like this.
As a starting point.
Cesar Munoz 00:27:49 Got it.
Jason Plumb 00:27:50 Yeah. Is that cool?
Cesar Munoz 00:27:51 Can you, can you share that link, please, of the Trask as well? Yeah, this one.
Thank you.
Jason Plumb 00:28:06 Okay, so it looks like Servi dropped this in, but is not on the call. Is she on the call? Oh yeah, hi Servi. Sorry, you were on the other page of people.
Surbhi Agarwal 00:28:13 Joined a bit later.
Jason Plumb 00:28:15 It's all good.
Surbhi Agarwal 00:28:16 I'll quickly share my screen.
Jason Plumb 00:28:20 Okay.
Surbhi Agarwal 00:28:22 Can you see my screen now?
Jason Plumb 00:28:27 No.
Cesar Munoz 00:28:28 Not yet.
Surbhi Agarwal 00:28:37 Can you see my screen now?
Jason Plumb 00:28:39 Yes.
Cesar Munoz 00:28:40 Yes.
Surbhi Agarwal 00:28:41 Awesome. So, I proposed this in the semantic convention working group yesterday. So, to give a gist of this, basically.
The conclusion was there isn't a signal in open telemetry that can be directly justified for this kind of a use case, wherein multiple timing attributes are needed.
Secondly, like, we sort of modeled it based on the existing resource timing API that is there in browser. So, with this, basically, you receive an object later on that contains all the timing, so it's not like 1-1 event callback, like how it is for OKHTTP3.
So, we receive all the data at a point, rather than at individual points. So, that is sort of collated into a standalone event.
Some, basically, ideas that were discussed, right?
Originally, like, a span event would have made sense for such timing attributes, but as those are deprecated.
The option was standalone events, but then instead of multiple events, we go forward with a event, a log record that contains all this timing data, because of how, like, browser has resource timing API.
Right? So the proposal was basically a standalone log record.
We added an event name, something of this sort.
Context, contains the correlation back to the original HTTP span.
then the attribute naming. Basically, what… like, I'm sort of summarizing the proposal, and we sort of need and feedback, back and forth, and approvals from Android, iOS, and browser, so there is confidence in the semantic convention group that they can have this as a signal, as semantic conventions, right, for this kind of a use case.
So, here, basically, browser does not have such granular details. So, what we did was, because mobile has such granular details, browser, like, just has, let's say, the response start.
And when the response ends, the call ends. So basically, this is what the browser can use.
Here, only the call start time and the end time are required. The other things are opt-in, so this is… This should also be opt-in, I'll correct this, because if there is connection pooling, you won't have these attributes.
So we added everything here, then there are some additional attributes that are needed for the browser use case. We added those as well. I'm going to bring this up in the browser sig as well to get their feedback on these things.
And then we discussed that there should be, for backends that can't yet correlate to different signals, there should be an option to copy certain HTTP span attributes on this signal. So, earlier I was mentioning that all attributes would be copied, but I think that is too much. So, like, having a configurable Boolean again, whether to copy or not.
But, like, defining what would be copied if this is set to true. Some things I feel like probably should be copied anyway, like URL and request method, but this is also, like, up for debate. And then there are some other things that are relevant to the metrics that can be derived out of these attributes. Like, we need server address, server port, network details for the action-level metrics, right, for filtering on those histograms for connection-related metrics, right? Then exception type becomes important.
The payload size becomes important, for things like the server processing time, time to first byte, those kind of metrics.
One thing that, came up was I earlier suggested using system.milliseconds, which is time since the epoch, but there was an argument that it is not monotonic, because the system time can be changed, so this is subject to change. So instead, only the first time should be that.
And the other times should be delta from that.
So basically, like, that was one of the suggestions. So yeah, this was the proposal, so I will stop here if… to see if anybody has any, feedback on this.
Hanson Ho 00:33:50 So, I think the clock that clocks could change is an implementation detail. I don't think that should affect what the values in the spec ought to be.
So… And… and having to… to do an offset, that's… that's okay, but do we have any other, examples of semantic conventions where we effectively have to know, the start, like, a point in time and then write offsets? Because… OpenTelemetry spec, you're not supposed to read from the telemetry. So basically, you would have to do accounting, or bookkeeping of what the original time is, just to write the offset. So it seems like as long as the clock is a stable instance, and then you lock it, which the OpenTelemetry, Java SDK at least, and Kotlin SDKs, already do, the timestamp should not change when you… well, actually, that's not true. That's only true for a span. But… But again, that's an implementation detail, so I… I would… I would… I would… I would caution against the deltas, unless there's, like, you know, Other examples that would do that?
My second question is, which is not really a question, which is, you know, almost like a… I wonder, is this effectively is a superset of information, of the span.
other than the fact that the span is a span, does it act… and maybe the relationships of that span with other spans.
does this… Contain any less, like, why would you need both?
Surbhi Agarwal 00:35:33 Yo.
I sort of, like, earlier we were discussing in the last call that it would be a superset.
But that's sort of… Did not make sense later on, so, like, reduced the amount of… Original span data that goes here to only the things that we know might be required for filtering for any of the metrics that could be derived out of these timing attributes.
Hanson Ho 00:35:59 But the fact it could be a superset, it's actually a good thing. It means people can just, like, hey, all I care about is the timing, so I just log these, these, these, these events and forget about the span, because I don't need it as a span.
Surbhi Agarwal 00:36:13 The long-term plan is… this is, like, the… this sort… was sort of an interim solution to help backends until they are ready to correlate, but, like, the long-term plan is, like, you should be able to correlate using this context, and we should not have redundant data, if possible.
Hanson Ho 00:36:33 So, I guess what I'm saying is that you don't need that that span. And it's not correlations, it's a direct… this is effectively direct one-on-one related to the other one. And, like, the fact that it's a span is, I think, the accepted semantic convention. But if we're gonna add a bunch of new data on top of it, that comes in in a different you know, time.
And you don't actually need the original span. You know.
Why can't you just use this event to do network timing?
Surbhi Agarwal 00:37:08 Yeah, I…
Hanson Ho 00:37:10 Sorry, this event, sorry.
Surbhi Agarwal 00:37:16 I think it would be probably difficult to justify that, like… An HTTP request is sort of… modeled as a span, right? This is an additional thing that we need in addition to that, for that HTTP request.
Hanson Ho 00:37:35 You got a start time, you got an end time, you have a parent that is a span.
Surbhi Agarwal 00:37:39 We don't have the start and end time for the… like, we can add attributes for the span start and end as well. Like.
Hanson Ho 00:37:48 I'm saying the… the… you have a start… you have a start time and a end time as an attribute. So… I mean, I…
Jason Plumb 00:37:55 Yeah, there's, like, there's pairs of start and ends in the, in that little… Yeah. Yeah.
Surbhi Agarwal 00:37:59 Yeah, I think this can be used instead of span, start, and end. This would be more accurate for the network duration, rather than start of the span and end of the span as well.
Hanson Ho 00:38:10 Like, unless you be very specific about what that start time is, like, the first spike goes on the wire, or the first connection requi- like… there's a bit of fuzziness in how it's defined right now, so, I would expect, other than, like, instrumentation differences, for that start time and that end time to be the same as, any related span, start time and end time.
I'm saying this is actually a good thing, because now we're saying that we have the ability to model what we used to do with a span, with a very specific event that has an optional, a bunch of attributes.
So…
Surbhi Agarwal 00:38:52 Did it?
Like, also, this is thinking ahead, but, like, then… I would still capture the span for those folks that do not require this, and they take the span.
For other folks.
like, implementation detail, let's say. Would they… would we stop capturing the span and instead figure out Of having all those details here.
And, like, not… or, like, capture the span, copy the details here, and don't emit the span. Don't, like, yeah.
Hanson Ho 00:39:33 So, I mean… Logically, this information belongs in the span, and if we're saying that, hey, we wanna… we can't do it because, you know, for whatever reason, putting it as an event, that's actually okay. But then, if you're saying, we have one logical thing that we want to model, which is network requests, and we're going to split it into two signals, and one is effectively, or can be a superset of the other, then one wonders why You know, other than, like, preserving existing semantic conventions and existing instrumentation, one wonders why that would even be necessary when… when this is… this… holy models.
And if you go back to say, hey, well, why don't we just put it in the span? Well, that's span events, and you've basically created a justification or use case for span events. So… This is interesting, I think this is really good.
Jason Plumb 00:40:28 So, yeah. I wanna jump in a little bit, if I may.
Can I give you a couple of pieces of feedback, just directly? I'm sorry I haven't commented on this issue yet.
The first one is, if you scroll up just a smidge, you've got both log record and event name mentioned there at the top of this list, yeah. So, signal type, I understand that, like, events ride on top of the log signal type.
But I think for clarity, we shouldn't put both. We can just call it an event. If you want to say signal type, it should be an event.
Any log record that has an event name is an event. And it's, like, nitpicky, but, like, that's one bit of feedback, that will, like, help make it… I think will help make it a little bit clearer.
Also in the list were… there's, like, two… Two things that are required, the call start and the call end, and they're kind of separated from each other, can you lump those two required together at the top?
Just to make it… just to make it clearer, and then those are, like, a matching pair.
And then one more specific thing I noticed, in the attribute list, the URL full is required. I don't know that you always… I don't know that every… I don't know that, you always have a full URL.
In the instrumentation.
Surbhi Agarwal 00:41:47 Okay, I think we do.
Oh…
Jason Plumb 00:41:50 But other… but other frameworks might not always, so I think that's gonna be a sticking point.
Surbhi Agarwal 00:41:56 Okay.
Jason Plumb 00:41:57 I don't… I don't know that you always know what the requested URL was.
Surbhi Agarwal 00:42:02 Okay. I think maybe then all of these should, like, should be marked opt-in, because they are, like, sort of opt-in behind this boolean.
Jason Plumb 00:42:10 Yeah… So, one other thing I think is an interesting, thought exercise, at least, is… touching on what… in support of, like, what Hanson was suggesting, is that you've already got, like, before you get any of these network details.
You've already got your baseline telemetry, which is a span that represents an HTTP request, right? And this is adding additional color, this is adding additional details to that existing span, right? It augments it.
Surbhi Agarwal 00:42:43 Ignoring what the signal is, ignoring what specific details are on there. It improves or makes that existing thing.
Jason Plumb 00:42:50 more useful.
Surbhi Agarwal 00:42:51 Hmm.
Jason Plumb 00:42:52 Are we aligned so far?
Surbhi Agarwal 00:42:54 Yeah.
Jason Plumb 00:42:55 Okay, so with that, there's… again, I'm repeating much of what Hanson already said. There's different ways that you can, go about slicing and dicing this. You can make an event, as you have listed here, but one thing I think we haven't done much of yet, and there was a lot of work done last year to support this was using complex attribute types for modeling this kind of data. So what you've got spec'd out here, and all of the constituent components, like, this becomes a pretty complicated, like.
object, right? And so you could consider… one thought would be to model a complex attribute that users could then opt into.
And if that attribute is then on that span, on the OKHTTP instrumentation span, Then, if it were spec'd.
As a complex attribute, then one could go in there and look at all of the… the shape of that data.
I don't know, I haven't seen yet in OpenTelemetry, in the semantic conventions, anybody doing that modeling yet, but the groundwork was definitely paved last year to support this kind of thing. So, just as a for instance, right, you could say that the attribute is named… network request details, or network timing details. You know, we can bike shut on the name.
But then in there, you could say that there is a field called DNS.
Or DNS resolution, or DNS activity, call it whatever. And then within that, there's a start time and an end time.
You could say that… you could say that the, network Details have another field called… request header timing, or request headers, or just request, and then within request, you have header timing, body timing, you know. So you model it more like a tree structure, which is already here if you kind of turn your head sideways, or it's just like… with dots, but, you know, you could model it as, like, a rich, like, object, and then maybe… I don't know, maybe that's useful. I don't know.
Surbhi Agarwal 00:44:56 Yeah, that sounds like a great idea. One thing, though, is… Like, in case of browser, this is an asynchronous Thing. Like, by the time these span… like, we might not be able to add that complex attribute to the span itself. We might still need a separate signal.
Because… Yaw.
Jason Plumb 00:45:22 Because you lose span context or something by the time you get this information, or…
Surbhi Agarwal 00:45:28 you have to… like, it affects the existing behavior, you sort of have to wait. Like, in browser use case, it is asynchronous. You receive these events asynchronously later.
Right now, that's why we modeled it separate to the span.
For our use case, it is synchronous by the… we can wait till the call ends, but then what happens is OKHTTP3 guarantees that call and call… end or call failed would be the winding up calls, but it's not necessarily always true. Sometimes people don't consume the response at all, they don't wind up the call, and it gets… leaked and picked up by the garbage collector, right? That's how it is cleaned up. So, like, there is no conclusive way to end the span, so we would need a periodic executor, like how we implemented an HTTP URL connection.
Jason Plumb 00:46:26 Yeah, you brought this up last week, too. Yeah. I keep forgetting about that. Like, these spans are… I mean, that to me, it feels a little bit like an instrumentation concern, like, if we have a mechanism to start a span and not end it properly and timely, like, with the semantic definition of, like, being done with the thing, then that's kind of a different and bigger problem, right?
Cesar Munoz 00:46:54 Yeah, it's kind of like we're looking at it from the other way around. We're kind of trying to address this semantic convention to… the implementation details.
Something like that.
I, I, I…
Surbhi Agarwal 00:47:09 Yeah.
Cesar Munoz 00:47:10 Yep.
Hanson Ho 00:47:12 I just have one question.
Cesar Munoz 00:47:14 survey. And probably, you have already addressed it, it's just that I haven't taken a look at this, And, to be honest, for a while, it's because it's just… it's huge. It's like, it's a lot of… information, and… and… And… Yeah, I gotta be honest, I usually just, kind of, like, get, you know, derailed to something else that I… that I think it might be quicker, because it's… it's a lot of information, and I'm kind of… there's a lot of context that I'm not sure why… This could be the best.
approach. And so, one of the questions that I have for it was.
Probably you already addressed it before.
So, following the same line of thought that Jason was saying, that what you're proposing here, it expands the information that we get from an HTTP span.
What… What it sounds like to me is that the natural way of doing so is just adding more attributes to the span.
So… so… Have we tried that?
Surbhi Agarwal 00:48:39 Yeah, exactly, so yeah, firstly, it was a good feedback from you. I'll try to figure, maybe I'll create a new issue, and put the important context there, so we can leave this bigger trail of discussion behind. I'll try that.
And, like, to your second question, So, basically, we can do, like, we can add it to the span, but the problem is, it has some side effects to the span. Now, the… first of all.
like, it would affect the existing folks who are using these instrumentations. They would need to set up another executor. If their codebase is not properly using OKHTTP3, that is, they are not winding up calls correctly, they are not closing the OKHTTP call correctly, they might not get spans.
So they would have to configure… based on the knowledge of that, they have to decide whether they need to configure an executor to close those spans or not.
And secondly, it might… delay the spans. Like, if they need all the information, it might delay the span. We might probably have an implementation in a way that if they don't need the timing attributes, we can close the span earlier, because right? Like, these timing attributes might take some time, but they don't need that, so we can close it earlier. So, like, it would affect the existing, customers. So we can probably do that, add it to the span, but we might… we have to be careful of these things.
Also, in browser use case, like, because we are talking about unified semantics, browser right now, like, some of the instrumentations do wait to close the span already, and put in some of those details there. Like, for our use case, we receive these events synchronously. For browser, it is asynchronous, so they don't know when this data will come to them.
So they don't hold up, they don't want to anymore hold up the span to be able to… Put these details into the span as well.
Hanson Ho 00:51:00 So, so, a couple… couple things.
Serby, it might be a good idea to think about the, semantic conventions and the instrumentation two separately, because the… I think the Jason's suggestion of making these more complex attributes, or just simply attributes, allows them to be consumed, and put on the span, or some sort of addendum object later on. So basically, you have an attribute that says, connection timing, and you have, like, a start and an end. If that lives on a span, HTTP span.
that can be consumed like that, and can be put there asynchronously by the instrumentation. Or it could be, you know, done through, like, the event that you're adding.
So, like, consider the semantic convention as separate from the… the other task, which is re-implementing OKHTTP instrumentation with the Event Listener API. And… You might be able to kind of, like.
have the semantic convention stand alone from the implementation, and have the implementation then, you know, do whatever you need it to be. Because, from what you're describing, it sounds like the implementation is being changed just because the instrumentation is doing things a little bit differently.
I think there may be a way of actually… connecting the two, but that's almost, like, a separate thing. So, if you can kind of, like… I don't know if there's one issue right now or two issues, but, like, break these down into two things. One is defining attributes, for the semantic convention to be consumed, either on the existing span or on, like, a log object.
And then, like, work on the instrumentation itself, you know, separately, because that is more of an Android concern, versus the other one is you have to worry about web and other places and have a unified set of conventions. They don't really care about, you know, when calls end.
Jason Plumb 00:53:01 I think… I think I agree with that, like, trying to treat those as separately as possible, I think will help to get some traction here. In Serbi's defense, though, it sounds to me like she's informing some of the modeling decisions based on the implementation. Like, it's being informed by that, so…
Surbhi Agarwal 00:53:17 Yeah. I don't think that's necessarily a bad thing.
Jason Plumb 00:53:19 But I think that trying to split them, or, like, treating those two concerns, the two concerns being Spans not being closed correctly because of timeout and usage problems in instrumentation versus how do we model the network timing data?
Surbhi Agarwal 00:53:35 Yo.
Cesar Munoz 00:53:36 Yeah. Also, I, I… I'm not sure if you… because you mentioned that there might be an issue with spans not properly closed.
If I remember correctly, you mentioned OK HTTP, but Probably, you were… you… you meant… HTTP URL connection, because… I'm not aware of issues with OKHTTP when it comes to not properly closing HTTP calls.
I mean, you have the event listener that Hanson mentioned, And… I mean, it could be, it could be, like, Something that you add on top of the existing instrumentation that It's managed by OKTTP internally.
So, I don't think we should worry about users not properly, you know, making an HTTP call.
Surbhi Agarwal 00:54:30 There is, like, here in the tracing interceptor, first of all, what happens is it ends as soon as the response is received. It does not wait for the response body to be read or the call to be ended. So, a solution for that is.
like, instead, I'm not sure if I have that open, but instead you go to the event listener.
winding up.
callbacks, which is call end and call failed, and you instead end the span there, but what happens, like, what I have gotten in my research is… OKHTTP does guarantee that either call failed or call end would be called, but that's not the case in reality. Like, if you are… the… like, you don't need to really read the response right, and you might… not… you might end up not calling any of those, and it would get leaked instead of being closed properly. So, like, there are… it is possible to use OKHTTP3 in a way that all callbacks are not called.
And the wounding up ones are not called, instead it is leaked.
Hanson Ho 00:55:39 So…
Cesar Munoz 00:55:39 Look, I mean… I just wanted to point out.
So you're saying that this package ended?
Surbhi Agarwal 00:55:49 Yeah.
So, one thing…
Cesar Munoz 00:55:50 before the HTTP request finishes. Is that what you're saying?
Surbhi Agarwal 00:55:56 Like, yeah, here, as soon as the response is received.
we close the span. So, after this, the consumer can be taking some time to read the response body.
And finally closing up the call. So what happens is, when I was doing it this way, that I was adding it to the span, I was not capturing the response body end and the call end timestamps, because it closes earlier than that.
like… Also, to add to our last discussion, like, there is a proper way of using OKHTTP3. The problem is the applications would have to change their code. So, to ensure that they definitely get this, they might not have that ready, that's the thing.
Hanson Ho 00:56:49 So the instrumentation as it is set right now basically does it at the interceptor. There's no guarantee of the response being read in the existing instrumentation. It basically only guarantees that the bytes go through the wire. So I think the existing behavior is adding the interceptor as close to the network request finishing as possible.
But, I think the existing instrumentation doesn't include deserialization. So basically, when the response is obtained, and that's done, and it passes on to the interceptor, that means all the bytes have gone through the wire. But if there's a deserialization problem, that's not gonna be… that's not gonna fail to span, because that's a… that's already done.
So, I think, the existing instrumentation ending it here is correct.
And, the call, abstraction through OKHTP is not simply just a request response. It includes a bunch of retries, and a bunch of queuing.
And I think, in your, in your instrumentation, I remember taking a look at the new change. You basically start the request when the when the connection starts. So there's a… there's a bunch of time when the call is happening, so when it's queued and kind of, you know, sitting there waiting to be executed, that part is not tracked. Which is correct. If you want to mimic the existing instrumentation and what the start and end times are, that start time is correct. And the end time, if you want to mimic what it is currently as well, doing it here is also correct, and doing it at the end call end is probably not correct, because that's basically when the OKHP internally says, hey, I'm done with this call, I can, I can, you know, deal with it. It's meant for cleanup, it's not meant for timing. So, you know, using that for timing is not probably recommended, and using the event listener, and tracking the end of the response, basically when all the bytes are through the wire. That timestamp is probably the most correct.
Cesar Munoz 00:58:55 That's, that's… yeah, I agree with that. Also.
based on that, what you mentioned, survey, it sounds like, like, really the only issue with OKTTP is trying to get the body.
And… and so… but the thing is that we're, like.
if you think about it, we're, like, we're talking about, in your proposal, we're talking about things like DNS, you know, times and stuff, and essentially, we are giving all that away, because one attribute, it's tricky to get, which is the body, which… Even if you can get it, My understanding is that getting it… From… from an instrumentation.
Even if it's possible, it probably might not be… the way the OKCDP is meant to work, because as far as I… I need to revisit it, but… I remember the last time I checked.
OKHTTP works in a way that the response body is meant to be read once.
And… and I think, if I'm not mistaken, if you read it once, then that, you know, response is kind of closed.
And so, any further attempt to read it will throw a closed exception or something like that, so… if you… So, what I'm saying is that I need to double check, but if you… if you succeed in reading the body before the users.
Then you might be, you know, breaking the user's use case, because they probably won't get access to the actual responsibility, which is something that I would say, arguably, they need more than us, so… It's… it's a lot, that's the thing, as well. It's… it's… like, your… your proposal covers a lot of stuff, and… It's, it's difficult to review it all.
In a single place.
Definitely.
Hanson Ho 01:00:54 So…
Surbhi Agarwal 01:00:55 Like, I understood what you were saying.
So, I was not receiving the body and timestamp. That could be a race condition, or… like… like, the span maybe just ends before and does not record this, or that could be something else. Like, we did need this, this is sort of an important attribute, like, you want to capture how much time it took to download the payload, the response payload.
And, like, there are other things, like, you need to know the… network… like, there are some metrics where this is required, right? So, like, this was sort of an import… leaving it out wasn't a good idea.
There is a bunch of information, but yeah, this was also important, that's why…
Jason Plumb 01:01:49 We have to play a little bit of Time Cop, and just keep a check on this. We try and end at 5Tel, it's okay that we've gone a little longer, but, we are gonna run out of time.
Cesar Munoz 01:01:58 Very soon, so… Yeah. I think this is a really good conversation, I'm glad we're having it.
Probably what you'll…
Hanson Ho 01:02:05 I'll make comments on the review, just so, just so, yeah.
protection. Gotcha.
Surbhi Agarwal 01:02:11 And if there are implementation, things, you can comment on this PR.
Oh, no.
Hanson Ho 01:02:18 I've been meaning to do that every week, but, you know…
Surbhi Agarwal 01:02:21 Yo.
There are some things, quickly, that I am going to improve. One is, like, Hanson, if you can mention what you were saying about the deltas. There is an open thread here, if you can mention, your concern about the deltas here.
And like, there are some bunch of issues, because right now, I am directly calling the network listener, and the old tests that use the common class are failing, so I'm going to use reflection instead to call the network event listener class only when it's available. So that should resolve these issues.
Hanson Ho 01:02:55 you should actually probably use the OKHTTP, mock server, and run, like, a fake, request through the mock server. yeah, sorry, time.
Jason Plumb 01:03:06 Okay.
Hanson Ho 01:03:07 I'll make comments, I'll make comments in the, in the thing.
Jason Plumb 01:03:09 Thanks, everyone. Sorry to be that guy, but I have to.
Cesar Munoz 01:03:13 Thanks, and thanks, Arby, for, you know, your patience.
Yeah, no kidding. It's not hot.
Jason Plumb 01:03:19 So… Yes.
Surbhi Agarwal 01:03:20 I need all of your inputs, thank you for spending time here.
Cesar Munoz 01:03:23 Yeah, for sure, thank you so much. See you next week. Thanks, buddy.
Surbhi Agarwal 01:03:27 Bye-bye.
