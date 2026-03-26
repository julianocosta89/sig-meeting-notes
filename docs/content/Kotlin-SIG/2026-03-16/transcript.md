SIG: Kotlin SIG
Date: 2026-03-16
Duration: 43 minutes
============================================================

## Zoom Recording Transcript

**Jamie Lynch** 00:57 Bye.
**Jason Plumb** 00:58 I joined this meeting an hour ago.
**Jamie Lynch** 01:02 Oh, sweet.
**Jason Plumb** 01:03 Very cool move, dude.
**Hanson** 01:09 Hello?
**Jason Plumb** 01:12 I…
**Hanson** 01:16 You weren't around this week, Jason.
**Jason Plumb** 01:18 I'm not. I'm not here at all.
**Hanson** 01:20 Okay.
**Jason Plumb** 01:20 I mean, I'm flying to the Netherlands in 3 hours.
**Hanson** 01:24 Oh, wow. Okay.
Shouldn't you be on your way to the airport, or… You're that confident that you don't, you don't do the, honey to eat.
**Jason Plumb** 01:34 Well, my flight is until 2. I'm on the way to the airport in 3 hours.
**Hanson** 01:38 Oh, I see, okay.
**Jason Plumb** 01:43 Mostly packed.
**Jamie Lynch** 01:50 That's for KubeCon, is it?
**Jason Plumb** 01:53 Yeah, but I'm extending it. KubeCon's not until next week, or technically it starts on Sunday, which is when the Maintainer Summit is.
Which makes for a long conference, like… Maintainer Summit, then Observability Day, and then KubeCon? So…
**Hanson** 02:10 Fantastic!
**Jason Plumb** 02:10 Yeah.
**Francisco Prieto** 02:13 Hey, everyone.
**Jason Plumb** 02:14 Ayy.
**Francisco Prieto** 02:18 How's it going?
**Hanson** 02:20 Good…
**Jason Plumb** 02:22 Good.
**Hanson** 02:31 I saw Independiente go 4-4 last week.
Was it last week, or was that the day before… week before?
What a score!
**Francisco Prieto** 02:41 idiot.
**Hanson** 02:43 Beautiful.
**Francisco Prieto** 02:45 like, at 23 of the first time, we were down by 3 goals. I never wanted to live so much in my life.
**Jamie Lynch** 03:01 I'll just give it a minute for folks to highlight some of the agenda, and then we can make it stop.
**Jason Plumb** 03:21 I've been pretty slow on approvals, and it will only be worse for the next 2 weeks, but hopefully after that, I'll turn back around.
**Francisco Prieto** 03:34 Me too.
I really need to find a balance, in this new company, so… Once I get a calendar pre… more established, I will be trying to help more sorry.
**Hanson** 03:48 Figure when you start a new thing, there's lots of stuff to catch up on or get up to speed on, so… understandable.
**Jamie Lynch** 03:59 Cool, let's start off with the first item. So, Hanson, you want to chat about issue templates.
**Hanson** 04:08 Yeah, we don't.
**Jamie Lynch** 04:08 We had been a lot less time.
**Hanson** 04:10 Yeah, we don't have any issue templates, I think when I go and create an issue, I think it's just the standard ones.
And then, since this is a new repo, I would expect people to have a lot of, requests for features, bugs, etc, etc. So I'm wondering if we should just come up with a handful of, of, of… Of templates, so that folks who are, creating new issues have, like, a guideline in terms of, like, what we want to put in there.
**Jason Plumb** 04:43 I don't think we have any in Android.
Just as a reference, do we? I don't think we don't.
**Hanson** 04:52 I mean, it's not standard, people just open issues, and we triage them.
**Jason Plumb** 04:56 It's up to us. No, it's completely up to us to decide, and if we find value in that, then yeah.
**Hanson** 05:07 Who do you folks think?
**Jamie Lynch** 05:08 I'm not opposed to doing it.
as long as it's not really, like, long-winded, I think that… puts me off from contributing if I see, like, a checklist, like.
**Jason Plumb** 05:24 Dozens of banks, same. Yeah.
And especially issues, because sometimes they're just really short, like, hey, I was trying it and I noticed this, you know, like… or sometimes it's just a question.
But have we had many external issues contributed yet?
Very few, right, if any.
**Jamie Lynch** 05:43 Perfect.
We've had a couple, but…
**Jason Plumb** 05:46 Yeah.
**Jamie Lynch** 05:47 Probably I can count them on two hands.
**Jason Plumb** 05:50 Yeah.
Yeah, I feel like it's more of a, I feel like there's two good reasons why repos do it, and the first one is just because… the volume. Like, if you're getting… if your project is successful, you get so many issues that just, like.
You want a little more structure there, and also you're putting a little, like, intentionally putting a bar in front of it being too easy sometimes.
**Hanson** 06:15 Hmm.
**Jason Plumb** 06:16 I don't know, I feel like… For this repo right now, I feel like it's premature, but also I'm not opposed to it. If you guys want to do the legwork, I think it's fine.
**Hanson** 06:28 No, if we don't all think there's, like… because, yeah, the issue… the issue… the, the thing I want to kind of head off is just, like, easier triaging. I didn't look at, like, the total number of issues and stuff that we have that are not created by us. I just saw, like, oh yeah, 44, okay.
But if it's, like, 43 are created by Jamie, then, you know, I don't think we need that. So… Can you just defer it?
I thought, I thought, in my head, it was just standard that they exist, but if it's not, then, you know, I wouldn't worry about it then.
**Jamie Lynch** 07:06 Yeah, I'd say just deferring until it starts causing pain feels like a good… approach.
**Jason Plumb** 07:13 I like it.
**Jamie Lynch** 07:14 Yeah.
Okay, following on from that, agent-aided PR documentation.
**Hanson** 07:24 So I feel like, A lot of people, myself included, have started experimenting with, you know, agents doing various things, even if it's, like, you know, restacking.
PRs and, and, you know, rebasing and stuff like that.
I know in the Android repo, we're looking to kind of add some… documentation about, hey, this is, you know, created by whatever, and largely that is mostly to head off, certain PRs that are a bit off the rails in terms of having a bunch of junk there that's not really, necessary, or even validated.
But, looking at it from a… I would say, the appropriate use of it. So, you know, you have a PR, and it looks like a regular PR, but it does have, like, elements that were, like, you know, hey, you know, Claude added some tests for me, or whatever.
how should we document it? Should we… or how… do we need to have this explicitly documented? And if so, you know, in what way?
**Jason Plumb** 08:30 Did you see the new one that's in Android that says they're added?
The agent's… yeah, we have an agent's MD now.
**Hanson** 08:37 Okay.
**Jason Plumb** 08:38 in… there… it's less… it's… I mean, I know you're asking about documentation here, and this is less for that, but it's… it's just, Helps to rough out some of the… Helps to smooth out some of the rough edges.
**Hanson** 08:52 Yeah, I think my personal kind of, like, view on this is, if you look at the PR and it looks kind of… ugh.
That you want someone to say, hey, you know, add some documentation to it, or say, hey, this was, you know, modified, because, you know, just from looking at it, it smells off. Versus if you do it, you know, in a thoughtful way, the fact that you used a tool, is almost incidental.
But at the same time, I'm like, well, is it incidental? Because things can creep in. So, you know, I… I'm kind of of two lines about this. I kind of want to hear what, like, you all are thinking, especially since, even what we thought 3 months ago isn't probably, what we might still think right now. So, at least for me, that's… that's… that's… that's true.
**Jamie Lynch** 09:42 So, I'm, little.
unclear on… Whoa.
this is discussing, is it talking about generating documentation for PRs, or, like, generating a PR description, or… Is it stating that a PR has used AI to some extent?
**Hanson** 10:04 It's that last one. Sorry, the word documentation's probably confusing. It's like, I have a whole new feature, and, and, you know, AI helped me with XYZ, whatever. Do we need to, do we need to, like… have that expressed in any way, because I could see 6 months down the line, or whatever.
most, you know, a lot of PRs will have been touched in some way, maybe even lightly. So if we start saying, hey, you have to add a checkbox, then the checkbox becomes irrelevant. If it's 95% has, you know, this checked.
But at the same time, do we want anything?
the default answer, again, is probably… could just be no, unless we get a lot of slop. And we, you know, we treat ourselves with, a bit of… a trust to say, hey, we're gonna, you know, do the right thing, but sometimes that… that… sometimes that doesn't offer enough protection, especially in a public forum, so…
**Jason Plumb** 11:11 Yeah, I mean, that was the entire bulk of the discussion on my spec PR around this topic, was like.
Really? You expect people to disclose this? And I'm like… Yes, I do.
And… I don't know, I think the checkbox is fine. I think we also agreed in Android that it's a good idea, because we've had a number of large PRs that were very much slop, and I think it's at least good for reviewers to know that ahead of time, and not think that they've got a really ambitious person who requires a lot of, you know, help and hand-holding, versus, you know, just… just, like, spearing stuff at repos, because a lot of that is happening now. I think it's good to at least have something like, you know, I think… Java has two things now. It's like, did you… did you use AI tools in making this? And then, did you thoroughly… like, review the output, are you comfortable, you know, claiming this work as your own? And then, almost a third one that's like, are you really sure of that? Or are you just saying that?
But, I think… I think the one in Java's pretty good.
See if I can find it. I'll look it up so we can link to it.
**Hanson** 12:23 Yeah, I don't mind doing this, or submitting a… if I have the, access to propose this in the settings or whatever. I don't mind taking this on.
**Jamie Lynch** 12:37 Yeah, I think it's just a case of adding the… Well, I guess in a normal… GitHub repo, you just added, like, a PR template on the GitHub folder. Is there… Jason, do you know if there's anything different? Because I know that some repo settings are managed by the admin repo.
**Jason Plumb** 12:57 No, I think in this case, it is just a matter of adding the right template in the GitHub folder.
**Jamie Lynch** 13:03 Okay.
**Jason Plumb** 13:03 I think so. I'd just have to find it.
**Jamie Lynch** 13:06 Cool.
**Hanson** 13:08 I can take, I can take a look at it if I don't have, permission, then, and I will, I will, Ask for help.
**Jamie Lynch** 13:17 Sounds good.
Okay…
**Francisco Prieto** 13:20 Feeling that this is going to become irrelevant in a few months.
Like, Not irrelevant, but a bit redundant, like… I expect a lot of people using AI, like, as the default, and I expect to see, like.
few PRs without that checkbox.
**Hanson** 13:39 Well, I mean, I expect that too, but I think the utility is… if you said you've reviewed this thoroughly, and we found that there are… that's evidence that it is not, or there are a lot of things about it, you know, that we can say, hey, why did you declare this? So it's almost like… it's almost like signing at the end of a thing. You kind of just do it anyway, because you just do it. But if you… if you are not confident in making those declarations, it gives people, hopefully, a bit of pause, and also gives us recourse to say, hey, you said you did… You vetted this, but you clearly didn't, kind of thing.
So, even if it's redundant, and maybe remove it in a year. But I still want people to say, hey, I sign up on this AI slop, because if you can't tell, you can't tell, but if you can tell, then you can point to it and say, hey, you said you didn't… you said this wasn't sloped, you said you reviewed this, how come you didn't?
**Francisco Prieto** 14:38 I would argue that using your GitHub account to post to a… to create a PR is pretty much a sign that you're actually vouching for that goal to be added, but… I do think that it's probably useful to… for someone to read that and say, oh, well, okay, I'm going to… Review that a bit more.
**Jason Plumb** 14:59 And me.
**Hanson** 14:59 There were some… go ahead.
**Jason Plumb** 15:01 These tools discourage thorough review, I'm sorry. It's just the way that it goes, and… It's accelerating.
**Hanson** 15:11 some of the PRs we've seen in the Android repo is so obviously, either unreviewed or under-reviewed that you want to say.
Are you sure? And this, this checkbox is almost like… Yes, I am… we're asking everybody this question, and I would have no problem, like, checking a box, because I would review all my stuff, but I think other people, you know, may not. And if you look at it, not super carefully, but carefully enough, and you say, hey, this is good enough, sure, sign it. But then there are people who completely, or, you know, at least, didn't even take that step, so…
**Jamie Lynch** 16:00 Boom.
Yeah, so, Hanson, if you're okay to propose something, and then… Folks can chime in on that.
**Hanson** 16:09 Sounds good?
**Jamie Lynch** 16:10 Boop.
Next topic, there are some getting started docs that are written for the website.
So it's basically just lifted some of the information that's already in the README, and put them on the Open Solomonetry website instead.
So… yeah, I think basically… We could use reviews on this from maintainers and approvers to progress it.
So if anyone has a chance, yeah, that would be much appreciated.
**Hanson** 16:47 I woke up that today.
**Jason Plumb** 16:52 Yeah, it's great to have that going so early, too. I think it's awesome.
**Jamie Lynch** 16:56 Yeah, and I think hopefully when that's in, I can… start doing a few others, I don't mind doing that sort of task.
**Jason Plumb** 17:05 Cool.
**Jamie Lynch** 17:11 So… Next topic… This VR is… Still kind of hanging around, so we don't have anything on the community calendar right now.
Which I guess isn't, like, a super big deal, but it'd be nice to… Kind of, like, clears the leaf on this.
**Carlos Alberto Cortez** 17:39 Yeah, for the record, I don't have permission to merge that. I confirmed sadly, so… Yeah.
Also, I think it… it was… the bill was failing, no? Oh yeah, it's failing, yeah.
**Jamie Lynch** 17:52 Yeah, I wonder if we can just check why it's failing.
**Jason Plumb** 17:57 links, like…
**Carlos Alberto Cortez** 17:59 laws.
**Jason Plumb** 17:59 Yeah, markdown link check, always, everywhere.
**Jamie Lynch** 18:02 Okay, that's flaky.
**Jason Plumb** 18:04 If you click that docs link, does it work?
**Jamie Lynch** 18:09 On the markdown link, sorry.
**Jason Plumb** 18:12 Sorry?
**Jamie Lynch** 18:13 I wish DocsLink.
**Jason Plumb** 18:15 Sorry, go to the, back to the link check failure.
I think I'm lagged, like, a second here. Down at the very bottom, I gave a 404. Can you click… yeah, that docs link. Is that working now? Oh…
**Hanson** 18:29 It doesn't exist?
**Jason Plumb** 18:31 So that's the wrong dock.
So, probably update the PR with the correct doc.
**Jamie Lynch** 18:37 Okay.
And then we've got another failure on this one, which seems to be… Something wrong with the YAML.
**Jason Plumb** 18:52 And this is Alolita's PR, right?
Yeah.
So I… I bugged her, like, a week or two ago, and she's like, I hope to be able to come back to it, and I think… She hasn't.
**Carlos Alberto Cortez** 19:07 Yeah, I think that… Going forward, what we should try to do is that we send some, suggestions to the PR.
Oh, at least… These two errors are fixed, so she can… she only has to press merge.
Otherwise, it may take longer, you know, because we need… we would need, her to find time to fix this stuff herself.
**Jason Plumb** 19:32 Yeah, that is very pragmatic.
I won't have time to do it in the next two weeks.
**Jamie Lynch** 19:40 So, what's the suggestion to… Basically, like, leave.
**Jason Plumb** 19:44 Recreate this PR. Yeah.
Just recreate it and fix those two build breakages, and be like, look, it's over here now, and it works!
All you have to do is push the button.
**Jamie Lynch** 19:54 Yes.
Cool. I'm happy to take that on unless anyone else wants to.
**Carlos Alberto Cortez** 20:10 By the way, just… it's not super important, but remember that this call is being recorded.
We had a similar, a moment of, in another cold, so… yeah.
**Jason Plumb** 20:23 What, was somebody being… somebody being a jerk?
**Carlos Alberto Cortez** 20:27 No, like… Or almost leaked some private information, probably.
Or I'm almost allowed to.
That person is called me, at least.
**Jason Plumb** 20:38 Yeah, okay.
**Hanson** 20:40 and pest… So, go ahead.
**Carlos Alberto Cortez** 20:43 Yeah, it's just, like, yeah, anyway, just for your information, yeah. Good reminder, just in case.
**Hanson** 20:50 No pasting in passwords in the chat.
**Jamie Lynch** 20:53 Yeah.
**Jason Plumb** 20:55 I think in my time in OpenTelemetry, I've definitely disclosed something on a call and had to go, like, rotate a token or expire something. I'm pretty sure that's happened at least once.
**Jamie Lynch** 21:07 Absolutely.
**Hanson** 21:08 A7E.
**Jamie Lynch** 21:13 Okay, cool. Next up, Hanson, you wanted to talk about the readable span interface.
**Hanson** 21:21 Yeah, so, we, I created the issue, we talked about a couple weeks ago about the, having a way of getting a readable span interface through the API, module, so not necessarily on the span. So my proposal was, was, like, you know, have method, like, you know, an extension method, working off a span in the API module that says, like, get, get… span, or get readable span, or get snapshot, or something like that, to support the use cases outlined in the issue. So, Jamie made a change to make it, create the exception function, but it's internal to the implementation, module, so it's, it's, it's a nice shim for us to be able to get it from, From there. But the issue is about the API module as well, and in the… in the comments, Jamie talked about, wanting to deal with this in the… at the spec level, but, I think in previous discussions, it… we didn't really say that it requires a spec change, for Kotlin to do this exposure, if… if we feel that there is a need. So I kind of want to figure out what the next steps are, if we want to have this, a readable, read-only interface, to be, gettable from the API, module.
but not necessarily part of the span interface. So, like, a… a sidestep, almost.
And then whether that's possible without, like, having, explicit permission at the spec level, which is gonna take a while.
**Carlos Alberto Cortez** 22:59 Yeah, I don't think it's possible, like… anything that is in the API, or even if it's, like, an API extension, shouldn't allow that. Like, the specification is making, like, super clear that you cannot do that.
Yeah.
**Hanson** 23:18 So I thought, like.
by writing this issue, there was, like, a recourse of introducing this, at least at the Kotlin level. So are we saying now that this first has to be, like, this is 100% forbidden that in the API module, for spans, thou shalt not be able to read data?
And that I need, I need that.
**Carlos Alberto Cortez** 23:44 Yeah, if you can enforce that, that is okay, I would say, mostly. So there is a related thing with Java. The Java, the SDK also is supposed to not You know, expose everything.
But… the Java SDK has some… Common artifact that has some package that exposes internal stuff.
And then it's just making it super clear, like, this may break any time, you know, and you shouldn't be using that, even if you are allowed to use the SDK because you are writing a stump processor. So something like that could work, if you are making very super clear that users shouldn't be using that. Users or instrumentation authors.
And, the second one is that you're making… you're… Like, basically, you are making it hard for people other than the coffee to use them.
**Jason Plumb** 24:39 We almost need, like, a non-spec annotation or something, like, like, like, not, not spec'd.
Or something, you know, is a stronger indication that it's not part of the spec.
**Hanson** 24:52 Like, which was… which was what I kind of want to do with, like, the extension function, that it's like, it's not on the SPAN interface, but it is effectively, you know, derivable. So I do understand, you know, the hesitation to do that. But, and if this is… if this is, like, you know, unless we get a spec change.
we can't do this, then we can close this issue, or I raise it at the spec level to see if there's something that can be carved out. Otherwise, people who require this will have to… and the use cases stated there, will have to do the workaround, which they can do right now, which is obtain a reference to the SDK.
Which… it's almost like… it's completely forbidden so people use, something that they… we don't recommend them doing. Is there something we could, like, a middle ground that we could do to say, okay, we don't recommend this, but if you do use it.
do it this way, so that it is more controllable.
it's… it's harm reduction in some way, but it also… it also opens up access a bit. And… I don't want the convention of… of just do this illegally as something that we carry forth as, like, the de facto, this is how you do it, which is… which is what it is right now.
**Jason Plumb** 26:16 As long as it's not packaged alongside, or like, there still needs to be an extra step to opt into getting this readability. I think having it side-by-side next to the span, the existing readable span API, is a problem.
But providing it, I think, is fine. As long as it's clearly, like, this is opt-in, this is experimental, or this is, like, internal, it's not part of the actual API, then I think it's fine.
**Hanson** 26:42 like, an API extension, inter… module. So, similar to in Java, we have the, we have, like, the experimental… or, what is it?
**Jason Plumb** 26:53 Incubating.
**Hanson** 26:54 Yeah, incubating?
**Jason Plumb** 26:56 Yeah.
But incubating has the intent of, like, maybe one day making it in, and I mean, I guess if you take that viewpoint that this, you know, we're gonna fight spec on this, then maybe it's incubating.
**Carlos Alberto Cortez** 27:11 Yeah, actually, that would be good, because in that case, you can at least exercise that, and feel the pros… the pros and the cons.
And if you ever want to show that respect group, you can show it, hey, we have this. It's incubating, we were testing that, etc.
**Hanson** 27:31 And also, if we… if it's literally outside the API module, then it becomes a… it is not part of the stable API. So, explicitly. So, if we choose to remove it, even in a minor version, you know.
you know, so sad. Just like you could do right now in the SDK repo for Java to prevent access to, you know, these things. It's, you know, users will have no complaints. So, yeah, this will create even further separation.
and… and, you know, so allow for this use case for those who want to opt in. And if… if it is kind of what I think it'll be, like, people will want to use this, then it just becomes one of those things that, hey, look, all these Kotlin users use it, and they use it for these specific use cases. Then I think there's a bigger, a more comprehensive case to take to the spec group to say.
We want a carve-out, or we want, like, you know, something.
So, I'm gonna alter my proposal to say, Let's make it… like the spec, and then move from that point to this kind of middle ground with the new module.
And then we could discuss the merits of that, if we want to do that.
Is that reasonable?
**Jamie Lynch** 29:01 Feels good, from my perspective.
**Carlos Alberto Cortez** 29:03 Yeah, sounds good to me. So we will have more, yeah, space to… Explore this, yeah.
**Hanson** 29:12 Cool. And I'll prove your, PR, Jamie, with a span of it.
**Jason Plumb** 29:17 Cool.
So we probably… if we're moving on, we probably shouldn't… to Carlos' point, we should not open… This list of security issues on this call.
Because it's not public, and not everyone can see it. I don't know, do approvers get to see it?
Anyway, there's a list of some security issues that we're getting raised on this repo, and, you know, our standards should be such that we don't allow these to linger. We do address them and get them resolved, and these have been out there for a couple of weeks, at least.
like, I'm just scanning through, it looks like 2 months, 2 months, 2 months, 3 weeks, 2 weeks, 2 weeks. Like, it's not, you know… You're able to see them, cool.
It would just be good to, you know, look at each of these and try and get it resolved. But in many cases, it's an upgrade.
It's a version upgrade that's probably already been fixed, but… We should look at them.
**Hanson** 30:17 Hmm.
**Jamie Lynch** 30:18 Yeah, I agree.
I think I can probably take that one on.
**Jason Plumb** 30:24 It's a lot of work.
I mean… I don't know, I could… I could see spending a few days, at least, probably just going through these and trying… because each one, like, you're like, what is this?
**Hanson** 30:35 A lot of JS stuff, yeah.
**Jason Plumb** 30:37 Shocking. I'm… I'm astonished.
**Hanson** 30:39 I was like, this is like college stuff, really? Oh, oh, right, JS.
**Jamie Lynch** 30:47 Yeah, I… Well, I can take the initial, like, kind of attempt at it. I'm hopeful it's just gonna be a case of, like, bumping the dependency and seeing if that works.
**Hanson** 30:57 There's sec…
**Jamie Lynch** 30:58 Yeah.
**Hanson** 30:59 there's 7 Dependabot ones, so I'm assuming we could just bump that.
**Jason Plumb** 31:05 Yeah.
Cool. Anyway, I just want to set that stage that, like, it's important for us to look at those when they show up, and… I'm also setting a bad example.
Of not having touched these.
I mean, literally, my thought process was, I see these and I'm like, oh shit, and then I look at it and I'm like, oh yeah, it's all JavaScript.
**Hanson** 31:32 Yeah…
**Jason Plumb** 31:33 But we… yeah, we should still… Get after it.
**Hanson** 31:38 Yep, either we don't support JavaScript target, or we don't have vulnerabilities. We can't have both.
**Jason Plumb** 31:44 Exactly, yeah.
**Hanson** 31:47 Let me know if you need any help on this, Jamie. Oh, actually, I can't… I can't approve any of this, or I can't merge any of these anyway, so… But yeah, let me know if I can help.
**Jamie Lynch** 31:57 Okay, thanks.
Cool. Anything else anyone wants to chat about?
**Francisco Prieto** 32:08 There was a PR on data instrumentation. I haven't reviewed it yet, but I think you… commented in the PR, Jamie, that we should discuss that on SIG.
**Jason Plumb** 32:22 Oh yeah, and that was huge, right? Wasn't it big?
**Hanson** 32:27 Scanned it, it doesn't… there's a lot of, like, test files and stuff. I think the code itself wasn't… but I don't know KTOR that well, so I… yeah.
**Jamie Lynch** 32:40 Yeah, I guess the question… I had in mind at the time I wrote my comment.
was… should instrumentation live in this repo, or should we be creating like, another repo, like, I know that Java has, like, Java contribs.
**Hanson** 33:01 I…
**Jason Plumb** 33:02 Copel.
Java also has Java instrumentation.
**Hanson** 33:09 I… I would… I would like it to be more, at least at this point, a Contribs model, because I think instrumentation is centrally maintained, right?
**Jason Plumb** 33:21 What do you mean?
**Hanson** 33:23 like, if there's a vulnerability found, or, like, a bug, it's up to the repo maintainers to fix it, versus, I think, contribs is up to the… I think each package has, like, an owner.
**Jason Plumb** 33:37 Yeah, in the contribib model for Java, each module has separate component owners.
Whereas, yeah, instrumentation is… is just… Maintained by the maintainers and community-driven.
**Hanson** 33:52 Yeah, I think at this point, I… I don't know if we want to take on instrumentation, essentially maintaining instrumentation that, you know, we didn't write. I would much rather have it as a buyer beware contribs model until we have the SDK and APIs all settled, and then we could basically expect… maybe we could think about expanding a scope. I mean, this would… this would… I would say this would… be something we want to probably eventually take on in the instrumentation repo, but I don't know if we want to do it now. If we do, then that's cool, but… I feel like there's a lot of work right now, just on the API and the SDK implementation, so…
**Jason Plumb** 34:41 Yeah, I… so I'm gonna make a proposal here. I think that, I think that we should be welcoming of new instrumentation like this. I wish this PR wasn't 1600 lines, but I like the idea that this instrumentation exists, and that someone who is… experimenting or trying out the Kotlin SDK for the first time.
could hook this up and actually use their HTTP client to get some tracing out, to get some data out, right? And… Right now, it's just one, and one can imagine that we get 2, 3, and 4. Like, someone's gonna do the same for OKHTTP.
And someone's gonna do the same thing for something else. And maybe when we hit, you know, 5 or 10, then we split it off. But my proposal is, why don't we make an instrumentation package and throw everything in there, make it a subdirectory, a module.
clearly marked experimental, or alpha, or something, like, and like a README that says, we're not giving this very much attention while we stabilize the SDK and API, and then, take those on, and if it starts ballooning, then we pull it out quicker.
But I think once we've got some critical mass, it would be the time to do it, and right now, it's just like… I want to accept it.
**Hanson** 36:01 I mean, the change really is one file. Most of the… the bulk of the change is in the JSON in, like, a test file.
**Jason Plumb** 36:10 Right.
**Hanson** 36:10 So, it's… I look at it, and it's like, it's using the semantic conventions, it looks correct, I just don't know… What other lifecycle things?
**Jason Plumb** 36:23 That's right, I forgot this code change was, like, very… it was pretty concise. Okay. Do you think that was all, like, generated test data?
**Hanson** 36:35 Yeah, I think this is, this is, you know, the… probably some sort of golden file diff about what the resource ought to look like, once exported.
**Jason Plumb** 36:47 where this came from, like, did they generate this?
**Jamie Lynch** 36:50 It's not too dissimilar to some of the test cases we already have.
**Jason Plumb** 36:54 Okay.
**Jamie Lynch** 36:56 to where there's basically a JSON file of expected output, and we're asserting that something hasn't changed.
**Jason Plumb** 37:03 That's cool. It would be great if and when we get other instrumentation that we could reuse these across them, right? Especially if it's, like, HTTP.
**Jamie Lynch** 37:11 Hmm.
**Jason Plumb** 37:11 Where it's like, you should pretty much look the same if you're doing this stuff.
And you're also an HTTP client.
**Hanson** 37:20 Yeah, there's, I mean, there's two ways of doing this, right? You look at the JSON serialization, or you kind of have, like, a test that asserts things that are the same. I think a lot of this is probably not necessary, like, things like, you know, resource instrumentation scope, so things that the instrumentation really isn't responsible for. Like, I feel that's redundant, especially if all it's doing is creating spans when it goes through the lifecycle.
what's setting with the resource and the instrumentation scope, you know, would be something higher level. Instrumentation scope, maybe. Maybe it makes sense to have this. But, like, Some of the…
**Jason Plumb** 38:01 It's like Golden, so it's still pretty good.
**Hanson** 38:04 Nope.
**Jason Plumb** 38:05 Yeah.
Yeah, I think the root of the repo is pretty crowded already. It would be cool to have this in a sub… subdirectory called instrumentation.
**Jamie Lynch** 38:18 Yep.
**Hanson** 38:19 Oh, good.
**Jason Plumb** 38:23 I can leave that comment.
Asking them to do that.
At least to show… and assuming they do that, it means they actually care, and they didn't just… Dump this.
**Jamie Lynch** 38:38 Okay.
**Jason Plumb** 38:41 Do we know why the workflows didn't run on that PR?
**Jamie Lynch** 38:45 They need manual approval.
**Jason Plumb** 38:47 Do we know why?
**Jamie Lynch** 38:49 No, I'd assume that's just a… Default or external contributors.
**Jason Plumb** 38:56 I don't think it is across the board.
**Hanson** 39:01 Maybe they didn't sign the SLA, or the.
**Jason Plumb** 39:03 They have. They definitely did sign the CL.
**Hanson** 39:06 Bye.
**Jamie Lynch** 39:08 But I don't think they signed it when the PR was initially opened.
**Jason Plumb** 39:12 And so maybe it's just been in that state the whole time.
Yeah, okay. I'll leave a comment that we're asking them to… to re… repackage it.
**Hanson** 39:23 We should also think about, like, when we need thorough golden files, and when we don't, because I'm just looking at… I'm just looking at the tests that they have, and the instrumentation quickly, and I don't know how much utility the golden files are adding.
I think for the SDK, we should have that, but instrumentation, that feels really heavy.
But I'll make a comment in the, in the, in the PR. We can discuss that.
**Jamie Lynch** 40:02 Sounds good.
Cool. Was there anything else to discuss around that PR?
**Carlos Alberto Cortez** 40:12 Oh, by the way, probably, I will, I couldn't find that now, but I saw that you, move around this set reception, or report reception for spam interface.
Since that's deprecated, probably, just the level, I mean, probably we don't have to add that.
ourselves, because we're a new SIG. So it sits in SIGs should add that, should keep that because users were using that. In our case, that doesn't make sense.
So we'll bring that with spec tomorrow and discuss that.
Just green.
**Jason Plumb** 40:47 I missed what the… sorry, Carlos, I missed what the subject was.
It was about the Spanish…
**Carlos Alberto Cortez** 40:52 world.
Yeah, it's about the… so, the span has this operation called, report deception, or cell reception.
Which, basically, you take an exception and create an event. Once these events are deprecated.
This method is itself a deprecated.
So existing sticks have this, operation, and they cannot move it. They cannot delete it.
**Jamie Lynch** 41:17 Okay.
**Carlos Alberto Cortez** 41:17 Because users are already relying on that. Since this is not our case, probably we can… Just get a wave.
**Jason Plumb** 41:24 you're moving.
**Carlos Alberto Cortez** 41:24 North Korea.
**Jamie Lynch** 41:25 Fair enough.
**Jason Plumb** 41:26 Yeah, okay.
**Carlos Alberto Cortez** 41:27 But I will do last, because, yeah, I think that… so, new features I have seen, they have this disclaimer, whether you have or don't have to implement something that is deprecated, like, for example, SIPKIN or Open Tracing, the, the compatibility packages is like, hey, you are using it, don't implement this, it's a percator.
So, but this operation, it doesn't have this clarification, so I will ask tomorrow.
**Jason Plumb** 41:56 And do we have an issue to track this yet?
**Carlos Alberto Cortez** 41:59 No, I just realized that when I was checking the, merge PRs in this repo.
**Jason Plumb** 42:04 Okay.
So, yeah, so creating an issue to remove it would be good, right?
**Carlos Alberto Cortez** 42:11 Yeah.
Yeah, yeah. I mean, yeah.
Yeah, I would like to disclose our inspect first.
I mean, yeah.
**Jason Plumb** 42:19 Okay.
**Carlos Alberto Cortez** 42:19 If people didn't agree on that point, I will update the spec, and then we can do that ourselves.
**Jason Plumb** 42:25 Okay.
**Carlos Alberto Cortez** 42:26 So, that's… that's unique, yeah.
**Jason Plumb** 42:28 Sounds good to me.
**Hanson** 42:29 I mean, the new workflow is just to use the events API and then associate the event exception event with the span, right? So.
**Carlos Alberto Cortez** 42:44 Yep.
**Jamie Lynch** 42:49 Cool.
Anything else?
Cool. We can leave it there, Evan, with 2 minutes to swap.
**Jason Plumb** 43:04 Sounds good. Carlos, Carlos, will I see you next week?
**Carlos Alberto Cortez** 43:09 No, I'm not coming to Cubicle in the end, sorry for that.
**Jason Plumb** 43:11 Alright.
**Carlos Alberto Cortez** 43:12 enjoy, feeling, you know? It was having nice to see you after… I think we saw each other, like, 3 years ago?
**Jason Plumb** 43:19 Yeah, it's been a while.
**Hanson** 43:21 Wow.
**Carlos Alberto Cortez** 43:23 We'll take photos.
**Jason Plumb** 43:26 Alright, thanks everyone.
**Jamie Lynch** 43:28 Beautiful.
**Hanson** 43:29 Yep. Bye.
**Francisco Prieto** 43:30 Yep.
