SIG: Project Tooling SIG
Date: 2025-08-14
Duration: 38 minutes
Zoom Recording URL: https://zoom.us/rec/share/irgG6cd1Y-z3HNQycvPiN9G5d1rP77hKK2TFxNEkp7E8ERMxOB6lBJGCgr26IzAQ.R_WmzGaMM7WC4by2
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:32 Hey, Adrill.
**Adriel Perkins** 01:35 Hey, Shirask, how are you?
**Trask Stalnaker** 01:38 Doing good. How you doing?
**Adriel Perkins** 01:40 Okay, thank you.
**Trask Stalnaker** 02:24 Not sure if we've got much… …
I'm just working through some backlog of community issues.
I did want to get to… at some point, I wanted to pick your brain about the Octo STS stuff.
But I think I'm not ready yet, … Too many other…
things I want to get done first to clear up room.
**Adriel Perkins** 02:59 Okay. Yeah, no worries.
I think the only questions I had for today were probably around,
the status on Cloudflare, saying if we, …
We've sorted out how people are gonna act this up.
**Trask Stalnaker** 03:20 Probably, you'll need to… ping Austin directly. He's been… pretty, …
Swamped by other things and hasn't been… … Too available for meetings lately.
**Adriel Perkins** 03:42 Okay, yeah, I can… I can take that action on it.
**Trask Stalnaker** 03:46 You're waiting for it in order to set up the, … the CICD stuff?
**Adriel Perkins** 03:53 Yeah, migrate that over.
**Trask Stalnaker** 03:55 Got it.
**Adriel Perkins** 03:56 I don't even think it's sending to the account right now, because I think our Honeycomb account expired.
**Trask Stalnaker** 04:03 Okay.
**Adriel Perkins** 04:05 But, yeah, I would like to get that back up and… get that back up and running.
Especially because I wanted to see, like.
how Antoine's, caching, cachings incre… like, improved the times. That would have been awesome to see those trends. That's, ….
**Trask Stalnaker** 04:23 Oh, yes, yes, the Docker image.
Yeah. Yep.
Alright, well, yeah, I kinda suspect we maybe… we may… maybe we'll…
Won't have too much to discuss in this meeting for…
a month or so, kind of, until I get through some of the existing backlog and, Austin…
is… Back.
**Adriel Perkins** 04:59 Okay, yeah, that's… that's… that's fine. Anything you need from… from me, other than…
wanted to pick around Octo STS in the future.
**Trask Stalnaker** 05:09 Yeah, let me, FA, I will… Think on that, I… Yeah, it's a little…
Like, I haven't quite figured out how this… Group.
how to… how to be affect… how this group can be more effective, like, without… like, so much of this stuff requires permissions.
Org-level permissions to do stuff, that… That becomes a challenge.
**Adriel Perkins** 05:44 Yeah, for sure.
**Trask Stalnaker** 05:45 Antoine!
**Antoine Toulme** 05:47 Hello again.
Yeah.
Yeah, just don't want to disrupt your meeting, folks.
**Trask Stalnaker** 05:56 No, no, we were just discussing that we don't have much to discuss. Okay.
**Antoine Toulme** 06:02 Well, maybe we could just do a discussion about, like, how that went to have someone from the outside like me, who
really doesn't know that much how it went to create this repository using the admin repo. I think it went overall pretty well.
… There's a couple funny sides of it, like, you can't just do it in one step, right?
**Trask Stalnaker** 06:28 Yeah, that… It is. I don't know if you saw my most recent Update, ….
**Antoine Toulme** 06:38 Hmm… no, ….
**Trask Stalnaker** 06:42 Because, yeah, thanks for going through that, that, and, it helped. We have somebody else, we have the SWIFT team going through it now, also, so I…
Filled out more stuff here, like, beyond just the…
I, … I see stuff then, like, you know, the follow-up stuff, like, add the README, add Renovate.
add OSSF scorecard, add the code owner's file.
**Antoine Toulme** 07:12 that's something you do Yourself?
Or you have to… you can automate that.
**Trask Stalnaker** 07:18 I used to do that myself, and so, but the… I think the maintainers can do that.
Themselves.
Would it… yeah, it would be…
Maybe it would be worth, you know, trying to wrap all of this into one automatic
Like, into an automation?
**Antoine Toulme** 07:47 So, here's… here's what I'm asking.
… I have a discussion going on where I'd like to add a…
to our OpenTemmetry Collector contribository. Every time there's a first contributor.
Who's, for the first time, is sending, like, a… you know, PR.
there are some additional steps that we need to take, such as kicking off the CI for them.
And usually it's also great to just tell them, hey, you know, we're happy to see you, here's the contributing guide.
Here's some ideas of how you can help, right?
And what… what to… what to watch for.
And… I was discussing that with Dan, Dan Blanco just now, on the,
developer experience, SIG,
And he mentioned that that might be something that would be interesting, like, for all OpenTeametry repositories, right, as a…
as a bit of a standard thing that we could add, and I don't know…
If that makes sense, or if that's something that we could do, from this automation perspective, because it would simplify a bit management.
Or if it has to be done per repository, one by one.
**Trask Stalnaker** 08:58 So there was, Austin was working at one point on… like, a… a bot… That would…
Sort of respond to stuff that would be sort of like, …
What does he call it? Auto. Auto, the bot.
… And the idea was this…
But, we would use, We would use,
Oracle Cloud instance, and actually have the Git hooks
You know, send it the event so that it could respond right away to those kinds of events.
Without having to be… like, right now.
Everything… all our automations have to be per repository.
Because that's how the workflow notifications… they can listen for events on that repository.
But if we set up a central…
an app that gets those GitHooked
from all the events, from all repos, then we could do something Like that, that would….
**Antoine Toulme** 10:14 Cover all repos at once.
**Trask Stalnaker** 10:20 So, I mean, Austin has… not been… working on this.
for a while, and probably won't get back to it for a while. So it's definitely something that, if somebody else wants to…
Take it and drive it, that we could.
Like, I can get, I can set you up with…
Oracle Cloud Permissions, that kind of stuff that….
**Antoine Toulme** 10:52 I've said Oracle twice now. Okay.
Okay, yeah, that's more ambitious than what I had in mind. I thought I would just be able to just drop some YAML into a GitHub action.
make that templatable, drop it in that repo, and make it easy for people to adopt it as a separate action. I mean, there seems to be a number of these type of things where in OpenCentry.js, for example, they have a survey when you make your first PR.
And it would be great to just make sure that whenever we do this for one project, all projects benefit, right? So I was more thinking about that in a very simplistic approach.
Yeah, maybe an app is going to be great.
for that.
**Trask Stalnaker** 11:37 …
I mean, we can start less ambitious, as you say, like, with a template. We've talked previously about where to put those kinds of templates. Certainly, we could…
put them… in this repo…
You know, something where people can copy them out of.
I guess we could… Put it over here, …
this is, I mean, this is private, so… but only maintainers necessarily need to see that, but… …
**Antoine Toulme** 12:20 Fantastic.
**Trask Stalnaker** 12:21 Probably put it somewhere else.
….
**Antoine Toulme** 12:26 there's a middle ground between this full-blown GitHub app and what I'm… what I'm advertising, which is the GitHub Actions that we would be pushing, and that GitHub action would be, like.
But no, no, no, that doesn't work. Even if you do a GitHub action, you still need to declare it in a… in YAML. They still need to adopt it.
**Trask Stalnaker** 12:47 Yeah, you could simplify it by having a reusable one, and you still have to have the…
YAML in each repo, but it could reference out to a central reusable one.
**Antoine Toulme** 13:01 That'd be neat, …
Yeah, I mean, I was wondering, like, what's in your toolkit when it comes down to having standardized actions, like the scorecard, right, that I saw you kind of open on all the repositories?
I think that this was something that wasn't done manually, but also just a provisioning thing. But you're telling me no, right?
**Trask Stalnaker** 13:27 I mean, we can make it into a provisioning thing.
**Antoine Toulme** 13:31 Okay.
**Trask Stalnaker** 13:32 That's what I did, like, with the OSSF scorecards, right? I didn't actually go around creating all those PRs. I had… I just used OpenTelemetry Bot to create them all.
**Antoine Toulme** 13:45 Oh, but you did that as a script, not as a platform thing.
**Trask Stalnaker** 13:49 Right, right.
**Antoine Toulme** 13:50 Okay.
So it's somewhat okay, it's almost there, but it's not quite there. Is there a telephone way to kind of, enforce content in a repo?
**Trask Stalnaker** 14:02 ….
**Antoine Toulme** 14:03 Is that amazing?
**Trask Stalnaker** 14:04 I don't know. All I've used has been for,
configuration settings, I don't know if it actually… … At least the GitHub chart.
**Antoine Toulme** 14:16 Might be a bad idea.
That might come back in bytes, because this type of repository is, like, Okay, so…
At least you're not using that today, that's good to know.
**Trask Stalnaker** 14:31 Yeah, and I don't think the… at least the provider, the official GitHub provider, I think is only for…
Configuring… configurations, not for… Code that lives, not for doing commits, code that lives in the repo itself.
**Antoine Toulme** 14:52 Yeah, that sounds like orthogonal things, like, if you try to do that….
**Trask Stalnaker** 14:55 Cool. Yeah.
**Antoine Toulme** 14:56 Your state might be kind of precarious, because you have both, like, the telephone state might not be able to work out.
I'm trying to see… GitHub repository, homepage, visibility, has issues, discussion template.
You could, you could, you could do a template for your repository, so you could start with something.
If you're interested in that.
**Trask Stalnaker** 15:22 Yeah.
**Antoine Toulme** 15:22 No.
**Trask Stalnaker** 15:23 For new repos, given that
we don't create new repos that often, and we have so many existing repos. I like the idea of it being, like, a provisioning thing where,
We can automatically push Those workflows out to repos.
**Antoine Toulme** 15:47 I can look into it, I mean…
I'm a little spooked by the idea, but I… we can…
Yeah, so, yes, there is a way. GitHub repository file.
Not that I know what I'm doing, but… Apparently, you can… Potentially do that?
Yeah, I mean, I would be tickled by this type of approach, if we could do that, because then you can really…
manage at large, a large population of SIGs without having to get in there yourself all the time. It's just that
Obviously, at some point, someone's gonna say, well, this doesn't apply to my repo.
And now he's good.
**Trask Stalnaker** 16:34 Yeah.
**Antoine Toulme** 16:34 No, how do we exclude you? …
Yeah, it's somewhat composable, you could do it, like….
**Trask Stalnaker** 16:46 I mean, keeping them up-to-date is tricky because of that issue with repos are, everybody is…
Very picky about their… or not everybody, but some.
**Antoine Toulme** 16:59 Oh, no.
**Trask Stalnaker** 16:59 People are picky about what exactly is there.
**Antoine Toulme** 17:02 Yeah, for sure.
**Trask Stalnaker** 17:04 But I… Which is where I like the, kind of, like.
Best effort, like, okay, we're gonna send this out everywhere, initially.
And people can merge it or not merge it.
….
**Antoine Toulme** 17:20 Yeah, I could see how some folks might be like, I know better, that's not the way I want to manage things, I don't want to promise anything.
This is not… Meh.
**Trask Stalnaker** 17:31 Right.
But definitely documenting somewhere best practices, and I mean…
What about… we have SIG contributor… SIG….
**Antoine Toulme** 17:44 Oh, yeah, I think I was just there. The developer experience?
**Trask Stalnaker** 17:47 Developer experiences for external… people, right? Like, users of OpenTelemetry contributor experiences for… I think.
… So, I mean, it… Could be….
**Antoine Toulme** 18:06 There's a bit to do in there. Seek contributor experience.
What does it say to-do? Oh, about is set to to-do.
Fair enough.
So, actually, on that one, I was just in there, I was posting on that.
Issue, for example.
…
Oh my god, I've posted the wrong link.
Okay, that's not good. What happened?
You're doing 5 things at once, and you don't do any of them well.
… Let me post the right link to the city earlier, didn't I?
That's annoying.
Yep.
I meant to… I meant to post this. Let me change that.
I mean, we can do it in collector country, see if it works, start to replicate that across multiple repositories, see if that works.
no one has to take up… take us up on it, right? If they don't want to.
**Trask Stalnaker** 19:59 Yeah, I do like the idea of having a repo somewhere where we
Can store, sort of, those kinds of reusable workflows that people can go to and just copy from.
have an authority, instead of… right now, everybody just goes around to different repos and copies them from different, you know, repos.
**Antoine Toulme** 20:22 Having one sort of authoritative source would be nice.
Yep.
**Trask Stalnaker** 20:30 I still don't know what… I think we've discussed…
What that should be before and never.
… Epo.
Best practices…
I'd proposed something like that. … Repository tooling… Contributors, resources…
I mean, there's some, like.
that maybe make… that make sense under SIG security, like OSSF. Although, it still would be nice to have just one place for all of them.
And we could reference out.
to there.
I don't feel like project infrastructure, SIG Project Infra, is necessarily the right….
**Antoine Toulme** 21:45 Hmm.
**Adriel Perkins** 21:47 Usually there's, like, a repo called Shared Workflows or something like that.
Or, … like, Project 10 for actions, just a repo full of actions.
Usually the paradigm I see at enterprises was GitHub.
**Trask Stalnaker** 22:06 Yeah, you know, we're creating, like, a dot project, or… something repo… … Yeah, like.actions, or dot…
I like the dot, meaning, like, that, hey, these are not, like, for external… workflows…
And we ended up having a meeting today.
**Antoine Toulme** 22:47 Yeah, don't, don't fake me.
Okay.
It's all good stuff for me to know to just know where to go from here.
I mean, I also want to keep it this very incremental, trying it in one repository first, see what reception is.
Before I start to deliver all the SIG that they need to do it my way.
Right.
**Trask Stalnaker** 23:15 Yeah…
I don't hate that.
bothered.
Dot repos do we have?
This is a new….
**Antoine Toulme** 24:18 So….
**Trask Stalnaker** 24:22 There's, name… dot all-star, I see, dot github.project.
Cool, yeah, yeah. Let us know how that goes, it does sound like a useful…
one, and it's kinda… reminds me of the other initiative coming out of Contrib Experience, which has been… …
Daniel's, … Oh, do we close it?
Here we all really roll it out. It was… For adding the… thumbs up.
Subscript to all the issue templates.
**Antoine Toulme** 25:10 Yeah, they were just talking about that.
Seems to have been very, successful.
But they did that as a one-off, right? So they…
I'm trying to see how you make it so that it's good to go going forward.
**Trask Stalnaker** 25:26 Yeah.
Yeah, that one's a little different, because it's not a workflow, but I do like the idea.
Sharing workflow, having an official place for reusable workflows.
**Antoine Toulme** 25:40 Hmm.
Yeah, and then maybe there's someone doing that already, that's the other thing, I don't know.
**Trask Stalnaker** 25:48 Someone doing what already?
**Antoine Toulme** 25:50 what exactly this section I'm trying to create does, which is.
**Trask Stalnaker** 25:54 Boom.
**Antoine Toulme** 25:55 post a message to the user saying, hey, welcome, and this is your first PR, here is a label to identify your PR, and then let's make sure you read the contributing guide so you know what you're getting yourself into, and just set some expectations about my… where to get help.
no need to winch, just go to Attack Collector Dev if you need a review, you can engage with people there, we're responsive. This type of stuff, right? And that might be specific to each project a little bit, but also.
there might be just some good guidance, some past, like, scratch issue from having done that maybe a year or two ago that could be helpful that I just don't know, because OpenTeometry is so big. For example, I don't spend time with the Pythonistas over there, and maybe they have a great experience. Maybe they know.
So…
But we can start in a little corner, and see how it goes, and just try it for a month.
**Trask Stalnaker** 26:49 Yeah, and I mean, the contributor experience folks, I mean, hopefully that SIG has enough representation from different places to know, at least for people who are interested in that kind of thing.
who might know, because, yeah, I don't know of any…
like that. I know, like, the post-merge… I've seen, I think, the website repo also has what you were describing that JS has.
For, like, a post.
**Antoine Toulme** 27:21 For example, we don't, and I don't know that that ever came up, so I'm actually asking the maintainers of the collector country report right now, like, why don't we have this? That sounds pretty cool.
Or are we not?
caring for this? Like, what's going on here?
**Trask Stalnaker** 27:36 I only learned about it recently, like, I think they only added it to the website repo.
in the last… Some number of months.
**Antoine Toulme** 27:47 Yeah, I thought they were special or something, and I'm realizing, no, actually, they want this for everybody.
Well, let's… let's go then, like, let's… let's engage.
… Yeah, I have another topic for you if you want, not to take your whole hour, but…
I've been invited to the GitHub community for maintainers. I'm not sure if you're in there.
**Trask Stalnaker** 28:13 You'd have community for maintainer… oh….
**Antoine Toulme** 28:19 That one.
**Trask Stalnaker** 28:25 Right, right.
**Antoine Toulme** 28:28 Okay, so you… so I think all of maintainers should try to get access to this type of resources, if possible, that might be…
That's really useful, like, if you're a maintainer on any of our projects, there are questions there that you can ask that are private.
Because it's not open to the public, but you can ask questions. And so, for example, you're just hovering over one of the issues open.
Around cash, you remember last time?
lift.
If you go down a bit, you'll see it. The cache approaching total….
**Trask Stalnaker** 28:56 Oh, you bet this is you, hey.
**Antoine Toulme** 29:00 And so, I mean, I'm asking because there are some…
Real, like, a lot of best practices and experience coming from different people.
There were some really interesting ones coming from the Apache folks who told me, hey, we use artifacts instead of caches.
the outcome, you put it into an artifact, there's no bounding limit on that, and you can just use that, like, however you like, and…
It works really, really well, and you should just leverage that as much as possible.
It was interesting. Also trying to reduce our cache usage for Contrib as part of that, it worked okay, but what I realized is it's a little tricky, so…
I actually opened a PR on cash, on the cash action to talk about this and see if they could document that as a best practice to see if it's actually a good idea.
What I've realized is that
So, you have caches, and those caches have some level of leadership or, let's say, inheritance between them.
So, if your cache is made on the default branch, on the main branch, then it can be used in any of the PRs.
That's cool, right? So, you run the… you know, you build one time, and it's reusable in all the PRs.
If it's used in a PR, it can only be used in a PR.
Right, so the second time you run the PR, you get faster.
**Jacob Aronoff** 30:19 So, that's not, necessarily true. It depends on the, like, GitHub has pretty advanced, …
cache keying that you can do for, like, hits and misses, so what I've done in other projects before is, like, you don't usually version by… or cache key by the
PR ID or, like, any hashes like that, it's better to do things on your dependencies, like.
we did, like, a Node version to NPM version to, you know, X version, whatever. Or, like, you start with, like, Linux version, and then you just, like, go down the train, right?
**Antoine Toulme** 30:58 Yeah, yeah, yeah, yeah, I follow you.
**Jacob Aronoff** 31:01 Whereas doing it on the PR key can get… that's what is probably… if we're doing that, like.
**Antoine Toulme** 31:06 No, no, we don't. We do it by the checksum of the go.sum files.
So you take all your good dots come across all your tree.
And then that's the key. For Java, I'm not sure what we do, or others, but this is for the collector. And so, the problem we're having is that our caches are so big.
that we go over the 10GB limit, but when we evict caches with GitHub.
It doesn't care which branch it's on.
So, let's say you have a really good cache on main, and you love this cache, and use it all the time.
But, you know, you gotta go, you have a 10 gig, it's 24 hours, they start to delete stuff randomly. And they take it in whatever order that is not disclosed to you.
So, your cache on main is gone, now you have 3 PRs building, they're building 3 PRs, those 3 PRs all get their own version of their own cache, which are isolated from main and others, so now you're wasting 3 times that cache.
Plus….
**Trask Stalnaker** 32:02 Why do you push… why do you push… cash on PRs.
**Antoine Toulme** 32:07 Well, that's exactly what I'd like not to do, right? I don't want it. And so, there should be a way for you to, in your PR, say, I'm going to pick up a cache if there's one, but if there's no cache, then we're not going to write one, because that would be wasteful.
**Trask Stalnaker** 32:21 Oh, that's not… for some reason, I was assuming that was….
**Antoine Toulme** 32:26 They don't do that.
**Trask Stalnaker** 32:27 Really?
**Antoine Toulme** 32:29 Instead, there is no good way to do that by default.
Yeah.
**Trask Stalnaker** 32:39 So it's not, like, just a read-only setting, like, I want a read-only cache.
**Antoine Toulme** 32:46 You can do that with an if, but you have to actually go down to the level of restore cache versus, …
create, like, there's… there's two actions under cache, right? Cache itself is overwhelming, just the whole thing, just take care of everything for you. If you want, you can have restore cache and save cache being separate actions that you run explicitly in your build.
**Trask Stalnaker** 33:11 Hmm, okay.
**Antoine Toulme** 33:12 And so, if you do that, then you could put an if on that and say, don't save the cache if you're in a branch, right? But that means that now I have to retool all of my stuff to just do that, and it's a lot of YAML. I'm gonna mess that up. So, if you go to the PRs on the… on this repository you're on, yeah, the caching strategies are this type of stuff.
So you go to the PRs, and you might see mine first, yeah, that's my PR, and I'm offering that we add to the best practices of Action Cash a way to
Say, okay, if… Yeah, only save if we are… On the default branch.
So I'm hoping that I'm getting some feedback on that sometime soon.
In the next weeks. That'd be nice. Cool.
if I do get feedback, then that's the best practice, then we need to adopt that, and it would be great to adopt it across OpenTeometry, and to start to have better cache hits, and find ways to reward our containers if their cache hits are high.
To tell them they're doing a good job of managing your repository, because right now you're not overusing, oversubscribing to the cache.
Otherwise, what's going to happen is we'll continue to have this type of issues, and we're going to spend a lot of minutes building stuff that we shouldn't have. We're going to run into, you know, rate API limits, API rate limits, and all sorts of issues that really are going to degrade the experience of everyone.
**Trask Stalnaker** 34:46 Yeah, I think there's probably… I'm not sure we need to roll it out across all repos, because there's a lot of repos that just don't build that much, or use that much cache.
**Antoine Toulme** 34:59 Yeah. That it probably doesn't matter.
**Trask Stalnaker** 35:01 But it would be nice to… definitely rep… like…
Be able to see what our cash usage is, and…
anything that's, like, exceeding that, like… I mean, these are the two… obvious ones.
But yeah, probably any of these top 10 would benefit from better cash management.
**Antoine Toulme** 35:29 So, yeah, that's… that's mostly it.
**Trask Stalnaker** 35:35 Cool.
**Antoine Toulme** 35:37 Yep.
Yeah.
Does that make sense?
**Trask Stalnaker** 35:45 Generally.
**Antoine Toulme** 35:46 You're good.
Okay.
**Trask Stalnaker** 35:48 Oh, we should add that, ….
**Antoine Toulme** 35:51 Huh.
**Trask Stalnaker** 35:52 link.
Where did it go?
Here we go.
**Antoine Toulme** 35:56 And it feels a bit, weird to work on this, because, in a sense, like, no one is seeing this. This is a very silent issue about the cache misses.
all we see is that our build is slow, so people complain it could be faster, but we don't know any better. It's also running on GitHub, so it feels very fast. Oh, you know, proxy.goline.org is just next door. Why are you complaining? And I feel like I'm shouting in the void sometimes about this.
It's not… it's not acknowledged as an actual problem, because we don't feel the burn of using this many minutes for workflow builds.
But I would assume that at some point, someone from the CNCF or something, whoever's paying that bill.
**Trask Stalnaker** 36:38 Seems to come back and say….
**Antoine Toulme** 36:40 hey, what you doing over there? Like, you're just… you know, you're crushing a data center all by yourself. You're closing… you're causing global warming in the state of Washington just by yourself, right?
**Trask Stalnaker** 36:52 Well, yeah, look at this, collector contrib is half of the total minutes across all repas.
**Antoine Toulme** 37:02 Yeah.
**Trask Stalnaker** 37:03 Oh my god.
**Antoine Toulme** 37:04 It's massive. It's… it is.
**Trask Stalnaker** 37:08 So, anyway, sounds like you're tackling the right repo.
**Antoine Toulme** 37:12 Okay, sounds like also this is the right… like, there's no need to go, like, on a… on a hunt for others, just that one would just yield so much, there is no need to go fight, others.
**Trask Stalnaker** 37:23 Yeah, I know we spent a good amount of time on cache configuration in the Java instrumentation repo, because that was killing us.
**Antoine Toulme** 37:33 Yeah.
**Trask Stalnaker** 37:34 And then…
That was several years ago, and then more recently, Gradle, the Gradle plugin built in a smart cache management.
And it's… Seems to be okay, … It's our…
Builds are slow for other reasons, still.
… But I like the idea of, like, you know, how… Ha…
I mean, it's only fair, though, to, like, divide this by the number of PRs that you get.
…
But that would be an interesting metric to share with other maintainers to, like, like you say, try to have more efficient
builds.
Cool.
Anything else that… You wanted to chat about today?
**Antoine Toulme** 38:38 M.
I'm all done.
**Trask Stalnaker** 38:47 Cool.
And… see y'all next time.
