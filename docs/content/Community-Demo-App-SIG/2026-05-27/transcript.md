SIG: Community Demo App SIG
Date: 2026-05-27
Duration: 35 minutes
Zoom Recording URL: https://zoom.us/rec/share/nlrjrwJzyTR4GVxxE-DDLEDQXokkVcJvkBmLkg8pusx9OkhHJb6aUyax-a7PDsmh.Zq6fPZHpeu2UBLG4
============================================================

## Zoom Recording Transcript

**Pierre Tessier** 00:33 Hello!
**Juliano Costa | Datadog** 00:35 Hello, hello!
Alright, thanks.
**Pierre Tessier** 00:42 I'm sorry, you're gonna have to repeat all that.
**Juliano Costa | Datadog** 00:45 Alright, thanks.
**Pierre Tessier** 00:47 I… they're well.
Very well.
**Juliano Costa | Datadog** 00:53 Cool.
Are you submitting anything to KubeCon?
No. It ain't.
**Pierre Tessier** 01:05 I am not.
I didn't even have time to think about it, honestly.
At this point.
**Juliano Costa | Datadog** 01:12 Yeah, it closes on Sunday, I think, yeah.
Fuck.
**Pierre Tessier** 01:22 Yeah.
**Juliano Costa | Datadog** 01:28 the… I, I was… I was thinking, Pierre, about the compose Change.
And how much that… How much that breaks all the forks. Should we add some sort of, I mean, we're gonna do… I'm planning a blog post or something to announce,
**Pierre Tessier** 01:57 Dito.
**Juliano Costa | Datadog** 01:57 at all.
But should we add something on the main README, like, a call out to vendors, like, hey, Please update your fork.
**Pierre Tessier** 02:14 Mmm, yeah.
**Juliano Costa | Datadog** 02:14 Yeah, being.
**Pierre Tessier** 02:15 should.
**Juliano Costa | Datadog** 02:16 Maybe even clean up, like, I saw that we have trace test fork here, yeah, no need for that.
**Pierre Tessier** 02:26 Hold on, I was just trying to get all my… get this dock ready. I actually had one thing I wanted to chat about, but… alright.
You're talking about… There's still some.
**Juliano Costa | Datadog** 02:43 demos.
**Pierre Tessier** 02:43 for trace testing?
**Juliano Costa | Datadog** 02:45 No, no, I'm talking about demos featuring the astronomy shop.
So, trace test is listed there, to point to their… to shop.
**Pierre Tessier** 02:57 We should probably audit this.
**Juliano Costa | Datadog** 03:00 Yeah, so, like… That's a thing, like… I don't want to be the one, like, removing… competitors from the README, you know? Like, I don't want that to be seen as a…
**Pierre Tessier** 03:15 Can we make a… no, I get what you're saying, but can we make something like… If you haven't updated your fork, Resync your fork.
In the last 12 months, we remove you.
**Juliano Costa | Datadog** 03:32 That's, something that we can even automate. Yeah, that would be cool.
**Pierre Tessier** 03:38 You know, like… I want to be fair here, and I agree with you, we should not come out and, like, you're gone, you're gone, you're gone. Like, Trace Test has been… it's not an organization anymore, right?
**Juliano Costa | Datadog** 03:50 Exactly,
**Pierre Tessier** 03:54 I think we could, you know, maybe we do a policy about that there, and we could even put a little star under the table. All these forks, have been updated within the past 12 months.
Or these are all active forks, and then, you know, or active… we say active forks, and then we put a little starter. Active forks mean updating the last 12 months.
Right? And then… or 24 months, or whatever we think is 18 months, whatever we feel is… is appropriate there. 12 months might be a little restrictive, because I know some vendors, probably, they fork it and they leave it.
Because, yes, this is a huge change. It's a big-time breaking change.
**Juliano Costa | Datadog** 04:34 So… Yep.
I'm like, I'm glad that I got everything working on my machine. Now I just need to update the docs whenever we release the.
**Pierre Tessier** 04:45 Yeah.
**Juliano Costa | Datadog** 04:46 But I… yeah, wait, yeah. I don't wanna…
**Pierre Tessier** 04:53 Yeah.
We should absolutely have a policy that says we only list active forks, and I think what we need to do is determine what the right cutoff date for active means.
**Juliano Costa | Datadog** 05:06 Okay.
**Pierre Tessier** 05:08 Yes, given the changes, okay, so I'm gonna drop that in there. Bullet points. There we go. Given the… Breaking changes introduced with the new layered.
Docker Compose files, new services… Services.
The table listing… Demo… repository forks.
Will be updated to only include Active repository.
Forks.
Active will… Meaning they have been updated within the past 12… 18 slash 24 months.
Actual cutoff.
Paint.
TBD.
I think what we should do is we should just do a quick audit and see. Like, if we said it was 12 months, what would we be left with? If it was 18 months and 24 months, what would we be left with?
and part of your blog post, you should also say, hey, we're only tracking active stuff.
For what it's worth.
**Juliano Costa | Datadog** 06:34 Yeah.
**Pierre Tessier** 06:35 Like, we broke so much stuff that we're only… that we're forcing everybody to come back to us.
**Juliano Costa | Datadog** 06:41 Good.
**Pierre Tessier** 06:41 I don't know.
**Juliano Costa | Datadog** 06:42 Yay.
**Pierre Tessier** 06:42 Nicer tone, clearly.
**Juliano Costa | Datadog** 06:44 Yeah.
What the hell?
**Pierre Tessier** 06:49 Oh.
**Juliano Costa | Datadog** 06:50 What, what, what?
Well, one thing that actually, it's something that we need to discuss is about… so this is, this is easy to… to be handled by by Forks, so you just checked the last update. But we have, for instance, Datadog, Damatrace, I think… signals… And other… a couple of other vendors, they have blog posts.
**Pierre Tessier** 07:23 Hmm…
**Juliano Costa | Datadog** 07:24 Well, Data. It's not a blog post, it's a doc page that I keep up to date, but, like, I know that some other folks may not…
**Pierre Tessier** 07:34 I think we should just say that your instructions need to be kept up to date, because we changed it so drastically that… Even vendor forks, how they're gonna have to do this is they're gonna have to implement the right changes.
Is there a date on this blog post when it gets updated by Datadog?
**Juliano Costa | Datadog** 07:53 So Datadog is, a doc page, so…
**Pierre Tessier** 07:56 Here's a dog's page.
**Juliano Costa | Datadog** 07:57 No.
**Pierre Tessier** 07:58 No danger.
**Juliano Costa | Datadog** 07:58 But… But on… I think Dynatrace has, it's a blog post, it has, like, the last updated.
But, like.
**Pierre Tessier** 08:12 That might be a little harder to enforce than I think.
**Juliano Costa | Datadog** 08:15 Yeah, and then… it's tricky to… to actually validate. Like, I think… AWS… No, this is the AWS, the game.
Yeah, I… I don't know.
**Pierre Tessier** 08:36 And the guy who maintains that at AWS no longer works there.
**Juliano Costa | Datadog** 08:39 Yep.
**Shenoy Pratik Gurudatt** 08:45 We'll be helping with Michael, or… Someone else.
**Pierre Tessier** 08:49 It's, Haas, yeah, Michael Haas, and… Bloss, I think is his last name?
**Shenoy Pratik Gurudatt** 08:54 Yep.
Just left recently.
**Pierre Tessier** 09:02 I'm not sure, no.
Judah, like, it definitely… it's something we should address, I just… how do you do this fairly?
**Juliano Costa | Datadog** 09:10 Maybe on the blog post, or… What we could do is open an issue, and just tag whoever added, the… And tag whoever added the link.
On that issue, and give them, like, a month or so to update, and come back to us, and then… On the issue, we just keep track, and then everyone can add their company back to the list, but…
**Pierre Tessier** 09:43 We do something like… I like where you're going. We create an issue, we tag all the people in that issue that look at a really busy issue, though.
**Juliano Costa | Datadog** 09:54 But we can have, like, checkboxes. So, like, with all the…
**Pierre Tessier** 09:58 Yeah.
**Juliano Costa | Datadog** 09:58 42, and then people can just check their link.
Jonathan, there is no link yet. We got… we are planning a 3.0 release.
But that was, we had a couple of changes recently that is a big breaking change.
So all… I don't know if you saw, but all the Compose files, were structured in a different way. Now we have the layered, Compose files that Pierre, sent.
it is easier for… for… fork maintainers to maintain their stuff. The problem is that it breaks the current behavior. Yeah. So, they need to…
**Jonathan Munz** 10:44 That makes sense. Yeah, I was just curious.
**Pierre Tessier** 10:47 Yeah, this is like a call to action that says, hey, everybody who's made a bow said, here's your fork, we made some breaking changes, can you make sure your fork is up to date? Yep. Or your instructions are up to date?
**Jonathan Munz** 10:58 Yeah, just timing-wise, I was just curious, because at Embrace, we are about to do a new fork of the OpenTelemetry demo for a new demo We're spinning up, so… Yeah, just to let people on my team know, because probably doing it Post all these changes makes the most sense.
**Pierre Tessier** 11:16 I think the changes are already all in. I don't think we're planning anything else major, except getting in Shanoy's trace testing framework, but that… should not… be additional stuff.
**Juliano Costa | Datadog** 11:30 There is one, the agentic.
**Pierre Tessier** 11:35 But, oh, we want immersion first, don't we?
**Juliano Costa | Datadog** 11:38 Yeah, and also all the dash… I don't know if you use, Jonathan, the Rafana dashboards, so currently they're, broken, because we renamed all the… So that's the thing. We renamed all attributes, so now they are demo.something, so that broke everything, and if you had a fork where you showcased custom metrics in your fork, now they're a gun.
Got it.
**Pierre Tessier** 12:12 Yeah, we broke the demo.
Gotcha.
**Juliano Costa | Datadog** 12:14 Yes, sir.
**Pierre Tessier** 12:15 book the demo.
**Juliano Costa | Datadog** 12:15 Yeah.
It's for the better.
**Pierre Tessier** 12:18 It's for semantic conventions and better now.
**Juliano Costa | Datadog** 12:21 That's gonna be the title of the article. We broke the demo.
**Shenoy Pratik Gurudatt** 12:26 Eatonic.
**Pierre Tessier** 12:27 That's actually a good title, because feisty titles get people to read.
Okay, so what we're saying here is we're gonna make a call-to-action issue then instead, and give people, like, 30 or 60 days to update it, and if they don't, we will remove them, or do we move first and force people to re-add?
**Juliano Costa | Datadog** 12:56 I would rather go the other way around, like, let's keep it, and then people can just validate, and if they.
**Pierre Tessier** 13:04 validate.
**Juliano Costa | Datadog** 13:04 validating X, we just, remove. Otherwise.
**Pierre Tessier** 13:09 I'm gonna update.
**Juliano Costa | Datadog** 13:09 It still works, like, we remove and then they re-add.
I don't think we need, all of that.
**Pierre Tessier** 13:20 We'll include Agile.
We will make a post, we will create a tracking issue and tag. I'll fork… What do we call it?
Contributors… Code owners.
Providing them… what do we want to do, 30, 60, 45 days? What do you think is fair?
**Juliano Costa | Datadog** 13:52 I don't know.
You know, 6…
**Shenoy Pratik Gurudatt** 13:59 See, this sounds good, yeah.
**Juliano Costa | Datadog** 14:01 Yep.
**Pierre Tessier** 14:01 Would you say 60?
**Shenoy Pratik Gurudatt** 14:04 Yep.
**Pierre Tessier** 14:04 Okay, yeah, it's Webinar.
Okay.
What's next?
this… 3356… PR.
Tracy.
**Juliano Costa | Datadog** 14:39 So the… yeah.
**Shenoy Pratik Gurudatt** 14:42 Got a changelog conflict again, but .
**Juliano Costa | Datadog** 14:46 I honestly don't know what's going on with the changelog conflicts, because… all PRs are having it, and then when I check the conflicts, like.
there are two issues that are already in the middle of the whole thing, but are listed as conflict on the top, and I'm like.
Dude.
**Pierre Tessier** 15:08 I think somebody added changes to the top, and other people added changes to the bottom.
**Juliano Costa | Datadog** 15:13 Yep.
**Pierre Tessier** 15:14 And it's causing conflicts, and we're probably gonna lose a change somewhere in changelog.
I mean, that's a bit.
**Shenoy Pratik Gurudatt** 15:22 I tried both the places. Both of them ended up.
**Pierre Tessier** 15:26 Yeah… .
**Juliano Costa | Datadog** 15:29 at the end is, I always try to put at the end, because then it, like, the issue number goes growing.
What is, like, assembly?
But, yeah.
Anyways, we should have some automated way of generating changelogs, as the collector has.
That would be… nicer.
**Pierre Tessier** 15:57 like, it generates a changelog entry on its own for each PR?
**Juliano Costa | Datadog** 16:01 So you, you had a Yambo together with your PR?
And then that generates, whenever they… Whenever they… they release this, YAML populates, whatever, so…
**Shenoy Pratik Gurudatt** 16:18 It's there in, collector contract today.
**Juliano Costa | Datadog** 16:22 Yeah, yeah.
**Shenoy Pratik Gurudatt** 16:23 It comes with its own change login.
**Pierre Tessier** 16:27 I think it's because we don't changelog every PR, that's another thing.
Some of them are so, like, you know, spelling mistake or something like that, that we just don't change log yet.
Or dependency bumps don't get changelogged either.
That's probably a different issue, and maybe we should just put a comment in changelog to tell people, hey, always add your entries to the bottom of the unreleased list, not to the top of it.
Would that help?
**Juliano Costa | Datadog** 17:04 I don't know. I'm sure that people don't read, but we can.
**Pierre Tessier** 17:09 They usually don't.
Okay, Shanai, can you please resolve these conflicts again? We're sorry.
**Shenoy Pratik Gurudatt** 17:25 Yeah, I'll do it.
But are there any comments on the implementation itself?
**Pierre Tessier** 17:38 You should be… did you pull in the new ad service stuff? The gRPC conference should be fixed now.
**Shenoy Pratik Gurudatt** 17:43 I've got fixed, yes.
**Pierre Tessier** 17:45 Okay, so that one's resolved.
We should all take one more pass at this, and if we don't have any issues, we should merge it by the end of the week.
**Juliano Costa | Datadog** 18:09 I totally missed the tag here, sorry, shall I?
**Pierre Tessier** 18:13 Yeah, yeah.
**Juliano Costa | Datadog** 18:15 I'm busy.
**Pierre Tessier** 18:15 To be ready?
Take one more pass with Target 2.
merge by Friday, May 29th.
Okay.
**Juliano Costa | Datadog** 18:32 I… I haven't looked at the… the PR, but there is a way to run locally, right? I don't need to… Yeah, so make round telemetry tests. Okay, cool.
**Shenoy Pratik Gurudatt** 18:46 Yeah, yeah.
I think Nonal had a suggestion that it should also… run, like, deploy the demo, and then run it in the same command, so that's what, I added in the only major stuff.
And also, if you want to look at how things work, the design.md is a good one that I've kept.
I can probably change it to README.
So that just lists up… it just tells how.
**Pierre Tessier** 19:16 Yeah, maybe, I was just gonna say, can it just be a separate README inside that folder instead?
**Shenoy Pratik Gurudatt** 19:23 Yeah.
**Pierre Tessier** 19:24 Yeah, let's do that.
**Shenoy Pratik Gurudatt** 19:29 Let me unmute that.
**Pierre Tessier** 19:31 One more, does this delete all the old trace testing folders?
**Juliano Costa | Datadog** 19:36 Nope.
**Pierre Tessier** 19:38 We'll do that as a follow-up PR.
**Shenoy Pratik Gurudatt** 19:39 Yep.
**Pierre Tessier** 19:41 Okay.
**Shenoy Pratik Gurudatt** 19:42 I'll take that one.
**Juliano Costa | Datadog** 19:44 Oh.
I mean, my old…
**Pierre Tessier** 19:48 Yeah, yeah, so we need to remove all the old case testing stuff before. Feels like a clean-up-y thing we can do.
Okay.
**Juliano Costa | Datadog** 20:10 So, for the tests to be done for 3.0, we need to bump the dependencies. I think Collector, we have two new releases. Updated Grafana dashboards.
Helm can only be done after that.
**Pierre Tessier** 20:31 Helma's gonna be such a pain.
**Juliano Costa | Datadog** 20:33 I'm sorry.
**Pierre Tessier** 20:35 So fearing the helm. It's gonna be a multi-day… Whatever.
**Juliano Costa | Datadog** 20:42 Clark can do that.
**Shenoy Pratik Gurudatt** 20:44 Yeah, a lot can help a lot.
**Pierre Tessier** 20:46 I think I'm gonna have Claude get me a list of all PRs tagged, Helm update required.
Since our last release.
**Juliano Costa | Datadog** 20:56 It's, let me check that.
**Pierre Tessier** 21:00 Along.
**Juliano Costa | Datadog** 21:02 gone. We have a tracker on the main README that says how many PRs we had since the last release, so that's 266.
**Pierre Tessier** 21:12 Yeah, but then you gotta figure out which ones are tagged helm update required. That tag is pretty solid, although there might be a case here and there where it's… something's missed.
Okay.
**Juliano Costa | Datadog** 21:26 We also have… so I'm adding on the… the sign notes here. We also have this… whatever… Integration tests.
No status on… the main README the tagged.
Let me… let me share my screen.
Hopefully, I'm sharing the right tab.
Yay, yup.
So in here, we have also this one. I'm not sure if the new one will actually replace it.
We've got…
**Pierre Tessier** 22:10 Where does that come from?
**Juliano Costa | Datadog** 22:12 It comes from here.
It's the same name?
if we keep the same name, then, that should get back to… to work. If not, then we need to remove the the GitHub workflow, and… and the tag from the main README.
**Pierre Tessier** 22:35 Okay, so this is based on just the GitHub workflow.
Being successfully completing.
**Juliano Costa | Datadog** 22:42 Yep.
**Pierre Tessier** 22:44 Okay, so when we rep out trace testing, and we wire this up into the CI workflow, we just need to make sure it has the same name? Is that what we're saying?
**Juliano Costa | Datadog** 22:52 I…
**Shenoy Pratik Gurudatt** 22:53 Badge has a link, yeah. I can check it out. Just needs one update, I'll do it. Either way, like, adding new or removing this one.
**Juliano Costa | Datadog** 23:02 It's, linked to this round integration test YAML.
So…
**Pierre Tessier** 23:09 And you can just have run integration tests just pull yours.
Right?
**Shenoy Pratik Gurudatt** 23:16 It's called, I think, telemetry test.
See ya.
**Juliano Costa | Datadog** 23:20 El… Yeah, it will only run when approved, right?
**Shenoy Pratik Gurudatt** 23:26 Oh.
No, it runs every time.
You shouldn't…
**Pierre Tessier** 23:32 Okay, so your… your runtime, which you test YAML should follow the existing workflow we have. A little bit more about when it runs.
Because we do only have it running on approval.
**Shenoy Pratik Gurudatt** 23:49 May I ask, like, why is it so?
**Pierre Tessier** 23:53 Because integration testing requires you to stand up the entire demo, start the entire thing.
and then run the load runner to test it. If you do this on every commit, we'll be in CI forever.
So we only run that CI on approval.
**Shenoy Pratik Gurudatt** 24:10 Hmm.
**Pierre Tessier** 24:10 Because it's a longer CI, right? It requires you to start the whole entire demo, and then run the test.
All the other CIs don't actually, they just build the demo, or they only build the change files, but they don't actually start anything.
**Shenoy Pratik Gurudatt** 24:23 Got it, yep.
**Juliano Costa | Datadog** 24:25 And also as… I'm just thinking…
**Shenoy Pratik Gurudatt** 24:29 Dependabot PRs, so if a dependabot PR comes in, we approve, and then the test runs, and only then we merge.
**Pierre Tessier** 24:37 And then it fails, we approve and it fails, and we can't merge.
**Shenoy Pratik Gurudatt** 24:40 Hmm, so…
**Juliano Costa | Datadog** 24:41 so the… for the Depend About PR, what we can do is, it's simply, Approve, and whenever we approve, the tests will start running, and then we just click on barge when ready.
So we leave, and then we.
**Pierre Tessier** 24:59 And we…
**Juliano Costa | Datadog** 24:59 Not too far.
**Pierre Tessier** 25:00 recreate.
**Juliano Costa | Datadog** 25:00 if…
**Pierre Tessier** 25:02 Can we make a workflow to run this testing for dependent bots automatically?
Just depend about PRs, though, and nobody else.
**Shenoy Pratik Gurudatt** 25:12 I think so.
**Juliano Costa | Datadog** 25:13 Yeah, I think it's possible. So, you… you say whenever the PR comes from the Penabot, then do it.
**Pierre Tessier** 25:19 Yeah, so if the PR comes from Dpendabot, or it's been approved is when we run the workflow.
That's what it should be.
So, it's on pull request review, then? Is that what it is?
Yeah, so instead of being on pull requests, it's on pull request reviews, the only real change there.
**Shenoy Pratik Gurudatt** 25:47 Or, yeah, it's a minor change.
**Pierre Tessier** 25:51 Okay.
**Shenoy Pratik Gurudatt** 25:53 been, telemetry tests were disabled for so long that I forgot how.
How it used to work, actually, on approval or without approval itself.
**Pierre Tessier** 26:07 Yeah, actually, I can see down there, under run test, we have if github.event.reviewState equals approved, we run it.
So I think we could create just another if statement there, or compound that if statement, so if it's approved, or the submitter is Dependabot, go ahead and run this thing. So if you're looking right… I'm looking at, like, line 17 of run integration tests. That's how we gate it.
**Juliano Costa | Datadog** 26:43 You know, it's typing. I'm gonna wait.
**Shenoy Pratik Gurudatt** 26:46 Yeah, I just noted these changes.
**Pierre Tessier** 26:48 Okay.
**Shenoy Pratik Gurudatt** 26:49 campaign, and… Okay, maybe…
**Pierre Tessier** 26:53 Okay.
**Juliano Costa | Datadog** 26:54 soap.
I added to the notes, the link to the age intake, whatever.
and I know that, you know, I was taking a look at it, so I'll, Do you have comments to add?
**Shenoy Pratik Gurudatt** 27:25 Yeah, like, after the composite broke again, so I need to work with Felix again.
What I'm thinking is, it would be great if someone else can also take a stab at it. We have been adding it, and then fixing a lot of things, and then again, like, there were API changes, there were some minor changes, gRPC changes, and again, it broke, so we fixed it again. There's a loop that's going on.
But now I think it, more or less, everything is stable, we'll not have any major changes before we release it.
So, it should be good to go.
But, for sure, we need a second reviewer there, because it's a big PR.
**Juliano Costa | Datadog** 28:04 Yeah, 3,000.
3,000 lines.
**Shenoy Pratik Gurudatt** 28:08 Most of it is that, cache prompt thing that he has saved, so… To be concerned.
**Juliano Costa | Datadog** 28:13 Okay.
**Pierre Tessier** 28:14 It still uses Docker Compose, we gotta move this to Compose.
**Shenoy Pratik Gurudatt** 28:20 At some point, I'm just thinking of taking over and trying to fix things, rather than doing the to-and-fro, just pushing changes in the field.
**Pierre Tessier** 28:28 Can you, can you.
**Juliano Costa | Datadog** 28:29 I do that.
**Pierre Tessier** 28:29 Arsenoi?
**Shenoy Pratik Gurudatt** 28:31 Sorry?
**Pierre Tessier** 28:32 Shanoy, can you push to this branch?
**Shenoy Pratik Gurudatt** 28:34 Yeah, I think so.
**Juliano Costa | Datadog** 28:39 Maybe not, because it's not a fork.
He's sending from his main. So if his main is configured.
To… with main protection, then, you won't be able to do it.
Yeah, that happens sometimes.
But we can…
**Pierre Tessier** 29:01 I want to make sure he… yeah, okay. He seems fairly responsive, right?
**Juliano Costa | Datadog** 29:07 Yeah, yeah, he was here last call.
**Pierre Tessier** 29:10 Yeah.
**Juliano Costa | Datadog** 29:11 Felix is, active on the… on this.
It's just, like, 130, conversations,
**Pierre Tessier** 29:21 I know.
**Juliano Costa | Datadog** 29:22 So I'm like, you know when it's, like, already too late to… to ask? So we were just like, yeah.
Ugh.
whenever you say that, hey, it's good to go try it out, then I can do the…
**Pierre Tessier** 29:38 Yeah, usually that's when I jump on it. Okay.
**Juliano Costa | Datadog** 29:46 But I can't think she's gonna need some…
**Pierre Tessier** 29:47 changes. This does still need some changes. We need to get it to the latest Compose layout.
And run it all the way through again.
**Juliano Costa | Datadog** 29:57 But I don't think that's a big, change, though.
It's just a couple of things. I see that he changed a couple of stuff on the Compose file that are not related to his PR, like how the comments are indented and stuff, so… It's just about the agent thingy and MCP.
And chatbot, okay, so, yeah, a couple of services, but .
**Pierre Tessier** 30:30 There's… yeah, there's several sources here, and then we have some shared tools across them all.
I will have to figure out why that's done like that.
**Juliano Costa | Datadog** 30:48 And…
**Shenoy Pratik Gurudatt** 30:48 The tools are used between MCP and the agent, so agent can directly call the tools via the MCP, and that's the thing.
**Pierre Tessier** 30:59 Oh my god, this thing adds a lot of environment variables.
**Juliano Costa | Datadog** 31:05 I don't want to be the one updating Helm.
Fuck.
I, I, I have another, I have another one, I'll have to drop. Thanks, everyone.
**Pierre Tessier** 31:28 Okay, sure, this is a big one. I… Don't have time this… oh, shit.
And next week, I got an off-site.
I will try to carve time to look deeper at this. It's a big PR.
**Shenoy Pratik Gurudatt** 31:43 Yeah.
**Pierre Tessier** 31:44 Like, I'm trying to figure out, why do we have a YAML ignore file here?
Okay, I need to dig into it. There's some files in here where I'm sitting there going, why does this file exist?
**Shenoy Pratik Gurudatt** 31:59 So yeah, the other two YAML that you see in fixtures are the… prompt caches.
So if you're not connected to a model, the agent will fall back to using the YAML files, which are recordings of your prompts and responses.
**Pierre Tessier** 32:15 That's what goes in fixtures VCR cassettes.
**Shenoy Pratik Gurudatt** 32:17 Yeah, yeah.
**Pierre Tessier** 32:24 So these are your prompt caches that end up at…
**Shenoy Pratik Gurudatt** 32:28 Yep.
**Pierre Tessier** 32:30 Maybe I'm just confused here.
Today, we have, like, an Azure GPT 5.5 cassette. This just looks like a system prompt, right?
**Shenoy Pratik Gurudatt** 32:40 Yes.
**Pierre Tessier** 32:42 prompt. So that stays. Why do… are they part of a YAML ignore, then?
**Shenoy Pratik Gurudatt** 32:50 I'll be done.
**Pierre Tessier** 32:50 YAMLINting them? Is that the issue?
**Shenoy Pratik Gurudatt** 32:55 YAML, like, node, yeah, that's the thing. It's ignoring the linter, that's it.
**Pierre Tessier** 33:04 Do we want to do that?
Okay, I'll play with it. I won't play with it.
**Shenoy Pratik Gurudatt** 33:12 I have a lot of opinions on it, but I don't know.
**Pierre Tessier** 33:13 I know.
**Shenoy Pratik Gurudatt** 33:15 What do you have lunch.
**Pierre Tessier** 33:15 opinions, I have a lot of opinions. I'm almost at the point where, like, do we want to just get something merged and then come in and fix our opinions?
Sometimes it's easier to do that.
**Shenoy Pratik Gurudatt** 33:25 Yeah, yeah.
**Pierre Tessier** 33:26 Right? Like, Felix should get credit for creating this. Right? So let's get it merged, and then the things that we feel like, meh… Not the right way to do it. We should take a note of all of them, create maybe a tracking issue to note all these things that we should update.
Like, I noticed, like, in environment variables, it's defining an environment variable called application endpoint, which is the same thing as front-end, which is defined almost everywhere else. Why don't we reuse one of the existing ones, you know what I mean? So, there's a couple things in here where I think we could clean up.
But… we don't necessarily need to do with this PR. We can maybe do it later.
What does VCR stand for here?
**Shenoy Pratik Gurudatt** 34:08 I think that's the Python library. It's the older cassette player we see are recording something.
Yeah, video gassette recorder. That's so…
**Pierre Tessier** 34:18 Oh, I know what VCR stands for, I used to own one.
**Shenoy Pratik Gurudatt** 34:21 Yeah, yeah, so.
**Pierre Tessier** 34:23 But, like, it just, like, you know…
**Shenoy Pratik Gurudatt** 34:25 Python level.
**Pierre Tessier** 34:26 outdated for a while. Why do we, you know, where does a name come in in this?
For this agent, why VCR?
**Shenoy Pratik Gurudatt** 34:33 Yeah, it's a Python library called VCRPI that will help you to replay the API calls.
And that's where the file is coming from.
**Pierre Tessier** 34:42 Okay.
Okay, I think there's some things here we can do to clean it. Like, the intent of this PR makes a lot of sense, and we should probably move forward with it. Especially if it works and it does what we need to do, and then we should have a series of small PRs to clean it all up. I think is what we should.
**Shenoy Pratik Gurudatt** 34:59 Yeah.
**Pierre Tessier** 35:00 Because you're right, this is getting to the point where it's a little unwielding, and we should just get it in.
**Shenoy Pratik Gurudatt** 35:05 Yeah, and we should… do that before the release, right? I don't want…
**Pierre Tessier** 35:11 No, no, we will, we will do it before the release. I think the release will be mid-June. Mid to late June, we'll cut a release.
**Shenoy Pratik Gurudatt** 35:18 I'm having.
**Pierre Tessier** 35:18 Okay.
**Shenoy Pratik Gurudatt** 35:19 chats with Felix anyways on the side, so I'll just ask him to fix the Docker Compose part.
**Pierre Tessier** 35:25 If we get into fixes Docker Compose file, I think that's the biggest one. And then, instead of making changes to NITs, I will just record all my nits as, issues that we should follow up on. If you have any nits as well, like, record those. We'll create a tracking issue, and then we'll do the quick, fast follow-ups on them.
**Shenoy Pratik Gurudatt** 35:43 Okay, good. Thanks, man.
**Pierre Tessier** 35:45 Yeah, fantastic. Thanks, Joy. See you.
**Shenoy Pratik Gurudatt** 35:48 Right.
