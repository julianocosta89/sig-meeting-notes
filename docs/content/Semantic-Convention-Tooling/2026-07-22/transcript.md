SIG: Semantic Convention Tooling
Date: 2026-07-22
Duration: 52 minutes
============================================================

## Zoom Recording Transcript

**ariannavespri** 00:10 Hello!
**Jeremy Blythe** 00:16 Hello.
Just have to rejoin.
**Jeremy Blythe** 01:43 Let's see if,
**ariannavespri** 01:46 Anybody else is joining?
**Jeremy Blythe** 01:48 I just want to see if Labrina can join, because I know, Josh and LaRon both said that they couldn't today.
So If Li joins, I was going to suggest we look at what we need to get done for the release. So let's just give it… she hasn't said… hasn't said no.
But then she hasn't said anything yet.
So… Just hang on for a minute, I guess.
**ariannavespri** 02:19 Yeah, I guess we can wait.
**Jeremy Blythe** 03:49 I guess, did you… Have anything… seems to…
**ariannavespri** 03:53 No, no, I mean, like, I'm just, like, continuing to work on the SimConva test package, you know? But, yeah, I'm sorry I missed, last week, last week meeting, because then I realized, in retrospect, I mean, I really couldn't, that you were talking about rappers and everything, so I don't really have, much updates to… to give. I… I have… I got, like, what I think is going to be the last round of comments to change some small things, but the PR is in a very good shape right now.
And so, I'm hoping to be able to merge it as soon as I address this, these last, comments by Braden, and after that, we already have, like, a candidate component to actually test this, package.
On, so… so today I was mostly… I mostly come just to… to listen to you guys, to… to new updates and everything.
**Jeremy Blythe** 04:57 I'm kidding.
**ariannavespri** 04:57 And that's all.
**Jeremy Blythe** 04:59 Yeah, I haven't heard from Libamila.
**ariannavespri** 05:04 then I saw, I saw the changes on the… on the Weaver packages, repo, I mean.
fine by me, to… to… to delete the… the Markdown templates and have this, new, kind of, more general framework approach that Liudmila is, is putting into practice is with, with this PR that, she opened.
And, so, as I said, was mostly… Motley drop by as a listener today.
**Jeremy Blythe** 05:39 Okay.
I'm not sure there's gonna be much to listen to.
It's just me. Sorry.
**ariannavespri** 05:46 Okay.
**Jeremy Blythe** 05:46 It's okay.
**ariannavespri** 05:47 Okay?
**Jeremy Blythe** 05:48 I guess I can tell you what stuff I've been working… I've been doing, more live check stuff. There was a good thing that came up, so… we had, Nimrod join, last week with some interesting things in live check.
and other stuff, but for me, some interesting things in LiveCheck that I've now been working to, To update, so it seems like… We'll see if.
**ariannavespri** 06:18 Alphabetical order thing? It was the alphabetical order thing?
**Jeremy Blythe** 06:22 no, this is, So there's a thing in LiveCheck where you can, in the TOML file, you can put in, filters for the findings that come up. So you can say… I want to exclude all findings of, like, a particular type. Say you're not interested in… Oh, I don't know, like a namespace clash.
Finding, or, I don't know. What's the one, Like, when you send in something and, It's an extension of the enum, for example.
Often people are, like.
they want to remove that noise from live check, so that there's some changes going in for, those, modifiers that you can make in the TOML file.
And what… this is for the Obi project. I don't really know… I don't really know what it is, but anyway, there's a few things going in there that are going to allow you to, make the filtering even more specific, so you can say, well, I don't want… I don't want the finding about… you know, problems with the namespace.
When it's these particular sample names, for example. So you can, You can be more, sort of, specific about what you want to exclude.
But there's a… there are, like… I think there were at least 3 issues that are… that are all in this area, so I wanted to get those done before we do the release, because then it will cover off everything, I think, to do with the… those finding modifiers.
**ariannavespri** 08:11 I see, interesting, thank you.
**Liudmila Molkova** 08:15 I don't know.
**Jeremy Blythe** 08:16 Heather.
**ariannavespri** 08:18 Oh, there you are, hello.
**Liudmila Molkova** 08:21 Yeah, sorry, I… I got stuck preparing my coffee.
**ariannavespri** 08:28 Sounds like a very good reason.
**Liudmila Molkova** 08:31 Okay, thank you, appreciate your understanding.
**Jeremy Blythe** 08:41 Yeah, we were just talking about the… I was wondering if you wanted to go through what we might… Doing a release signal?
**Liudmila Molkova** 08:53 Yeah… Let me see, I have a bunch of… fixes… Give me a sec.
**Jeremy Blythe** 09:04 I started putting them in the next release.
Column in the… in the board.
That's what I was trying to do.
**Liudmila Molkova** 09:14 Yeah.
I'll share in a sec, I just… I'm just preparing.
Oh, great.
So… This front.
Oh, nice, this is something new, right? I haven't seen it.
the namespace… Nice.
**Jeremy Blythe** 10:01 It's all…
**Liudmila Molkova** 10:02 Next.
**Jeremy Blythe** 10:03 Those first two.
And the one I've just got merged.
Are all to do with this finding modifier stuff, and where you can say what you, You can, change the filtering, like, very specifically. So… This was to do with, you could almost do this now with the change I just made, but it's a subtle… if you scroll down a bit, there's my comment, where at the moment, we can exclude.
But if you've got a lot of things, you kind of want the inverse, you want to be able to include.
So I think… I'm not sure I'll cover everything that's in this issue, but I could include the bit to do with… the include.
It's one of those include-exclude things, where sometimes it's… you want to specify one way or the other.
**Liudmila Molkova** 10:59 Oh, okay.
Oh, for this one, I thought, like, It's… You just declare a new registry?
And you just declare dependency on the 4, and you just temper it to what you want to cover. And that's, like, the ultimate fix. I kind of… I, I like this.
But I don't like this.
**Jeremy Blythe** 11:27 Yeah, I wasn't…
**Liudmila Molkova** 11:28 I'm…
**Jeremy Blythe** 11:28 I wasn't gonna do that, I was just gonna do the… the, scoop.
So the scope for your filter is based on… Exclusion, but it could also be based on inclusion.
**Liudmila Molkova** 11:48 So you're… like, you're doing this part.
And… It's… It's different from… Or… I had another mechanism for this, right? The one you improved yesterday.
**Jeremy Blythe** 12:10 Yeah.
**Liudmila Molkova** 12:14 But it's just the wild card.
**Jeremy Blythe** 12:17 I've done the wildcard, I did that.
**Liudmila Molkova** 12:20 Oh, okay.
**Jeremy Blythe** 12:21 So there's a thing at the moment called exclude samples. It's not keys, it's exclude samples.
And then you could do that line that you've got higher up.
But maybe it's not needed, actually, now that… now I'm thinking about it.
I need to look at it some more. We may be able to do what Cleo's trying to do here.
with what I did yesterday, right? Maybe I… maybe we can.
I need to look at it. I might… I might be able to just take this one out of… Not being needed.
**Liudmila Molkova** 13:00 And… But it was this year, saying I'd only pay attention to this.
So, like, it also can be done with The existing mechanism, but it doesn't support it for now.
**Jeremy Blythe** 13:19 Yeah, I think so. It's, like.
I'll have a look at it. My brain's not working, but I think… I think we may need the… we may need the opposite.
if you've got a… if you've got, like, a giant library, and you're… and you… I think in their case, they've got, like, a giant model.
And they don't want to make a small model, but they want to have targeted tests at portions of that model.
So they sort of want to go… this test is across the whole model, but I'm only interested in this subsection of it in this namespace.
And so, rather than saying exclude a big list, you sort of want to go include just a small list.
**Liudmila Molkova** 14:11 Yeah, it's also easy to do a sub-registry, and just say.
**Jeremy Blythe** 14:15 That was my first suggestion in this, in my comment.
**Liudmila Molkova** 14:19 Jed doesn't like it, or… oh, right, yes.
Gosh, we cannot sell out to an inline registry.
Because it's so small.
**Jeremy Blythe** 14:43 Yeah, so does that.
And then the other one I added… Is in a similar… Dang, it's the other… it's the second half of what… Came up in the last meeting.
So in that way, in this one, though, the request is to… Be able to change the… Level.
So, they want to… Like, make things that are normally we emit as, like, information level and actual violations, so this is a… It's like… They want to raise the… raise the level. But I think that's useful.
I actually had it in there at one point.
in a PR, and then we took it out for some reason.
**Liudmila Molkova** 15:31 It reminds me of fluvels.
So, this one suggests to change the level of Violation itself.
But… Similar, like, in log levels, Would rather say.
Only show levels for this category above this value.
I'll find an example.
Right, so, for example, like, for this category, the level is warning. For that category, it's warning. For the, like, by default.
Only show errors.
And this way, we don't change the… Level of… of the advice.
But we change what we fail on.
**Jeremy Blythe** 16:52 Oh, I see. So, it's… it's still reported as… It's still reported as information.
information level.
**Liudmila Molkova** 17:04 Huh.
**Jeremy Blythe** 17:06 But we're saying specifically for that match.
We want to fail.
**Liudmila Molkova** 17:19 It just… yeah, there is a similar, I think, issue from C. Joe, or maybe somebody else, that… the fail on threshold, or maybe it's even merged.
**Jeremy Blythe** 17:31 That was failed… that's across the whole… It gets complicated, because it's actually more like your example, because… What they want to do here is… Not fail across the hall.
all of the findings. It's only specific findings that are scoped to specific samples.
that they then want to treat them like a violation. So, look, in this example.
If they get an extends namespace for messaging.system, they want that to be a failure case.
**Liudmila Molkova** 18:09 Yeah.
It's just the granular way of the same thing, so I'm saying they kind of work complement each other, right? So there is a global level, You'll fail on this.
And there is a more local level. So, for this match… Eww.
Oh, sweet.
It's just Feilon.
You don't change the level, you don't set the threshold, you just say, fail on this match.
**Jeremy Blythe** 18:48 Yeah, we'd have to… Doesn't it amount to the same thing, though?
**Liudmila Molkova** 18:55 Yeah, maybe.
Maybe.
**Jeremy Blythe** 18:58 If you've said that you want to fail on a violation, then doing it this way, you're just… You're saying what you consider to be a violation.
**Liudmila Molkova** 19:07 Yeah, maybe my log-level analogy doesn't work hard, yeah.
Yeah.
I think it's good.
**Jeremy Blythe** 19:22 I was gonna do that.
And the other one… We need to get in is this HTTP fix.
There were a couple of… nitpicks that… Incredible.
We need…
**Liudmila Molkova** 19:43 Oh, we want Trusk, too.
**Jeremy Blythe** 19:46 At the very least, the interchange log.
But… Also, we're introducing this COMD, this conditional variable thing, convol.
Which works, and it's fine, and it works, it's just, it's more code than you really need. You can just use a… You can just use a channel.
So it's okay, that's why I made it a nitpick, because that actually works, that's fine. It's just, you can do it Maybe a little more simply.
**Liudmila Molkova** 20:13 That… that's totally fine, I… I… I don't think Trask is a Rust expert, so… If you feel it should be approved, I think it… like, we just might need to ping them, him to address it.
I was worried about this one.
But… Maybe you can think of something that would allow not to do this?
**Jeremy Blythe** 20:38 I had a… I had a look at that, I couldn't find it.
Didn't find it nice.
I couldn't find a nice way of doing that.
**Liudmila Molkova** 20:49 Okay, so if you couldn't, then… I'll just have to live.
**Jeremy Blythe** 20:53 I didn't… I mean, I didn't spend forever on it, but I… It's, Yeah. I know it could be flaky, right?
**Liudmila Molkova** 21:04 Yeah.
Huh?
**Jeremy Blythe** 21:07 Keep an eye on it, I guess.
**Liudmila Molkova** 21:09 Yeah.
Okay, so then we'll wait for Trucks to come back and, we can ping him.
I have a bunch of… PRs, I don't need all of them.
To be in the release.
But I want some of them.
Okay, so Josh approved this one.
It's good… And… I'll work on merging it… oh, no comments.
Cool.
And… This is another small fix.
I think there is… there are some comments.
And… I'll work on this.
Oh, we need… we need to get this in.
And Josh approved, and… Awesome.
This… the friends can wait.
So, I'll work on merging this.
it seems it's just conflict resolution and a lot of CI, but… And then we should be ready for… Oh, you're… you will be working on those changes, right?
**Jeremy Blythe** 23:06 Yeah, I'll probably do them tonight.
**Liudmila Molkova** 23:11 Okay.
**Jeremy Blythe** 23:13 Okay, everyone.
**Liudmila Molkova** 23:17 Then we should be ready to release. I would… I would really love to cut the release this week, because we are… There are a bunch of fixes that are already in.
And we depend on them.
In many places.
**Jeremy Blythe** 23:32 Yeah.
The releasing one… Apart from problems that we found, the actual mechanism of doing the release was really… was really smooth. Like, I had to do it 3 times.
So… It has been… it has been a bit of a problem in the past.
With, like, cargo dist.
Giving us issues.
There are things… sometimes there are things you don't discover until you've gone through the release process, like with the Docker images, which is kind of annoying.
But it's been really smooth, so we shouldn't be held up, I don't think.
**Liudmila Molkova** 24:12 Awesome. Then, once I get through this list.
I'll try to cut the release, hopefully. It seems like you will have some changes today… you mentioned today, right?
**Jeremy Blythe** 24:24 I'd like to get this… my… yeah, I'd like to get my stuff done probably this evening.
**Liudmila Molkova** 24:30 Yeah.
And I'll try my best to do it throughout the day. I can't bank Trask about the fix.
And… sounds like, optimistically, I can start earliest tomorrow, and it will be done tomorrow. But we have Friday as a buffer if we need to.
**Jeremy Blythe** 24:52 Sounds good.
**Liudmila Molkova** 24:54 Awesome.
Yeah.
**Jeremy Blythe** 25:05 So… The only other thing I was going to bring up today… is, whether it's time to add, like, AI coding guidelines stuff to, to the Weaver project. I know, like, it's in a few places now, I think Did you pioneer this for the GenAI SEMCOM? Was that you?
Anyway… what I've noticed is we've been getting some luck.
lazy PRs coming in where… there's one that's in there right now, where… The code that's been written is a test.
And they haven't even run their own test, because the test fails.
Like… It's… it's… There's an assertion looking for a line of text.
And that line of text is always… and it's asserting that that text should not be there, and that text is always there, because it's a constant. It's just, like, it's always in effect, so…
**Liudmila Molkova** 26:18 Yeah, I mean, absolutely, let's… yeah, AgentsMD has been very helpful, and yesterday, I was writing something.
And, well, obviously, I do AI.
Especially the right rust, sorry. And it left a bunch of namespaces, and I remember you saying, too, use, use.
And I was like, what? It would be nice If we had Agent SMD to… Say what our preferences are.
**Jeremy Blythe** 26:50 Yeah, so I have all of that in… I've got a… well, it's… it's a ClaudeMD, but I can… I can call it AgentsMD, and I could put that in as a PR.
And it… it contains things like… a sort of Rust styling that we've got.
it also… Actually, I was doing something last night, and then I… and then I I asked Claude, hey, how much did the Claude MD help you to do this session? And then it tells you, oh, with that, this saved me time because I read this guideline, this guideline, this guideline, and that meant I wasn't putting, I was like, or is returning errors properly and not putting in accept or unwrap? I was like.
I made sure I ran the format and clippy and the full test suite before I, like, said that I was finished, and, like, a bunch of things, so… I think it'd be useful to have that, but it's also the other guidelines.
That you've got.
about… like, in the PR, I think in… yeah, this project you're showing. Like, in the PR, you have to declare that you've… you've used AI in some way.
**Liudmila Molkova** 28:08 I found it helpful because… Not because I care about assisted by.
I think it came from some other project, but because it… sometimes, Like, if you don't tell it, It would use its own… Like, altered by.
And ordered by doesn't pass silly, because, yeah, it's a silly.
So this is sometimes helpful.
what we do, I think, here, and maybe in other places, we do this, and then we have the Simulink for… for CloudMD.
It doesn't work on Windows, but nobody complained yet.
And worst case, we can duplicate, and maybe eventually Claude will support Agent ZoomD2.
**Jeremy Blythe** 29:03 Oh, I think you just… in the cloud, you just do… at.
Agent SMD.
**Liudmila Molkova** 29:09 You can do… it's actually a Simulink, but… You can also do… Just link, regular link.
**Jeremy Blythe** 29:21 Okay.
**Liudmila Molkova** 29:27 Yeah, so this file just points to this file.
And we can also have, like, if we had… skills, we could do a simulink for skills.
Okay. We also have this, like, you know, I personally, I use Copilot Review a lot.
And you can tell Copilot to… Do specific… To review it in a specific way.
And I know if this one… It's good. So, the thing that works… being the best, at least for me, maybe because I did it, and I did it for myself.
S… Here… So it's, like, very… actionable things. The moment I put anything back in there, it starts going… misinterpreting it.
And in some other project, I tell it, okay, don't, like, this is what is CI validating, don't ever… Validate… But… yeah, this is just a register, like, the best practices on how to run stuff.
And there is the other part with instructions. This is, like, the mirror of… AgentsMD, Oh, and it has some samples. It actually told me that it likes samples the most.
Out of this, because, yeah.
There is the opposite part of what to check for. It's much more… Much more concise, and it's, like.
It's out of date. Anyway, so whatever we add is awesome, I will probably evolve it.
**Jeremy Blythe** 31:45 Shall I just, because I don't have all of this detail, I just have a list of, like.
15, 16, like… things that are… you know, for writing Rust and… I just, like, do a PR and put that in there to begin with, and then… Maybe we can collaborate on adding other bits or something?
I know, just so I can get some stuff in.
**Liudmila Molkova** 32:11 Yeah, absolutely.
**Jeremy Blythe** 32:12 Okay.
There's also… on that project, there's also the, you have a, like, a… Template for the pull requests as well.
on your Gen AI.
Project.
**Liudmila Molkova** 32:30 Yes, I think we do, but it… yeah, Do you want to have a template for pull request?
**Jeremy Blythe** 32:39 I don't know, it's like… Isn't there a checkbox that you have to check to say, I've used AI a little bit, a lot, or completely, or something?
**Liudmila Molkova** 32:55 Yeah, we have it in semantic conventions.
**Jeremy Blythe** 33:02 Do you find that useful?
**Liudmila Molkova** 33:04 I don't know, not… not… not really. I think I added it out of spite.
Like this.
**Jeremy Blythe** 33:13 Yeah, don't.
**Liudmila Molkova** 33:14 I said, This is Coffee at Fermap and Telemetry.io.
And… There is this checkbox, I know my stuff.
That you can actually understand.
You should understand what you wrote and should review it.
I feel like we are surveying people who contribute about their AI usage more than we are… there is anything actionable in it.
**Jeremy Blythe** 33:45 Okay, so we think.
**Liudmila Molkova** 33:46 But I don't… Joao, what do you think? Do you find it useful?
**Joao G. (Dynatrace)** 33:51 well, not… I guess, similar to you, but I guess what this achieves is a little bit, Makes people a little bit, accountable, or… or, you know, like, guilty if they… if they… if you want to think like that, that they are, you know, like, just… but if you get such low-quality things, I… I doubt that this will make any… Like, if the person is daring enough to obt such a low quality, this won't prevent them from doing so, let's say like that, but… So, yeah, Take it with a grain of salt, a grain of salt.
**Liudmila Molkova** 34:31 I've tried the trick.
We hated it, that we had a hidden item, an edge in some days saying people to, Saiyan bots to add, I am an AI bot, somewhere, random place.
Like, a comment with it.
And I hated it myself, I added it, I hated it, because it added the thing everywhere all the time, and it was very hard to get rid of.
**Joao G. (Dynatrace)** 34:58 An actual cold changing, that's it.
**Liudmila Molkova** 35:01 Right.
**Joao G. (Dynatrace)** 35:01 So you're forced to…
**Liudmila Molkova** 35:02 And I had a check that, like, flagged it in a very vague manner, so you still have to.
**Joao G. (Dynatrace)** 35:07 Look for… Okay. They will just build a skill to remove it then, afterwards.
**Jeremy Blythe** 35:14 I guess the complaint isn't… there's not… there's a… like, AI is just a thing, that… it's just another tool, and everyone's using it, and of course they are, and it's great, it's amazing, but it's not… the complaint isn't about, are you or are you not using AI? It's like, use AI, but don't be lazy.
**Joao G. (Dynatrace)** 35:32 Yeah, exactly.
**Jeremy Blythe** 35:33 They hadn't use AI, like, but, you know, run the.
**ariannavespri** 35:35 this.
It's not that slow PPRs are a thing of the AI age. I mean, people could do that before, it's just that now it's like, you could do that in series, basically.
But, I mean… It's like.
**Jeremy Blythe** 35:52 It, you know.
**ariannavespri** 35:53 Accountability is something that It was a requirement before, too, it's just that now it's like… Can happen, like.
more, like, you can do things more frequently, more often, like, and but… but I agree, I agree with you, it's not really about… it is a tool, it is a tool, it's the person behind it taking responsibility, understanding what they are producing with that.
How they're using it.
**Joao G. (Dynatrace)** 36:23 I guess what this little tech also allows us to do is that if you see such thing.
Like, slips.
you know, lower for PR, I'd say this is the freedom to just… Like, yeah.
Because, like, if somebody opens the PR and they see this question and say, I have the experience, I don't know.
I would hope that the person feels, like, a little bit of, you know, like, yeah, I actually don't… don't feel experienced, I don't have the experience, I don't feel knowledge about this, so maybe I'll… I don't know, either close it or have discussions before I… You know, like… like, I personally wouldn't open a PR or something like that. I have zero experience, and I just completely vibe-coded something, so… I don't know if everybody thinks like that, but the check, to me, has this weight on it, so maybe it makes people consider before they do stuff.
**ariannavespri** 37:25 Yeah, sure, it's like a prompt for yourself to ask yourself some questions, for sure, yes.
Uniform. Yeah, yeah.
**Joao G. (Dynatrace)** 37:31 Yeah, I guess that's the minimum we can do.
**Liudmila Molkova** 37:36 And I find… it… the… I probably gave up.
because we… in Gen AI repos, we have so many AI-driven contributions, like, 90% of them are… Fully vibecoated.
And I find AgentsMD and Copilot instructions as the way to protect my sanity, that I have some way to not talk to people behind agents, but talk to agents themselves, and also the auto-review the stuff.
And, like, if we… like… Especially if we publish Copilot instructions, like, okay, you get the Wipe-coded thing, but Copilot is the first line of defense, and it leaves comments, and we don't even look at this PR until Copilot Review is clean.
And most of the time, this, contributors, I don't know if they're people, or they're just rock bots, they don't come back.
Or they cannot figure out the really, like, I don't know, revasing and merging conflicts for some reason. Maybe they don't use a good AI or something, I don't know.
**Joao G. (Dynatrace)** 38:53 That's in the same company AI people.
Yeah, I guess to attract the most source of it, yeah.
**Liudmila Molkova** 39:03 there are the whole issues, and now even Slack threads, where I feel like it's AI talking to AI, and AI replying back, and they start with the specific phrases, and… Joao G. (Dynatrace) 39:16 Oh, yeah, that's true.
**Liudmila Molkova** 39:17 AI language, yeah.
**Joao G. (Dynatrace)** 39:19 You can really clearly spot it very, very, yeah.
Early on.
**Liudmila Molkova** 39:31 Cool, but it sounds like we are all in support of AgentsMD, whatever we put there first, we will evolve it, and yeah.
**Jeremy Blythe** 39:38 Yeah, okay.
**Liudmila Molkova** 39:39 Can add the template, but… If… if people feel it's important.
**Jeremy Blythe** 39:47 I… dunno.
It's interesting is your use of Copilot.
to… at work, What I… what we've recently done, is we switched off Copilot.
Yeah, because… I got annoyed that people would put in a PR, and then they'd go and say, here's my PR, like, they're done.
And then the very next thing they do is they go, okay, Copilot, review it. And then they've still got a bunch of work to do. Whereas I'm saying, you don't need Copilot to review it inside of GitHub.
Just ask your AI to review it before you put it in GitHub, right?
You just go, like.
**Liudmila Molkova** 40:26 Ew!
**Jeremy Blythe** 40:27 Slash review.
**Liudmila Molkova** 40:27 But then Copilot still finds something.
**Jeremy Blythe** 40:31 So…
**Liudmila Molkova** 40:35 We did because it's on GitHub, right?
It's just because we have free credits for Copilot. Anyone can request copilot review.
Here, it's not your account.
**Jeremy Blythe** 40:49 Yeah.
No, we were like, we're paying for Claude and we're paying for Copilot, and I was like, guys, we don't need both of these.
Just review it before you put it in, and then… So I was thinking, in the Agent's MD, you could say, Run a review process.
thorough review process before you do your first commit, like, a full code review or something. I wonder if that would trigger something to happen if that was in AgentMD.
**Liudmila Molkova** 41:18 I… you probably should?
maybe… I did something yesterday, I just wrote it in the prompt, I didn't check the outcome, it's on a different machine, so I'll check later today. It should review with the fresh context. I don't know if you can instruct it to, like, review with the fresh context, but we can try, we can see.
**Jeremy Blythe** 41:43 Anyway, this is, it's funny.
**Liudmila Molkova** 41:47 Yeah. Do we have… Yeah, we have pull request dashboard.
So, like, this intends to solve the problem that Okay, where is my PR?
And do I… what do I need to look at? So if somebody is, like, if we had a pilot review, or whatever, AI-driven review.
It would show up here as waiting on authors.
**Jeremy Blythe** 42:14 Yeah.
**Liudmila Molkova** 42:14 And… Ideally, you don't even look there as a reviewer.
**Jeremy Blythe** 42:23 That reminds me, just looking at this, there's another thing we need to get done.
We've got PRs in here that are, like, 350 days old? That's crazy.
We need to time out some of these things.
**Liudmila Molkova** 42:39 Okay.
So… let's just go and do… Couple.
So there are… it can close a couple now. What we can do is distal your workflow.
It'll just run, mark them as stale. If there is no activity after X days, it will be closed.
This is a common practice in our towel.
**ariannavespri** 43:07 Yeah, in a collector country, it's after 2 weeks that it becomes stale unless there is, like, you know, then you can unstale it, of course.
Bum.
**Jeremy Blythe** 43:19 Two weeks might be a little… Fast for us, man.
**ariannavespri** 43:22 Yeah, it is, it, it is actually, yeah, yeah, yeah, even for… even for contributors, I would say… I mean, in Collect2Contrib… for myself, like, two weeks is… I'm always, like, there unstailing things, because… Yeah, of course, then you… you have to… it's not just you, then you have to wait, of course, on the… on the… on the availability of the… of the maintainers and everything, so… But as I said, you… one can unstale it by just commenting And say, I don't know, I'm looking into it, or something like that.
**Jeremy Blythe** 44:02 Yeah, cause we've… cause there's only… We'll maintain us.
And approvals. I guess in con… in… Collector contrib, you've got more.
There are more people who are able to approve and maintain.
**ariannavespri** 44:18 Yes, yes, yes, it's another… Absolutely, absolutely.
**Jeremy Blythe** 44:23 Yeah, so 2 weeks would be a bit… I think that would be too quick for us.
**ariannavespri** 44:28 Yeah, one could do, I don't know, like, 3 months, 4 months, I don't know.
**Jeremy Blythe** 44:33 I mean, a couple months would probably be about right, I reckon.
**Liudmila Molkova** 44:45 This person didn't even sign CLA.
Okay, I've done my two cents, and if we do the… Two worse toilators.
And we can, I think Trask was going to do something about stale PR, so maybe he was going to steal them based on their presence in this category.
Maybe not this one, because, well, in theory, we're still waiting for the review. People are still waiting for the review, and it's us who didn't give it.
But, yeah.
**Jeremy Blythe** 45:55 Okay.
**Liudmila Molkova** 45:56 And we can just go enable it, it's just one workflow.
Doesn't hurt. If you want to pick, I don't know, 30 days of an activity, Bish… It's fine with me.
Does anybody want to… Enable the workflow.
There are examples all over.
Not here.
Sorry.
**Joao G. (Dynatrace)** 46:31 sometimes is a bit buggy, though. I had a few times, I even opened a few issues on the… being, but the source that, things.
Got clothes where they shouldn't get clothes, or… We didn't get, didn't get marked as stale when they shouldn't have marked stale, but it works good enough that, I don't see this often, but I saw it already.
**Liudmila Molkova** 46:57 Yeah.
**Joao G. (Dynatrace)** 47:01 Just as a heads up.
Something like that.
**Jeremy Blythe** 47:12 Okay.
**Liudmila Molkova** 47:18 Okay.
Cool.
I'm thinking, Joao, do we need to chat about anything V2?
**Joao G. (Dynatrace)** 47:29 Yeah, it was only the same. I reviewed the messaging PR, I think that looks good to go, I will approve it.
But other than that, I saw there's other few PRs that are blocked.
on… on things on Weaver, right?
**Liudmila Molkova** 47:47 So this is one of the reasons we… Need, the neural list… Let's see… So… Excellent.
**Joao G. (Dynatrace)** 48:09 No.
Well…
**Liudmila Molkova** 48:12 Yeah.
**Joao G. (Dynatrace)** 48:13 Once we have the release.
**Liudmila Molkova** 48:14 release.
So this referens are unblocked.
This is… I'm going to make sure it lands in the PR, it should be… Just conflict resolution.
This is unrelated to Weaver.
**Joao G. (Dynatrace)** 48:33 So the one that is still open, but we already have the PR, I saw it, right? So that also will be part of the release, if we release now?
Or is…
**Liudmila Molkova** 48:43 Yeah, so, oh.
**Joao G. (Dynatrace)** 48:44 grilled.
**Liudmila Molkova** 48:46 We don't… okay, so we don't need to move this to V2, but we want… we need to get rid of body, because we don't support body on V2.
So this, getting rid of the body unblocks us.
Even without V2.
**Joao G. (Dynatrace)** 49:05 I know I meant the PR on Weaver about entity refinements, but you have the PR already for that. It's, like, all discussion's gone already, everything's fine.
**Liudmila Molkova** 49:16 Yeah, I just need to… Joao G. (Dynatrace) 49:19 Oh, yeah, okay, I saw it, I think, yesterday or so, and then I still saw that it was, things open, but okay, cool.
**Liudmila Molkova** 49:27 Yeah, and… Joao G. (Dynatrace) 49:31 Yeah, then I will review the other small, the other, yeah, unrelated PRs, then we should be good to go on those, yeah. And then I think there's just the generate schema next.
Right.
**Liudmila Molkova** 49:46 Yeah, this is the only one that's still unblocked.
Well, this will be a lot of work, actually.
**Joao G. (Dynatrace)** 49:57 Yep.
**Liudmila Molkova** 49:58 And once we release, we cannot find the work.
**Joao G. (Dynatrace)** 50:03 The hardware also probably was gonna be a little… Or… another one.
**Liudmila Molkova** 50:07 Hardware, it's all here. It's all contained.
It's actually turned out to be pretty easy.
**Joao G. (Dynatrace)** 50:14 Okay, that's good.
**Liudmila Molkova** 50:17 Oh.
**Joao G. (Dynatrace)** 50:18 Every time I have to touch the hardware thing, it's such a… a pain.
Okay, nice.
**Liudmila Molkova** 50:27 Since GitHub is not doing well today.
Yeah, so then we will release Woover, and we will have a lot of work to do.
And it seems the viewer release will unblock.
Everything, and if you see any issues anywhere in.
you.
Just let me know, I'll try to fix them.
**Joao G. (Dynatrace)** 50:53 G.
But, template stuff?
This is public groups, okay. So once we do that, then we can start working on templates.
**Liudmila Molkova** 51:08 Yeah, I, I have, somewhere, like, maybe a branch was templates. It's easy to… anyway, to use AI to just translate it. And… It works pretty well, I don't try ginger anymore, it's so good.
**Joao G. (Dynatrace)** 51:26 Yeah, yeah, I'm also very relieved that I don't have to dodge that anymore by hand.
I can be…
**Liudmila Molkova** 51:33 I've been… Joao G. (Dynatrace) 51:33 no.
**Liudmila Molkova** 51:36 I've… I've seen Jinja, like, so AI, trying to, work out through Jinja white spaces, and I saw it, like, learning and loose, oh, I've… I've changed this, but now that the new line appears there, and it comes back, and it was so satisfying to watch it struggle, too.
**Joao G. (Dynatrace)** 51:54 Yeah, I felt stupid so many times, like, why can't I get this right? Like, in my… do I have a problem? Like, do I not think? And then now I see also, yeah, I struggle, and it's very satisfying, yes.
**Liudmila Molkova** 52:10 Yeah.
**Joao G. (Dynatrace)** 52:12 Beyond me, why this is so complicated.
Cool, okay.
**Liudmila Molkova** 52:19 So then we have a plan.
**Joao G. (Dynatrace)** 52:22 Yes.
Yes, I'll get on those FTRs to unblock you, and then we can merge.
Merit all of those.
**Liudmila Molkova** 52:30 Awesome. Thank you, appreciate it.
Ben, anything else for today?
**Jeremy Blythe** 52:41 Not for me.
**Joao G. (Dynatrace)** 52:41 No, for me, no.
**ariannavespri** 52:43 Well, for me.
**Liudmila Molkova** 52:46 Awesome, Jen, good to see you all.
Excellent.
**ariannavespri** 52:50 Likewise, thank you, have a nice rest of the day. Bye, bye.
**Joao G. (Dynatrace)** 52:53 Bye.
