SIG: Ruby SIG
Date: 2026-01-13
Duration: 64 minutes
Zoom Recording URL: https://zoom.us/rec/share/aaoPR6E_gpz5H-Mycij-M2nKL65vCepT1Vl-MO0duba40Jsov-cbIpItoj0ivj55.dvB9AE14fu5MgTeS
============================================================

## Zoom Recording Transcript

Kayla Reopelle 00:06:53 Hi, Daniel.
Daniel Azuma 00:07:00 Hello?
Kayla Reopelle 00:07:01 How you doing?
Daniel Azuma 00:07:02 I'm good, how are you?
Kayla Reopelle 00:07:05 We're doing alright.
Hey, I haven't had a chance to look at your, your PRs yet, but I'm really curious to see them.
Daniel Azuma 00:07:14 Oh, okay.
Yeah, yeah, I think we'll… we'll probably want to talk about, releases a little bit this, this meeting anyway, so yeah.
Kayla Reopelle 00:07:27 Sounds good.
Actually, we have a couple other people, but, we'll give them another minute or so.
80s?
And get started, and then I also have to leave at, 40.
So 20 before the hour today, to go to an appointment.
Alright, so… the spec sig today… I feel like there wasn't a whole lot that was kind of new from our discussions that we raised last week.
There's, just in general, more conversations kind of happening around declarative configuration. You know, this hotel resource attributes environment variable might change its structure.
If you happen to be in Brussels, sometime, I think, next month? Yeah. On Groundhog's Day, if you happen to be in Brussels, there is an OTEL event happening.
And then… let's see, what else?
Yeah, declarative config is getting closer to, the spec being stabilized. They have a lot of prototypes, so I don't think that they really, like, need anything.
from Ruby until it gets stabilized. But, if you've been using it in any other languages, or just in general have some… some thoughts about how configuration should work, I think now is a great time. They're really looking for, kind of.
Critical questions to clear up anything that might be major before the spec goes in.
I feel like this… this may not happen. The discussion here was adding an opt-in metric advisory parameter. So, what that would essentially do is allow you to… It got to a point of, like, being able to add levels for metrics, kind of similar to the way that we have levels for logs.
So, you could, you know, if you only wanted critical metrics rather than needing to go to each one and change the aggregation, or kind of disable them individually, there could be, you know, kind of a more broad strokes option to control metrics.
They had talked about maybe having, like, a recommended versus often… I don't… lots of different strategies, but, Overall, I think there's some concerns about this duplicating behavior that is already available in metrics.
So… so yeah, so I think if you have… Ideas about this, or if you have been… feeling limited by the options that you have to control, what metrics are sent, this would be a good conversation to join.
Ariel @arielvalentin (ATX, USA) 00:11:35 Kayla, can you send a link to that?
Kayla Reopelle 00:11:37 Yeah, sure thing.
Here's the link for the opt-in.
And here is just the SIG notes in general.
That's… that probably happened about halfway through the meeting, If you wanted to rewatch the meeting.
Oh, and then I think the last one that makes sense to call out here is that for, RPC events, they're trying to deprecate the RPC message span events, if you're using them. I don't remember if our gRPC instrumentation is emitting them or not, but if you are using them.
I think you should chime in here. I… I have a feeling that they may want to move quickly on this one, just kind of judging by how they felt in the meeting. So, yeah, that's… That's another one to call out. Anything else on here?
That people want to look into a little more closely before we move on?
Alright.
Okay… So, we don't have anything on the agenda right now, but, I guess just starting with Core, I know, Daniel, you're here, you have, some thoughts about, like, release tooling that you wanted to present. Is there anything else, on the agenda today that people want to Add or go over?
Okay.
Wendy Smoak 00:13:23 Sorry, I was late. The… the, not running the… GitHub Actions on Forks discussion, wherever that fits. I didn't… I just got back, I didn't add it to the agenda.
Kayla Reopelle 00:13:36 Yeah, no problem. I think that I might have merged that one… Today…
Wendy Smoak 00:13:45 I just… Are we in the right place to do it?
Kayla Reopelle 00:13:48 Yeah, I mean, I think.
Wendy Smoak 00:13:49 Okay.
Kayla Reopelle 00:13:50 around. I, I feel then Cora contrib. But go ahead.
Wendy Smoak 00:13:54 There were two, I think. So I… what I was trying to prevent is… when I… I have a fork, and when I sink it.
everything runs, like, on the main branch, which I just feel like is… wasted effort. It already… all of that stuff already ran on the main branch upstream.
I was thinking today, like, are… do people use forks not the way I use forks? Like, I always keep main matching main, and then I have a branch.
So if people are doing stuff on their main branch in their forks, then… I have a different worldview, and my request is not appropriate.
Ariel @arielvalentin (ATX, USA) 00:14:31 Typically myself, I create a branch so I will always keep main in sync with Upstream.
Wendy Smoak 00:14:38 Yes.
Ariel @arielvalentin (ATX, USA) 00:14:38 I create branches, and I open PRs for branches for mine… to upstream.
Wendy Smoak 00:14:45 Yes, that is how I've always done it, and in that case.
isn't it just wasted compute to, like, rerun the checks on main, like, when I merge them? Yeah. So, okay, that's what I was trying to prevent. Not stuff on branches on forks, but just that redoing everything, because that means, like, everyone who has a fork I mean, GitHub should care, I guess, they're the one paying for it.
Kayla Reopelle 00:15:08 Yeah.
Wendy Smoak 00:15:09 all it's doing is sending me emails, I can delete them, but that's where I was going. Nothing about, like, not doing anything on a fork, but just that anyone, I just felt like it was…
Ariel @arielvalentin (ATX, USA) 00:15:19 Yeah, we, we take up, you know, electricity on the grid, so everybody pays for it in some way.
Wendy Smoak 00:15:25 Yes.
Kayla Reopelle 00:15:27 So, so does this… I always assumed that this was for any… Trigger, not just… main or… or pull requests. So, like, if it, you know, like, for the CI, for example, like, I don't think the CI will run on pull requests on personal forks anymore.
But I think this is a good experiment for us to try. We can find out if anyone is missing it and using it.
And go from there. I used it heavily, like, in the past, but I think that was also at a point where I felt really shy about, like, putting work in progress on upstream, so… We could just Trying to normalize that.
Ariel @arielvalentin (ATX, USA) 00:16:13 I will say that as a GitHub employee, my thoughts do not necessarily reflect those of my employer.
But it doesn't seem like there's a simple way, or, like, a configuration option, even in Actions, to say.
Don't run these jobs on forks, only run them… On the upstream repository, of the owner repository, or whatever.
And…
Wendy Smoak 00:16:36 Does seem hard.
Ariel @arielvalentin (ATX, USA) 00:16:38 And it seems like this is the only way to do it, is to restrict it by the repository name right now. Like, there's other things, like, if there are events that… You know, if you're on a fork and you received an event, But that seems… To be not as clear as this?
So I went through the process of identifying all the jobs, running… and adding this… this if statement, essentially, to all of the jobs in the repos, both here in Contrib and in… or sorry, in Contrib, and in this repo, Ruby.
And so hopefully, if you sink.
That's the other problem, is that you need to sync in order for that to take effect.
Wendy Smoak 00:17:18 Yes. Yeah. But everyone will eventually. Hopefully.
Alright, I will merge it in and just watch my email. And again, like, it's not… it's not bothering me, I can delete emails, it was just something that…
Kayla Reopelle 00:17:33 No, I think…
Wendy Smoak 00:17:34 This should not be happening, I think, so…
Ariel @arielvalentin (ATX, USA) 00:17:36 Yeah, we… there's gotta be some sort of way, like, with all of us having… with the YAML filters… sorry, linters coming through, we might want an actions filter that says… make sure that these actions… all the… all of the jobs on actions has this constraint in it.
Yeah, I could do that. Or an actions template file, or something like that. So, you know… This is mostly my fault for being lazy, and… copy, pasting, modifying what I'll do in this, you know… Neatly.
I'm pretty sure if you blame all these files, my names are on them.
Wendy Smoak 00:18:12 Thanks.
Ariel @arielvalentin (ATX, USA) 00:18:20 But again, we don't use forks internally, so I… It's like a feature I never use.
You know, Wakila is typing, and This is not on the agenda, but… I am, I'm working on, getting test… the test suite passing for Ruby 4.
And, dropping support for 3-2. I wanna do those in… I'm doing those in two separate… Prs?
And then I think there was another… And Rubicop rules are disabled for new cops on main… in the Ruby… main repo.
And I'm trying… and I enable them, and I see a bunch of… Rules that were added in.
So I'm wondering if, some things that we can do… Is to take a look at these, and Decide whether or not we want to opt into those particular rules as a group.
And I don't know what's the easiest way to communicate that.
Kayla Reopelle 00:19:52 Yeah. And how's…
Ariel @arielvalentin (ATX, USA) 00:19:53 you know… Because there are some rules that it's like, or do we do a rule at a time per PR?
Kayla Reopelle 00:20:00 Mmm, interesting.
Daniel Azuma 00:20:03 There's often a lot of those. Like, I… for my personal repos, I… once a year, I go through and, you know, update RoboCop, you know, enable all the rules, figure out what's, you know, what's changed and what's breaking my repos, and… And making decisions on… on all the new rules. And there are often… there's, there's, like.
anywhere between a dozen and a few dozen new rules that pop up. I think it can be… if we try to do them one at a time, or, like, you know, it might be just really tedious, I would suggest that we have one person, go through, do a first pass of it, through it, and kind of put together kind of a straw man, you know.
suggestion, along with maybe some notes on some that are, you know, that they're not sure about, and then we can talk about…
Ariel @arielvalentin (ATX, USA) 00:20:55 Okay, so what I could do is in the… maybe do a PR… in the PR body?
Put together a matrix of all the new rules.
Give everyone a chance to chime in on the rules and say, like, yeah, nigg.
I don't know if that… I guess I'm trying to figure out the easiest way for us to communicate with each other and all agree on… like, give a consensus.
Daniel Azuma 00:21:15 PR.
Ariel @arielvalentin (ATX, USA) 00:21:16 on certain things.
Daniel Azuma 00:21:16 PR, you know, add the new rules to the Rubicop YAML with enabled, disabled, or whatever, as a first pass, and then get people to comments, and then we can, if there's any discussion, we can talk about in the SIG.
Ariel @arielvalentin (ATX, USA) 00:21:30 Okay.
See how simple… Daniel gave me the simplest solution, which was just use the… The PR. I love your comment.
Sounds good to me.
And then the last thing was… Was that the last thing for the… before upgrade.
Yeah, I think that's the last thing. Everything else is kind of like gem housekeeping.
Kayla Reopelle 00:22:01 Okay.
Was there anything you wanted to look at with the Ruby 4 upgrade here, or just mentioning it?
Ariel @arielvalentin (ATX, USA) 00:22:08 Just mentioning, I mean, what I did was I added the… I added the configuration, and it… I expected it to fail.
I haven't looked at what needs to change. My guess is that it's still gonna be more of those… Open struct problems, and…
Kayla Reopelle 00:22:24 Hmm.
Ariel @arielvalentin (ATX, USA) 00:22:26 Rake not having OpenStruct pulled in anymore.
Kayla Reopelle 00:22:32 Sounds good. Thanks for taking care of that.
Alright. Any… Anything else? The floor is open.
Daniel Azuma 00:22:54 Well, we did want to talk about relief.
Release stuff, so, I guess I can kick that off real, real quick. So, so just some context, the release system, is, one that, that we're currently using is one that I wrote, a few years ago. It's, it's what I use for.
my own repos, and there's a few other… the number of customers of this system is probably on the order of 5.
it's… so I… it was… I… I… kind of gotten busy and stopped maintaining it for a while, and then, just a few months ago, I quit my job, and had, as a result, had a bunch of time, so I actually was able to finish some of the pending fixes and updates that I wanted to make to it.
So that's what the, the… I have a pull request in both repositories to update the system to that new version of this release system.
So, the hope is that, you know, if we, if we choose to go that way, that, you know, it'll make it… it'll fix some of the issues that we currently have, as well as, make, additional, issues and, and, and, improvements a lot easier to, to, to make.
So, that's one, direction that we can go. There's also this question that, I think Ariel had, investigated earlier about moving to release, please, which is a more, more commonly used, system.
Out there. I had some thoughts on that that I wanted to, bring up.
So, you know, a little context. Release Please was written, by actually my team when I was at Google.
I was part of the SDK team for Google Cloud, and one of the team members, one of the engineers, the same person who actually came up with the whole idea of conventional commits.
In fact, he did the first, implementation of Release Please some years ago for our use internally, but did so open source. Back then, our team was much more open source friendly, community-friendly, and so we… We kind of put it out there just as a, you know, you're, you're, you know.
Check it out if you, if you find it useful.
the, google, and in particular, the organization around my team, has evolved since then.
considerably. We got reorged, a few years ago, moved… we used to be part of developer relations. We got moved out of that and back into, traditional engineering, and our current.
Organization and kind of director-level leadership is, not hostile to open source, but not really… it's not a priority for them. And so, as part of that, a lot of the tooling that we had put together that was open source, initially, is in the process of either being put… moved back internally.
Or… or is, is, or, or at minimum, you know, it might still be open source, but the amount of kind of community support or support for, for external users, really, is, is probably not gonna be, that great, moving forward. In particular, release, please.
The original developer who, who wrote it, left Google a few years ago. The current maintainer, internally at Google is a friend of mine, I… my… my sense is that he's ready to retire, and probably going to be leaving Google in a few months, is my guess. the, anyway, the long and short of it is, I'm… I… I am not confident about the amount of support for external users that we're going to be able to get, out of the Google team, moving forward.
I think that… I don't have a good sense for how many external users Release Please has. Ariel says that there's a bunch at GitHub, at least.
I think the best case scenario would actually be that, if… Someone, somewhere, decided to fork Release Please and maintain it externally. If that were to happen, that's great. I think that that's a, that's a path forward for the community users of Release Please.
If that doesn't happen, I don't know to what extent we can really expect support for it moving forward. So that's kind of the risk for moving to release, please.
So that… those are kind of the trade-offs here. We're looking at a system that's kind of, you know, for now, dependent on me.
To maintain… And that doesn't have a whole lot of community use, or a system that does currently have a lot of community use, but where the current maintenance of it is, moving forward, is a little bit uncertain unless it gets forked.
So, that's this… there's kind of this decision that we will want to make, Which, which direction we want to go.
I haven't been around for a while, but I'm trying to be back now, especially since I have some time now that I'm not working full-time anymore.
So I'm, so I'm, at least at the moment, available to, to make, changes and improvements to the, to the release system if people have things that have been bothering them or want to, you know, features that they want.
But I'm also, happy to support us, moving to release, please, if that's what people would prefer. So… And I do have some familiarity with Release Please myself, because it was my team that maintained it.
So… Yeah, those… I just kind of wanted to put that out there and, see what, especially people who have done, been doing the releases here have, people have opinions about this.
Ariel @arielvalentin (ATX, USA) 00:30:12 Thank you for giving us that background. So, it sounds to me… There's the other option, which is for… if we had the appetite for us to create a fork of Release Please and, maintain it, but it sounds like… that extends the scope of, you know, what we're trying to do, which is release Ruby Gems from our repository.
Daniel Azuma 00:30:34 Release Please is in Node as well. It's written in Node, so you can…
Ariel @arielvalentin (ATX, USA) 00:30:39 Yeah, so it's like, so, you know, given that information.
it sounds like it's gonna be volatile in the future, this is good information to know, I can… and As far as, like, if you have time… To help us, you know, kind of work out features or work out issues that we run into during the… releases, I really would appreciate it.
And I think, like, if you're able to commit some time with us… I think the problem that we have is that we don't dedicate any time to trying to manage The release tooling, either.
Right, so for me, it's like… I'm a little bit ambivalent about it, as long as I can outsource it and it works.
That's why I was looking for more of a… Of, out-of-the-box situation, because it was, like, a little hard also to get in touch with you when you were gone for a bit.
So that's a lot of my motivation for wanting to try it. What I found out in the process is that it didn't give me anything… Did it make it easy for me to transition from one to another?
And I think one of the biggest problems we have in our repo is the… The gem hierarchy, the release gem hierarchy.
Where all depends on all of these gems, and they must be released together, But they have to be released in a specific order.
And then, there's, like, interdependencies between, you know, the contrib repo.
or transit dependencies, where it's like, all depends on Rails, and Rails has all of the Rails gems that it depends on.
And it's gem spec.
I don't, you know, the release please didn't solve that problem for me, so I gave it up.
I was like, I'm not even gonna try going forward. I left the configs in there.
And that's about where we were. Right now, what we do is we do a lot of… this manual… process, like, today, I went and tried to… if you can open up, Kayla, the rep… the contribib repo?
Daniel Azuma 00:32:39 And I even made this mistake. I'm gonna show you a mistake that I made, and then I…
Ariel @arielvalentin (ATX, USA) 00:32:43 ended up having to correct it. If you're looking closed.
So we have this sort of, like, automatic… Let's not do this one yet.
Grab release 11, right there. Release 11 gems.
We have a cron that runs weekly right before this meeting to say, were there any gems that we need to release?
And that's great, it does all this, but all… because these are our… Excuse me, child implementations, or child jumps.
Of all, we need to also release all in this batch.
So there was nothing that said… that discovered. There was a change set that occurred that also needs to be applied to all, and all has to update its dependencies.
And it's kind of like… making Renovate or Dependabot functionality As part of, part of this rollout process, kind of redoing that implementation.
And so I close it out, I say, okay, well, I've identified all of these gems that need to be released, so I'm also gonna release the all gem, which was on 12.
And then.
Daniel Azuma 00:33:52 to win.
Ariel @arielvalentin (ATX, USA) 00:33:52 And then I fat-fingered the all-release number to be 9 instead of 90.
So I messed that up, because it requires my, my, you know, my manual input.
And then foolishly, I approved it and released it.
The release got most of the gems out, all fails, and I said, darn it.
Then I created a follow-up release, which was another manual release where I did, like, a bug fix.
A release to try to address that problem.
And this is the kind of friction that I face when I'm trying to do rollouts of gems.
And it's just, you know, that's one of the… one of the things. The other part of it is, I really don't know what's gonna get rolled out unless I do a release request.
So, one of the things that I liked, and I mentioned this to you already, either in Slack or in one of the issues.
what I really appreciated about Release Please was that it would give me sort of, like, a running draft PR to tell me this is what's going to… this is what's going to go out in the next release when you merge this. And it was… it allowed me to do more of this on-demand by reviewing the changes.
you know, in this accumulated, in this accumulated PR.
And… Though the challenge that I found with release, please, was I didn't know of a mechanism to say, well, let me also add the all gem that also needs to be bumped as a part of this.
And keep bumping it, and And so, when I ran into that, and I didn't want to investigate more, that's another reason why I had dropped it. Because our release process allows me to say, oh, I'm gonna continue pushing up… Or I'm gonna, you know, redo this again, and do this with the Allgem, and make any changes as necessary in the PR review.
Which is what I do now, right?
so…
Daniel Azuma 00:35:47 when you do the Allgem, so the, the, the process there is, is, updating the gem specs with, with all of the, dependencies as they will be released by this, by this release, and then, and releasing the Allgems. Am I correct on that?
Ariel @arielvalentin (ATX, USA) 00:36:05 Affirmative.
Daniel Azuma 00:36:06 Oh, okay.
Ariel @arielvalentin (ATX, USA) 00:36:08 So once I do this, once I've done the manual release request with the subset of gems to get updated.
I go and I manually, you know, I'll create a comment here, and I'll comment on these, or I'll push up from my local host or code space or whatever. I will bump the versions of the gems that are the most recent ones in the repo.
And then, update the changelog to reflect that we're doing some changes, because it shows up as no significant changes, as it could not detect that something changed about the all gem itself.
Daniel Azuma 00:36:40 Yeah. Because there's no associated commits with it.
Yeah.
Ariel @arielvalentin (ATX, USA) 00:36:44 So I'm sure there's, you know, other ways that we can make that happen.
Daniel Azuma 00:36:53 Okay.
Okay, well, yeah, so… so if… if we, were to want to stick with the current, current release tooling, I can… I certainly have, time to, go look at, those two things. So I'm hearing two, basically, feature requests. One is, you know, automatic handling of the Allgem, and number two, This workflow where we have release pull requests that get updated dynamically as new commits come in, so that you can kind of see at any given point what's, what's ready to be released, and not have to manually Create new release pull requests every single time.
Ariel @arielvalentin (ATX, USA) 00:37:44 Yes, that, that, that describes it accurately, yeah.
Daniel Azuma 00:37:49 Okay, yeah, I can certainly, I can certainly do, do those two things.
Ariel @arielvalentin (ATX, USA) 00:37:55 Thank you. That's what we would want to do.
Daniel Azuma 00:38:02 Yeah. Are you the person who does the releases generally, Ariel, or are other people doing releases, or how have we been doing releases?
Ariel @arielvalentin (ATX, USA) 00:38:14 Typically, it's Kayla and I, because we're the only maintainers of the repo that are… You know, regularly attending meetings.
Everybody else kinda just vanished.
So, You know, we get an occasional, like, request to, you know, fix a bug or something like that.
And, you know, the… I want to say the emeritus maintainers come by and add something.
But it's pretty much just Kayla and I… Maintaining the… The repo… And we're hoping to get Hana and Schwan some maintainership soon.
Kayla Reopelle 00:38:56 And I second, like, my experience releasing is pretty similar to what Ariel shared.
And I think… one other feature in, kind of, the whole all improvements, which I think he touched on, but just to make it more explicit.
Is if the changelog could be generated with, kind of, the summary of the same changes that were made in the gems that we're pushing up.
I think that could… that could be helpful as well, since we're doing a lot of, kind of, copying, pasting, combining to simplify that.
Ariel @arielvalentin (ATX, USA) 00:39:30 Yeah, if possible, also, like, you know, whatever PRs were merged, if there's any metadata that we can attach to the changelog itself that has the URL, essentially, or, like, the… at least the… either the PR number or the issue number that was fixed as a result. That would also be, like, super… like, an A++.
Kayla Reopelle 00:39:49 Yeah, I agree. That's a nice-to-have, above and beyond, but, yeah, something… Certainly, like, figuring out how to make the all releases less manual would be a massive win, and… Yeah, yeah, but happy to keep using toys. I mean, it's worked pretty, pretty well for our uses. I would say this is just the main friction point.
Daniel Azuma 00:40:16 There's an allgem and conscrib, there isn't… there isn't one in the main repo, if I…
Kayla Reopelle 00:40:21 No, there isn't. I guess… Potentially, exporters could have maybe a similar problem, because they have dependencies on… I believe the API, so if the API gets updated, then… you know, do we have to go back and also update these? I'm not sure if that's something that makes sense, but I would say that all gem is probably the prototype that would solve any other problems that do occasionally come up in the core repo.
Ariel @arielvalentin (ATX, USA) 00:40:56 Yeah, I think, what is it, the Common Library, I think it is?
Is one that's shared amongst all of them?
Kayla Reopelle 00:41:08 Yeah, I do think there's a lot, I don't know how to easily look on the GitHub UI to find out.
what gems I'll install common.
Daniel Azuma 00:41:23 So, for… in the all case, I imagine that, anytime any of the gems, the kind of individual gems get updated, then we do want all to be updated and have its dependency updated.
In the common case, I would imagine that it might not be necessarily every single time that we want dependencies updated.
Like, you know, we could just have a small… a small bug fix in common that affects maybe one or two of the gems, but not everything do we want. So it does seem like a slightly different use case, I guess.
Kayla Reopelle 00:41:58 Yeah, let's… let's hold off on that one, then, and maybe… I can look into it a little more and see if there's things that are similar. But one thing you did just… mention, I don't know if we necessarily need to release a new version of the Allgem if we're just doing a patch release. I think only if it's a minor release do we really care to update the Allgem, because the patch release, I think, should be brought in automatically whenever someone rebundles.
But, I'm open to other opinions on that. I'm not sure how you feel about it, Arielle, or anyone else.
Ariel @arielvalentin (ATX, USA) 00:42:32 I think the bug fix one patch is… yeah, because I think most of them are scoped to pessimistic for patch.
Kayla Reopelle 00:42:41 -
Ariel @arielvalentin (ATX, USA) 00:42:41 It's gonna be, like, because we don't have a 1.0 version.
We treat minor bumps as sort of, like, feature releases.
We tied them to, to those.
And, so, yeah, I think in most cases, the bug fix version doesn't need a bump.
Kayla Reopelle 00:43:11 Thank you for offering to work on this, and coming back, and, you know, being ready to contribute again. It's really nice to have more people involved.
Daniel Azuma 00:43:20 Of course, yeah, I've always felt a little bit… I think I'm still a maintainer, which is odd, because I haven't been around, and I'm not sure, but that's… if we want to expire maintainerships for people who are kind of, no longer, no longer engaged.
Ariel @arielvalentin (ATX, USA) 00:43:38 Yeah, I brought that up, actually, to the hotel, like, governance folks, like, how do we keep folks engaged, and at what point do we… You know, is there, like, a turning point for folks to be emeritus status on some of the repos?
Cause it gives us a better sense of… These things are actually being maintained, or people are not maintained, and if somebody comes along.
If a repository is effectively dead.
Or a project is effectively unmaintained.
then perhaps it should be archived, or if new folks come out of the woodwork, and they want to become maintainers, how do… what's their… Acceptance process for them.
To participate if no one's around to merge anything.
You know what I mean? So… That's, that's something that I think the governance committee was gonna talk through, or, you know, the maintainers working group was gonna talk through, and get back to me on.
But…
Daniel Azuma 00:44:40 I imagine this, yeah, I would have expected this would be a common… common question, common issue that, I guess is surprised… it's surprising that, to me, that, hasn't been addressed by now, but… Okay, but yeah, I'm, I'm, I am… I am… I am back right now, at least I'm trying to be back, at least in the medium term, so, so yeah, I'm happy to… I'll definitely start looking into the, looking at the release stuff, and happy to… Start helping with reviews or other stuff as, you know, as need arises.
Kayla Reopelle 00:45:29 Great, thank you.
Okay, I should probably sign off pretty soon, so I can get to my next appointment, but is there anything else that people want to talk about?
Anyone wants to take over?
The screen share.
Ariel @arielvalentin (ATX, USA) 00:45:49 I know we're targeting the… deprecating… Pre-1.0… Semantec attributes… Lord, is that happening?
Kayla Reopelle 00:46:04 For HTTP stuff. I haven't looked at the date for a while. I think we had to wait 6 months from the first release. I'm pretty sure it was… end of February, was our initial target, but I know there's a few things with semantics that, we wanted to work through with you to make sure that the The span names and attributes are at a good spot.
At least in one release, you know, before we take it out.
Ariel @arielvalentin (ATX, USA) 00:46:31 Is there any chance that we can try to get… The schema version number?
Added… to the SDK in that time period?
Kayla Reopelle 00:46:42 Yeah, I think that's reasonable, as long as it just needs to be the, we can try reopening that PR. I forget if I already did.
And… Take a look at it.
Hannah Ramadan 00:47:03 Yeah, I believe the day that we sat was… I think it was, like, the end of February, but that's just when we're allowed to… I guess remove the old semantic conventions and only move forward with new, but we can kind of do whatever we want. Keep it around until we're ready.
Ariel @arielvalentin (ATX, USA) 00:47:32 And then… I mean, outside of that, I ain't… I got nothin'.
Kayla Reopelle 00:47:43 Alright.
Well then, I guess, we'll see you all on Slack if anything else comes up, and see you next week, if not.
Take care.
Ariel @arielvalentin (ATX, USA) 00:47:54 Daniel, do you have 5 seconds to hang her out for a second?
Daniel Azuma 00:47:57 Sorry, I got a question for you. Yeah, yeah, yeah. Sure, yeah.
Ariel @arielvalentin (ATX, USA) 00:48:00 As a… Yeah, kiddo's gonna… But also, Schwan, Wendy, if you want to stick around. I wanted to ask, Folks about, how we would want to try to handle different implementations of the SDK at some point.
Because I'm very keen on trying Raptors out.
To see if we can… Deal with the concurrency problems?
By avoiding having multiple threads, For each of the batch processors?
And, The other thing that's, you know, a little tough is sort of, like, the G… the protobuf maintenance and protobuf upgrades.
We really need a better process about that.
Oh, because we have RenovateBot now, which is allowed to… which, you know, we can schedule some jobs to do some updates, but I think we… Really wanna stay ahead.
We'll stay as close as we can to most recent changes of the proto… definitions to regenerate protobufs.
And, And that's the most, like, for us, that's the most expensive part of the SDK, is generating the protobus.
And the const… and I guess, you know, the second most expensive thing is the constant uses… use of mutexes.
We still have an outstanding bug where you can't use onEnding at the moment, because it… causes a deadlock, because we have non-regentrant, you know, mutexes.
So, if anybody's interested in working on that kind of stuff.
I think those would be great improvements for us in the SDK.
And I'm putting that out there into the ether.
To see if any of y'all have interest in that. I know Schwan has his hands tied right now, trying to get metrics stable.
Wendy Smoak 00:50:07 Your first question was, like… so this is a, like, there's a specification, and the stuff that's in OpenTelemetry Ruby is actually an implement… like, one implementation.
So you're asking about how we would go about having an alternate implementation of the SDK, or…
Ariel @arielvalentin (ATX, USA) 00:50:24 Well, specifically, it is an alternate implementation of the batch band processor and the… and the…
Wendy Smoak 00:50:32 I just want part of it, not, like.
Ariel @arielvalentin (ATX, USA) 00:50:33 Yeah, and the concurrent features… I don't know what they're called.
the periodic metric reader, I think, and the metric… Well, whatever it is that exports metrics to the metric exporter.
Those components heavily rely on mutexes.
Wendy Smoak 00:50:51 And…
Ariel @arielvalentin (ATX, USA) 00:50:52 Are running in a separate thread.
And so, I'm wondering… You know, the thread still requires… you know, all of this, adds overhead.
for… our main Ruby process that's running.
And so, it forces a situation where, when you're trying to capture or export telemetry.
The main process is competing With the batch band processor and the exporters.
To do things like take messages off of the… the array, Which is effectively the queue.
Build up that batch, and convert it to intermediate structs to send them off.
to a specific type of exporter, whether that's gRPC or Jaeger or Thrift.
Or, you know…
Wendy Smoak 00:51:47 So would we have to, like, extract that part of it, almost to be like this, I don't know, a separate gem, so that you could pick your implementation? Like…
Ariel @arielvalentin (ATX, USA) 00:51:54 That is what I'm wondering, is it may not need to be extracted as a separate gem, but we might have, like, a separate batch band processor for versions Ruby 4 and up.
Wendy Smoak 00:52:02 Okay.
Ariel @arielvalentin (ATX, USA) 00:52:02 So it's like, instead of using threads, instead of using a P thread.
Let's use Raptors instead, which don't have to compete for the gill in most cases.
And then allow the Ractor to implement the behavior of the batch band processor.
So, essentially, have a Raptor-based batch band processor, and then, it can send things off to the exporter.
Now the exporter… Right now, the slowest part of the export is generating protobufs.
So.
Wendy Smoak 00:52:37 So there's gotta be a way to configure it, or to, like, convince it, so when it loads up, it knows which… which one you want.
You know, it's behavior.
Ariel @arielvalentin (ATX, USA) 00:52:47 And that brings up another thing, but I'm gonna table that for a second.
The OTLP export, again, it's one of the slowest things, so I'm wondering if there's a native extension version of that that we can have.
that I know is not portable, that's not necessarily gonna be portable, but if there's some native extension version of that.
That could generate protobus for us, because one of the problems that we have… is that, at least where at GitHub, is that all of our… whenever we import the OTLP exporter.
we have to have it match with that specific version of Protobus that… The exporter can match, right?
So, in some of our cases, we have apps that cannot upgrade protobuffs because of… there's a bunch of different gems that include Protobuffs. And now you've got this transitive dependency, making it really hard For you to upgrade all those in place.
So, for example, if we chose, like, a… and I'm gonna, you know, this is an idea that I've been toying with.
But if we had the OTLP exporter use the Rust SDK exporter.
then we would take the Ruby objects that were in memory.
we'd have to grab the GIL and convert those Ruby objects into struct… into, Rust objects.
and pass them on to the Rust exporter, and then it can bundle a version of its binary, that includes its protobufs, and not have an impact on the Google proto-libraries that are required By the host application.
So essentially, it's essentially, you know, quarantining the protobuf usage in there.
As an example, right?
That might be a little bit risky, for whatever reason, because of, you know… Writing native extensions is a little bit hard.
But that's something that I had in, you know, had in mind for that as another kind of project. So I'm saying all these things to brainstorm stuff out, by the way.
Let's do all this.
I'm just kind of putting these out there as ideas.
Daniel Azuma 00:55:04 Oh, or even thinking about, things that are still kind of in the experimental, in the Ruby experimental phase, like Raptors, I think, is still… they're still not quite recommending it for production. Ruby Box?
Can… is… I… I have… I don't have a very clear understanding of the box, but it seems like it might.
Let us do funny things like, like, pull in multiple versions of a… of something like… Protobuff, or…
Ariel @arielvalentin (ATX, USA) 00:55:40 Not to my understanding.
My understanding… I don't see anything in Ruby… boxes that says it allows Bundler to load multiple versions of gems.
Daniel Azuma 00:55:51 I know it creates corp… like, an isolation for your monkey patches.
Ariel @arielvalentin (ATX, USA) 00:55:56 Similar to, sort of, like, I think it, like, boxed feels to me like it's a evolution of refinements.
Where you have, like, a scoped… Monkey patch or a scoped version of code that you've written.
And, I don't know the full extent of it, but, I think Ruby Rachter's in 4?
It's, it's more of, like, it's… It's ready for people to use?
Daniel Azuma 00:56:25 It's close.
Ariel @arielvalentin (ATX, USA) 00:56:27 I don't know… I know in… I know that in 3-4 it was an absolute, no, don't do that.
But I think it needs more wide-scale usage.
In order for us to know, like.
Like, if we could have an experimental version that uses reactors.
Daniel Azuma 00:56:45 And…
Ariel @arielvalentin (ATX, USA) 00:56:45 Folks can opt into using the Raptors if they wanted to, and they can report back.
hey, here's the problems that we're seeing. Or if we can somehow add… Add some sort of… A test bed, or a test suite.
that runs… Ractors to try to get some performance statistics, correctness.
Daniel Azuma 00:57:07 And so on.
Ariel @arielvalentin (ATX, USA) 00:57:07 and so forth.
So we can give feedback upstream.
Daniel Azuma 00:57:18 Have you played much with Raptors yet?
Ariel @arielvalentin (ATX, USA) 00:57:22 Nope, nope.
All I saw was Bayroot's comments about, you know, Ractors being unstable in 3-4.
Outside of that, I haven't really seen anything other than now it's included.
Daniel Azuma 00:57:32 it's… it's a lot better than it was in the 3X, in Ruby 3X. It's, the, I think the big… Yeah, the ports, change was very welcome. That simplified a lot of things. It's better with… it actually works with threads.
Ariel @arielvalentin (ATX, USA) 00:57:56 You can mix threads and Raptors now, or before, you really couldn't.
Daniel Azuma 00:58:00 So yeah, it is a lot better. I've been playing with it a little bit over the past few weeks. I'm still running into some bugs, though, so…
Ariel @arielvalentin (ATX, USA) 00:58:10 Oh, okay.
Daniel Azuma 00:58:12 so, I, I think… I'm… I'm hopeful that's… that the… That, yeah, people will start… actually start playing with it, and start reporting bugs, and over, you know, over this year, maybe it'll… maybe it'll stabilize to the point where we… We think that it might make sense.
Ariel @arielvalentin (ATX, USA) 00:58:40 Yup, so those are the things that were kind of on my mind, because, you know, we keep adding… with every one of the components of the SDK, we're adding another thread.
Which introduces more context switching, but there's… it's kind of like… There's not much that we can do about that.
Because we want to have logs and metrics and traces all running together.
But I don't want to do things that cause overhead for the main Ruby process that's running and trying to service the user's request.
You know, and a lot of what our stuff does is I.O. and serialization.
So it's like, take this… Take this value, convert it to something that could be streamed over the wire, and then… Send it over the wire.
But when we get these really huge… Batches that we have to run through.
You know, we don't want to… It, you know… introduce GC overhead, or introduce a lot of context switching, where it's like, oh, I'm gonna… I'm exporting… spans right now, but I'm gonna pause so I can export these metrics, and I'm gonna pause so I can write these logs, and then go back to giving the user their request.
And they're waiting, you know.
Wendy Smoak 00:59:50 Yeah. Whatever.
Ariel @arielvalentin (ATX, USA) 00:59:51 Whatever it is, 25 milliseconds for all this stuff to finish.
Daniel Azuma 00:59:54 That makes sense.
Wendy Smoak 00:59:55 As a… as a user, the impact of having this thing in the app is… has been kind of a… almost… I mean, part of it's just kind of a marketing thing, but in the… before, we would just write a log to a file, and the application developers didn't have to think about it, it would just go.
be there. And similarly with the metrics.
there was an agent running kind of outside, and it was UDP, and so you just kind of, like, say, stats D, do whatever, and you didn't… like, it didn't stay in the… now we've got… it's inside the box of the application. This gem is, like, in memory, doing stuff, affecting us.
And causing concerns, whether or not they are warranted. So, anything we can do to make it not… cause problems would be fabulous. Like, I'm… the metrics right now, like, I'm aware of, like, there's no limits on cardinality, so if someone does the wrong thing, they are gonna just blow out the memory, and… So, just, you know, just as a user, like, I'm being careful with it, but I also come to these meetings, and I kind of know what's going on, and I've read the code.
The rest of the people in my company are just kind of, like, looking at it like, what is this thing, and what is it gonna do, and so… The more, like, safety there is around it, that, would be great.
Ariel @arielvalentin (ATX, USA) 01:01:13 Yeah, so, you know, there's… there's that thing, and the other thing, now that you mention it, that I… there's two things that I just was reminded of hearing your voice and hearing you say this.
was we're re-implementing some of the metric logic that other SDKs are doing them, importing them and doing them purely in Ruby. So could those things be handled by an extension and taken out of… Out of band to… To relieve… to allow for some sort of parallelism to happen that would relieve… the user's process, and allow them to continue to work, so… Let's say we were computing a histogram or something like that. Can that be sent off to, like, a native extension?
And somehow, release the gill so that we're not… blocking the user? Like, can this be done in parallel?
Right? In some way, without it impacting the main user's workload.
So… that's something that I had in mind, and then the third thing was the… Ulta configuration thing.
where this SDK configurator does not currently meet the spec's OTEL configuration.
Specifications, so we need… You know, help implementing that as well.
Daniel, you came back, and there's, like, a laundry list of things that need to get done, you know what I'm saying?
And we're not doing a great job of using issues to do project management, which is a whole other… Dang, like, we need a project manager out here.
But, you know, those are some of the compliance changes.
That, you know, we're really behind on.
So…
Wendy Smoak 01:03:08 Now, if we haven't chased you off, welcome back.
Daniel Azuma 01:03:13 Thanks, my dear.
Ariel @arielvalentin (ATX, USA) 01:03:17 And, you know, really, you know, with 3 minutes left in the hour, that's all I had to say about that.
There are a plethora of work items to do.
Wendy Smoak 01:03:32 Alright, back to corralling my AI minions!
Ariel @arielvalentin (ATX, USA) 01:03:35 Until no…
Daniel Azuma 01:03:36 It's Tuesday.
Ariel @arielvalentin (ATX, USA) 01:03:37 even.
Just let the agents do their thing, and let them spawn sub-agents who spawn sub-agents.
And then below.
Wendy Smoak 01:03:48 Thanks.
Ariel @arielvalentin (ATX, USA) 01:03:48 This is not what I meant.
Daniel Azuma 01:03:52 Even a lot of electricity.
Wendy Smoak 01:03:54 Yeah.
Daniel Azuma 01:03:57 Alright.
