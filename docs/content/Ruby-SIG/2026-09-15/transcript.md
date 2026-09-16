SIG: Ruby SIG
Date: 2026-09-15
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 00:16 Hi, Matt!
**Matthew Wear (Dash0)** 00:18 Whoa.
**Kayla Reopelle** 00:21 How's it going?
**Matthew Wear (Dash0)** 00:22 Not too bad, how are you?
**Kayla Reopelle** 00:24 Not too bad.
Still recovering a little bit from a cold, so might… You know, go all on mute for a little bit to cough or something.
**Matthew Wear (Dash0)** 00:35 Good to hear you're feeling better, at least.
**Kayla Reopelle** 00:37 Thank you. Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 00:42 Hi there, folks.
**Kayla Reopelle** 00:44 Hey, Rob!
How's it going?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 00:48 It's okay.
**Matthew Wear (Dash0)** 00:51 It's hard to hear you, Rob.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 00:53 It is? Okay.
Let me see if I can fix that.
Maybe if I just talk at the microphone? How's that?
**Kayla Reopelle** 01:01 That's better.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 01:06 I won't mutter, away from the microphone.
**Kayla Reopelle** 01:08 That's one strategy.
Cool. We have a pretty solid group. I don't know of anyone who is not coming today.
But we have a lot of it on our agenda, so we could go ahead and get started.
Alright, I was in a different meeting this morning, so I wasn't able to go to the Spec SIG. Was anyone there who wants to provide some updates?
**Matthew Wear (Dash0)** 01:42 was there. Let me take a quick look and see.
See what's relevant or interesting.
I guess the second one about attribute limits.
Like, the current things that don't have limits are… Resource metric and scope attributes, and everybody kind of agrees that's a… That's a bad… a bad thing, that there should be limits, that they should introduce them.
But, like, I guess the… the summary is that… That will probably end up being a breaking change for somebody.
**Kayla Reopelle** 02:27 Hmm.
**Matthew Wear (Dash0)** 02:29 When they're actually introduced, but, That's kind of our fault for not… Introducing those sooner.
So another thing that was kind of interesting, the ecosystem and registry freeze, I don't know if… if anybody is an active registry user, some people were, at the spec SIG, but… like… Apparently, it's just… there's not enough… I think… I think there's two issues. There's not enough, like, people actually, like… To keep up with all the requests to add things to the registry.
And then the second thing is that there's, like, really no validation of the stuff that's in the registry.
So, So we're just going to freeze it for now and try to come up with a better plan later on.
But… some people said that they kind of use it actively, like, if they're trying to help customers, if they're trying to see, like, if… Hotel will be a good fit for them, for example.
To find instrumentation that might not necessarily be Boom.
Corp.
**Kayla Reopelle** 03:46 Interesting. Yeah, we just made some registry updates, so I think there probably isn't a whole lot more that we'd want to add anyway.
But, that's good to know.
**Matthew Wear (Dash0)** 04:00 There is a specification pull request for, auto instrumentation, and basically the… PLDR of that is that Requiring auto-instrumentation should never, like, crash an app.
And I think that's not… that's probably not necessarily true for, for… for RUI, and for… War.
you know.
for various SDKs, but I think It's mostly true for Ruby, I think, for us, but I think there's a potential for protobuff conflicts.
it's like, we're doing our best to mitigate it, but I think, I think it is technically possible for the Protobuff version our exporter depends on… if the host app also depends on Protobuff.
Like, they're… It's possible that there will not be, like, one dependency that solves, okay.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 05:13 Well, that… that wouldn't crash the app, that would be a dependency resolver issue.
**Matthew Wear (Dash0)** 05:21 I guess it depends, because that's…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 05:22 Because the exporter is an SDK thing, and that's not auto-instrumentation, that's… Oh, I see, SDK injection is included in this.
Oh, yeah.
**Matthew Wear (Dash0)** 05:33 Yeah, yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 05:34 When injecting, I see the…
**Matthew Wear (Dash0)** 05:36 Yep.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 05:36 now.
**Matthew Wear (Dash0)** 05:37 What injecting is, like, we always… yeah, that whole process is a little bit ugly, but we always put ourself on the load path first, so we don't really know anything about the application, and, like, our dependencies go there first, so our protobuf will end up there first.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 05:50 Shouldn't crash the app. I'm like, okay, we just won't write bugs.
So…
**Matthew Wear (Dash0)** 05:57 I feel like the only way to… I feel like the solution is simple in theory, but not in practice, and the theory is just have no dependencies.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 06:07 Yeah, right.
**Matthew Wear (Dash0)** 06:09 And… But the practice is a little harder there.
And… Yeah, the last stuff, We didn't really have too much time to talk about.
I guess… Though.
Merge algorithm has been cleaned up very… very nicely for the… for entities, which also, I think, dovetails a little bit with resources, but, I haven't actually read through that.
But, yeah, that was basically the… the highlights of the spec SIG.
**Kayla Reopelle** 06:49 Nice. Thanks for breaking that down with us.
One question on this auto-instrumentation before we move forward. Do you think that the TracePoint, evaluator that you've proposed would help avoid some of that?
Or is it just… Too dependent on… how things are installed, and that one actually get around it.
**Matthew Wear (Dash0)** 07:12 I mean, TracePoint is an improvement over Bundle Require, because Bundle Require's just not going to work in certain circumstances, so it's going to be, So your auto instrumentation is not going to be very auto, and be somewhat frustrating, whereas TracePoint removes, Yeah, it… it will remove those scenarios. It will work in all the scenarios where, where it really can. I think the… The dependency issue is outside of what Of what we can really solve, there, and I think, really, the only real answer to that is that our… We cannot depend on Protobuff if we want to make sure that we don't crash anything. Right now, our solution is we have, like, a very wide range.
And that's… that works fine, and I think it will probably work in 99% of cases.
**Kayla Reopelle** 08:19 Okay.
Nice. Thank you.
Alright, so onto our agenda. In the core repo, we have a… Question from James to relocate API projects into an API folder to enable introducing an API common and eventually have a log and metric API as a dependency of the API gem once it's stable.
I know we've talked a little bit before about the duplication that's in the metrics and logs APIs, just based on stability concerns and to kind of keep the APIs flexible.
So, I mean, I haven't reviewed this pull request yet, but my gut says we might not be ready for it, but I'm not sure. I'm curious if anyone else has been able to take a look at this, or has other thoughts.
**Matthew Wear (Dash0)** 09:22 I haven't looked at it. It does sound like it's a little bit forward-looking.
And it will probably be useful someday, but yeah, I'm not positive that we need it now.
**Kayla Reopelle** 09:37 I could see maybe after we get to stability, like, working on that refactor, so that it's just easier, too, for the… I mean, maybe it's not easier for the technical committee to review, But it does feel a little more compact and separated.
**Matthew Wear (Dash0)** 09:55 I feel like that's probably the right time for it.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 10:00 Is there a future where they just fold into the API gem?
**Kayla Reopelle** 10:05 I think so. I think that's a reasonable move, especially once they become stable.
I think the main reason for keeping them separate was because of stability concerns.
But I don't know, does anyone have concerns about that?
**Matthew Wear (Dash0)** 10:28 I don't have concerns, but I think we should think about it more, like…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 10:31 Yeah, I…
**Kayla Reopelle** 10:32 Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 10:33 I don't think we would decide today, but that's what I would picture the ideal to be, that there's just an API gem and it serves all signals.
**Matthew Wear (Dash0)** 10:42 Like, yeah, I think… I think we should look at what everybody's doing. I know JavaScript has a separate package for literally everything. That's my other frame of reference, which is a little maddening, but… sometimes I do kind of like… Separation, just because it… keeps things from… becoming spaghetti, in a way. But…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 11:10 Sure.
**Matthew Wear (Dash0)** 11:11 In the API gem, I think that should be not necessarily… not so much of a concern. But yeah, like, the downsides are that, like, it makes it harder to share things.
And then you end up having to grow a common gem for everything. But, But yeah, I'm open to any futures there.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 11:39 Okay.
**Kayla Reopelle** 11:48 So, we'd like to revisit once we have, technical committee review.
Metrics and logs for stability.
In the future, need to think about what, want to do with the API gem?
Okay, cool.
Any other thoughts on that before we move on?
So, okay, so this, logs and metrics.
API stuff, I didn't expect it to get kind of picked up and have people notice it, straight away, so apologies for that. I thought I could kind of silently post things.
But, essentially, what I've done is… worked with Claude to look at the differences between our, metrics and logs implementations and the specification. Guess maybe, actually, we'll start with the pull request, which… I… somewhere… So, these are the documents that it created, which have tables that kind of break the API and SDK down into more specific steps than just kind of the line numbers or the general concepts.
And so I'm thinking right now that we can use these documents as kind of the… Source of truth about where we're at, and use them to keep an eye on what it is that needs to be done before we can Actually submit the issue for the technical committee to review, our implementations for stability.
And the deviations that were found in here, most of them, but not all of them.
I turned into issues, which are in these two milestones.
This log stability prep and metric stability prep.
And so… They were also created by AI, but I attempted to edit them to make them a little more reasonable in some cases.
And so it has, like, a reference to the specification, how it analyzed, things are currently behaving, and then also, like, a proposal for how to fix it, and references in the markdown files.
I feel like just trying to prioritize these different milestones and Work through them, would be… a focus I'm at least interested in. I don't think we have to do metrics and logs at the same time. If we all want to invest in metrics or in logs, you know, that's another way to do it. I know that we all have limited time and, you know, ability to review as well, so… I'm hoping that we can have Maybe some organization that will help us with this.
But yeah, that's kind of… those are the resources I have out right now. We could go as far as adding a project board, if that's interesting to other people.
One other thing that I'd add is that I did have… someone from a company based in the EU approach me and say that they're interested in, contributing to metrics.
And… So we might have some folks from, like, a specific company interested in contributing a couple of features. I'm gonna meet with them later this week.
To, learn more about what they're interested in.
But, I think, yeah, that's the hodgepodge.
of what I have available, and a rough plan, But yeah, I'm really curious about… What?
other people think about this, what, you know, maybe your own goals are related to signal stability, and, if you have any, like, recommendations or suggestions on how we can Make this better, or make this easier for people to work on.
**Matthew Wear (Dash0)** 16:28 You know, I think this is great. Thank you for putting that together.
I think.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 16:38 go ahead.
**Matthew Wear (Dash0)** 16:39 Oh, go ahead.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 16:41 I… plus one, I, that… that there's a… Document that shows the, something has evaluated status, and we've got issues. Milestone's probably sufficient, I'd say. Adding a… adding a board might… introduce even more complexity to us getting it done. I don't… I'm open to a board, but I don't think it's needed if we've got a milestone.
Great, I'm…
**Kayla Reopelle** 17:11 Complexity is preferred.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 17:13 And I imagine that's why you would stop at just a milestone instead of cranking out a board.
I have to admit to less familiar with the complications of metrics than with logs, so if other people want to work that, that's fantastic.
But I might be able to contribute to logs.
**Kayla Reopelle** 17:40 Excellent.
**Matthew Wear (Dash0)** 17:41 Yeah, I feel like my only reservation about any of these things is maybe part of our burning questions about bots and low-effort PRs.
**Kayla Reopelle** 17:51 Yes. Because…
**Matthew Wear (Dash0)** 17:53 they… Yeah, I don't know what people are doing, but they seem to just be, like, firing up Claude's, and be like, go… go find anything, work on it, and then they just, you know, randomly open PRs, and some of them are okay, some of them are not great. Some of them… yeah, most of them, it just feels like you're interacting with Claude remotely.
It's sometimes not bad, because they usually just take your feedback and apply it.
You know, within 5 minutes of you giving it, and
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 18:24 Maybe we could leave off the good first issue label to discourage.
**Kayla Reopelle** 18:28 That was me.
**Matthew Wear (Dash0)** 18:28 Probably leave off the good first issue.
**Kayla Reopelle** 18:30 Brett.
**Matthew Wear (Dash0)** 18:32 label. My… my other thought, I guess maybe I'm… Moving into burning questions. But my only other thought on this right now is just, like, is not… is not foolproof, but collector… the collector at least has, like, a checkbox that says, well, first they have a policy that discussions are for humans, so, PR descriptions should be written By you, or at least, you know, Not written directly.
by the LLM. Yeah. I feel like there's… I feel like everybody does some hybrid approach, and I think that's totally reasonable.
But when you come to, like, a wall of LLM text, like, it sucks, and…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 19:17 We could auto-close if there's an emdash.
**Matthew Wear (Dash0)** 19:22 Well… not necessarily… some… sometimes the M dash is actually appropriate, but,
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 19:29 But then a human could go, no, no, no, I wrote that, and then we can reopen.
**Matthew Wear (Dash0)** 19:33 Humans have been using them more lately, I think, since AI has been using them. It's a trend, but…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 19:38 Ugh.
**Matthew Wear (Dash0)** 19:40 The one thing that I think the collector does do that is not, like, a horrible idea is they have a checkbox And you check this box saying, I, a human, wrote this PR description.
And the… I mean, unless you explicitly, instruct Claude to override that, like, it won't check… it won't check the box by default.
So I think you will, you will find… yeah.
You will find that a lot of bots will actually just… because people aren't really supervising them very heavily, will just kind of leave that unchecked, and… I think the other thing we can do is just have, like, a really minimal template, since we're gonna… if we add this checkbox, which is basically, like, what is this PR doing? Why is it here? And then maybe the next thing is just, like, can you just summarize the changes?
Bum.
and since I'm suggesting this, I could take up this action item of just, like, minimal template with checkbox, and then I think the… The main goal, from this is that if we do get, like.
you know, a lot of these PRs, or as these PRs get opened, if… our template is replaced with a wall of AI text, or if the checkbox is not checked, it's like, you kind of already know that this is not a human.
**Kayla Reopelle** 21:03 No.
**Matthew Wear (Dash0)** 21:04 And, like.
you know, if a human opens a PR, I feel like, you know, I… I should review it. I'm obligated to review it, because they've put in some effort, but if a bot is just opening these things, I don't feel like I have to review it. If it looks like it's low effort and not really useful, and can just let… either let the sale bot, you know, reap it, or, you know, we can close it if it's just… Obnoxiously bad.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 21:33 Sir?
**Matthew Wear (Dash0)** 21:34 Yeah, those were kind of my… some of my thoughts to… try to manage some of this, and I'm definitely open to any Any other thoughts anybody has? Because I feel like… I don't know, I feel like this is a problem that everybody's dealing with in some capacity, but I don't know that… We have any great solutions just yet.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 21:55 I like these proposals as baby steps towards… Managing it.
**Kayla Reopelle** 22:02 Yeah, I agree, and I've seen that checkbox in a couple of hotel repos and think that it's… helpful, especially because it requires people to read and think as well about whether or not they… can actually explain what it is that the LLM created.
If they did collaborate with an LLM to make it. So, yeah, I'm all for support of that.
I'm sorry for adding the good first issue label, I almost didn't, but I had too much hope in humanity, so… Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 22:40 It's okay to have hope, but we dialed back.
**Matthew Wear (Dash0)** 22:44 Just not in humanity.
That's the error there.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 22:52 Circling back to the, make… make metrics and logs stable.
**Kayla Reopelle** 22:59 Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 23:00 I like… I like the tracker. It's good to have a list. It's like a punch list, and I would say that that was even a… that was a good use of a bot. Do the… Parity evaluation, and then crank out some issues that we can work on.
**Kayla Reopelle** 23:15 Nice.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 23:16 Huge fan.
**Kayla Reopelle** 23:17 Question on that, too, is just on maintenance of it, because eventually this will go out of date. I was thinking of just writing up a prompt that can update it by analyzing the changes in the code.
And maybe just run that weekly.
does that sound good? Would we rather have people edit it in their poll requests?
Yeah, any thoughts on that?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 23:44 In an ideal world, I think I noticed on the issues that were produced, it has a ref… like, you have the… there's a section, related rows, and file name, and the identifier, I guess, from the spec.
In an ideal world.
I'd like to see that the PR that fixes this, before it merges, updates the associated file.
Yeah. And I know that that's… Probably having too much hope in both humanity and bots, but… I guess that's the ideal. Include that in a review of a PR addressing one of the spec requirements.
Try to include that the review is, like, did the… did the spec compliance doc tracker get updated? If not.
that's a review comment, let's update the review tracker. And then also, as a… as a catch-all, like, a weekly prompt that would go and Verify.
Did any of that make sense? I feel like I just sort of stream of consciousness there.
**Kayla Reopelle** 24:52 Yeah, ideally, in pull requests, people will update the document, and then do an automated check just to make sure we didn't miss anything.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 25:01 Yeah.
**Kayla Reopelle** 25:03 Sweet. That sounds good. Okay, well, if folks can take a look at this, if you have any feedback on… where they're located, or, you know, if we want to add more information about, like, PR review guidance somewhere.
Just let me know, but, it'd be nice to get this in, since we are getting some pull requests, so people can update the files.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 25:28 Would it… would it be silly to have… the spec compliance traces.
**Kayla Reopelle** 25:34 So, I thought about that, and I wanted to wait, because we do have stable traces, and I think, we will need… I mean, we can, we certainly can.
It will probably mean a 2.0, or trying to figure out braking changes versus non-braking changes.
But I'm happy to generate that if you think it would be helpful.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 25:58 I think it would be… Like, writ large, it would be helpful.
Does it help us get these two signals stable? No. So, maybe that's a follow-up we could do after these two.
More progress is done on metrics and logs, because… Traces suffice, I guess, at the moment.
**Kayla Reopelle** 26:16 Yeah, I guess that's where I was at. Like, I don't want to distract the limited effort that we have if we could keep the other signals stable, but it is widely used, so people might be wanting features that we don't currently support, so I understand updating it as well.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 26:33 I'll retract my suggestion. I'm convinced to not do that right now.
**Kayla Reopelle** 26:38 Maybe we'll check in in… a month, and see if it makes sense to add traces then. Does that sound good? Sure.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 26:43 Yeah.
**Kayla Reopelle** 27:00 And I'll add, add links to the milestones.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 27:05 Like, I get, related to a topic that's come up recently, like, schema URL, and… rotation scope, that stuff.
**Kayla Reopelle** 27:15 Yeah, for sure.
Hannah, I know you were working on those. Is there anything you want to throw out about that?
Okay, maybe not right now. But,
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 27:31 Nope.
**Hannah Ramadan** 27:33 Sorry, I was typing something, and I thought I heard my name. What was the question, Kayla?
**Kayla Reopelle** 27:37 Oh, Rob was just mentioning schema URLs, I didn't know if I wanted to throw anything.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 27:43 Were we to add to the… like, we've got the logs and metrics compliance, like, tables of whether we meet it or not. We don't have a traces one.
producing a… Trace's compliance evaluation would… probably show that at least the schema URL is meant. It's basically, we're talking about doing schema URL on instrumentation scope.
and that… that would be a thing that would show up in a… compliance evaluation for the traces signal. So, generating a trace… like we did for… like you did for logs and metrics, if we did the same thing for traces and had another milestone.
**Hannah Ramadan** 28:33 Yeah, I mean.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 28:34 schema URL would show up. Go ahead, I'm sorry.
**Hannah Ramadan** 28:37 Yeah, well, I really actually like these milestones. I'm not sure I've seen us do them before, but they're really helpful. So while we were making those, I was like, oh, like, would it… be helpful to have, like, a schema URL milestone, but I think a trace is one, if it would show that the schema URL was missing. I think… I like that idea, generally, to help track things. I feel like… schema URL has.
a couple tickets, I don't… I actually don't even have quite a handle on how many of them exist, or what each of them are, like, linked to, so I think that's some cleanup that I was hoping to do anyways.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 29:14 We could probably work on schema URL without having a whole trace and signal spec compliance evaluation, but we had talked about checking in in about a month to see how we're doing on the milestones for logs and metrics, and maybe If that has helped.
We could introduce a traces one to circle back on traces and fill the gaps.
And maybe decide in those implementations which are… Which could be implemented without backwards breaking changes.
And so it wouldn't necessitate a 2.0.
But we can do that later. We can make progress on schema URL without having a whole compliance assessment.
Let's check in on a month, is basically what I'm saying. Not necessarily on schema URL, but on the rest.
**Kayla Reopelle** 29:58 Yeah, I specifically left schema URL out of the issues, even though it was something that the bot identified was missing from metrics and logs, because I knew it was being worked on by Hannah, so that's why we have a different issue that looks.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 30:11 Cool. Well, let's… let's do it that way.
**Kayla Reopelle** 30:14 Cool.
**Matthew Wear (Dash0)** 30:15 I was just gonna say, plus one on later for traces, just because I think… Oh, listen… we shouldn't ask for more work than we can review, and I think we're already… we're already there, so… Oof.
Yeah, I think that's one of the limiting factors.
**Kayla Reopelle** 30:36 Sweet.
Okay, cool, are we ready to move on to Contrib?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 30:45 Sure.
**Kayla Reopelle** 30:47 Sounds good. Alright.
This DevContainers PR has been open for a minute.
I am curious if anyone has worked with dev containers before, or has any opinions on them.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 31:05 I have found them hard to hold.
They get complicated quickly.
I haven't looked at this particular change.
I've found that they're useful at first, and then they get more and more complicated, and then they become Hard to impossible to maintain.
**Kayla Reopelle** 31:25 This is my fear, and also why I have… admittedly avoided this PR. I've tried to review it a few times, and I'm worried that it's adding complexity, that… we… Aren't going to be able to maintain well.
Yeah, so… But because I haven't used them, I don't want to prejudge it. I also don't… I think because I haven't used them, I'm not really qualified to review those pull requests.
Because I just don't, I would need to learn a lot, and I think there's a lot of other priorities right now of things I… Should spend my time reviewing.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 32:12 I guess, what problem is this solving?
I see the… See the list.
of… Reason for this approach is that we can CI check if the test folder contains… You know what? I'll try to review this.
Okay. Since I've… I have… experience with Docker and… Docker Compose, and our dev environment, and some with dev containers, and I'll try to form an opinion.
**Kayla Reopelle** 32:44 Thank you.
Yeah, I feel like the way we have things set up right now.
make sense to me. I mean, like, there's been some added complexity in Drift that, you know, make them make a little less sense to me now, but, overall… Just want to keep things simple and consistent.
But also functional, so… Yeah.
Alright, cool. Matt, do you want to chat about this issue?
I don't know what…
**Matthew Wear (Dash0)** 33:17 Nope.
**Kayla Reopelle** 33:17 Sorry.
**Matthew Wear (Dash0)** 33:18 I know we've… this has come up several times, in the past. I know there's currently a PR… up for making the logs API, you know, available to, to some OpenAI instrumentation.
Is that the right instrumentation?
**Kayla Reopelle** 33:40 Yeah.
**Matthew Wear (Dash0)** 33:41 And… And also, there was something at the Spec SIG last week that made me start thinking about this more. Basically, there… deprecating… Span events, and everything that's a span event is supposed to become, like, a log event instead, and Yeah, so, so, ultimately, I was looking at what other languages are doing, and it… And yeah, you've been talking to Jack from Java, and it's fine for our instrumentation, which is, unstable, to use unstable APIs. It's just kind of the other way around. Stable, stable components cannot, have, like, dependencies on… on unstable, components or unstable APIs.
So, I just, worked through this, and, Wanted to see how this would look, how we could make instrumentation available to, or make logs and metric APIs available to instrumentation without exposing it to the users. And basically, it… yeah, there are not that many changes. Like, the biggest problem right now is when you require the logs API or the metrics API, it wires up a global on the OpenTelemetry module, which, like, really puts it in the, in the user's hands.
So… I don't wait.
So yeah, I guess this table really kind of shows you what… what happens now with this refactor, and I can just show you a little bit how this actually looks, but if you require OpenTelemetry Metrics API, the instrumentation will get, a meter provider off of the internal module, which is API private.
And then there's no top-level open telemetry meter providers. That's kind of like… I guess one of the tricks that we're doing is, putting the meter provider on internal instead of open telemetry, and then the same thing for logs.
And then… if somebody actually wants to export, you know, data or metrics, they would, you know, require the OpenTelemetry Metrics SDK and wire that up.
And that meter will be, will be backed by the SDK. It will, it will be backed by the SDK, And it will be wired up as… as a global at that point.
And that's just because that's the way things kind of currently work. If you require metrics SDK, you'll get a meter provider.
We don't have to make it work that way, but this actually, is still, like, a valid… a valid way for this to work.
I don't know. Any questions about that? Do we want to look at some code, maybe?
**Kayla Reopelle** 37:03 Yeah, no questions for me right now, down to look at code. Would you rather share your screen to take a… Sure.
**Matthew Wear (Dash0)** 37:07 Yeah.
**Kayla Reopelle** 37:09 Let me find that…
**Matthew Wear (Dash0)** 37:27 I'm having trouble finding mine.
you know.
having trouble finding the window. But, Yeah, so the main things that, that had to change is that, Boom.
Is that we end up, having this global logger provider that we… yeah, so we kind of remove this where we wire up the, the logger provider on the OpenTelemetry module, and we instead require this global logger provider, and this is the one that sets it up on, on the internal module, as API private instead.
And then… there's this, There's this logsglobal.rb that is not required by the logs API itself, and this just kind of delegates. This sets up the logger provider on the OpenTelemetry module and delegates to internal, if that makes sense.
And then, And then, if you require the logs SDK, it will require that global, and that's kind of how it gets set up. So that's how you can kind of depend on the API and not get the global set up.
But you get the global setup as soon as you bring in the SDK.
And it's kind of basically the same thing for metrics, and that's really all we had to do on the core repo.
And then, The biggest change over here is just, instrumentation base. We now get, in addition to the tracer, you get a meter and a logger.
And we… And we, yeah, we set those up at initialized time along… along with the tracer.
And then, We actually wire these up with the right name for the instrumentation, which is actually a problem, which actually has been a problem, because we have some instrumentation that uses, that uses the logs API, but it's using the wrong, The wrong names, you're getting the wrong… so your… your traces… The name on your traces does not match the name on your logs, and they should all kind of be uniform for the same instrumentation.
So… Yeah, base is the biggest change, and then, instrumentation will depend on the Logs API and Metrics API, only API, not SDK.
And then… There were just some bug fixes of things that I found along the way, as well as just updating… updating these things that want to use, like, the logger to actually use, the logger. So this is how you'd use it in practice. It's the same way you get the tracer, you just gotta get the instrumentation instance, and then .logger.
But the… I think the other problem that we're having is, like, the name does not match, for example. This is… Oomph.
The name you would see on your spans is, like, Capital O, open.
capital T telemetry, and then colon, colon, capital I, instrumentation, colon, colon, capital L, logger.
So, the names are close, but they don't match exactly.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 41:20 That would come… that's the, like, the value for a telemetry SDK, that is the key.
The instrumentation scope, you know.
Alright.
**Matthew Wear (Dash0)** 41:30 Yeah, yes.
So… So, all in all, this is pretty straightforward, and it, follows the rules, I think, in OpenTelemetry, and I think it will allow us to use, like, the logs and metrics API from our instrumentation, which I actually think is a… It… it is a great way for us to dog food these, I guess, before trying to release them to the public, and, like, if we haven't used them, then I don't think we should be, be making them stable, so I feel like… We are the first to be able to kind of, like, find issues and fix them.
And, yeah, I guess the other thing I was just gonna mention is that, like, yeah, there's… There is precedent for this. I know, like, I was just looking at JavaScript, but… Their logs as development, for example, but if you look at At their instrumentation base, like, it's kind of… they have the same… the same thing happening, where their instrumentation is getting a logger and a meter, And, yeah, based on what Jack was telling me, this is kind of how stuff works in Java as well. So, like, instrumentation ends up getting, access to some of these unstable APIs, and, You know, users, if they wanted to, like, be… If they wanted to use these APIs, they can, you know.
But this is always a problem in Ruby.
We've… we're not advertising them as stable or putting them somewhere that's, like, easy for them to get access to them. So it's like, I think they know… they know what the hoops that they have to jump through to… to use them that they, are not.
Are not meant for their use.
I don't know, I've been talking a lot. Any thoughts, questions?
**Kayla Reopelle** 43:47 I think this is great. I have really wanted an easier way to use logs and metrics and instrumentation for a long time, and I think this solves Some important bugs, and knowing that there's precedent for doing this in other languages.
It's also reassuring to, you know, make sure that we're not breaking that kind of stability.
expectation.
And yeah, I'd love to get more metrics and logs, especially looking at that span event migration into our instrumentation sooner rather than later, and I think having it in instrumentation that's being used is going to be helpful for our stability.
Recommendation or review as well.
So, yeah.
Go ahead.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 44:34 Is it possible in the method that we have for creating a span event for it to use a logger underneath the hood instead of… Creating a Spain event, Spain event.
**Kayla Reopelle** 44:44 We… could possibly do that, I haven't really looked into it yet, But, yeah, I think we'd just have to think about if it's a breaking change or not.
**Matthew Wear (Dash0)** 44:56 Yeah, I think we'll have to… we'll have to think through that one, and see how other people are doing it, but… Technically, creating a log event, Chrome, from… you know, tracer.createEvent or addEvent, whatever that API is called, would mean that tracing depends on logs, which I think cannot happen. Yeah. I think it's actually supposed to be a call to the logger in your instrumentation instead, is the migration path.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 45:26 That makes sense.
**Matthew Wear (Dash0)** 45:28 Oh, that… I don't think you're meant to cross the signals like that.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 45:31 Yeah. Well, and… and while it… Yeah, agreed.
**Matthew Wear (Dash0)** 45:38 Bum.
Yeah, I think the… Yeah, though… The one thing that, Yeah, I guess the one thing about all this is this thing… is this, Functionality, it crosses kind of, like, several dependencies, and… I guess just the sequencing of things that need to happen. I need to think through that. Like, we can't just turn these draft PRs into, you know, non-draft and start merging them, like, it's a little more complicated.
Because of the fact that Yeah, I think we're gonna have to do, like, the core changes first, and then, like… So these changes to these API and, SDK gems, and those need to actually release.
And then, I think we need to do bass.
And then bass needs to release, and then we can do the instrumentation. That's kind of off the top of my head how this will work.
I need to, Think that through just a little bit more to make sure that that is the right… Oh, the right sequence?
**Kayla Reopelle** 46:48 I think that seems reasonable.
Right now, and… Yeah, we could… try it one signal at a time, but I don't think we have to.
But yeah, I understand that that means probably opening up some separate PRs, maybe, for these to merge, or…
**Matthew Wear (Dash0)** 47:10 Yeah.
Yeah, I think, you know, this one may be actually the one on… core probably works as is, but I can just split this into one for… metrics and logs, I think that'll just make it a little bit easier to review. And then… I think that's going to be the prerequisite for the stuff going on in Contrib, and Contrib, I think, we just need, once we have new API, gems, then we can, have a PR for base, and then, base can depend on those new API gems.
And… And then we need… To release bass, so that, we can update instrumentation to use the… The new base, and… We might run into some problems with our versioning if it's too loose, but we'll figure that out.
as well.
**Kayla Reopelle** 48:09 That sounds good. I think because this is such a complicated release across many PRs, what do you think about opening an issue that kind of documents What release order we need to take, and kind of links everything so we can make sure we're just checking off boxes rather than trying to keep track of a bunch of stuff.
**Matthew Wear (Dash0)** 48:26 Yeah, that sounds like a good idea, and Initi seems like the right place, because, like.
it can't really go on a PR because there's multiple PRs to coordinate, so I'll… I'll draft that up next, and then I'll kind of take the steps of, like, breaking this… breaking these down into their PRs.
**Kayla Reopelle** 48:47 That sounds good.
**Matthew Wear (Dash0)** 48:57 Anything else on this topic?
**Kayla Reopelle** 49:01 So I… am wondering if, I guess I should move the OpenAI… Should I take out, I guess, the log stuff from the OpenAI pull request that I have right now, and take it back to just a CI update?
And maybe hold off on release until this goes through? What do we think about that, Jim?
**Matthew Wear (Dash0)** 49:30 I don't have super strong opinions, like… I think… Well, I think the one thing we can do is… if you want to get this out, I think… this hasn't had a release yet, right?
So I think the one thing that we could do is… I don't know.
Maybe I need to think this through more before I say anything, but we should… We should look at this, but if there's a way to, like, make this a seamless transition to the new way.
Then maybe we can, release it as… as is, and then transition when it's ready. The one thing that needs to happen, though, I think, is the name needs… should be updated, actually, so we don't end up with a… Breaking change when we do migrate.
So… I think the TLDR is… If we can migrate that transparently, and nothing will break, then we can, kind of… ship that. If it's going to be more complicated, then maybe we, hold off.
And I don't know, maybe I can look into this as we… as I come up with a plan.
The sequencing plan for, poor… Making the… Yeah, making… The metrics and logs API is available to instrumentation.
Possibly.
**Kayla Reopelle** 51:03 Nice, yeah, that sounds good. If you can just think it over as you're processing stuff today, I'd love to get OpenAI out before the end of the month.
And I also, if it makes sense to hold it back, that's fine too.
Yeah, so whatever, whatever makes the most sense, I'm happy to adapt.
**Matthew Wear (Dash0)** 51:26 Cool, yeah, let me work through that as I work through the other sequencing, and we'll come up with a plan.
**Kayla Reopelle** 51:34 Okay, sounds good.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 51:39 If you get to a point where it's ready for a re-review, Matt, if you were to mention it in CNCF Slack, that would get my attention a little better than… Just activity in GitHub.
**Matthew Wear (Dash0)** 51:49 Cool, yeah, I'll do that when I get the issue and the real PRs up.
**Kayla Reopelle** 52:00 Sweet. All right, well, we're nearly at time, and we're through our agenda. Any other, like, burning questions or concerns we should discuss in the couple of minutes we have left?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 52:26 I don't have anything.
**Kayla Reopelle** 52:30 We'll… I'll take the silence, then, as we're good here.
So yeah, thanks everyone for the great discussions today. Seems like we have a lot of… stuff that we're building towards, and I'm excited about that. So, we'll see each other on Slack, and see y'all next week.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 52:48 Indeed. Take care, everybody.
