SIG: Python SIG
Date: 2026-08-13
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Riccardo Magliocchetti 00:00:31 Hello, Magukas.
Lukas Hering 00:00:34 Hi, Riccardo.
Riccardo Magliocchetti 00:02:38 So welcome, everyone, to this week's Python SQL.
We're within a few more minutes for more people to join.
In the meantime, in the meantime, please add yourself as an attendee, and also feel free to add any topic you want to discuss. Thank you.
Aaron Abbott (Google LLC) 00:03:39 Hey everyone, how's it going?
Riccardo Magliocchetti 00:03:45 Yeah.
Diego Hurtado 00:03:46 Hey! Hello, everybody.
Riccardo Magliocchetti 00:04:01 Yes, it looks like everyone is on PTO this week.
Okay, I guess we can start?
Saw some triaging, yeah.
Oh, okay, welcome again, and if you haven't added yourself to the attendees list, please do so.
So… First one is invaluable metadata in Azure Resource Build.
detector build.
Okay, seems… Premium?
Okay.
Not so trivial, though.
That's interesting.
But I guess it's… Ready to review.
But… Yeah, like… I have an idea, optioning 1.27 is… New, or released, anyway.
Please review the view.
Okay, when we have this one for SDK, exem library server bucket before sending.
We don't have a tracking issue.
But, yeah.
Looks like a fix, so… Possibly ready for review.
Stuff very well.
And then… okay, this one from Diego, and this is interesting. Could you please elaborate a bit on… the issue?
Diego Hurtado 00:06:33 Right, did I add… did I add that?
Sorry, that's 3SG, yes, sir.
Aaron Abbott (Google LLC) 00:06:42 the one we talked.
Diego Hurtado 00:06:43 Ugh.
Aaron Abbott (Google LLC) 00:06:43 That'd be great.
Diego Hurtado 00:06:45 That's right, yes. So, for the injector, we have, I mean, every dependency that we have, it's a risk in injectors, so what we're trying to do here is to implement Part of the packaging, Functionality in our… In a repo, just like, I proposed for protoboth.
We discussed this last week, got, thorough ideas from… Other people regarding… How to better do this in the way In the sense that this is code that we are adding, and Maintaining it, it's, it's a burden.
For us, so… ways to minimize that, that could be rendering, stuff like that. So, I still haven't, looked into those ideas, I have to do it as soon as I have, I'll update the issue.
Riccardo Magliocchetti 00:07:54 Okay, thanks. Yeah, yeah, like, no need to discuss this again. I yet have to… To listen to last week, cool.
Anyway, like, I asked because I was looking at the packaging, like, Michaela showed me some… linked me some packaging code, and I see that you're using packaging there.
Diego Hurtado 00:08:13 No, no, no, that's… that's just something that's named packaging, but the packaging SIG is just a different topic.
Riccardo Magliocchetti 00:08:20 Okay.
Diego Hurtado 00:08:22 Okay.
Riccardo Magliocchetti 00:08:24 And then… we have 2 more minutes… Okay, I've seen also this one, and I also… I forwarded the issue and PR in the Genera instrumentation channel.
Aaron Abbott (Google LLC) 00:08:39 Yo.
Riccardo Magliocchetti 00:08:41 Yeah.
Like, we probably, like, need to make… more clear, but… We don't want to touch base instrumentation anymore.
But, like, if you're going to… to release, A new version with the deprecation.
We need to also sort out this, like… Or just, like, Reducing the supported, instrument to pin a library to less than 3.
Or… merge with SPR, like…
Aaron Abbott (Google LLC) 00:09:22 I think we updated, like, the docs and the agent docs to tell people to contribute to the other repo. And then the plan Of course, is gonna be to delete these after the release, so… I think we should just redirect this one to the other repo, not merge it here.
Riccardo Magliocchetti 00:09:41 Okay Yeah, but, you know, but… The problem we have is that the release are the last of Navy to release.
is, I guess, crashing with OpenAI 3, but yeah.
Okay, then, gRPC? Okay… This is an audit show.
And then OPR.
Let me check.
Ultimately, the ridiculous, yeah.
Okay, so we have this issue from last year.
And the PR is smaller enough.
Okay, so if anyone has some… GRPC clue.
Please take a look, but… It looks like.
Sophie, what can I review.
So… Oh, it is in.
Yes, ready for review.
Okay, and we are late.
Okay, so enough with that.
Judging… First topic is from me, and this is, like, the… service name behavior, we have an SDK.
So… I was looking at fixing, the… the SDK behavior when running under… configured by the CADI config.
Where we are not following the semantic convention, because we are not currently adding them.
Base name of the executable process, running the application after the unknown service name.
And so… Pablo?
Where is it?
Nope.
Okay.
So… no. Anyway… Pablo, when doing the review, Noticing the difference of behavior?
from the current SDK code.
Where, We implement it properly, in the sense that we append the process name for some definitional process name, because it's wrong, but it's another question.
another issue.
And, but, like… We are not just calculating the process name.
If someone will set manually the plus-executable name as, For a source attribute, we'll use that.
And so I asked… well, first I took a look at the other languages implementation.
And everyone is doing something different.
Javascript is… Ignoring the suggested algorithm for finding it out, and just using the first, Arguing?
Java just uncodes Java, and go… Do something similar than us?
Where, like, there is a… an helper from the Standard Legos and the Library.
But returns, like, as a capital name.
And if it's not able to find out using this, we'll set our code, good name.
channel, and… It has been suggested that… We shouldn't look… I thought the attributes when, building this, And no service, service name.
I saw the discussion.
And so my question is, are we fine in, changing this behavior… It is being added, I think, since 2021.
Bye.
to see the actor here, because he added this, but 5 years ago, I guess.
Anyone?
Like, no one can remember why.
And so… If anyone has opinions.
Diego Hurtado 00:14:50 Okay, why is, wait, do we… why do we consider this to be a breaking change?
Riccardo Magliocchetti 00:15:02 Because people will get a different, weather.
It's not really a breaking change, but a change in behavior.
Diego Hurtado 00:15:14 No, that's fine. I mean, I want to understand… okay, let me rephrase my question. Why do we think this Can affect users.
How do we think users will be affected?
Riccardo Magliocchetti 00:15:31 research, like, if… Someone, for whatever reason, will set manually the process executor name, but not set a service name, but we'll get a different… service name.
And, if you have queries.
looking at values in the service name attributes you may store in your DB.
It may break still, something. Like, I don't expect people But cares about this stuff to not set the service name.
But, yeah, it's more periodic, periodic.
Furity of it, whatever, more than practical.
Aaron, you have your own answer raised.
Aaron Abbott (Google LLC) 00:16:18 Yeah.
Diego Hurtado 00:16:19 I have more to say, but I'd like to hear Aaron first.
Aaron Abbott (Google LLC) 00:16:24 Yeah, I was gonna say, this one kind of feels like the bug territory.
I think, obviously, the potential thing that could hit people is their queries might break if they're, you know, doing, for some reason, matching, like, metrics or whatever on the specific attribute, but I think the like, this one seems more like a metadata kind of attribute to me, to be honest, so maybe it's unlikely. I just… I wanted to call out that, like.
There's… there's also a schema version.
Which is supposed to kind of let people know, but, I mean… Presumably when we implemented this, whatever you said, 5 years ago, it was before the schema version, or this was in the semantic convention, so… the… the only problem, I think, is there's no schema version on resource. I think it happens through, entities, and somebody keep me honest there.
Yeah, perfect. Limila, do you want to jump in?
Can't hear you if you're talking Ludmila.
Liudmila Molkova 00:17:29 I know? Sorry.
Yeah. What is it today? Is it a known service?
Like, if nobody said service name, it is a known service, right?
Riccardo Magliocchetti 00:17:39 Yeah, the problem is on the second part, on the… And the process is executable there.
Liudmila Molkova 00:17:47 Right, so the break and change would be that people would get, instead of unknown service, they would get something meaningful.
And if they happen to match against a known service, it will break.
Riccardo Magliocchetti 00:17:58 No, no, no, it's… Now it's a known service.
And then, a process executable name.
At the moment, if you set a process executable name and source attributes manually, you'll get this value.
And… what they're implementing in the declarative config path is that we don't look at currently set resource attributes.
And we just get the value we read from… There are 6 executables in this scale.
Liudmila Molkova 00:18:37 If we are worried about breaking changes, can we limit it to declarative config? Whoever opted in into declarative config opted in into new behavior?
This is non-breaking.
Riccardo Magliocchetti 00:18:48 But my idea was, like, to… also fix the current SDKs.
Liudmila Molkova 00:18:55 Okay.
Riccardo Magliocchetti 00:18:57 So, to be, like, the same way we will be without the config.
I lost you at the end of the race.
Carlos Alberto Cortez 00:19:05 Yeah, I would like to clarify.
Diego Hurtado 00:19:06 code.
Carlos Alberto Cortez 00:19:07 Oh, sorry, yeah, I would like to clarify something, but my impression is that Currently, the problem is not that the SDK is setting the service known to as known service, which is something that other SIGs do as well. The thing is that if you are using resource detection at the SDK, and the user provides there a process name, then you use that.
I think that's the problem, right? Which is something you are not seeing in the… declarative configuration part. That's what you are afraid of changing.
Riccardo Magliocchetti 00:19:45 Could you please repeat?
Please, like, I don't think I understood.
Carlos Alberto Cortez 00:19:51 Probably it's better if I just, share my screen, so give me 2 seconds, probably they all can go in the meantime.
Diego Hurtado 00:19:59 No, Alberto finish.
Carlos Alberto Cortez 00:20:04 The thing is that I had to find the exact file.
Or it may take a little while,
Diego Hurtado 00:20:11 Okay. Alright, nope.
Well, what I mean is that, Any change is a breaking change.
Depending on the user, right?
So, what I'm trying to say here is that, any change we make and… Introduce non-desired behavior.
For a particular user.
we are… if this is something that's wrong, in the sense that, I mean, if you're going against thematic conventions.
We gotta fix that. And, This is a job for the changelog, in my opinion. Can… introduce a message in the changelook that says, hey, by the way, we did this thing, and so if you're doing that, you can probably be… Affected by this change.
Carlos Alberto Cortez 00:21:11 By the way, I'm ready to share my screen, if that's okay. No, actually, that was good. Whoever was sharing, that was good enough.
Could you share again? But yeah, that's basically the line. Thank you so much, Lukas. Lukas. So basically, I think that the problem is this one, which is that basically you are using a non-service, which is totally fine, but then the thing is that if you check, on LAN line 1956. Basically, that's the breaking change, if I understood correctly. Like, you don't use… The actual executable, but basically, if the user passed, as part of resources, a process executable name, then you use that.
So, if any user was relying on that, they will be broken. I think that was my understanding, that this would be the problem. Is that correct?
Riccardo Magliocchetti 00:21:58 Yes.
Carlos Alberto Cortez 00:21:59 Correct, okay.
So I would treat that, as a bug, as somebody else said before, because no other implementation, does this.
Probably it's worth checking with users, or do some search, but overall, I would consider this as a bug.
Riccardo Magliocchetti 00:22:22 Yeah, like… I don't expect people that manually set this one to not set also service names.
Right. Okay, so… Good to know.
Yeah, through the notes.
Diego?
Diego Hurtado 00:22:56 I wonder if we could have, like, tags in the changelog for situations like this, a tag that says, like, warning, right? And explains what we do here.
So that, we can highlight things that we think Kind of cause some desire behavior.
For a user.
Riccardo Magliocchetti 00:23:21 Yeah, as Lukas said, Louis… We added in the… breaking in,
Diego Hurtado 00:23:29 Right. Cops. I… Yeah, I get the intention. I… I think I would… Reconsider using the word breaking.
Because, it's kind of weird to see a changelog that says breaking, and we don't have a major… version release, right? But something like that, that's the spirit.
Riccardo Magliocchetti 00:23:57 Yeah.
And also related to this issue.
When looking at the current SDK code, I noticed that… The values were, like, Wrong.
Like, we set the path instead of the name, and the full path instead of the path.
Oh, oh, sorry, only the deer name instead of the path.
Yeah, so… yeah, like, Aaron did some digging into the… Implementation.
And, yeah, like, if you're using this sys executable, It won't match.
what, semantic conventions suggest, but is to look at and resolve to whatever proc, PDEX points to.
But… as I… said before, like, no other SDK really look or solve this link.
So I guess, for the sake of simplicity, I think it's fine.
to, like, And the difference is that one has… One… one will display.
Python 3 and Python, sorry, and the other will display Python 3.14.
Which I don't think is a… It's a big issue.
Aaron Abbott (Google LLC) 00:25:32 Well, I mean, I think it's more like if you're running in a virtual environment.
You can get, like, these sim links.
Or if you're running, like, it's not just about the version number, right? It's like, if you're using the build from UV or the system executable and stuff like that, it might be hidden if you're using sim links, but, like, I think either behavior is defensible, but it does seem like the… Excuse me, like, the semantic invention says to resolve all the links.
But clearly, like you said, nobody's doing that.
Riccardo Magliocchetti 00:26:04 Yeah, like, on the other hand, like, I have no idea if… Other languages have the same issues.
Like, like, where the path of the… Interpreter or runtime is not… Like, it's a SIM link, or…
Aaron Abbott (Google LLC) 00:26:23 Yeah. I also just shared, I looked at the Go. Thank you for digging into the… what Go does in it. It looks like they don't even… define… I don't know if you can see my comment.
Basically, it says that depending on the operating system, the.
Riccardo Magliocchetti 00:26:41 Yeah.
Aaron Abbott (Google LLC) 00:26:42 Salt might be a sim link, or the path… the underlying path for the sim link, so…
Riccardo Magliocchetti 00:26:45 It's… I read it on the.
Aaron Abbott (Google LLC) 00:26:49 Yeah.
Riccardo Magliocchetti 00:26:49 library documentation.
Aaron Abbott (Google LLC) 00:26:51 Yeah.
So I… yeah, I don't have… like, I think maybe it's separate… a separate question from the change, and this seems like a small thing to update later, but, like, the… I don't know if anybody worked on the semantic dimensions for this one, and has, like, a strong opinion, but… yeah, they seem like distinct things, and… Yo.
Riccardo Magliocchetti 00:27:18 So, like, a…
Liudmila Molkova 00:27:19 Could be…
Riccardo Magliocchetti 00:27:20 Sorry, sorry. Go ahead.
Liudmila Molkova 00:27:22 Yeah, sorry, the semantic conventions are in RC?
And if you believe there is something that's not clear from them, this is absolutely the right time to raise it. So please create an issue.
Aaron Abbott (Google LLC) 00:27:41 yeah, sounds good. Riccardo, do you want me to do that?
Riccardo Magliocchetti 00:27:46 Yeah, like… I don't think semantic information, not clear.
The problem is that everyone is doing something different, more than… And I guess for Gorilla, because the implementation is older than the semantic information, maybe?
So maybe, like… We should probably ping the other SDK… other languages, Sikhs, and… And say, like, please take a look at the service name.
Because everyone is doing very often.
But yeah, like, maybe I can, open a different semantic convention and… Cite the languages groups.
Liudmila Molkova 00:28:35 Yeah, that would be great.
Riccardo Magliocchetti 00:28:38 Let me add it to the notes before.
Aaron Abbott (Google LLC) 00:28:42 Yeah, I was just gonna say that sounds good to me, but I don't wanna block this PR, because I think… If it's vague, there's no point waiting.
Because the… the greater bug is much more… disruptive, so…
Riccardo Magliocchetti 00:29:12 Okay, so, and… So the thing is that, at the moment?
If you're not… if… We don't care, we don't have, a value from a sys executable.
We don't, append the… This process name?
So I was wondering if… We should follow other languages and Articoda, Python.
Or… Nope.
Like, I'm pretty sure that… No one is looking at… Like, any… no one is using this second part to… Discriminate between languages, but… Because, like, we have a ton of other fields in the CSUS attributes in order to do that.
Yeah, maybe, like, assholes, or… As this in the same semantic machine, if you will.
And we figured out that.
Aaron Abbott (Google LLC) 00:30:19 Riccardo, what was the case where… It cannot be there? Is it… is it, like, some niche thing, or is it, like, Windows, different operating systems?
Riccardo Magliocchetti 00:30:29 Now, I think we have it on Windows. I have an idea In which case, but the documentation… in the Python library, it says it can be none or an empty string.
But not the case, and I started to look at the… see Python code, but… I haven't found the actual implementation, because the excludable is returning a field in some struct, but I haven't found who set the… this value.
Okay.
Next talk… next topic from Carlos.
That's great.
Carlos Alberto Cortez 00:31:22 Yeah, this is one about adding this, dashboard, it's from the shared workflows, And other SIGs are using that, basically just goes and creates this issue, which can be pinned.
And the top-level repo, so it's always visible.
But basically, it's trying to gather a summary of what… what's going on. And it updates, you know, every some days, and you can go and check what's the status, and that's something that we could use.
It was mentioned in the specification call, by the way, so if you were there, you already know what this is.
And it can be enabled at the Shared Workflows repo, and then it will just automatically, once it's added, it will just be Yeah, doing this for us.
I don't know if you… if you people have any opinion of this one. I think it could be… We're To stay in the loop of what's happening.
Emídio Neto 00:32:25 Yeah, I just have one small question. Do you have any repo?
With, like, more than… 100 of PRs open, how it looks like in the issue body.
Because I know GitHub has, bought Limit… on the issue, and PR description, and things like that. So I'm afraid that… the body will be truncated at some time, at least for Python reposaris.
Carlos Alberto Cortez 00:32:54 After 100?
Emídio Neto 00:32:57 Yeah, I think, for Python, we have almost 170 PRs open.
Carlos Alberto Cortez 00:33:11 No, no idea, good question, yeah. Yeah, Liudmila, by the way, posted a link there, you can see that.
Oh, you opened that already, good.
No idea about that. Agohev.
Liudmila Molkova 00:33:23 I… if something doesn't work, Trask is usually very fast to fix it.
It's, like, something that we did for ourselves, and there is a link in every commented post, like, where you can just go ahead and create an issue. I don't think there would be any problem in doing something custom for repos with a lot of pull requests.
Emídio Neto 00:33:52 Yeah, like… Yeah, it works, like, if we can add in comments.
The rest of the body.
Riccardo Magliocchetti 00:34:05 Yeah, and I think that's… Thank you. Let me add on this, but I don't remember which call it was, but Trash said that we don't need… we don't need to provide any token.
So, it should be easy to… to introduce.
PR2.
And she'll probably find the link from the shader repo.
But, I've seen it in some other notes. Yeah, exactly.
Carlos Alberto Cortez 00:34:37 I just posted a link in the chat, that's how a PR would look like Jack from the Java Ward just did that for the specification, so it's very easy to do. It's just mostly about the decision of the group itself.
Riccardo Magliocchetti 00:34:58 I think, we can give you a try, like… But everyone seems to agree, but… It's Artemis.
Emídio Neto 00:35:08 Yeah, I agree.
Riccardo Magliocchetti 00:35:16 Anyone?
Volunteering for creating the… Sane for us?
Okay.
The volunteers?
Emídio Neto 00:35:37 I can add.
Riccardo Magliocchetti 00:35:39 Thank you.
Okay?
Next one is from Diego.
Diego Hurtado 00:36:00 Yeah, so Riccardo, let's do something. I have two topics, Let's start with the one that I have below, and then let's continue with the medios, because the one that I have below is actually the most urgent.
Riccardo Magliocchetti 00:36:16 Okay.
Diego Hurtado 00:36:20 Right, so we have been discussing this for a while, and, We wanted, you, Riccardo, to be present, also, for the discussion, so… We have noticed, that, we get too many PRs, and actually, it was great that we just discussed this topic, because, The fact that we have, so many PRs open, right?
What's, It's completed, so I think there is, some support from… Several people around here to follow this approach.
Which is pretty straightforward. It works like this. Nobody can open up your app.
With a few exceptions, for maintainers and so on, right? First, you need to submit an issue.
The issue gets discussed, and Then, someone gets assigned to that issue.
And that person is the one who can open a PR, To close this issue, right?
If someone opens a PR without following this process, there's a bot that will automatically close it.
People can open draft PRs, That's fine.
Many times, many times it's useful to have a PR when you open an issue, so that you can I don't know, explain what… We are trying to do with code.
That's fine. Graph PRs are… are acceptable.
But, And yeah, I… some… A few things were discussed regarding what happens when somebody gets an issue assigned, and there's no progress, so… there is already a PR for… that I opened here, that creates a GitHub action that, after a while.
It unassigns that issue to that person, if that happens.
This PR that, that I opened, 5386, also includes these exceptions for maintainers, so that maintainers can open a PR straight without an issue.
So yeah, now that, we got you here, riccardo.
I think it'll be a good moment for… to discuss this.
Riccardo Magliocchetti 00:39:03 Okay, so, a few random folks.
It seems to me that… We had… A wave of random people throwing bots.
And open NPRs.
That scared us.
But lately, I think that… the… maybe still AI assisted whatever PRs we get.
Looks like a more decent.
And so, like, before, going, like… And setting up these kind of processes.
I would really, like, try to… X.
fund the contributors that may care, and so get, like, approvals, rights.
In the repos?
Because, like.
even if we had all these processes, I think the bottleneck is still that we don't have enough.
Eyes and time from people.
looking at PRs.
Yeah, liudmila, I'm not sure we can do that with the Terraform, like, I… with the terraform configuration.
Unless any other repo has been able to do that.
Liudmila Molkova 00:40:50 I think Marilla did it, and she has some… she wanted to share something in the maintainer channel, I'm not sure if she did.
Riccardo Magliocchetti 00:41:01 I don't remember that, but…
Liudmila Molkova 00:41:05 I'll check with her, but it can be done. The other thing to add to what you're saying… sorry, Aaron, I don't want to interrupt you, but it's just… the flow that this PR dashboard enables.
is that you… Prioritize what's waiting for reviewers.
when I bought, or… Well, human-driven bots and the PR.
the Copilot review automatically reacts to it.
And as long as there are open comments.
That author did not address. The PR stays on the bottom, and nobody ever looks at it, and most of the bullets never come back to the PRs they created.
And this way, they can create how as many as they want, we just never look there, we don't care, because we see that the PR is on their side.
Diego Hurtado 00:42:02 But wouldn't it be better not to have PRs at all?
Not to have these PRs at all.
Liudmila Molkova 00:42:09 I don't know, like, some of them are genuinely people who want to contribute it, but they just don't know how.
Also, it puts a lot of process on us and on all the contributors. We create gates for the good people to fight bots.
Right?
Diego Hurtado 00:42:26 No, no, no, we… we are not, this process is rejecting every PR that comes up without an issue. So people can still contribute, they just need an open… to open an issue first.
Liudmila Molkova 00:42:39 It is a gate, right? It's a lot of friction.
It's a lot of time, and in order to fix a trivial bug somewhere.
We would just create more process to prevent it from happening.
Diego Hurtado 00:42:53 I mean, it, it is, but, Most of our issues are, I don't think, trivial bugs.
We… We kinda have to discuss… Reach an agreement, since this is an open source project.
So, most of the contributions need.
Conversation for us.
Liudmila Molkova 00:43:22 Some don't, but I think what we're trying to protect, the number of open PRs or human attention? I think if we're trying to protect human attention, then we can have multiple ways to do this. Number of open PRs becomes slightly irrelevant, and the stale boards can be more aggressive, closing them.
Diego Hurtado 00:43:42 We can protect both with this approach, the… I don't think, but… open… I mean, bots open PRs, because their intention is to get a commit in a repo, so that, I don't know, people can claim credit of having contributed to this open source project?
But they don't have the same incentive when it comes to issues.
Because if they open an issue, they don't get… any commit.
In their, in the repo, so there is no incentive for them to spam with issues.
So… This process, I think, benefits us twofold.
Because it first stops, removes incentive for people to have bots that open PRs.
And, and the other thing is that, it's, it actually… Helps us, no.
the… I mean, it implements, A way that we can just focus on the issues.
That's the only thing we, as maintainers, need to focus on. The PR will come at some point… at some moment, and… get reviewed, and I'll implement whatever it was discussed in the issue.
So human attention is… It's not as spread out as it was before.
Because maintainers now need to focus mostly on the issue.
Not on the… not on the PR. And nowadays, actually, code is pretty cheap, right? It's mostly AI-generated.
So, human attention is more valuable.
to… to put in on issues, rather than their PRs.
Aaron Abbott (Google LLC) 00:45:46 Sorry, I'm just gonna jump in, say one thing, or two things. The first one was, do… can we, like, set a time box, or a time to aim to finish discussing this? I'm just worried about, there's a couple other agenda items.
Maybe, like, we can give it till, 12.50? 12.50 my time, is that alright?
Diego Hurtado 00:46:09 Share for more minutes.
Aaron Abbott (Google LLC) 00:46:12 Yep.
And I was just gonna say, on the concurrent PRs thing, regardless of all that stuff, I think we were struggling to find a number, and then immediately after that, somebody, like, opened 100 or maybe, like, 50 PRs. There were some AI flow, so I think that kind of… straight… straight up, like, abuse of the system, we should probably… limit the concurrent PRs, but I think that's maybe a separate topic from all this. And I think it's a good starting point, though.
Liudmila Molkova 00:46:44 Yeah, I just wanted to add that, focusing on the issues is not, what I think the main responsibility of the maintainer.
I think we… We maintain the project, we want to get bug fixed, we want features to be addressed, we want to grow the community.
By adding friction, and process, we just spent time on the… Creating gates rather than getting better contributions.
We will block both boats and… Humans trying to start contributing to the project.
Diego Hurtado 00:47:35 Right, oh, Lukas.
Lukas Hering 00:47:38 Yeah, I just want to add, I think… Like, I mean, we can maybe try something out in steps. I think the… PR limiting… I know we brought it up a lot, but I would say that's the first step.
And I wouldn't be opposed to, like, requiring issues on PRs.
Maybe not… Maybe not require, like, the assignment right away, but at least just, like, requiring just a link to an issue.
Even if there is, like, a small bug you want to fix, like.
I don't think it's… I don't think it's that much effort to just create a new GitHub issue, just to describe what the issue is, and then link it to the PR.
I mean, it's also, you know, pretty… you can have Codex or Cloud do that for you, even, so, like, Yeah, that's just… that's just my thoughts. I do, like, kind of get the point, though, that, like, we don't want to… Actively discourage, like, Real people contributing, but at the same time, like.
We're limited by mostly review time, so… There's that to take into account, so…
Liudmila Molkova 00:48:54 My proposal, give it the… make her pilot, make the first pass and review.
Very few bots pass it.
you would never see the PRS, that people, like, bots sent that Copilot rejected, because there is no issue, there is no, point, or it's alt, or something. Just put instructions in the Copilot instructions. Don't review it by humans.
Lukas Hering 00:49:18 Yeah, I think… yeah, I think that would be, like, a good first start. I don't know, do we… do we have that enabled already? Like, I've been seeing… I thought I saw a few times where Copilot left a comment without asking, but…
Liudmila Molkova 00:49:33 I think it's not on by default, but you can turn it on. I think it's in the admin repo, to turn it on by default for every PR.
Riccardo Magliocchetti 00:49:47 Okay?
We're 10 boxed, but I'll have the… to simple facts.
When discussing the number of concurrent, PRs we should allow for new contributors.
I run some scripts to see who's the, like.
What's the median or the percentile?
And I think that, Lukas, you were the outlier with the most open PR at the same time.
And we don't want to discourage you to open PRs.
Liudmila Molkova 00:50:23 You can set it by role, right? So, first-time contributors can get one.
And if you are an approver, you can get more, or unleavened.
Riccardo Magliocchetti 00:50:32 Yeah, but…
Lukas Hering 00:50:34 I've, I, I…
Riccardo Magliocchetti 00:50:34 Thanks, man.
Lukas Hering 00:50:35 Trying to slow it down, sorry.
Riccardo Magliocchetti 00:50:37 No, it's not, it's not likely.
it's that, like, I've been on your same position also, like, where, like.
you open more PRs when people can review.
And it's not your fault. The fault is meant to… I think we are kind of unbalanced on… Like, we produce more, we can review.
And the other thing I would like to say is that, have you seen before on the… when we did some triage?
all the PRs were legit.
There was a nice description. Most of them, I think three-quarters of them had Valencia dishes. The other one were all trivial, or well explained.
And so, like… It's not something that… like, I agree with Limila, like, we should not add friction for… people doing the first contributing, but doing them. They're, like, doing this contribution, like… like, as I said, for a decent way, like, writing good code, writing a good description.
I stuck at that.
But, yeah.
So… Sorry to… Overflowed by 2 minutes.
Aaron Abbott (Google LLC) 00:51:59 That's alright. Do we feel like we know the next steps? It sounds like we want to… look into doing the concurrent PR aluminity again, and then enabling co-pilot reviews as a first step.
Riccardo Magliocchetti 00:52:11 Yeah, I think we can try both.
Aaron Abbott (Google LLC) 00:52:14 Okay.
Diego Hurtado 00:52:17 What about this process, then?
Do we get a next step for… This one?
Riccardo Magliocchetti 00:52:28 Click.
Me personally, I would like to try something else before adding more processes to the contribution.
process.
Like, I always try to… To, you know, increase our, review Availability.
Instead of decreasing the… the PRs.
Or get… or… as Liudmila suggested, to get… AI assisted reviews before.
people attention.
Alright. Okay.
Thank you.
Next topic is Emidio.
Emídio Neto 00:53:20 Hey, while you're reviewing some PRs, I noticed that we have at least 4 PRs that are, trying to add new semantic convention attributes to messaging instrumentations, mainly Kafka.
The thing is… We don't have the opt-in.
CENCOM support for messaging yet?
And, QN7 Convention is in development for… for message.
So I'm really not sure how to proceed with those.
like, we can't simply… chose, Modify the attributes and break the queue out.
Cementations? Implementation?
So I'm wondering what we think, if you should support the… some converting.
Or do we allow some breakages?
Riccardo Magliocchetti 00:54:29 Lukas?
Lukas Hering 00:54:31 Do all… or… I see that example had previous messaging attributes So, in that case, I would say we should… we should add the opt-in for messaging, but… I think for packages that don't have any.
Does… does… does… I don't think Kaf… does… does Kafka have… That many, or any?
Emídio Neto 00:54:53 There are some, like the closer IT, alerts…
Lukas Hering 00:54:58 Oh, okay. Yeah.
Emídio Neto 00:55:00 Salini.
Lukas Hering 00:55:02 I was just gonna say, like, maybe we wouldn't need to add the opt-in. If we didn't have anything previously, there's no… there's nothing that breaks, right? So… Maybe what makes sense there, but also for consistency, maybe we should just… Do it this way.
at least, like, I think… For one instrumentation, I added some metrics, and they were using the new SEMCOMF, and I just… there weren't any metrics previously, so even in that case, I think we still required the SEMCOM opt-in to be enabled to enable those metrics.
And then by default, nothing was emitted.
Emídio Neto 00:55:37 Right, yeah, I remember the sun.
Yeah.
Lukas Hering 00:55:40 Yeah, I would say, I mean, my… Take would be just to… it should be pretty trivial to just add the new option.
to the utility.
Library.
Emídio Neto 00:55:53 Yeah.
Yeah, just bring here to sake of diligence to… check with the… with the group. But yeah, I can volunteer to… other helpers.
And protocols can use those to implement, if they want.
Liudmila Molkova 00:56:12 I was going to say that the person who contributed for 7 to 7, he was interested in messaging in general.
And he was interested in resurrecting Symmetric Convention's messaging group, so maybe he's open to driving more than just this attribute and also implementing the, opt-in.
I'm just taking care of more semantic… oh, sorry, more instrumentations than, just this specific one.
Emídio Neto 00:56:43 Nice. Yeah, I think once we have the helpers, it'll be easy for anyone to implement.
Liudmila Molkova 00:56:51 Nice, thank you.
Emídio Neto 00:56:52 Alright, thank you.
Aaron Abbott (Google LLC) 00:57:04 Cool.
I added one more thing at the bottom. We've got 2 minutes, we probably won't make much progress, but I guess I'll just mention it right now.
So… oh, I also have the issue from Jask. Basically, I was gonna say, like, huge portion of the time that I add something to the merge queue, it fails because of the… it basically times out because of the… GitHub workflows queuing.
So I opened, this issue, and it doesn't… It's weird, because I do think other repos are experiencing it.
But nobody's really interacting on the issue, and… You can see Tras left a comment. I think, if you can… we're sharing, yeah, if you scroll down a bit… A little more to Trask's comment.
So I think the… these numbers in the table, the left side is the number of jobs And the right is the P90 in minutes to get picked up. But, as you can see, also, Python is, like, the outlier in terms of number of jobs, so… I'm wondering if, like, the way we have our CI right now, it seems to not work well with the GitHub org limits, so I… I'd like to, like, verify this before we make changes, but, Yeah, is this bothering anybody else? Any thoughts?
Emídio Neto 00:58:26 Yeah, I have noticed this behavior during peak hours, like… early morning for me, my time zone, I don't, like… Everything is working pretty fast.
But… Right now, if you try to put some PR in the merge queue, you see that behavior.
Fortunately.
Riccardo Magliocchetti 00:58:50 That's…
Lukas Hering 00:58:51 Now that we have the merge queue, we could… I don't know if we want to stop, like, select… some checks to not run on PRs.
like, Docker tests, for example, I don't know if there's some other ones, would… I will… I also wonder if, like, If we, would… like, coalescing the PyTest tests into a single, like, logical job, would that help here? I don't know.
Aaron Abbott (Google LLC) 00:59:25 Yeah, yeah, so I… I think it would help in the sense that, like, the limits are… there's a burst limit on GitHub, and then there's limits based on, like, the overall number of jobs, but it's not based on, like, CPU time or anything like that. So I think doing some kind of, like, discharting them into buckets might help.
So it's something we can definitely test out, but I also like the idea you mentioned, like, maybe we just run the lowest Python version and oldest… sorry, newest Python versions in PRs, and then when we submit to the merge queue, it checks everything. It's kind of an interesting idea.
But yeah, we're at time, so… I guess I'll take it to the other issue, maybe follow up with Trask.
Thanks, everyone.
Riccardo Magliocchetti 01:00:07 I guess, everyone.
