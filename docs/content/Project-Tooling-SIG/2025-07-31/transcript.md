SIG: Project Tooling SIG
Date: 2025-07-31
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/5JXP-2RCrwqDVpkjeQ3hgwrkkEFLhYnr6J8OwJ8uOhzD2mrMYfG5SyrxqANkMQb1.6V7onafEZ0eMcsyG
============================================================

## Zoom Recording Transcript

**Jacob Aronoff** 02:07 Hey! How are you?
**Trask Stalnaker** 02:09 Hey, Jacob, being good, how about you?
**Jacob Aronoff** 02:13 Doing doing well overall things considered.
It is.
I'm on a pseudo vacation on a Martha's Vineyard. I'm still working, but I'm just
on the vineyard. It's very nice here.
**Trask Stalnaker** 02:27 Nice.
**Jacob Aronoff** 02:28 Well, it's kind of a gross day today, but it's been very nice.
How about yourself?
**Trask Stalnaker** 02:36 Yeah, in and out of
small lot of little small vacations day here, day there. Couple of days I'll miss next. I'll be out next Thursday, and
not quite sure what we're I think we've lost a little momentum in this.
**Jacob Aronoff** 02:58 Just.
**Trask Stalnaker** 02:58 From summer, being summer.
**Jacob Aronoff** 03:01 Yeah, I think summer. That's just how summers are, you know, especially because, like all the Europeans that we work with are all out having fun.
**Trask Stalnaker** 03:09 But Austin is here!
**Jacob Aronoff** 03:11 I am for one.
We've all converged.
**Austin Parker** 03:16 Hello!
**Trask Stalnaker** 03:18 Hey!
**Austin Parker** 03:19 What's new?
**Trask Stalnaker** 03:22 Yeah, we should.
Oh,
**Jacob Aronoff** 03:27 I've just been dealing with 3
consecutive botched collector releases. I think.
**Trask Stalnaker** 03:37 Sorry about that.
**Jacob Aronoff** 03:40 I don't think no, I don't think it's your fault. This is a it's a Prometheus problem, because it's always a Prometheus problem.
**Trask Stalnaker** 03:47 Some of them have been my thought.
**Jacob Aronoff** 03:51 These are not being permissions, things these are like, they release something, and then we.
**Trask Stalnaker** 03:56 You're downstream, I see. Yes, yes, I've I've caused problems with the release collector release process itself.
**Jacob Aronoff** 04:06 Yeah, that that's but those those are fixed easily.
**Trask Stalnaker** 04:09 But.
**Jacob Aronoff** 04:10 Trying to get them to like fix a upstream Prometheus problem. That's then causing a problem in Prometheus. Go Prometheus Hotel go, which then causes a problem in Collector Core which then causes a problem in contrib like
a very horrible chain.
**Trask Stalnaker** 04:26 Gotcha!
Why can't? Oh, I know why I can't share my screen.
Let's fix this.
**Austin Parker** 04:36 I need to get somewhat. I need. We need to get the cloudflare.
I need to give the cloudflare stuff to someone.
**Trask Stalnaker** 04:48 Tell me what the Cloud buyer stuff is.
**Austin Parker** 04:50 We have a cloud. We have like an hotel cloud account now, and I am on it, and I need to.
Add other people to it so that people can do stuff with it, cause I am.
You don't have time to do stuff with it.
**Jacob Aronoff** 05:17 I think I could have what what is needed.
**Austin Parker** 05:20 I don't know. I know Adriel wanted it for something.
**Jacob Aronoff** 05:25 Should we ping him and ask him if he's
**Trask Stalnaker** 05:29 He just, and he'll be here in a minute.
**Austin Parker** 05:32 Okay. Well, we can wait for him to get here. But also I just like I think we should
make sure there's a
let me log in
**Trask Stalnaker** 05:47 Are all the credits in one password.
**Austin Parker** 05:55 They sent it. My! I I already had a cloudflare account, so it was sent to my
thing. I think I need to make a shared. I think we should make a shared account, I guess.
Make sure we make an admin ad.
Okay, we can do that.
I have an ipad here now as like an extra monitor, my laptop. But like sometimes I forget, it's an extra set to extra monitor, not to like
whatever mode. And so I'll go over and I'll try to scroll something, and I can't.
It's setting okay, manage account members.
Add.
oh, I can't do that.
I can access the folks out except for membership management and billing.
Awesome.
**Trask Stalnaker** 07:21 Is this like a open source account.
**Austin Parker** 07:23 It's yeah. Let me.
It's it's like.
yeah, is open telemetry. So we we have cloudflare now. An open telemetry organ. Cloudflare manage with a Cncf. But I can't add new users to it, so I
need to.
**Trask Stalnaker** 07:51 Service desk at.
**Austin Parker** 07:53 I guess service desk. Yeah.
**Trask Stalnaker** 08:03 Okay. So it is managed by the Cncf.
**Austin Parker** 08:06 Yes, this is a problem.
**Antoine Toulme** 08:40 Hello!
**Trask Stalnaker** 08:41 Yeah, I'm fine.
2 times in one day.
**Antoine Toulme** 08:47 I'm trying to pay attention to stuff.
plus I mean, Jacob is we, I mean, is the operator seek. So Jacob's here. We can discuss, we can discuss operator stuff instead.
**Jacob Aronoff** 08:57 We can hijack the whole meeting. That sounds good. Everybody loves that.
Do not invite me to meetings.
**Austin Parker** 09:05 Alright. Well, I've emailed or I've responded to the service desk ticket so
hopefully they'll get that sorted. And then we can add admin, add, and then we can go from there.
But if we need something now, I guess
oh, no, I can't. I mean if someone, if someone needs something now, and tells me what it is.
Can do it, but we should probably wait until
we can add other people to it.
**Adriel Perkins** 09:39 Do you have any like limitations on what services we can use.
**Austin Parker** 09:48 I. Is there a way to t.
**Adriel Perkins** 09:54 Yep, I don't know but I'm curious like the one service I'm curious about is.
**Austin Parker** 10:01 I'm pretty sure.
**Adriel Perkins** 10:02 This is the under the 0 trust stuff.
**Austin Parker** 10:05 Yeah. So looking at 0, trust.
we don't have permissions to continue.
Okay? Well, what? Specifically under 0 trust, do you need.
**Adriel Perkins** 10:21 Tunnels.
**Austin Parker** 10:24 Tunnels.
**Adriel Perkins** 10:26 Think it's been a while since I've looked at it. But that would be for.
**Austin Parker** 10:34 I see I thought you needed waf.
**Adriel Perkins** 10:40 Ish, but tunnels, tunnels, for sure.
I think so. When you do a tunnel I'm pretty sure it comes with a laugh in front of it, and you get to configure all that stuff how you how you like.
But but what a what a tunnel is! It's opening it into their edge network instead of publicizing it over over the world. And so everything goes to their edge network first, st which allows you to, you know, get
all the security things without opening your internal infrastructure.
**Austin Parker** 11:20 Okay. I also sent that one.
We will see.
The things I see on here right now is we have domain, log analytics, waf, turnstile load balancing. IP compute, secret store.
R, r, 2
analytics engine.
**Adriel Perkins** 11:54 So is the is the domain getting transferred over or pointed to their name service?
**Austin Parker** 11:59 I think at some point we'll do that like I just don't know when it's gonna be a great time.
**Adriel Perkins** 12:06 Got it.
For for any projects that would require a domain name
in the interim, while that gets sorted out for transferring things, do we have like a
another one that we would be able to use? Or do we just need to wait for that?
**Austin Parker** 12:32 I mean, we still we have like
Oh, gosh! I mean, we're still
I mean we right now. Dns is handled through like I don't wanna
I don't really want to do the migration until we have other people added to this, because right now Dns is handled through our
atlify account. And there are like multiple people that have access to that. So like I don't we? We should make sure that we've
like. I think we'll need to like, plan this and coordinate this with several people. But
functionally, I'm pretty sure netlify is also just using cloudflare. So.
I don't think it'll be that big of a deal to transfer.
**Adriel Perkins** 13:38 Sure, cool.
**Austin Parker** 13:41 But yeah, okay, that's where we are with cloudflare.
**Adriel Perkins** 13:48 Do you have the ability to in in medify, just point specific records outside of
like, do you have the ability to manage certain records like for subdomains
cause we could just create a record for
and then apply, prior to the migration, to point to something on cloudflares and for one specific sub domain.
**Austin Parker** 14:10 Oh, yeah, but don't. But you have to have a domain. I thought you had to have a domain in Cloudflare. You have to like verify the domain, or something to let it to create.
**Adriel Perkins** 14:18 So, yeah.
**Austin Parker** 14:19 No, actually you might. I mean, I can.
**Adriel Perkins** 14:27 It's been a while.
**Austin Parker** 14:28 No, it'll let me create a it'll let me create a
I think it depends like, apparently, I can just create a worker.
**Adriel Perkins** 14:37 Chan.
I feel like I can. I I pointed most.
I don't know. It's been so while so long.
you know, but many days since then
I'll I'll look at my setup and I'll I'll come back with some tactical information that questions.
**Austin Parker** 14:58 Yeah,
but we have it. We just, you know, once we get the, we'll figure out this login stuff and then get people set up with it, and then
we can do more.
So.
**Trask Stalnaker** 15:26 Oh, maybe I was thinking to go through
the backlog. I think some of these might be done, and some of them, I'm not really sure
are really under project. Infra sig like enabling zoom summaries.
do we really? Do we think that's a project? Infra.
**Austin Parker** 15:59 I mean, it'd be project info to actually accomplish, and it would be someone else to side.
**Trask Stalnaker** 16:08 I see. So it's yeah, should we? That makes sense? Yeah, cause it's still under deciding.
**Austin Parker** 16:14 Yeah, I mean, I think we're still.
Have you looked at a recent Gc summary.
**Trask Stalnaker** 16:24 No.
**Austin Parker** 16:25 I haven't, either. I looked a while back, and it wasn't super impressive.
**Trask Stalnaker** 16:32 Yeah, I'm gonna remove project infra, like.
so that it doesn't show up sort of for us until it's actually.
**Austin Parker** 16:41 Inside it.
**Trask Stalnaker** 16:50 See if we can clean up the backlog a little bit. 3rd party note taking zoom bot policy.
I think this is gonna get closed by Dan Dialez,
2681, 20, related to 2681. Okay.
But in either case I don't.
Do you think this one is project infra Austin.
**Austin Parker** 17:24 No, this one isn't. This is definitely policy.
**Trask Stalnaker** 17:41 To one time tokens for.
but.
**Austin Parker** 17:53 Oh, this is this is definitely us.
**Trask Stalnaker** 18:01 So what? Adrian, maybe you can explain
how this like, how is this different from
So we're using for this like auto update
kind of these fix commands that update a pr,
I kind of jumped through a bunch of hoops to do this in a way, I think is secure over here.
**Adriel Perkins** 18:40 Yeah.
it's the. It's the removal of the private key. So on. I'm I'm amazed that I can see this because I am driving on the phone. But my phone is right in front of me. So I'm being very safe and I've come to a stop. But the app Id and the private key. The private key is essentially long lived right, and you have to provide it to the org for your your bot through. You know Github secrets right with Octo. Sds, what you you do? That bot
does that work for you so that you never have to have the key. Instead, you define the permissions on your identity as a codified file. It's a yaml file that's at the root of the repo.
I'm sorry. It's not the word of the repo. It's in the chain guard, chain guard, folder inside of Github.
and what your workflow does, and I have an example. I I just
Their examples are pretty good.
Excuse me, but what it does is like, you'll say, Hey, I want, read or write, or whatever, and then you allow, of course, just like you would do as a Github bot. You say this Octo. Sds spot is the one who's allowed to bypass certain permissions. And when you go and get your token, it's, you know, confirm real just like a github
So just like a regular github app, except you just don't need the private key, and you can exactly define as code what permissions are needed. You can even centralize that, and like a dot Github repository at the or root of the organization, or you can have it spread out in each repository and let them let them own that separately. But it's a it's a pretty nice and more secure workflow for ephemeral tokens, reducing the need for long live secrets.
**Trask Stalnaker** 20:27 Does this require? Trusting the Octo Sts.
**Adriel Perkins** 20:32 Yes.
**Trask Stalnaker** 20:33 Okay,
**Adriel Perkins** 20:36 Which is built by chain guard for what it's worth.
**Trask Stalnaker** 20:41 Okay.
Surprise.
**Adriel Perkins** 20:44 We we I've used it like really large enterprises, really, successfully. And we use it for everything, almost everything internally.
**Austin Parker** 20:54 I think, as I think this would be fine.
this like cause we could also, if we ever.
That's just.
**Adriel Perkins** 21:01 Codes open so.
**Austin Parker** 21:02 Yeah.
**Adriel Perkins** 21:03 Post office. Yes, you can totally do that.
**Austin Parker** 21:06 Let's play. Pretend that I will never finish that fucking bot, and just assume that like, let's just use this.
I am not going to have my just
practically, I am not gonna have time for hotel stuff that is not directly connected to graduation for at least like another 6 months. So.
**Trask Stalnaker** 21:34 Does this help with any of the other stuff that your bot was doing?
**Austin Parker** 21:40 No, this would help with this. The only thing this would help with is the like being able to replace all of the pats with
like access tokens with one time tokens. So we should do this anyway, like the in terms of the on call rotation stuff. We'll just need to
to have people deal with that.
**Trask Stalnaker** 22:04 Yeah.
Yeah, that's not a problem. The twist. Yes. Okay.
just trying to get a sense of how popular it is. We're
giving out that level of trust.
**Adriel Perkins** 22:26 If you want to see an example of it being used. Actually, that, like Mcp, at the labs uses it.
I think I used it there.
Yeah, I did, because it's it's how we commit our releases automatically without having any type of token to to do that.
So if you go to oops.
If you go to github.com slash Liatrio dash lobs.
**Trask Stalnaker** 23:02 Oh, that's okay. I I can. I mean, it's I think,
make.
**Adriel Perkins** 23:12 Makes sense enough.
**Trask Stalnaker** 23:13 To me now, yeah.
**Adriel Perkins** 23:14 Cool.
**Trask Stalnaker** 23:18 Yeah, I just went. I was.
I didn't realize it was like an app
that we had to trust separately, I thought, and I couldn't figure out how how you would avoid needing to trust something.
In order to get those one time tokens.
Cool?
Yeah. Maybe if you could just
may, if you feel comfortable writing in just our slack channel, sort of a brief defense of a trusting Octo Sts, just so that we can have. I don't know.
unless, Austin, you're.
**Austin Parker** 24:05 I'm honest. I I don't. I don't have a problem with it.
**Trask Stalnaker** 24:09 Okay, then let's bless this. I I.
**Austin Parker** 24:15 Like nothing. Yeah, nothing is going to.
Nothing's going anywhere with it. It's it's just a proxy between
**Trask Stalnaker** 24:30 Yeah. But
yeah, we're just intermediating token exchange between Github. And it's something that Github should just like. It's something. Honestly, that Github should just do.
Yeah, yeah.
I mean it. It is giving our tokens to a 3rd party, essentially, or or ability to generate tokens for our stuff to them.
**Austin Parker** 24:51 Right, but like any github app, you install like you're giving the ability to that 3rd party to generate a token right like if you set up? O off for it.
**Trask Stalnaker** 25:03 And I am concerned about every github app that we install that has.
**Austin Parker** 25:08 Sure I I trust the Chain Guard people, I mean, I trust, chain guard more than I trust. Like
my Claude code abilities.
**Trask Stalnaker** 25:20 Cool.
Yeah, yeah, this cool. I can take a look at that. Then see what that would take to
trial out.
**Adriel Perkins** 25:36 Cool. I'll when I get back
home to my computer about an hour I'll I'll ping you, too.
**Trask Stalnaker** 25:43 Okay, sounds good.
Add, existing lambda. Sig maintainers
don't understand
access. Now, it sounds like I'm just gonna close this
docker open source program requirements.
We can close this right.
**Austin Parker** 26:52 Yeah, I think, yeah, how did did they ever like finish with that.
**Trask Stalnaker** 26:57 Yeah. I saw the I saw the band, the badge.
**Austin Parker** 27:01 Badge and everything.
**Trask Stalnaker** 27:02 Yeah, yeah.
**Austin Parker** 27:04 Oh, but do we have like a nice page?
**Trask Stalnaker** 27:08 Nice page.
**Austin Parker** 27:08 Meant. Like.
**Antoine Toulme** 27:10 What does it.
**Austin Parker** 27:10 Have.
**Antoine Toulme** 27:11 First.st
**Austin Parker** 27:12 I guess. Like, do they have like a nice landing page for us, or is it just this.
**Trask Stalnaker** 27:19 I don't know what that means. Sorry.
**Austin Parker** 27:22 I thought some some of the I thought some of these had, like some of these sponsored ones like had a landing page that was like
prettier.
Maybe not.
**Antoine Toulme** 27:32 I would. I would hope it would give us better limits to upload, but we ran into limits again during the last release.
**Trask Stalnaker** 27:39 No, you ran into we hadn't given your token permission to the.
**Antoine Toulme** 27:47 Oh, collect!
**Trask Stalnaker** 27:47 Builder. We missed one of the
**Antoine Toulme** 27:50 Okay.
**Trask Stalnaker** 27:51 Docker? Repos, yeah. Yeah.
**Antoine Toulme** 27:55 Does it give people better rate limits when they pull the image? Because that's meaningful.
**Trask Stalnaker** 28:04 I think that was part of it. Right, Austin.
**Austin Parker** 28:07 Yeah, huh!
What I mean, what do you mean? Like.
**Antoine Toulme** 28:13 Oh, well, so if you pull from Docker hub right, and even if you're signed up like, if you're not logged in 1st off, you get throttled pretty hard, even if you're signed in, you get throttled. And so we have a number of people where, if this becomes part of their critical infrastructure, and they pull in this every time they're doing a Ci, for example, that may very much impact their day to day if they're not able to pull our image in a regular fashion. So if we have this.
this actually could be a meaningful increase in capacity for people to use other images much more.
**Austin Parker** 28:44 Oh, the thing is so like we can. Only I think those have to be
like, I think we could add, like I think we could ask for more people to be added to the account
like right now, we can have 10 people.
**Antoine Toulme** 28:59 No, no.
**Austin Parker** 29:00 Members.
**Trask Stalnaker** 29:00 One is asking about anonymous like.
**Adriel Perkins** 29:03 Thank you.
**Austin Parker** 29:04 People just downloading.
**Adriel Perkins** 29:06 I think that affects them. I think I think that is purely on Docker side, for who they limit
or authenticated, and they do that usually by it. And whatever other authentication mechanism you have in play.
**Austin Parker** 29:20 Yeah, yes, like, I don't think there's anything we can do to
like. We can make tokens that you can use, that we can give to a repo, or whatever that kind of acts authenticated tokens. And then you can like, pull or push. But if you're asking for like an actual end user. Then that's that's
that's what.
**Antoine Toulme** 29:43 Oh, yeah.
**Austin Parker** 29:43 That's between Docker and the end user.
**Adriel Perkins** 29:49 I pull everything from Ghcr. For that very reason, if I can.
**Austin Parker** 29:56 Well until.
**Trask Stalnaker** 29:57 Do you think access tokens have been working? Well, now that we've got them.
**Antoine Toulme** 30:02 Set up.
**Austin Parker** 30:03 Yeah, that's but yes, good.
**Antoine Toulme** 30:07 Had a question. Recently. We have some of our docker images being pushed to Github, and some of them are being pushed to Docker hub. Is there a rationale for what we push? Where.
**Austin Parker** 30:20 I mean, I would think we should push everything to both.
**Antoine Toulme** 30:23 Okay, that might be an option.
We are not. We haven't
done that for everything. Is that something that we should target.
**Austin Parker** 30:34 I mean, I guess. Is there a reason like, is there a rationale for the stuff that's pushed to one versus the other?
**Antoine Toulme** 30:41 Yes, at least for the Collector Control Repository. We have a couple images which are only pushed to the Github Docker Repository because they're deemed as internal tools or testing tools like telemetry. Gen. Just that it golden to that. I could see how
those type of things could be construed to be meaningful for community like you will not also like it might be a discovery tool, like, you know you. You might not think to go look on the Github packages to go look for docker images right like it's not that might not come to you, or vice versa. You might not.
**Austin Parker** 31:16 Hey!
**Antoine Toulme** 31:17 By default.
**Austin Parker** 31:18 I mean
I don't. I don't think I will say like I know some places I think anything that is like
that people would use should go to both, because there are some places that
for whatever reason, we'll only support docker hub.
mostly enterprise. I think, like there's some enterprises that only support, like images from docker, hub, and.
**Antoine Toulme** 31:43 Yeah, I also get some. Some people will eventually also only want this on Ecr.
because they only want it on. Ecr, I mean, there's there's been a lot of like interesting discussions there.
**Austin Parker** 31:57 Yeah, like, at some point, we probably should think about publishing to cross publishing to like.
**Antoine Toulme** 32:03 Everything.
**Austin Parker** 32:04 Everything. It's just.
That seems like a good like post. 1 point. Oh, thing to talk about.
**Antoine Toulme** 32:11 Yeah, that's fine.
That's okay.
**Austin Parker** 32:13 One thing I am curious, though, is that there is stuff. There are images like Trask. If you go to the docker hub
and go to the actual hotel.
Propose.
**Antoine Toulme** 32:31 To close on that. I'll just open a quickly an an issue on community to discuss the policy on that. Okay.
**Austin Parker** 32:36 Yeah. So if you go to the like at the end of this list.
for yeah, like, there's these old. There's these things here that haven't been updated in over a year like, especially the hotel hotel call and the hotel like, what's that bottom one? The last one.
**Trask Stalnaker** 32:57 Play, they all have the same. Yeah.
**Austin Parker** 32:59 No, I know, but if you go down one, you could hover over the title, and it should.
**Trask Stalnaker** 33:03 Park.
**Austin Parker** 33:03 Tooltip.
**Trask Stalnaker** 33:05 Oh, yeah. Yeah.
**Austin Parker** 33:06 Open telemetry, collector, dev.
**Antoine Toulme** 33:08 Well.
**Trask Stalnaker** 33:09 4 years ago.
**Austin Parker** 33:10 Yeah, these are a ton of polls, but they're not being updated. It would be nice if we could get an idea of like which of the repos on here are actually
like like people are still pulling these like? Should they be.
**Antoine Toulme** 33:26 They should not. Conversely, if you go to the Github packages, there are stuff that's not been updated for years as well in.
**Austin Parker** 33:33 Yeah, it would.
It would be nice if we could like clean up some of this old stuff, because, like looking at the tags on that collector dev.
**Antoine Toulme** 33:43 What's the way to do that, do we?
**Trask Stalnaker** 33:44 Yeah.
**Antoine Toulme** 33:44 Shoe.
**Austin Parker** 33:45 Can open an issue, and we can delete the repos on our side. But we need to make sure that nothing is pushing to them.
I understood. I see
nothing is because I look at the tags last push almost 4 years by hotel bot.
**Antoine Toulme** 33:58 Yeah, let me look into it, and I'll I'll organize it.
**Trask Stalnaker** 34:00 But if we if we delete something and somebody's using it, say in their old Ci that they haven't updated.
**Austin Parker** 34:08 Yeah, maybe we can archive it is there.
**Trask Stalnaker** 34:12 Yeah, that would be better if that's an option.
**Austin Parker** 34:16 Oh, no!
What is it?
Obviously we can't.
**Trask Stalnaker** 34:23 Yeah, okay, yeah, I, totally support archiving.
**Austin Parker** 34:29 Yeah.
So I think we should just have an idea of like which one of these can be art, which ones of these can be archived
so that we don't break people's stuff. But, like
I, I don't know. Actually, I'm kind of curious what happens if you try to pull an archived image.
Maybe I would. I would like to think that Docker tells you like, Hey.
hey, yo! This is not super useful.
**Trask Stalnaker** 34:59 They're called Docker Repos.
**Austin Parker** 35:01 Yes, hilariously, non.
**Trask Stalnaker** 35:06 Confusing.
**Austin Parker** 35:07 Non confusing name.
**Jacob Aronoff** 35:09 Austin. It looks like archiving just means new images can't be pushed, and there's an archived label that gets added to the page.
Yes, but can still pull it.
**Austin Parker** 35:18 But what but if you pull an archived image? Is that like metadata that the docker pull, or your Ci system will flag.
**Jacob Aronoff** 35:27 I think that there will be some metadata on it like it seems like it adds a label to it, but.
**Austin Parker** 35:31 Yeah. So as long as it's.
**Jacob Aronoff** 35:32 Something.
**Austin Parker** 35:33 It's like, Oh, hey! This is an archived repo.
like something out there is pulling. The art is still pulling this stuff like, I don't want to just like break a bunch of people's shit. But I also don't want people pulling things that are like
10 years old, or, you know, 4 years old, or whatever, and.
**Antoine Toulme** 35:51 How about work I did for 6 months, and in 6 months we delete it. That's
that's an option right.
**Austin Parker** 35:57 Yes, I think
we would need to. I think the collector team needs to figure out what they want to do about stuff like that.
Yeah. But
if nothing else would be good to have a list of like, hey, these are the things that are actually, you know, just just a little little late summer cleaning.
**Antoine Toulme** 36:14 Yeah, that's that's perfectly fine.
But archiving seems like a 1st good step, anyway, like, it's a great step to deprecate things. And yeah.
**Austin Parker** 36:24 Archiving, and we can always, I imagine we can always archive things.
**Antoine Toulme** 36:28 Yes.
**Austin Parker** 36:31 Wow!
**Antoine Toulme** 36:36 Well, some of that stuff like. This is just old and creaky.
**Austin Parker** 36:42 So this is interesting. I wonder if they start if they.
**Antoine Toulme** 36:50 The health of the open imagery. Bpf. Project might not be that high, so.
**Austin Parker** 36:54 Yeah.
**Antoine Toulme** 36:55 It's not getting that much traction, and there's no releases. In the last year.
**Austin Parker** 37:00 So here's an interesting thing, Trask. If you go look at the analytics.
I wonder if they started tracking these differently after, or when we.
**Trask Stalnaker** 37:16 How do I look at analytics?
**Austin Parker** 37:18 Go down to analytics and then do like hotel collector and collector control, pick like collector and collector contrib.
You would have to search for it.
**Trask Stalnaker** 37:35 Oh, thanks!
**Austin Parker** 37:38 Oh, yeah, actually, that's it. Does that to me, too, that that's inner cell doesn't scroll
but do collector collect. Yeah, do collector conserving collector, and then
Look at the dots.
**Trask Stalnaker** 37:55 Oh, I see what you're saying. Yes, probably it looks like when we got the open source.
**Austin Parker** 38:01 Do you think that it wasn't being tracked before, or like it? Because the 1st dot there is like from 2023.
**Trask Stalnaker** 38:09 Yeah, I guess you're right there. Yeah.
**Austin Parker** 38:11 Like, why is there? What's up with the Gap
cause? If I look at the.
**Antoine Toulme** 38:16 Whoa!
**Austin Parker** 38:16 Oh, wait! No! All years report. June may.
**Trask Stalnaker** 38:20 There's like.
**Austin Parker** 38:20 March September.
If you look at down, if you look bought at down the bottom, there's a
if you scroll down on the page.
**Trask Stalnaker** 38:29 Yeah.
**Austin Parker** 38:30 So it actually did. It just stopped tracking it between September 2023, and March of 2025, which is probably, I guess around when we got into the program.
I think we must have just gotten like big enough that they stopped recording it. And then when we got the plan, and then
the plan got upgraded and they started again.
That's interesting.
**Jacob Aronoff** 38:53 Why would the that 1st dot before the spike be so low?
**Austin Parker** 38:59 Probably because it was a partial month.
That would be my guesstimations.
Partial month makes sense.
Yeah, wow, 200 fine, 359.3 3 million polls. In June.
**Antoine Toulme** 39:22 Guess we should.
We should push those stats when we graduate.
Just show off.
**Austin Parker** 39:30 I think that's that must be monthly. It's not cumulative.
I would assume it's not cumulative, at least.
**Antoine Toulme** 39:41 I wish it was, but.
**Austin Parker** 39:43 It doesn't actually tell you. It just says it just says, analytics beautiful.
Nothing.
**Trask Stalnaker** 39:51 There's a Csv file.
**Austin Parker** 39:53 Yeah.
literally, every single thing other than like, if you have collector contrib on here, it just skews everything. So immensely.
Summary data gives high level
repository. Some high level counts per repository on the number of polls in the time period.
Oh, you! There's
Oh, there's the you under usage. You actually get better stats.
Wait!
Oh, wait! What.
**Trask Stalnaker** 40:44 Oh, I think this is what people signed into. I think this is what we are pulling.
Oh, okay.
**Austin Parker** 40:53 Yes, because if you look down at like top users by polls, this is what authenticated accounts
this is what authenticated users in this org are doing so that's not.
**Antoine Toulme** 41:04 Oh!
**Austin Parker** 41:05 But I thought it was so. Yeah, it's analytics.
**Antoine Toulme** 41:12 Yeah, it's to show your billing right? Pretty much.
**Austin Parker** 41:15 I guess.
**Antoine Toulme** 41:15 It.
**Austin Parker** 41:17 Repository is easy, unfinished.
**Trask Stalnaker** 41:23 3.1 TB.
**Austin Parker** 41:27 Wow! What's using? Oh.
**Trask Stalnaker** 41:29 No.
**Austin Parker** 41:29 1.6. I mean Demos. A lot of stuff in it.
**Trask Stalnaker** 41:41 Alright! Let's see what else.
**Austin Parker** 41:45 Anyway, I think we're yeah. We could. We? We can close that one. It's good. Oh, yeah.
**Trask Stalnaker** 41:51 Yes, yeah. Yeah.
Delays with Github.
So we haven't seen this. I haven't seen this in a while.
**Austin Parker** 42:19 Me neither.
at least not without unless there's like a Github issue.
**Trask Stalnaker** 42:41 Yeah.
**Antoine Toulme** 42:47 Have you guys seen docker caching making a difference in terms of runtime for executors for runners?
Is that something you track.
**Austin Parker** 42:59 Isn't that something we're tracking? Adriel.
**Antoine Toulme** 43:02 Yeah, as of about 3, 6 months ago, we started to add docker caching to collector contribute jobs. It made a massive difference in terms of reliability of our jobs, because now we have a cache that contains all the docker images we use for integration testing. And it was actually a lot of like trouble for that, like at least slowdown and slowness from the runners.
And now we're seeing a much faster clip like in terms of execution.
**Trask Stalnaker** 43:27 Nice.
**Antoine Toulme** 43:28 I would just want to make sure we actually should probably document that as a best practice for any Ci like this type of caching makes a huge difference in terms of execution. Time.
You have to believe a little bit right? You have to kind of put your hat on like, I'm gonna believe that this works because the 1st time you run the caching well, it's not that fast and second time it
eventually you can see it.
**Adriel Perkins** 43:55 It does pay dividends. I don't know if we capture that just because I haven't looked at the platform in a while. I know telemetry is probably still going through there, but I'm not sure if I think the honeycomb some expired, and I'm not sure the signals broke on the Vm. So I haven't checked, but I can try to take a look
cause I would be interested if we. If we do have it. I would love to see the trends there for for those pipeline traces over time.
See exactly how much it actually improved.
**Antoine Toulme** 44:29 Is it worth documenting that somewhere.
**Adriel Perkins** 44:36 I would say it wouldn't hurt.
I mean, I I think these types of build caching things and also run caching. Things are are just good practices to have in terms of Ci and if others can, you know, be saved the pain by lessons you've learned. Because it's been documented. I've
I don't see anything wrong with that, but that's just my own personal opinion.
**Antoine Toulme** 45:01 Yeah, okay.
**Trask Stalnaker** 45:04 Yeah, I've definitely seen. I mean, caching of like in the Java builds, we cache
dependencies. We cache even build cache class files so that it's only does like incremental builds.
We, the Java instrumentation repo is another one. If you look at the total Github action minutes across repos. It's 1 of the big offenders along with the collector.
Okay, let's look at that. That's that could be, I think, insights action, usage, metric.
So this is per yaml.
So yeah, you can see the
the top 6 are either collector, contrive or Java instrumentation.
Oh, repositories! Yes, here we go. This is what I wanted to see.
So yeah, collector contrib.
**Austin Parker** 46:16 Does it not show cache minutes here, or anything.
**Trask Stalnaker** 46:22 How would you? I mean, you potentially cash sizes we could check. But like how much time you're saving by cash.
Oh.
**Austin Parker** 46:31 Yeah.
No. I mean.
**Jacob Aronoff** 46:34 I think that there's a way to look at like percent cache. If you go to the repository.
**Austin Parker** 46:40 Yeah, I'm more interested in like cache sizes, I guess, than.
**Jacob Aronoff** 46:43 Yeah, you'll if you go to the repo. It should show you that. And it's
**Antoine Toulme** 46:47 Yeah, you can see that.
**Jacob Aronoff** 46:48 Let's go to like repository runs, and then there's like a thing in the bottom for cache size.
**Antoine Toulme** 46:59 An example down there in the chat.
**Jacob Aronoff** 47:03 Yeah, that one.
**Austin Parker** 47:08 So cash.
**Trask Stalnaker** 47:09 Storage limit 145 GB out of.
**Austin Parker** 47:13 What I was curious about with the caching.
**Antoine Toulme** 47:19 It's lovely.
**Jacob Aronoff** 47:21 Yeah, this is probably.
**Austin Parker** 47:22 Kind of confused as to why we're so far over the limit.
**Jacob Aronoff** 47:27 Yeah, I also don't believe
like, I don't know how much that does. I've I've seen that warning a lot. I've never seen it result in a problem.
**Austin Parker** 47:37 I guess. My yeah, my thought is, if we're
like, aggressive caching is fine. But is that limit per repo? Is that per like? What is? What is the cache per repo per org.
**Antoine Toulme** 47:52 Breweryboo.
**Jacob Aronoff** 47:53 Definitely per repo.
I don't really don't know is like, if there's actually a penalty for going over that number. I've never.
**Austin Parker** 48:01 I think I mean, I think the penalty problem.
So I guess my question is like, is it? Actually, I mean the fact that it shows 1, 44 out of 10 makes me think that. No, they don't actually evict those caches, but if they started to, then wouldn't like.
I guess, since it's an Lru cache, you're probably fine. But if you had like aggressive caching across multiple things, then would you start
dropping some of the heavier like good example.
Nope Bill publish, probably has, like publish workflows, have different caches than like Ci, and you do those less frequently so would all of like the Pr. All the cash is being used for the Pr. And pushing stuff into that cache. Would that drop off the larger, heavier things for publish? I don't know. The fact that we're like super far over the cash storage limit makes me think that they just don't care. And they're not dropping anything from the cache.
**Antoine Toulme** 49:02 I think we're creating way too many caches before they have time to evict.
That's the other question is like, Yeah, what's the?
Because if you look at what I'm like, let's go to page 17. The caches go all the way to yesterday right?
Like our caches. They probably have a job that runs.
**Trask Stalnaker** 49:21 They are. They are evicting stuff.
**Austin Parker** 49:24 Okay. But if they're.
**Trask Stalnaker** 49:26 This like a toy.
**Austin Parker** 49:27 So if we're using 2.
**Trask Stalnaker** 49:28 Oh, yeah.
**Austin Parker** 49:28 Gigs of cash a day. Then, yeah, I don't know how much the cash is really helping.
**Antoine Toulme** 49:36 Well, some of it must be surviving over, because it's actually useful and and used heavily like.
**Austin Parker** 49:43 Yeah.
**Antoine Toulme** 49:44 You make a good point, we should probably look at why we have so many caches that are per pr, and that's something that we can do a review of.
because if we're able to just even reduce that by 1020% we could increase even more our time to execute. That's cool.
**Jacob Aronoff** 49:59 Yeah, cache keys. That's a good question. But I mean, that's a hard analysis to do across every repository.
**Antoine Toulme** 50:06 No, I think we should be looking for like the really low, low hanging fruits, like I see, like the shot to 56 of the commits are in the cache key. Right? That's that's.
**Jacob Aronoff** 50:15 Yeah.
**Antoine Toulme** 50:15 That might make sense in some cases, such as building building things. But maybe for lanes or things like that, we don't need that.
**Jacob Aronoff** 50:23 The yeah. The strategy that they tell you to deploy is
It's like you're supposed to deploy like partial misses, where, if it's something where you're changing.
It's like you build
**Antoine Toulme** 50:36 What? What's the word for this.
**Jacob Aronoff** 50:39 I forget it. It's like you start with the most common thing down to the least common thing. And then you can do a partial cache hit on something. So if you're including your commit hash as the main key, your actual hits will be very low. You want to do like Java version, you know Gradle version, and and so so forth. Basically.
**Antoine Toulme** 51:08 Yeah, should, we can do better.
**Trask Stalnaker** 51:10 Java, the actually the Gradle.
The official gradle action does all of that for you, which is nice.
We used to manage that all manually. And yeah, it's painful.
Cool. Let's see, we've got a couple of minutes left. Let's see if we
can close out anything more.
Fossa is still on. Hold
github team for publishing crates.
This should be good.
**Austin Parker** 52:04 They ever say it was good.
I assume that since nobody's complaining, it's probably good.
**Trask Stalnaker** 52:11 Yeah.
I removed. Why did I remove? Oh, I stopped it from getting auto close by removing, I think Severn
don't know. Anyway. Yeah, let's just see it.
They say it's okay to close it, and
can always open a new issue later.
Think it's nice for some of these, the project info ones to be more like transactional like. I mean, there's some that we have to research and do, but some that are just like.
Hey, just we've already done the planning image.
Oh, this is from Adriel. Image build repos for utilities that are used during local development like yaml lint.
Could I.
**Adriel Perkins** 53:27 That was so long ago.
**Trask Stalnaker** 53:29 To have a repo that's maintained.
Example is yaml lint. In many workflows yaml files are linted.
which is installed through Python, as Simcom group is standardized, I see. So
instead of running like yaml lint directly via python.
Yeah, we would have a docker. We would run it via Docker image.
**Adriel Perkins** 54:05 Yup, and we have some, I know, like
hotel. Hopefully, you can hear me. It's kind of noisy in here. But in in the hotel contrib on the hotel collector space.
There was like a go build tools, repo. And then there's another build tools, repo. And then there are build tools within the repos.
And then
I had mentioned that in the simcom meeting originally, because again, this is almost a year ago.
and there was some desire for us to have, like a consolidated build, tools
place that would have like these images published. But I honestly, I don't know if it's still a desire or a problem at this point in time.
cause I haven't haven't been able to attend any of the simcom meetings for Main simcom and and March and I haven't been in the tooling for longer than.
**Trask Stalnaker** 55:05 So this came up kind of recently in Java. Gregor was
because, yeah, some of these toolings, you know whether a slide sheet or whatever
we have to version, we have to keep them updated. And that sometimes requires
having that fake docker file that. Then we pull in through the make file and some of the repos.
He was proposing.
**Adriel Perkins** 55:40 Yeah. And that's definitely part of it, too.
**Trask Stalnaker** 55:42 Wise.
**Adriel Perkins** 55:43 Hard diversion in the way that you have to do all sorts of automatic or like shenanigans, to be able to update those make files with specific versions if you want them. So like.
**Trask Stalnaker** 55:54 Yeah.
**Adriel Perkins** 55:55 Approach, I think, just makes it a little bit more easier, and and allows you to do like things like renovate bot.
**Trask Stalnaker** 56:03 Yeah, yeah, basically, being able to have renovate auto update, these things would be nice.
Have you heard of my SE, as a like. I have no idea
it's like a.
**Austin Parker** 56:22 This.
**Trask Stalnaker** 56:22 Make file sort of alternative.
and it has a bunch of plugins for
**Austin Parker** 56:35 Like.
**Trask Stalnaker** 56:36 Like. Gee! They had
**Austin Parker** 56:42 If we're going to do this we might as well do Nick's.
**Trask Stalnaker** 56:46 What's that?
**Adriel Perkins** 56:47 Lost one on that, although.
As well, yeah.
**Austin Parker** 56:52 I was. Gonna say, if you're gonna do this, you might as well do fucking Nick's flakes.
Make everyone really hate us.
Hi, it's different.
**Adriel Perkins** 57:02 Flashy mode. I'll just get so even after it.
**Austin Parker** 57:05 Is.
**Trask Stalnaker** 57:06 So like they've got a plugin for, or they support yaml and
and supposedly they work with renovate like it kinda handles some of that stuff.
**Austin Parker** 57:17 Who's who built this.
**Trask Stalnaker** 57:24 Good question. Jdx. No idea who this person is.
**Austin Parker** 57:33 Rust, dev.
**Trask Stalnaker** 57:36 At Figma pretty, popular with 18,000 stars.
**Austin Parker** 57:42 I was. Gonna say, maybe he's gonna be.
I don't know if we should do something from a figma person they're about to all fucking. Go
live on an island.
I don't know if you wouldn't see watching their stock today.
**Trask Stalnaker** 57:55 Don't know anything about anybody.
**Austin Parker** 57:58 Oh, they picked my Ipo today.
They actually halted trading on it because that was up so high
current market cap 55 times 2025 sales.
healthy, healthy, healthy market we got here very normal.
This looks cool. I haven't looked. I have not looked at it, but like
I'm fine. I think it would probably be.
**Adriel Perkins** 58:26 Is that an invasive change, though to all the other repositories of.
**Austin Parker** 58:31 Like. I mean, I've looked at the make files for itself and shrink. For example.
**Adriel Perkins** 58:35 And like they're not. They're not simple, right?
**Austin Parker** 58:38 Yeah, like.
**Adriel Perkins** 58:39 It's all invasive pieces.
**Austin Parker** 58:42 I mean, I think that we have a lot of people using make and doing a lot of like really intense stuff with make
**Trask Stalnaker** 58:53 Yeah, that's a good
point, is we? I mean, I think there's 2 varieties of people there's like Simcom and spec repos that are just using make to run like your garden variety like linting.
**Austin Parker** 59:07 And then there's.
**Trask Stalnaker** 59:09 More hardcore usage for actually building product.
**Austin Parker** 59:15 Yeah.
**Trask Stalnaker** 59:30 Oh, we have hit our time box.
We'll add a link there.
**Antoine Toulme** 59:45 Thanks. Everyone.
**Trask Stalnaker** 59:47 Yeah good to see y'all, I'm gonna be out next week. But we'll be back after that.
**Austin Parker** 59:58 Cheers, take care! Have a good day!
