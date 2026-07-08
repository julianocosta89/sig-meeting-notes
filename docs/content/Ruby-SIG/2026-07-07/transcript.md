SIG: Ruby SIG
Date: 2026-07-07
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**hramadan** 02:09 Hi, Kayla.
**kreopelle** 02:11 Bye, Hannah How you doing?
No, we don't have Matt today. Let's see if there's anybody else on the channel.
Not right now.
But we're we're 3 min past, so we can go ahead and get started.
**hramadan** 02:53 Sounds good.
**kreopelle** 02:55 And.
Let's see.
Go to Ruby Sig. Great. We already have notes, which is kind of exciting. Oh, look at! Are you anonymous frog?
**hramadan** 03:10 Oh, I am frog.
**kreopelle** 03:12 I don't know.
**hramadan** 03:13 You are anonymous ferret.
**kreopelle** 03:15 Lovely. Sweet. Okay. Well, I was unable to attend the spec SIG today.
Let's move a couple of things around.
Let's see, these are all I'm telling 4 things.
And then Contribute things.
and What else? And then questions.
Yeah, thank you. Can you add that? And I'll pop up the spec. Sig.
Okay, so let's see what they talk about today.
Cross-language usage guidance for instrumentation library authors. That sounds kind of interesting.
Attribute value depth limit.
Hmm, interesting. Okay, security. Sig needs some help.
Client SIGs could use cross SIG management.
and then a C plus plus SDK wrapper.
Interesting. Okay, I feel like there's a lot of good details in here, but since… I believe nobody here attended this PECSIG this morning.
I think I'll postpone talking about those, and we can just kind of Explore on our own.
Okay, so 1st topic, being able to deprecate or turn off Otel Ruby is nearly impossible. The registry now contains links to the Ruby docs. Okay, these are different points.
And there we go. Okay, so I think James has brought this up before.
And we I think we need to track down what he was saying about this, but… So maybe we follow up.
in issues or channel about this, I'm pretty sure.
the there was an issue that he opened about it.
**hramadan** 06:33 I'm not really sure.
What? What is this? This link? Are we looking at the 1st bullet? Why are you looking at?
**kreopelle** 06:41 Yeah, I'm looking at the 1st bullet point, and I think that might just be the wrong link.
**hramadan** 06:49 Right, okay, yeah, I wasn't.
**kreopelle** 06:50 I thought.
**hramadan** 06:51 First.
2.
**kreopelle** 06:53 Age I'm So.
Yeah, I'm not.
link.
Seems… I'll forward the question.
**hramadan** 07:10 Mmhm.
**kreopelle** 07:14 Okay, so we'll check in with him in the.
somewhere after that.
I guess I can look for turn off. Is there anything in here? Nope.
I assume that's where it would be. I guess we can look at pull requests, too.
I don't see anything in here, either. Okay.
Well, hopefully, he can let us know.
Okay. OTel registry via this PR now contains links to the RubyDocs pages, which is what the GitHub I.O. page was being used for, with the links, descriptions, etc. being synced after each gem release.
The preview of the updated registry can be seen here. This is a really cool update. And James, if you're listening to this, I'm really happy that you made it.
The… Yeah, the registry deploy view looks really nice.
Oh, nice. And now you can, like, go to the documentation and get straight to the Ruby… or I guess this is still using the… Github I/O link. Is that maybe what he was talking about?
Hmm, okay.
And then the package details goes to the RubyGems, and so you can find, like, source code. Those other improvements that he made there are… even more helpful.
And then the repository.
jumps into the specific one for that gem, that directory.
So, I think in this pull request… It's probably a request for more feedback. So if any of the folks here or watching, or Hannah, you being here today, are interested in taking a look. It's a… it looks like it's a really big PR, but it's mostly because the registry page has been updated, and I think the meet is mostly… hear about how the script has changed.
Let's see. Okay, so the next one.
This pull request… doc fixes. It's been merged.
Oh yeah, this was important, I think, for this registry because it was the only area where some things were broken.
Hopefully that takes care of the issues with some of the syncing.
Okay, when we look at this one, again, I see you also add merged.
here. Is this the same one? 2424 and 2210. This is also okay.
They're just kind of similar.
GRPC and Gruff.
And this one was, oh, SDK specific changes. Nice.
And then this one.
is limiting gem and tests to MRI.
So in contrib limits the gems to only be used on MRI.
Or CRuby, since they require native C code, and no Java replacements are available as drop-ins. So it looks like that's for gRPC, Gruff, and LMDB.
And… Interesting.
That's kind of just adding some extra protections.
for Jay Ruby here.
All right. So yeah, so folks, Take a look at this.
We're kind of cruising through on the pre-made questions. I guess we'll go through all that and then if there's anything else we can… Talk about that after.
Okay, so is it possible to manually release a patch after the above PRs for… OTLP exporters, Zipkin exporter, API and SDK, in addition to Gruff and gRPC and Contrib.
Yes, I think that should be fine. I'll commit to that.
I think Gruff has a release that was opened through the weekly release, but since it needs another change, we can fix that, too.
One thing I didn't notice, though… Okay, since it's chore for the prefix.
We just need to do a bit of extra effort.
So I'll,
**hramadan** 12:52 Mmm.
**kreopelle** 12:55 That's just more of a mental note for myself to make sure that I take on that extra effort.
But yes, I think I think that should be very doable.
And then, do we need to add a redirect from GitHub pages to the registry, or don't need to bother given it hasn't been maintained, etc?
What do you think, Hannah?
Do you know what the context is here?
**hramadan** 13:25 Not exactly, I mean, like… Actually, sorry, the question was, do we need to add a redirect?
**kreopelle** 13:33 Yeah. Do we need to add a redirect from GitHub pages to the OTEL registry? So GitHub pages being this.
Let's see if I can show you.
We used to have them in.
Here we go.
Something broke about their deployment, but basically.
there's this page, this gem reference documentation that is like hosted by Github. And you can have one of those for any repo.
But it's out of date.
And I think it's been broken for a while.
And you can see, like, how few gems are on here, kind of compared to all of the gems that we… Release. Yeah.
**hramadan** 14:20 Yeah, yeah, makes sense better.
**kreopelle** 14:22 So yeah, I think it makes sense for it to go.
A redirect?
could be helpful, but I think… Yeah.
I… I don't think it's needed, but I also am not, like, the maintainer of… documentation for this, so I think I would recommend reaching out to, like, Challenge.
and I'm sure that's not his real name, and just his Github handle or Severin.
I think that's his.
Because, yeah, since they're maintaining documentation, I would rather know what their preference was for these kinds of cases, just in case they have other testing and stuff that would fail if we just removed it without a redirect.
**hramadan** 15:28 Yeah, I like that idea.
**kreopelle** 15:47 Okay.
Cool. I think that takes care of those things. And.
**hramadan** 15:55 Goodbye.
**kreopelle** 15:56 Record time. Hannah, is there anything you wanted to look at today?
**hramadan** 16:03 There was nothing in particular for me. I guess we could just look at If you want to do… Issues and PRs, if you want?
**kreopelle** 16:11 Yeah, yeah, we can.
Peek in on those.
Okay, Prs.
We have the release.
**hramadan** 16:25 Sorry.
**kreopelle** 16:26 Devastating REL PR for this repo.
few different dependabots or renovates rather.
Oh, as an update, I tried to get semantic conventions 141.1 released and failed. And so I think we just need to move forward to 142.0 and for future releases try to use the auto release functionality that James proposed to help us not miss any other releases. I think the other thing we could do too is double check the… the script that's generate generating the Renovat.
Pull request to make sure it makes one for every… patch version.
Even if there's like a new release that comes out that's like, you know, a minor release or something like that.
I don't know how to do that in Renovate.
But I imagine I would be surprised if there wasn't a way to do that.
What do you think of that approach?
Does that seem.
**hramadan** 17:45 Yeah, yeah.
I think that's reasonable.
**kreopelle** 17:48 Okay.
Actually, would you mind summarizing that, Hannah? Yeah.
Thanks.
What else we got?
We can be.
Do not report disabled instrumentations as failures.
Hmm. Oh, yeah, that's a good idea.
**hramadan** 18:18 What is that?
**kreopelle** 18:19 So I think the, the request is, so right now, whenever the dependency.
**hramadan** 18:25 Yeah, okay.
**kreopelle** 18:25 fails. It just says it failed to install.
**hramadan** 18:29 That's so reasonable.
**kreopelle** 18:31 Yeah. Yeah. So I think this is really.
**hramadan** 18:33 So good.
**kreopelle** 18:35 Yep. Yep.
Yeah. Awesome. Yeah. And it's already been approved. This is beautiful. I look forward to approving this.
What else we got?
Read me badges. Set up Ruby.
I know the declarative config conversation has been behind.
This is kind of interesting.
Why is that open?
**hramadan** 19:09 Two different.
**kreopelle** 19:11 I thought that got merged.
1 41 1 to 1 42.
Okay, that looks reasonable.
Hmm… What do you seek in the changelog?
Oh, auto load. Oh, that's right.
Glad we saw that. So that was Bart's update to.
**hramadan** 19:44 Okay.
**kreopelle** 19:45 the way that loading works, and that needs to be included. So I'm going to close this release PR, actually.
Okay, so we need to merge that other PR first.
Could you add that note, too?
**hramadan** 20:13 Yeah. Do we want to wait on that? Or we could.
**kreopelle** 20:16 I guess we could just merge them now, right? Great point.
Knock it out.
So… I suppose we should update the branch.
I don't think it will change too too much.
Oh, or maybe because it's renovate, I shouldn't have updated the branch. Shoot.
Okay, well.
It has happened.
I guess we'll just see… Right.
Keep an eye on that.
Okay, configure how to… Okay.
Then what else we got going on.
naming, suppression, simcomp, release, declarative, config.
simple curve.
Okay, I think everything else is pretty.
familiar.
And the issues we do have… A new one, or new to me.
Hmm. Okay.
Interesting.
Okay, well, we'll take a look at that.
Did Lee get back on this one? He did not. Okay, cool.
And then that's one's proposal.
All right, I think that's all for Otel Ruby Core right now.
Let's look at contrib.
Alright. So we have the Gruff instrumentation, which I think I might close this one.
Possibly. I'll just leave it as is for right now until I can investigate.
whether it will include the Grp or the other documentation changes that James was interested in.
And then…
**hramadan** 23:27 Documentation.
**kreopelle** 23:29 It's been interesting.
Hmm.
Okay, I think this is this seems helpful, but we might need it moved a little bit, because that does not seem quite.
**hramadan** 24:06 Right spot.
**kreopelle** 24:07 Right, yeah.
**hramadan** 24:08 Good, yeah.
**kreopelle** 24:09 But,
**hramadan** 24:11 I can take a look at that.
**kreopelle** 24:13 Okay, that would be great. Thank you, Han.
**hramadan** 24:15 Okay.
**kreopelle** 24:17 We have a whole bunch of Renovate.
PRs.
some of those other prs that Thompson Tomo called out. Oh, Hannah, could you actually take a look at this Pr. Today, too.
It's just a follow up from Ariel's emeritus switch to remove him from the code owner's file too.
**hramadan** 24:43 Yeah, did we just get an approval on that.
**kreopelle** 24:45 Yeah, just need an approval.
Okay, I think everything else has kind of been around for a minute. Postgres affected rows. I know we talked about this in a recent meeting.
Okay, you're good with it.
Sean had a comment. All right, I want to get back to this one this week.
because I think we were pretty good with moving forward on that.
All right, here's a new bug.
Hmm.
This is a problem.
It's a helpful reproduction.
Okay.
Well, we should take a look at this one, too.
**hramadan** 25:56 What did I saw? James had some.
**kreopelle** 26:01 Okay. It was, yeah, adding labels.
Yeah, this will be an interesting one to reproduce.
And then did I comment on this one? Or did I just think about it? Okay.
Awesome. All right. This is very helpful.
So yeah, I can kind of check this out a little more.
But I'm not sure like where exactly the source of this is, or even maybe, Hannah, if you've come across this, too, with working on the database instrumentation.
**hramadan** 26:43 Yeah, I've just not seen the lone semicolon situation.
**kreopelle** 26:47 That's pretty pretty wild. Not ideal.
**hramadan** 26:51 Why not? So… Okay, so we can't reproduce.
**kreopelle** 26:58 Yeah. So I was just trying to get a little more info on his environment to see if we could reproduce it in a different way.
**hramadan** 27:03 And it'll be…
**kreopelle** 27:05 Because I think reproduction is going to be important as a next step.
The configuration is really helpful, but Yeah, if we can't reproduce it, I might ask him for just a little more information or Maybe if you can write a test or something like that, that would help us.
My initial curiosity is whether it has something to do with the way that we're parsing the statements for Postgres.
And if there's a way that the regex might just, like, short-circuit and only return a semicolon, or… clear everything else out.
**hramadan** 27:52 It's I mean, that parsing regex shows stuff that's been around for a very long time. This is like an odd.
**kreopelle** 27:58 Right, yeah.
**hramadan** 28:00 across.
**kreopelle** 28:03 Yeah, so we'll see. We'll take a look.
Maybe we can bring.
Our favorite bug sleuth from our team.
Cool! Okay, and then in the instrumentation, auto instrumentation, so small update on that. I think we have the secrets we need now to release, so I just need to check in with Schwan about… whatever it is that he wants to do with the release itself. It looks like we have a few renovate… Pull requests to address.
But we're getting really close. I did also hear another interesting use for a repository like this, like Java's version of this repository not only has the auto instrumentation library inside of it. It also has specific instrumentation libraries that the maintainers have chosen to maintain. So whereas like contrib is kind of more intended to be like a community focused endeavor.
for key libraries and their ecosystem.
They've decided that they want, like.
a stronger level of support for them, so an equivalent for us would probably be, like, Rails, or… you know, net HTTP or something like that.
that we want the entire community to make sure that there's like a different level of maintenance for I don't know if we're at that point yet, but it could be something we could explore in the future, since we now have this third repository to work with.
All right. Cool.
I think that's all for me, outside of just, you know, diving in and continuing to review things. Fortunately, my… Other projects are quiet for the moment, so I'm hoping to do a lot of hotel this week.
**hramadan** 30:18 I'm.
**kreopelle** 30:19 Anna, is there anything else you wanted to go over or?
You know, surface…
**hramadan** 30:24 Well, we'll take the extra time and look at some of those open PRs and see if we can.
get previews and move on.
**kreopelle** 30:32 Fantastic. All right. Well, with that, we will see you and anyone else who's on the internet next week.
**hramadan** 30:40 All right. Thank you.
**kreopelle** 30:42 Take care. Bye.
I.
