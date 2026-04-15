SIG: .NET SIG
Date: 2026-04-14
Duration: 21 minutes
============================================================

## Zoom Recording Transcript

**Julius Koval** 02:13 Hi.
**Martin Costello** 02:16 Hey, Julius, how you doing?
**Alan West** 03:53 Hello, everybody.
**Martin Costello** 03:55 air.
**Alan West** 04:11 I assume we're just waiting to see if Raj will show up.
And he did.
**Rajkumar Rangaraj** 04:30 Hello, everyone.
**Alan West** 04:32 Here, hush.
**Rajkumar Rangaraj** 04:43 Martin, would you be able to drive it? Like, just running and coming back from the other meeting?
**Martin Costello** 04:48 Sure.
Let's see, so… this… the… issue… that you've already replied to, Raj, about self-diagnostics?
If anyone else… As an opinion on this. It was, I noticed while doing some load testing that all the self-diagnostic stuff is enabled.
And in the case where you're running a production in a container that you can't change, it feels a bit wasteful to me to have all this stuff running, watching for something that will never happen.
So I was proposing if… That could be a way to opt out of it.
So if anyone has any opinions on that…
**Rajkumar Rangaraj** 05:53 You are saying we are… that we are not changing the default behavior. You're saying we will have an opt-out flag.
**Martin Costello** 06:01 Yeah, that's what I'm proposing, because all of my production containers, I will never add the file to them once they're created. If I needed to do this, I would build a new container with the file in it. So it just seems a bit wasteful to have all of these threads… a thread running in the background looking for something, it'll never happen.
**Rajkumar Rangaraj** 06:20 It's reasonable, I believe, and instead of introducing a new contract, if we can try something on. We already have the environment variable for, Do I… I think we haven't… we have an environment variable or something related to this one. Probably we could utilize.
**Martin Costello** 06:39 Oh, do we? I didn't… I didn't realize there was, an environment.
**Rajkumar Rangaraj** 06:42 Yeah, I don't… I don't… I'm not sure, like we did here, or in the… application inside, so… but somewhere, like, if it is there, we can use the similar contract to Disable that.
Or in the file, read it for the first time and disable that, so it does not go through that. Instead of introducing a new property or anything, if we can keep the contract minimal, that should be good enough, yeah.
**Martin Costello** 07:10 Oh yeah, it wouldn't necessarily have to be programmatic in code, but yeah, if it was just, like, an environment variable, you could tell it to not bother.
Yeah. Because then I could just set that in, my app service config, and then it would just never do it.
I'll have a dig through the code, tomorrow to see if it's possible, if there's something already there, and if not, I'll propose something.
**Rajkumar Rangaraj** 07:38 Sure.
**Martin Costello** 07:42 I opened an issue the other day, this… it was just… I happened to notice while we were doing the last release that we had… we… the automation runs as two distinct Git identities.
So I was just wondering if there's a reason for that, or if it's just leftovers.
**Rajkumar Rangaraj** 08:05 Interesting.
**Alan West** 08:07 Probably not intentional.
**Martin Costello** 08:12 Okay, yeah, I didn't know if it was, like, something that happened during, like.
migration, or if there was, like, an intentional hidden reason I wasn't aware of. If it isn't intentional.
I'll do a PR to, like, unify it.
And then tidy that up.
There was an issue that Sujo opened last week.
I think, if I remember correctly, there was a… there's a comment somewhere in the code that talks about a bug.
But it wasn't… there wasn't an issue for it, so it's created an issue.
For this… I don't know how important it is for anyone to pick up, or if this is just, like, officially documenting it to sit on the backlog.
Okay, now let's go ahead and get another one. I mean, all the other issues are quite old.
What have we got on? Contrib? So… Alright.
**Rajkumar Rangaraj** 09:22 Before you move to Contriba, Martin. Like, there is a huge inflow in the number of PRs this week. Do you know if there are any reason or anything that we are seeing a Huge incoming.
change requests or PRs there.
**Martin Costello** 09:41 So, part of it is… I was doing some performance investigations and found a bunch of stuff.
**Rajkumar Rangaraj** 09:50 Okay.
**Martin Costello** 09:51 And then another chunk of it is… me and Pyotr have been independently using AI stuff to look at the code, and finding things that should maybe be fixed.
To, put it in vague terms.
**Rajkumar Rangaraj** 10:19 Thanks for that being Martin. Like, if, like, I know I was not very active this week, so if anything that needs my immediate attention, please let me know.
**Martin Costello** 10:31 I guess just check your notifications and look at what might be in there.
**Rajkumar Rangaraj** 10:37 Yep.
**Martin Costello** 10:41 So then, on contrary.
Yeah, as part of the… some changes I'll be doing are performance-related. I noticed that the process metrics are quite out of date, so I've just created a Help Wanted issue for someone to pick up and update those.
And… Someone opened an issue complaining that the Stack Exchange Redis uses a lot of memory.
But I'm not convinced there's an actual issue. I think it's just they're doing something that makes it use a lot of memory during one request, so it uses a lot of memory during that request.
Because they say it uses lots of memory, but then the repo they gave is doing 2 million operations in a single HTTP request.
So I think it's just buffering all of that.
Until it finishes, because they're all child activities of the parent ASP.NET Core activity.
So, I pointed that out to them.
And… They've not really come back with anything substanti… substantive more than… So, is it supposed to do that? Which I said, I think it is.
So I don't know if anyone's got any more insight onto that one, but I don't think… I don't… based on what they've already said, I don't think it's an actual issue.
And then… there's this one… I think… I think this one's for you, Raj, because it's Geneva-related.
**Rajkumar Rangaraj** 12:29 I'll take a look at it.
**Martin Costello** 12:33 So that's all the issues since last week.
Actually, there wasn't a meeting at all last week, was there? So we should probably go a bit… see what there was last week as well.
I noticed that… The schema… we haven't put the schema URL onto everything in Contrib.
So, I've created a tracking issue for everything that's missing the schema URLs, and I'm slowly going through them.
And adding stuff. There's been a bit of refactoring I've done to make it easier to do that. I'll put how I wanted on this, because people can pick parts of it up.
If they wish.
while I was doing that, I also noticed that there was a to-do in the code.
that said that we should add tags onto the AWS meters.
But, I created an issue to track that, but then it was trivial to do while I was doing something else, so that's got a PR open for it already.
And that's all the issues.
Since 2 weeks.
That's still open.
PRs, there's… 13 PRs open that aren't in draft at the moment.
So, some of them are Julius's related to the log bridge stuff.
I think that one's been reviewed. I can't remember why we haven't merged it yet.
There's another one of Julius's for key value lists.
**Julius Koval** 14:16 Yeah, I, I actually marked it as ready for review, because it was… Draft previously.
**Martin Costello** 14:23 Okay Anything specific you want to mention about that, other than just we should take a look at it?
**Julius Koval** 14:31 I don't think so.
**Martin Costello** 14:34 Okay.
I… there was a PR back in, I think it was November, that added support for GZIP, that you had some concerns with Raj, and then it got staled away. I've brought that original work back in a new PR, and I think I've addressed your comments.
So if you want to take a look at that when you have the time.
Then… These couple… So these three, these are just minor performance optimizations.
That I think I've made, so they're ready for a review.
I don't know why, POS hasn't merged this yet, I've looked at it, and this is to do with spec compliance.
for Trace State, And then… there's two PRs.
That I reviewed already about, hardening some stuff.
That's come up from some reviews.
And then in CompTrib, there's a ton of PRs open, ready for review.
Most of them by me.
I don't think there's any that need… I think the only one I will call out is the oldest one.
In .NET 11, ASP.NET Core has made some changes to set tags relate to the HTTP semantic conventions by default.
So, as part of the .NET 11 work.
We can skip a bunch of work.
But then I also realized that in .NET 10, they did some of that work as well. Also.
But you have to opt into it.
Instead of opt out.
So, I've done a PR that… makes the instrumentation aware of if you've opted in to ASPNet, or setting things automatically, so if you opt in, we can skip work knowing they'll have already done it.
So that should give some performance improvements as well, so that would be a good one to get some, reviews on sooner rather than later.
Other than that, I don't think… If there's any PRs or issues.
That need any further discussion, unless anyone wants to talk about any of them specifically.
Cool, so… The only thing on the agenda… Unless someone's added something. Come on, it's refreshes.
Oh, is… Some point soon, we need to do a new release.
For all the various changes that have been happening this week.
But I don't know when we want to draw a line in the sand and cut that release.
But otherwise, that's… that's it. I wanted to say about that.
**Alan West** 18:01 is the main thing in this release. The, Http for vulnerability.
**Martin Costello** 18:10 So… Point 2 that's already shipped fixes one issue.
And then 0.3 will fix some more issues.
But yeah, there's, like… this… 3… Vulnerabilities in the queue to be published.
Plus, there's some other PRs that haven't been merged that I don't know if they're going to get vulnerabilities drafted.
**Alan West** 18:45 Sorry, say that again, there's more PRs that may be merged?
**Martin Costello** 18:49 So, there's more… there's several PRs that have already been merged or are open that mention security in the descriptions.
But there are fewer… GitHub advisories that have been created that haven't been published yet.
So I don't know if there's an intention to have a one-to-one or not.
**Alan West** 19:13 Hmm.
**Rajkumar Rangaraj** 19:13 No, it's not… I don't think the CV is always a mandate thing.
The things, whichever we have fixed, are the small code based bugs, not a real GP that's impacting the product. If that is.
**Martin Costello** 19:29 Oh, yeah.
**Rajkumar Rangaraj** 19:29 Yeah.
**Martin Costello** 19:30 I just meant that I don't know if they're intending to create some and just haven't done so yet.
**Rajkumar Rangaraj** 19:36 Yeah, okay.
I think I'm supportive in releasing the… as there are some, like, security enhancement, it's always good to release it. This is the way it's going to be for another few months, I believe.
**Martin Costello** 19:51 Oh, sure, it's just, I know there's PRs that aren't yet merged.
So, it would probably be best to bundle them all together, rather than have, like, a release, and then a release tomorrow, and then release the day after, and then a release the day after.
If we, if we know they're coming.
**Rajkumar Rangaraj** 20:11 Yep.
**Martin Costello** 20:14 Plus, as well, all the fixes need to be rolled up into the, Instrumentation and shipped stable before they get published.
The advisories get published, those.
Anything else anyone wants to… add to the AOB at the end of the agenda?
**Alan West** 20:49 Nope.
**Martin Costello** 20:57 Cool. Well, that was a… that was a swift meeting then.
Cool, that's… Called that that for today, then.
See you all next time.
**Rajkumar Rangaraj** 21:08 Thank you.
**Alan West** 21:08 later. Thanks.
**Martin Costello** 21:10 Bye.
**Julius Koval** 21:10 Thanks, mate.
